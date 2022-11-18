# spexod
Community tools for **SpExoDisks** (**Sp**ectroscopy  of **Exo**planet **Disks**) data

https://github.com/spexod/spexod
## Quick Installation

See the Section **Recommended Community Installation** below for a 
detailed installation instructions that use python best practices.

`pip` is the recommended installation method, you can 
use it in to ways to install the `spexod` python module:

### Download from pypi.org

    pip install spexod

### Download the latest version from github:

    git clone https://github.com/spexod/spexod
    cd spexod
    pip install .

# FITS files

See the detailed instruncions for data format for SpExoDisks FITS
files at [~/spexod/spexod/FITSREAD.md](https://github.com/spexod/spexod/spexod/FITSREAD.md).

# Required Software for Community Contributors 
## Git
Git and GitHub are standard tools across astronomy, computer science, computer engineering,
and other fields. This is a tool set that everyone should learn for code management. It is 
always useful, and often expected for contributors to a project of any size.

https://git-scm.com/downloads

This installation will include _gitbash_ on Windows machines. This is a terminal application
that simulates a unix terminal on Windows. It is useful for managing code and working with
git and github. If this is the first terminal/shell you have installed on your
Windows computer, you will be able to use this to enter all of the terminal
commands present in the rest of this README.md file.

A 15-minute introduction video for *git* is available at  https://www.youtube.com/watch?v=USjZcfj8yxE


## Python3
Get the latest version of Python3

https://www.python.org/downloads/

This project was tested with Python 3.8.5 to 3.10.x. It probably works with older
versions of Python, but it is not guaranteed.

Some python 
installations will need to call `python3` instead of `python` from the terminal. 
Check your python version with `python --version` if it comes back with 
2.7.x, try `python3 --version` and expect to get 3.x.x. 

Modern Python installations require you to sign and SSL certificate after
installation. This is done by simply running a script in the installation 
directory. Programs like, [Homebrew](https://brew.sh/) will do this step for
you. If you see SSL errors in Python, it is probably because you skip the
certificate step.

# Recommended Community Installation

## Download
From a commandline interface (terminal, gitbash, cmd, or powershell)
Clone this Repository (https://github.com/Wheeler1711/submm_python_routines)
using the following:

`git clone https://github.com/spexod/spexod`

then cd into the directory using:

`cd spexod`

Remember to update the repository periodically with:

`git pull`

## Virtual Environment Setup and Activation (recommended)

Configure the virtual environment for DetMap or from the terminal.

### Initial Setup 
This step is done one time to initialize the virtual environment.

Window and Linux Tested in Windows PowerShell and OSX Terminal. Some python 
installations will need to call `python3` instead of `python`. Check your python version with
`python --version` if it comes back with 2.7.x, try `python3 --version` and expect to get 3.x.x. 

If you have a many python installations, or if you just downloaded the latest version
of python then you should replace `python` with the full path to the python executable.

```
python -m pip install --upgrade pip
python3 -m venv venv
```

### Activating a Virtual Environment
This step needs to be done everytime you want to use the virtual environment.

For unix-like environment activation:

```source venv/bin/activate```

Windows CMD environment activation:

```.\venv\Scripts\activate```

for Windows powershell environment activation:

```.\venv\Scripts\activate.ps1```

After activation, the term ail will add a `(venv)` to the command prompt. At this point
you can drop the full paths to the python and pip executables into the terminal, 
and the `python3` in place of `python` commands.

I like test that everything went as expected with the following:

```
python --version
pip list
```

### Package Installation
This step needs to be done everytime you want need to install new python packages.

The requirements.txt has the list of all packages needed for submm_python_routines. 
From a terminal with the virtual environment activated, do:

```pip install -r requirements.txt```

Packages can all be installed individually with `pip install <package_name>`

## Install as Python Packaage
If you are a user of the submm_python_routines but are unlikely modify (develop) 
the code in this project, then it is recommended that you install the 
`spexod` as a python package. This can be done within a
virtual environment, or for a user, (or global version of python which makes a 
mess https://xkcd.com/1987/).

With a your chosen python environment active and in the folder `/spexod/` 
(where `setup.py` file is located ), you can install with `pip` via:

    pip install .
