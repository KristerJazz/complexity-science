import numpy as np
import pandas as pd

class DataCollector:
    def __init__(self, collector=['mean'], custom_function=[]):
        self.data = "Nice"#pd.DataFrame() 
        self.flist = []

        if 'mean' in collector:
            self.flist.append(np.average)
        if 'min' in collector:
            self.flist.append(np.amin)
        if 'max' in collector:
            self.flist.append(np.amax)
        if custom_function:
            for f in custom_function:
                self.flist.append(f)

    def collect(self, array):
        for f in self.flist:
            f(array)
