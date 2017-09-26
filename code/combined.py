import glob
import numpy
import matplotlib.pyplot
import scipy.ndimage
import pytesseract
import PIL.Image
from toolz.curried import map, pipe, compose, get, do, curry, count, pluck, juxt, flip
import pandas
import skimage
import skimage.measure
import skimage.filters
import skimage.morphology

import dask
import json
from dask.multiprocessing import get as dak_get

from dask.diagnostics import ResourceProfiler, Profiler, CacheProfiler, ProgressBar, visualize
from dask import compute
from dask.dot import dot_graph

from threshold import *
from min_size import *
from clean import *
from reveal import *
from pearlite import *
from ferrite import *
from cemmentite import *
from save import *

def finalize(saves):
    print("done.")
    
data_path = "/Users/fyc/Desktop/Hackaton-09-11-2017/Demo/study/data"

dsk = {}
files = sorted(glob.glob("{0}/*.tif".format(data_path)))
final_saves = []
for filename in files:
    filename_cleaned = filename.split("/")[-1].split(".")[0]
    dsk['threshold-{0}'.format(filename_cleaned)] = (threshold, filename)
    dsk['min_size-{0}'.format(filename_cleaned)] = (min_size, 'threshold-{0}'.format(filename_cleaned))
    dsk['clean-{0}'.format(filename_cleaned)] = (clean, 'min_size-{0}'.format(filename_cleaned))
    dsk['reveal-{0}'.format(filename_cleaned)] = (reveal, 'clean-{0}'.format(filename_cleaned))
    dsk['pearlite-{0}'.format(filename_cleaned)] = (pearlite, 'reveal-{0}'.format(filename_cleaned))
    dsk['ferrite-{0}'.format(filename_cleaned)] = (ferrite, 'pearlite-{0}'.format(filename_cleaned))
    dsk['cemmentite-{0}'.format(filename_cleaned)] = (cemmentite, 'ferrite-{0}'.format(filename_cleaned))
    dsk['save-{0}'.format(filename_cleaned)] = (save, 'cemmentite-{0}'.format(filename_cleaned))
    final_saves.append('save-{0}'.format(filename_cleaned))
dsk['finalize'] = (finalize, final_saves)

dot_graph(dsk)

with ResourceProfiler(0.25) as rprof, Profiler() as prof, CacheProfiler() as cprof, ProgressBar():
    dak_get(dsk, 'finalize')

visualize([prof, rprof, cprof])