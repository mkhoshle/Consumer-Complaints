#!/bin/bash

echo "First we check the code to see if it pass the tests" 
python src/test_complaint_analysis.py -v

echo "Running the main code to produce the result!"
python src/run.py --ipath 'input/complaints.csv' --opath 'output/report.csv'
