import os
from setuptools import setup, find_packages


# the user default config file that users use as a template to create their own config file
md_fit_read_path = os.path.join('spexod', 'FITSREAD.md')

setup(name='spexod',
      version='0.2.1',
      description='Community tools for SpExoDisks (spexodisks.com)',
      author='Isaac Jaramillo, Caleb Wheeler',
      author_email='chw3k5@gmail.com',
      packages=find_packages(),
      url="https://github.com/spexod/spexod",
      install_requires=[
            'numpy',
            'astropy'
            'requests',
            'setuptools',
            'pandas',
            'plotly'
        ],
      data_files=[('spexod', [md_fit_read_path])],
      include_package_data=True,
      )
