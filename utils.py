import os
import sys
import csv
import time
import math
import glob
import os.path

import json
import difflib
import numpy as np
import pandas as pd
import seaborn as sns
import sys, networkx as nx
import dynetworkx as dnx
import matplotlib.pyplot as plt
from sklearn import preprocessing
from matplotlib.animation import FuncAnimation
from sklearn.cluster import AffinityPropagation
from scipy import stats, optimize

import random
from scipy.stats import bernoulli
import scipy.linalg as la
import scipy.sparse as sparse
import scipy.sparse.linalg as sla
#------------------------------------------------------------------------------
def rankorder(x):
#   """

#   Parameters
#   ----------   
    
#   :param list x: list of int

#   Returns
#   -------
#   :returns: Rankordering, i.e. descending list of occured values 
#   :rtype: list(int), list(int)    
    
    x1 = list(np.sort(x))
    x1.reverse()
    y1 = range(1,len(x1)+1)
    return np.array(x1),np.array(y1)
#------------------------------------------------------------------------------