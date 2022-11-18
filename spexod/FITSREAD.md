# FITS 
This is an explanation of the FITS generated as downloadable data from https://spexodisks.com.

This file (FITSREAD.md) comes standard with every downloadable data set. Also included in every download is fits_read.py, 
a python file (fits_read.py) that contains an example of how to read-in the FITS files and store the 
various tables in 
as a [numpy strucured array](https://numpy.org/doc/stable/user/basics.rec.html) as attributes of python object 
(A custom data class called SpexodFITS). Numpy structured have columns be called like python dictionary keys.
Each column of data can define it own data type, making struted array ideal for casting into 
[pandas dataframes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) for additional 
analysis.

SpExoDisks is, and always will be, a tool to serve the astronomy community. We welcome feedback and 
collaboration. Open dialogs are paramount for advancement, scientific or otherwise. Contact the 
spexodisks team at https://spexodisks.com/contact to make suggestions and share your talent.

# About FITS File Format
FITS is a ubiquitous file format for storing astronomical data, however it is not a modern standard and 
is often frustrating for each generation of students to learn. FITS files generally consist of one or more
Header Data Units (HDU), with each HDU containing a `header` and a `data` section. The `header` is a 
collection of
key-value pairs for storing metadata (data that answers the questions where?, when? & how?), and the 
`data` section is an often an image (multidimensional array of floating point values), or 
a table (2D arrays addressable by row and columns where
each column is allowed to have a different type of data i.e. integers, floats, strings). HDUs are organized
in a list, with the first HDU being the `Primary HDU`; this list is called the Header Data Unit List (HDUL).

## SpExoDisks FITS File Format
Like almost all astronomy data sets, SpExoDisks data is incomplete and is always growing. This type of data
does not lend itself to a standard format. Moreso, data is enriched and more easily understood by adding
contextual data. The data science team at SpExoDisks provides all available contextual data to the 
Primary Spectrum. 

This includes dynamically
added metadata about the observed star (multiple name types, simbad link, standard stellar 
properties with references to the literature), the observing instrument, and anything else we are able to
collect. When available, it also includes associated data like spectral line data from https://hitran.org, 
the original header for the observation, flux calibration data

## Static Extensions
At a minimum, each SpExoDisks Fits file will have three (3) static extensions at HDUL[0], HDUL[1], and HDUL[2].

### SpExoDisks FITS Header extension = HDUL[0].header
The SpExoDisks Header only (Table data, like a spectrum, is not allowed as a primary 
(hdul[0]), cite https://docs.astropy.org/en/stable/io/fits/index.html). Access this metadata 
with HDUL[0].header.

While additions to this header are on going, the following information is provided when avaliable:
- spexod_header['POPNAME'] is the populaur name for the observed star in astronomy literature.
- spexod_header['SIMBAD'] is the primary name displayed on [SIMBAD](http://simbad.u-strasbg.fr/).
- spexod_header['SIMBLINK'] is a link to the SIMBAD page for the star.
- spexod_header['SIMBBIB'] is a link to the SIMBAD bibliography for the star.
- spexod_header['SKYCOORD'] contains J2000 Right Ascension and Declination in (hms dms)
- spexod_header['RAJ2000'] = ra_epochJ2000_deg 
- spexod_header['RAREF'] = is the literature reference for the right ascension. 
- spexod_header['RAUNITS'] = 'degrees' 
- spexod_header['DECJ2000'] = is the literature reference for the declination.
- spexod_header['DECREF'] = dec_ref 
- spexod_header['DECUNITS'] = 'degrees'
- spexod_header['INSTNAME'] = the spectrometer instrument that observer the primary spectrum 
- spexod_header['WAVEMIN'] = The spectrometer's wavelength range minimum in micrometers (um)
- spexod_header['WAVEMAX'] = The spectrometer's wavelength range maximum in micrometers (um)
- spexod_header['WAVESTEP'] = The spectrometer's wavelength step size in micrometers (um)
- spexod_header['WAVEUNIT'] = "Wavelength Units: um=10^-6 meters"
- spexod_header['OBSDATE'] = The observation date in datetime format. 
- spexod_header['OBSJUL'] = The Julian observation Date 
- spexod_header['REFFRAME'] = Spectral Wavelength/Velocity Reference Frame 
- spexod_header['SPECREF'] = Reference for Primary Spectrum (Warning: FITS format forces us to strip accents from people's names,
 this was very upsetting to the data  scientist.)
- spexod_header['DATAREF'] = The citation reference for assembled SpExoDisks data 
- spexod_header['DATASCI'] = "The SpExoDisks Data Scientist and Database Architect is Dr Caleb Wheeler 
(chw3k5@gmail.com), Underground Instruments"
- spexod_header['CALSTATE'] = The calibration stat of the data
- spexod_header['FLUXCAL'] = An explicit description of the flux units and calibration.

When available we dynamically provide the following information:
- spexod_header['REDUCREF'] = The citation for the Primary spectrum Data Reduction 
- spexod_header['HITRANRF'] = "Reference for Spectroscopic Line Data: Hitran2016 molecular spectroscopic 
database (Gordon et al. 2017) at hitran.org"
spexod_header['LINEFLUX'] = Citation  Reference for Line-Fluxes Measurements
spexod_header['STACKLIN'] = Citation Reference for Stacked-Line Profiles
spexod_header['PI'] = Citation for the Principle Investigator (PI) of the Primary Spectrum
pexod_header['AORKEY'] = The Spitzer AOR Key (Spitzer spectra only)

And finally we dynamically provide all the available SpExoDisks data for the Distances to the observed star 
and the Effective Temperature including the Value, reference, units, and when scale, the uncertainty. 

### SpExoDisks Primary Spectrum Extension = HDUL[1].data[0:2]
The 1D spectrum as with wavelenghts and fluxes.  Note that many values Flux and flux error can be 
Not-A-Number (NaN).

- HDUL[1].data[0] = wavelength in micrometers (um)
- HDUL[1].data[1] = flux in units disribed in HDUL[0].header['FLUXCAL'] and HDUL[0].header['CALSTATE']
- HDUL[1].data[2] = flux error (uncertainty). This is always provided but is sometimes and array of only NaN.

### Original Observation header Extension = HDUL[2].header
When a spectrum has a FITS header, or is a text file with a header. We provide that information here.

- HDUL[2].header = The original header from the observation, data completion, or reduction. Depends on the
source of the spectrum. Minimal header is still defined even if no original header is available.

## Dynamic Extensions
Each spexodisks FITS file can have any number of dynamic extensions. No dynamic extensions is possible,
but unlikely as most data has spectroscopic lines from Hitran.org for CO or H2O molecules.

Below we discuss the expected types of dynamic extensions. Each type is identifiable  by the header card
dynamic_hdu.header['DYNMTYPE'] which is resitrect to having one of the following values (lowercase, no spaces):
- hitran, 
- fluxcal
- lineflux
- stackedline

### Hitran Spectroscopic Lines Extension(s) dynamic_hdu.header['DYNMTYPE'] = 'hitran'
The Hitran Spectroscopic Lines Extension(s) is a FITS table extension. There can be 0-2 dynamic extensions
of type, one for CO and one for H2O molecules. Each molecule has its own extension as the table shapes
are different do to the difference in rotation and vibration quantum for different molecular species. However,
multiple isotopologues for given molecule are present in a single table. 

Table data is available with:
- hitran_hdu.data

Additional header information is available with:
- hitran_hdu.header['DYNMTYPE'] = "hitran"
- hdu_this_molecule.header['HITRANRF'] = "Reference for Spectroscopic Line Data: Hitran2016 molecular 
spectroscopic database (Gordon et al. 2017) at https://hitran.org
- hdu_this_molecule.header['MOLETYPE'] = The molcule type for this dynamic hirtan table

### Flux Calibration Extension dynamic_hdu.header['DYNMTYPE'] = 'fluxcal'
When the flux calibration is available, we provide a table with a single row with only a single calibration
value, or in some cases a multiple rows with multiple calibration values at different wavelengths. Only one
extension of this type is possible.

Table data is available with:
- fluxcal_hdu.data

Additional header information is available with:
- hdu_fluxcal.header['DYNMTYPE'] = 'fluxcal'
- hdu_fluxcal.header['FLUXCAL'] = same as the SpExoDisks header i.e. hdul[0].header['FLUXCAL']
- hdu_fluxcal.header['CALSTATE'] = same as the SpExoDisks header i.e. hdul[0].header['CALSTATE']

### Line Flux Measurements Extension dynamic_hdu.header['DYNMTYPE'] = 'lineflux'
0 - to any integer number of dynamic extensions of this type. One table per vibration transition, per molecule, 
per isotopologue.

Table data is available with:
- lineflux_hdu.data

Additional header information is available with:
- lineflux_hdu.header['DYNMTYPE'] = 'lineflux'
- lineflux_hdu.header['MOLECULE'] = molecule
- lineflux_hdu.header['ISOTOPOL'] = isotopologue
- lineflux_hdu.header['UPPERLVL'] = Upper vibration level
- lineflux_hdu.header['LOWERLVL'] = Lower vibration level
- lineflux_hdu.header['FLXTRANS'] = a label for the vibration transition

### Stacked Line Profiles dynamic_hdu.header['DYNMTYPE'] = 'stackedline'
0 - to any integer number of dynamic extensions of this type. One table per vibration transition, per molecule, 
per isotopologue.

Table data is available with:
- stackedline_hdu.data

Additional header information is available with:
- stackedline_hdu.header['DYNMTYPE'] = 'lineflux'
- stackedline_hdu.header['MOLECULE'] = molecule
- stackedline_hdu.header['ISOTOPOL'] = isotopologue
- stackedline_hdu.header['UPPERLVL'] = Upper vibration level
- stackedline_hdu.header['LOWERLVL'] = Lower vibration level
- stackedline_hdu.header['FLXTRANS'] = a label for the vibration transition
