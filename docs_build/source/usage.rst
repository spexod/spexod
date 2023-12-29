Usage
=====

.. _installation:

Installation
------------

To use SpExod, first install it using pip:

.. code-block:: console

   pip install spexod

Or try one of the other installation methods.

.. code-block:: console

   conda install -c conda-forge spexod

Or

.. code-block:: console

    git clone https://github.com/spexod/spexod
    cd spexod
    pip install .


Retrieving Data
-------------------
.. note::

   It may be helpful to view the :doc:`dataflow` source page as you follow along with the documentation.

The following functions are used to retrieve almost all data from the database:
``API.get_available_isotopologues()``, ``get_params_and_units()``, ``get_curated()``, ``get_spectra()``,
and ``get_star_aliases()``. Each of these functions returns a list of dictionaries, where each dictionary
represents a row in the database. The keys of the dictionaries are the column names of the database,

.. autofunction:: spexod.api.get_available_isotopologues

.. autofunction:: spexod.api.get_params_and_units

.. autofunction:: spexod.api.get_curated

.. autofunction:: spexod.api.get_spectra

.. autofunction:: spexod.api.get_star_aliases

Navigating the SpExoDisks Database
----------------------------------

.. warning::

    If the alias is not typed verbatim as it is in the database, it will return a list of the closest alias it finds
    and also informs you of other possible aliases. Incase it does not select the correct alias,
    copy and paste the alias you want to ensure you get the correct alias(es).

.. autofunction:: spexod.api.find_spectra_handle
.. autofunction:: spexod.api.get_curated_data
.. autofunction:: spexod.api.get_all_spectra_handles
.. autofunction:: spexod.api.get_wavelengths
.. autofunction:: spexod.api.get_fluxes

Misc Functions
--------------
.. autofunction:: spexod.api.get_stars_from_file
.. autofunction:: spexod.api.create_spectra_file
.. autofunction:: spexod.api.download_spectrum
.. autofunction:: spexod.api.plot_spectra

.. note::

    To see a working example of the API, check out the following jupyter notebook:
    https://github.com/spexod/spexod/blob/python_api_tool/getting_started.ipynb