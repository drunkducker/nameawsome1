from os.path import dirname, basename, isfile
import glob

# Automatically import all vocabulary files in the directory
modules = glob.glob(dirname(__file__)+"/*.voc")
__all__ = [basename(f)[:-4] for f in modules if isfile(f)]
