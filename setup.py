import os
from setuptools import setup, find_packages


setup(name='spexod',
      version='0.4.0',
      description='Community tools for SpExoDisks (spexodisks.com)',
      author='Caleb Wheeler',
      author_email='chw3k5@gmail.com',
      packages=find_packages(),
      url="https://github.com/spexod/spexod",
      install_requires=['numpy', 'astropy']
      )