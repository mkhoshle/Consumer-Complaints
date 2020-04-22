#!/usr/bin/env python
import numpy as np
import pandas as pd
import unittest
from pandas._testing import assert_frame_equal
from preprocessing import preprocessing
from complaint_analysis import complaint_analysis

class TestComplaintAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls): 
        cls.pp = preprocessing('insight_testsuite/test_1/input/complaints.csv')
        cls.pp.input_data
        cls.pp.make_lowercase()
        cls.data = cls.pp.extract_year

    def test_header(self):
        expected_cols = ['Date received', 'Product', 'Sub-product', 'Issue', 'Sub-issue',
                         'Consumer complaint narrative', 'Company public response', 'Company',
                         'State', 'ZIP code', 'Tags', 'Consumer consent provided?',
                         'Submitted via', 'Date sent to company', 'Company response to consumer',
                         'Timely response?', 'Consumer disputed?', 'Complaint ID']

        data = self.pp.input
        self.assertEqual(list(data.columns),expected_cols)

    def test_using_type(self):
        assert self.pp.input['Date received'].str.match('[0-9]{4}-[0-9]{2}-[0-9]{2}').all()
        assert self.data['product'].map(type).eq(str).all()
        assert self.data['company'].map(type).eq(str).all()


    def test_complaint(self):
        report_correct = pd.read_csv('insight_testsuite/test_1/output/report.csv',error_bad_lines=False,engine='python',
                                     encoding='utf-8',header=None)     

        ca = complaint_analysis()
        ca.setReport(self.data)
        report = ca.getReport

        assert_frame_equal(report,report_correct)

if __name__ == "__main__":
    unittest.main() 
