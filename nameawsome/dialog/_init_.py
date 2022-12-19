from os.path import dirname, basename, isfile
import glob

# Automatically import all dialog files in the directory
modules = glob.glob(dirname(__file__)+"/*.dialog")
__all__ = [basename(f)[:-7] for f in modules if isfile(f)]
