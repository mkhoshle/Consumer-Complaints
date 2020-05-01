#!/usr/bin/env python
import unittest
import csv
import os
import re
from collections import defaultdict
from preprocessing import preprocessing
from complaint_analysis import complaint_analysis


class TestComplaintAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pp = preprocessing('insight_testsuite/test_2/input/complaints.csv')
        cls.processed_data = cls.pp.input_data
        with open(cls.pp.ipath, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            cls.items = [row for row in reader]
        cls.data = cls.items[1:]
        cls.header = cls.items[0]

    def test_header(self):
        expected_cols = ['Date received', 'Product', 'Sub-product', 'Issue', 'Sub-issue',
                         'Consumer complaint narrative', 'Company public response', 'Company',
                         'State', 'ZIP code', 'Tags', 'Consumer consent provided?',
                         'Submitted via', 'Date sent to company', 'Company response to consumer',
                         'Timely response?', 'Consumer disputed?', 'Complaint ID']
        
        self.assertEqual(self.header,expected_cols)

    def test_using_type(self):
        dic = defaultdict(list)
        dic['Date received'] = [row[0] for row in self.data]
        dic['product'] = [row[1] for row in self.data]
        dic['company'] = [row[7] for row in self.data]

        p = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
        assert all(map(p.match,dic['Date received']))
        assert all(isinstance(item, str) for item in dic['product'])
        assert all(isinstance(item, str) for item in dic['company'])


    def test_complaint(self):
        with open('insight_testsuite/test_2/output/report.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            report_correct = [row for row in reader]

        ca = complaint_analysis()
        ca.setReport(self.processed_data)
        report = ca.getReport
        report = [list(map(str,row)) for row in report]
        self.assertEqual(report,report_correct)

