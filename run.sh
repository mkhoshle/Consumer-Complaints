#!/bin/bash

echo "First we check the code to see if it pass the tests" 
python3.8 src/run_tests.py -v

echo "Running the main code to produce the result!"
python3.8 src/run.py --ipath 'input/complaints.csv' --opath 'output/report.csv'
