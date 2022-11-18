# twine is PyPi's upload tool
pip install twine --upgrade
# make a distribution wheel file
python setup.py bdist_wheel
# make a distribution source file in tar.gz format
python setup.py sdist --formats=gztar
# # upload to test PyPi
# python -m twine upload --repository testpypi dist/*
# # testpypi installation
# pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple spexod==0.1.0
# upload to PyPi
python -m twine upload --repository pypi dist/*
# # PyPi installation
# pip install spexod