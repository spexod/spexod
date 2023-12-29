.. Spexod documentation master file, created by
.. sphinx-quickstart on Fri Aug 11 15:12:11 2023.
.. You can adapt this file completely to your liking, but it should at least
.. contain the root `toctree` directive.

Welcome to Spexod's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. note::

   This documentation is still a work in progress. If you have any questions,
   please feel free to open an issue on the GitHub repository

   `github.com/spexod/spexod <https://github.com/spexod/spexod/>`_

**spexod** is a Python package that provides a Python interface to access the
SpExoDisks API `spexodisks.com/api/ <https://spexodisks.com/api/>`_. The project is provides users with a
convenient access data for a particular source.
It offers a set of functions  making it easier to retrieve and manipulate
the information as needed. One of the key advantages of using the Python API is its ability to access more data than
what is typically visible on the explore data page or user interface. While the explore data page may present a
limited subset of the available data, the Python API allows users to query and retrieve a broader range of information.
This can be particularly useful for users who require comprehensive access to the data for analysis, research, or other
purposes. Furthermore, the Python API allows users to access the data in its purest form, including any NULL or empty
values that may exist. This means that users have direct access to the original data structure and can work with it as
it is, without any modifications or preprocessing. This level of data integrity can be beneficial for advanced data
analysis or when specific processing steps need to be performed on the data.


Check out the :doc:`usage` section for further information, including how to
:ref:`install <installation>` the project.

Contents
--------

.. toctree::

   dataflow
   usage

.. autosummary::
   :toctree: generated

   spexod.api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
