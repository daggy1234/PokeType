import warnings
warnings.filterwarnings('ignore')

from .interpreter import PokeType
import logging
import warnings

__title__ = "poketype"
__version__ ="1.0.0"
__author__ = 'Daggy1234'
__license__ = 'MIT'

logging.getLogger(__name__).addHandler(logging.NullHandler())