"""
API tool for SpExoDisks

This is meant to be an alternative to downloading data from SpExoDisks.com,
instead this package will allow users to connect to the SpExoDisks database directly w/ Python.
"""

import requests

server = 'https://spexodisks.com/api/'


def get_available_isotopologues():
    url = server + 'available_isotopologues/'
    response = requests.get(url)
    return response.json()


def get_params_and_units():
    url = server + 'available_params_and_units/'
    response = requests.get(url)
    return response.json()


def get_curated():
    url = server + 'curated/'
    response = requests.get(url)
    return response.json()


def get_spectra():
    url = server + 'spectra/'
    response = requests.get(url)
    return response.json()


def get_star_aliases():
    url = server + 'objectnamealiases/'
    response = requests.get(url)
    return response.json()


def find_spectra(alias=None):
    aliases = get_star_aliases()
    aliasesandhandles = {}

    alias = alias.lower().strip()

    for i in aliases:
        aliasesandhandles[i['alias'].lower().strip()] = i['spexodisks_handle'].lower().strip()

    if alias is None:
        print("Please provide an object name to search for.")
        return
    if alias not in aliasesandhandles.keys():
        print("Object not found in database.")
        return
    else:
        return aliasesandhandles[alias]


def get_curated_data(handle: str) -> dict:
    curated = get_curated()

    for i in curated:
        i['spexodisks_handle'] = i['spexodisks_handle'].lower().strip()
        if i['spexodisks_handle'] == handle.lower().strip():
            return i


def get_all_spectra_handles(spexodisks_handle: str) -> list:
    spectra = get_spectra()
    handles = []
    for i in spectra:
        if spexodisks_handle.lower().strip() == i['spexodisks_handle'].lower().strip():
            handles.append(i)
    print(f"Found {len(handles)} spectra for {spexodisks_handle}")
    return handles


def get_wavelengths(handle: str) -> dict:
    url = server + handle + '/'
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    # print("This file is not meant to be run directly. Please import spexod instead.")
    # exit(1)
    # print(get_available_isotopologues())
    # print(get_params_and_units())
    # print(get_curated())
    # print(get_spectra())
    # print(get_star_aliases())
    # find_spectra('[C91] IRS 1')
    # print(get_data_from_handle('leftsqbracketc91rightsqbracket_irs_1'))
    # print(get_all_spectra_handles('IRAS_08470minus4321'))
    print(get_wavelengths('crires_2254nm_2356nm_IRAS_08470minus4321'))