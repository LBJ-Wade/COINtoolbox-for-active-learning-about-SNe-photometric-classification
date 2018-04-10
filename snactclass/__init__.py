"""Supernova Photometric Classifier using Active Learning."""

__author__ = "CRP #4 team"
__maintainer__ = "CRP #4"
__copyright__ = "Copyright 2017"
__version__ = "0.0.1"
__email__ = "iaa.coin@gmail.com"
__status__ = "Prototype"
__license__ = "GPL"

from analysis_functions.diagnostics import efficiency, purity, fom
from analysis_functions.ml_result import MLResult
from analysis_functions.print_output import save_results

from data_functions.loadData import loadData
from data_functions.randomiseData import randomiseData
from data_functions.read_SNANA import read_snana_lc
from data_functions.snid2filename import snid2filename

from actConfig.initialSetup import initialDataSetup, initialModelSetup
from actConfig.initialSetup import initialQuerySetup
from actConfig.learnLoop import learnLoop
from actConfig.print_output import save_results

#from lc_functions.light_curve_functions import karpenka_theano, karpenka
#from lc_functions.light_curve_functions import bazin, sanders_theano, sanders
#from lc_functions.light_curve_functions import newling
#from lc_functions.light_curve_plot import plot_lc_raw
#from lc_functions.pymc_plotting import plot_karpenka, plot_sanders
#from lc_functions.sn_observation import SNObservation, SNBand, FittedObservation

try:
    import threeML

    from lc_functions.threeml_functions import SN_Karpenka, SN_Bazin, SN_Newling
    from lc_functions.threeml_functions import SN_Sanders

except ImportError:
    pass
    