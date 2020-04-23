#!/usr/bin/env python
import csv
import os
from collections import defaultdict, Counter

class complaint_analysis:
    """A class for performing all the calculations and delivering output in the desired format.

    Attributes:
        opath: Path to the output file
        _report: Pandas DataFrame representing pre-processed data
    """

    def __init__(self,opath=None):
        self.opath = opath          # Path to the output file
        self._report = []           # Output

    @property
    def getReport(self):
         return self._report

    def setReport(self,data):
        """Return the report DataFrame."""
        yp = Counter(data[('year', 'product')])
        ypc = Counter(data[(('year', 'product'), 'company')])

        for k1 in yp.keys():
            comp_per_company = []
            for k2 in ypc.keys():
                if k2[0]==k1:
                    comp_per_company.append(ypc[k2])
            max_ = max(comp_per_company)
            self._report.append([k1[1],k1[0],yp[k1],max_,round(max_/yp[k1]*100)])

        self._report = sorted(self._report, key = lambda x: (x[0],x[1]))

    @property
    def write_data(self):
        """Write the reported output into csv file."""
        if self.opath != None:
            if self._report is None:
                raise ValueError('No output to write')

            with open(self.opath, "w", newline="") as f:
                writer = csv.writer(f,delimiter=',')
                writer.writerows(self._report)
