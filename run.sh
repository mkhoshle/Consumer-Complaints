#!/bin/bash
#
echo "Installing the required packages"
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
pip install numpy==1.18.1
pip install pandas==1.0.3


echo "First we check the code to see if it pass the tests" 
python src/test_complaint_analysis.py -v

echo "Running the main code to produce the result!"
python src/run.py --ipath 'input/complaints.csv' --opath 'output/report.csv'
