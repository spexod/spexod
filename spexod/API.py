"""
API tool for SpExoDisks

This is meant to be an alternative to downloading data from SpExoDisks.com,
instead this package will allow users to connect to the SpExoDisks database directly w/ Python.
"""
from typing import List

import requests, zipfile, io
import pandas as pd
import os
import plotly.express as px

SERVER_URL = 'https://spexodisks.com/api/'


def get_available_isotopologues() -> dict:
    """
    Returns a dictionary of available isotopologues and their properties
    """
    url = SERVER_URL + 'available_isotopologues/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching isotopologues: {e}")
        return None


def get_params_and_units() -> dict:
    """
    Returns a dictionary of available parameters and units.
    """
    url = SERVER_URL + 'available_params_and_units/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching parameters and units: {e}")
        return None


def get_curated() -> dict:
    """
    Returns a dictionary of curated data and corresponding handles.
    """
    url = SERVER_URL + 'curated/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching curated data: {e}")
        return None


def get_spectra() -> dict:
    """
    Returns a dictionary of available spectra.
    """
    url = SERVER_URL + 'spectra/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching spectra: {e}")
        return None


def get_star_aliases() -> dict:
    """
    Returns a dictionary of star aliases and corresponding handles associated with alias.
    """
    url = SERVER_URL + 'objectnamealiases/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching star aliases: {e}")
        return None


def find_spectra_handle(alias=None) -> dict:
    """
    Returns a dictionary of spectra associated with a given alias.
    """
    aliases = get_star_aliases()
    aliases_and_handles = {}

    # Use a dictionary to map aliases to handles
    for i in aliases:
        aliases_and_handles[i['alias'].lower().strip()] = i['spexodisks_handle'].lower().strip()

    if alias is None:
        print("Please provide an object name to search for.")
        return None

    alias = alias.lower().strip()

    if alias not in aliases_and_handles.keys():
        possible_aliases = [i for i in aliases_and_handles.keys() if alias in i]
        if len(possible_aliases) > 0:
            print(f"Found {len(possible_aliases)} possible aliases for {alias}: {possible_aliases}")
        else:
            print(f"No matching aliases found for {alias}.")
        return None

    return aliases_and_handles[alias]


def get_curated_data(handle: str) -> dict:
    """
    Returns a dictionary of curated data for a given handle.
    """
    curated = get_curated()

    handle = handle.lower().strip()

    for data in curated:
        if data['spexodisks_handle'].lower().strip() == handle:
            return data

    return None


def get_all_spectra_handles(spexodisks_handle: str) -> list:
    """
    Returns a list of all spectra handles for a given star/alias.
    """
    spectra = get_spectra()
    handles = []
    for i in spectra:
        if spexodisks_handle.lower().strip() == i['spexodisks_handle'].lower().strip():
            handles.append(i)
    print(f"Found {len(handles)} spectra for {spexodisks_handle}")
    return handles


def get_wavelengths(handle: str) -> dict:
    """
    Returns a dictionary of wavelengths for a given handle.
    """
    url = SERVER_URL + handle.lower() + '/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['wavelength_um']
    except requests.RequestException as e:
        print(f"Error fetching wavelengths for handle '{handle}': {e}")
        return None


def get_fluxes(handle: str) -> tuple:
    """
    Returns a tuple of fluxes and flux errors for a given handle.
    """
    url = SERVER_URL + handle.lower() + '/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        fluxes = data.get('flux')
        flux_errors = data.get('flux_error')
        return fluxes, flux_errors
    except requests.RequestException as e:
        print(f"Error fetching fluxes for handle '{handle}': {e}")
        return None, None


def get_stars_from_file(filename: str) -> list:
    """
    Returns a list of stars from a given file.
    """
    try:
        df = pd.read_csv(filename, sep=",")
        return df.columns.tolist()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except pd.errors.EmptyDataError:
        print(f"File '{filename}' is empty.")
    except pd.errors.ParserError:
        print(f"Error parsing file '{filename}'.")
    return []


def create_spectra_file(stars: list) -> None:
    """ Creates a file with all spectra handles for a given list of stars"""
    # Get all spectra handles for each star
    star_spectra = {}
    for star in stars:
        spectra = find_spectra_handle(star)
        star_spectra[star] = get_all_spectra_handles(spectra)

    # Create a folder for each star
    for star, spectra_list in star_spectra.items():
        # Create a folder for each key
        if not os.path.exists(star):
            os.makedirs(star)
        os.chdir(star)
        # For each value, find from API and write to csv
        for spectrum in spectra_list:
            wavelengths = get_wavelengths(spectrum['spectrum_handle'])
            fluxes, flux_errors = get_fluxes(spectrum['spectrum_handle'])
            print(f"Writing {spectrum['spexodisks_handle']}.csv")
            print(f"Found {len(wavelengths)} wavelengths and {len(fluxes)} fluxes for {spectrum['spexodisks_handle']}")
            df = pd.DataFrame({'wavelength_um': wavelengths, 'flux': fluxes, 'flux_error': flux_errors})
            df.to_csv(f"{spectrum['spectrum_handle']}.csv", index=False)
        # Create a csv file for each key
        df = pd.DataFrame(spectra_list)
        df.to_csv(f"{star}.csv", index=False)
        os.chdir("..")

def login() -> dict:
    """
    Logs into the SpExoDisks database.
    """
    access = False
    while not access:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        url = SERVER_URL + 'users/token/'
        try:
            response = requests.post(url, json={'email': username, 'password': password})
            response.raise_for_status()
            if response.status_code == 200:
                print("Login successful.")
                access = True
                return response.json()
            else:
                print("Login failed. Please try again.")
        except requests.RequestException as e:
            print(f"Error during login: {e}")
            return None


def download_spectrum(spectra: List) -> None:
    """
    Downloads spectra from the SpExoDisks database.
    """
    access_token = login().get('access')
    if not access_token:
        print("Login failed. Cannot download spectra.")
        return

    url = SERVER_URL + 'datadownload/?spectra='
    for spectrum in spectra:
        url += spectrum + '%'

    headers = {'Authorization': 'Bearer ' + access_token}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        zip_file.extractall("Spectra")
        print("Spectra downloaded successfully.")
    except requests.RequestException as e:
        print(f"Error during spectrum download: {e}")


def plot_spectra(wavelength, flux) -> None:
    """
    Plots a spectrum
    """
    df = pd.DataFrame({'wavelength_um': wavelength, 'flux': flux})
    fig = px.line(df, x='wavelength_um', y='flux')
    fig.show()


if __name__ == "__main__":
    print("This file is not meant to be run directly. Please import spexod instead.")
    exit(1)

