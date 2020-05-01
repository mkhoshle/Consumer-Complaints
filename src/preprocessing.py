#!/usr/bin/env python
import csv
import os
import warnings
from collections import defaultdict, Counter

class preprocessing:
    """A class for preprocessing input data and converting it to the desired format.

    Attributes:
        ipath: Path to the input file
        input: representing input data read from file
    """

    def __init__(self,ipath=None):
        self.ipath = ipath                          # Path to the input file
        self.input = defaultdict(list)              # Raw Data

    def store_input(self,row):
        year = str.lower(row[0]).split('-')[0]
        product = str.lower(row[1]); company = str.lower(row[7])
        if row[0] and row[1] and row[7]:
            self.input[('year','product')].append((year,product))
            self.input[(('year','product'),'company')].append(((year,product),company))
        else:
            warnings.warn('Data needs to be cleaned',RuntimeWarning)

    @property
    def input_data(self):
        """Load input data from file and Convert all strings to lower case."""
        if self.ipath != None:
            if not os.path.isfile(self.ipath):
                raise FileNotFoundError('The file does not exist')

            with open(self.ipath, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                [self.store_input(row) for i,row in enumerate(reader) if i>0]

        if not self.input:
            raise ValueError('No data to load')

        return self.input
