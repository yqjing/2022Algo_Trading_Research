__all__ = ['SAVEFOLDER', 'PROCESSEDDATAFOLDER', 'GRAPHICSFOLDER',
           'NUM_INTERVALS', 'NUM_INTERVALS_IN_FILE', 'ALL_SYMBOLS', 'ALL_DAYS',
           'DEBUG', 'logger']

import inspect
import os
CUR_DIR = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

SAVEFOLDER = CUR_DIR + "/Pickle/"
PROCESSEDDATAFOLDER = CUR_DIR + "/Data/"
GRAPHICSFOLDER = CUR_DIR + "/GraphicsFolder/"

# SAVEFOLDER = "/Pickle/"
# PROCESSEDDATAFOLDER = "/Data/"
# GRAPHICSFOLDER = "/GraphicsFolder/"
NUM_INTERVALS = 390
NUM_INTERVALS_IN_FILE = 392
ALL_SYMBOLS = ["AAPL"]
ALL_DAYS = [
    '20220401', '20220404', '20220405', '20220406', '20220407', '20220408',
    '20220411', '20220412', '20220413', '20220414', '20220418', '20220419',
    '20220420', '20220421', '20220422', '20220425', '20220426', '20220427',
    '20220428', '20220429', '20220502', '20220503', '20220504', '20220505',
    '20220506', '20220509', '20220510', '20220511', '20220512', '20220513',
    '20220516', '20220517', '20220518', '20220519', '20220520', '20220523',
    '20220524', '20220525', '20220526', '20220527', '20220531', '20220601',
    '20220602', '20220603', '20220606', '20220607', '20220608', '20220609',
    '20220610', '20220613', '20220614', '20220615', '20220616', '20220617',
    '20220621', '20220622', '20220623', '20220624', '20220627', '20220628']

DEBUG = True

# logs - export only the logger
import logging
reload(logging)  # for iPython interactive usage
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler(CUR_DIR + '/../code_errors_log_.txt')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)
