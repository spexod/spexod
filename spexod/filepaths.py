import os


spexod_module_dir = os.path.dirname(os.path.realpath(__file__))
fitsfile_md_path_test = os.path.join(spexod_module_dir, 'FITSREAD.md')

if os.path.exists(fitsfile_md_path_test):
    fitsfile_md_path = fitsfile_md_path_test
else:
    fitsfile_md_path = None

fitsfile_py_path_test = os.path.join(spexod_module_dir, 'fits_read.py')
if os.path.exists(fitsfile_py_path_test):
    fitsfile_py_path = fitsfile_py_path_test
else:
    fitsfile_py_path = None
