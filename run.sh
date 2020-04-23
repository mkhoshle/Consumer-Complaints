#!/bin/bash
<<<<<<< HEAD
#
echo "First we check the code to see if it pass the tests" 
python src/test_complaint_analysis.py -v
=======

#echo "First we check the code to see if it pass the tests" 
#python src/test_complaint_analysis.py -v
>>>>>>> 7208cdf2ceaf0b52f19b268eb70992502b1d1337

echo "Running the main code to produce the result!"
python3.8 src/run.py --ipath 'input/complaints.csv' --opath 'output/report.csv'
