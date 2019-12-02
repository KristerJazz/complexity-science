import numpy as np
import pandas as pd

class DataCollector:
    def __init__(self, collector):
        self.data = []
        self.flist = []
        self.columns = []
        
        for key, f in collector.items():
            self.flist.append(f)
            self.columns.append(key)

    def collect(self, array):
        collected = [] 
        for f in self.flist:
            collected.append(f(array))
        self.data.append(collected)

    def data_to_pd(self):
        self.data = pd.DataFrame(self.data, columns = self.columns)
        return self.data
