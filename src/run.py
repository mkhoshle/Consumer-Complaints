#!/usr/bin/env python
import argparse
from preprocessing import preprocessing
from complaint_analysis import complaint_analysis

parser = argparse.ArgumentParser()
parser.add_argument('--ipath', help='Path to the input file',required=True)
parser.add_argument('--opath', help='Path to the output file',required=True)
args = vars(parser.parse_args())

print('Ready to pre-process the data')
pp = preprocessing(args['ipath'])
pp.input_data
pp.make_lowercase()
data = pp.extract_year

print('Pre-processed data is ready')
ca = complaint_analysis(args['opath'])
ca.setReport(data)
ca.write_data

print('Ouput file written to the disk')

