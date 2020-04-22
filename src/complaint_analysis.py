#!/usr/bin/env python
import pandas as pd
import os

class complaint_analysis:
    """A class for performing all the calculations and delivering output in the desired format.

    Attributes:
        opath: Path to the output file
        _report: Pandas DataFrame representing pre-processed data
    """

    def __init__(self,opath=None):
        self.opath = opath          # Path to the output file
        self._report = []           # Output

    def percentage_complaint(self,df,index,i):
        """Return the highest percentage of complaints directed at a single company."""
        out = ((len(group),len(group)/len(df)*100) for ind, group in df.groupby('company'))
        max_ = max(out, key= lambda x: x[1])

        self._report[i].append(max_[0])
        self._report[i].append(round(max_[1]))

    @property
    def getReport(self):
         self._report = pd.DataFrame(self._report).sort_values(by=[0])
         self._report = self._report.reset_index(drop=True)
         return self._report

    def setReport(self,data):
        """Return the report DataFrame."""
        for i,(index,group) in enumerate(data.groupby(['year','product'])):
            self._report.append([index[1],int(index[0]),len(group)])
            self.percentage_complaint(group,index,i)

    @property
    def write_data(self):
        """Write the reported output into csv file."""
        if self.opath != None:
            if not self._report:
                raise ValueError('No output to write')
            if not os.path.isfile(self.opath):
                raise FileNotFoundError('The file does not exist')
            pd.DataFrame(self._report).to_csv(self.opath,sep=',',index=False,header=False)
