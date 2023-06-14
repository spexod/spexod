"""
API tool for SpExoDisks

This is meant to be an alternative to downloading data from SpExoDisks.com,
instead this package will allow users to connect to the SpExoDisks database directly w/ Python.
"""

import requests
import pandas as pd

server = 'https://spexodisks.com/api/'


def get_available_isotopologues() -> dict:
    """
    Returns a dictionary of available isotopologues and their properties
    """
    url = server + 'available_isotopologues/'
    response = requests.get(url)
    return response.json()


def get_params_and_units() -> dict:
    """
    Returns a dictionary of available parameters and units
    """
    url = server + 'available_params_and_units/'
    response = requests.get(url)
    return response.json()


def get_curated() -> dict:
    """
    Returns a dictionary of curated data and corresponding handles
    """
    url = server + 'curated/'
    response = requests.get(url)
    return response.json()


def get_spectra() -> dict:
    """
    Returns a dictionary of available spectra
    """
    url = server + 'spectra/'
    response = requests.get(url)
    return response.json()


def get_star_aliases() -> dict:
    """
    Returns a dictionary of star aliases and corresponding handles associated with alias
    """
    url = server + 'objectnamealiases/'
    response = requests.get(url)
    return response.json()


def find_spectra(alias=None) -> dict:
    """
    Returns a dictionary of spectra associated with a given alias
    """
    aliases = get_star_aliases()
    aliasesandhandles = {}
    possibleAliases = []

    alias = alias.lower().strip()
    # Use a dictionary to map aliases to handles

    for i in aliases:
        aliasesandhandles[i['alias'].lower().strip()] = i['spexodisks_handle'].lower().strip()

    if alias is None:
        print("Please provide an object name to search for.")
        return
    if alias not in aliasesandhandles.keys():
        for i in aliasesandhandles.keys():
            if alias in i:
                possibleAliases.append(i)
        return print(f"Found {len(possibleAliases)} possible aliases for {alias}: {possibleAliases} \n"
                     f"Choose one of these aliases to search for and type it in verbatim.")
    else:
        return aliasesandhandles[alias]


def get_curated_data(handle: str) -> dict:
    """
    Returns a dictionary of curated data for a given handle
    """
    curated = get_curated()

    for i in curated:
        i['spexodisks_handle'] = i['spexodisks_handle'].lower().strip()
        if i['spexodisks_handle'] == handle.lower().strip():
            return i


def get_all_spectra_handles(spexodisks_handle: str) -> list:
    """
    Returns a list of all spectra handles for a given star/alias
    """
    spectra = get_spectra()
    handles = []
    for i in spectra:
        if spexodisks_handle.lower().strip() == i['spexodisks_handle'].lower().strip():
            handles.append(i)
    print(f"Found {len(handles)} spectra for {spexodisks_handle}")
    return handles


def get_wavelengths(handle: str) -> dict:
    """ Returns a dictionary of wavelengths for a given handle"""
    url = server + handle.lower() + '/'
    response = requests.get(url)
    return response.json()['wavelength_um']


def get_fluxes(handle: str) -> tuple:
    """ Returns a tuple of fluxes and flux errors for a given handle"""
    url = server + handle.lower() + '/'
    response = requests.get(url)
    return response.json()['flux'], response.json()['flux_error']


def get_stars_from_file(filename: str) -> list:
    """ Returns a list of stars from a given file"""
    df = pd.read_csv(filename, sep=",")
    return df.columns.tolist()


def create_spectra_file(stars: list) -> None:
    """ Creates a file with all spectra handles for a given list of stars"""
    # Get all spectra handles for each star
    star_spectra = {}
    for star in stars:
        spectra = find_spectra(star)
        star_spectra[star] = get_all_spectra_handles(spectra)

    for k,v in star_spectra.items():
        df = pd.DataFrame(v)
        df.to_csv(f"{k}.csv", index=False)

    # spectrum_handles = {}
    # for k,v in star_spectra.items():
    #     for i in v:
    #         spectrum_handles[i['spexodisks_handle']] = i['spexodisks_handle']
    #
    # print(spectrum_handles)



    # From spectra handles, get wavelengths and fluxes


if __name__ == "__main__":
    # print("This file is not meant to be run directly. Please import spexod instead.")
    # exit(1)
    # print(get_available_isotopologues())
    # print(get_params_and_units())
    # print(get_curated())
    # print(get_spectra())
    # print(get_star_aliases())
    # find_spectra('IRS')
    # print(get_curated_data('leftsqbracketc91rightsqbracket_irs_1'))
    # print(get_all_spectra_handles('IRAS_08470minus4321'))
    # print(get_wavelengths('crires_2254nm_2356nm_IRAS_08470minus4321'))
    # print(get_fluxes('crires_2254nm_2356nm_IRAS_08470minus4321')[1])
    # print(get_flux_errors('crires_2254nm_2356nm_IRAS_08470minus4321'))
    # print(get_stars_from_file('test.txt'))
    stars = get_stars_from_file('test.txt')
    create_spectra_file(stars)
