#!/usr/bin/env python
import pandas as pd
import os

class preprocessing:
    """A class for preprocessing input data and converting it to the desired format.

    Attributes:
        ipath: Path to the input file
        input: Pandas DataFrame representing input data read from file
        _data: Pandas DataFrame representing pre-processed data
    """

    def __init__(self,ipath=None):
        self.ipath = ipath                     # Path to the input file
        self.input = None                      # Raw Data
        self._data = pd.DataFrame()            # Pre-processed data

    @property
    def input_data(self):
        """Load input data from file and store it into a Pandas DataFrame."""
        if self.ipath != None:
            if not os.path.isfile(self.ipath):
                raise FileNotFoundError('The file does not exist')
            self.input = pd.read_csv(self.ipath,error_bad_lines=False,engine='python',
                                     encoding='utf-8')

        if self.input.empty:
            raise ValueError('No data to load')

    def make_lowercase(self):
        """Convert all strings to lower case."""
        cols = self.input.columns
        for x in cols:
            try:
                self._data[x] = self.input[x].str.lower()
            except Exception as AttributeError:
                pass
        self._data.columns = list(map(str.lower,self._data.columns))

    @staticmethod
    def split(x):
        """Split the column date received into three separate columns
        of Year, Month and Day"""
        return x.split('-')

    @property
    def extract_year(self):
        """Return the final pre-processed DataFrame in desired format."""
        Date_received = pd.DataFrame(map(self.split,self._data['date received']),
                                     columns=['year','month','day'])
        cols = list(self._data.columns)
        cols.remove('date received')
        self._data = pd.concat([Date_received,self._data[cols]],axis=1)

        return self._data
