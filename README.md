# Consumer-Complaints
Insight Data-engineering Code Challenge. The instructions to the challenge is given here: https://github.com/InsightDataScience/consumer_complaints

# My Approach
My approach to this problem include two parts:
1) Pre-processing where I prepare prepare the data for processing. (`preprocessing.py`) 
2) Consumer complaint analysis where I analyze data to deliver them in the final format. (`complaint_analysis.py`)

## Pre-processing
In this part the required columns including `company`, `product`, and `Date received` are stored into a dictionary.
`Date received` columns are splitted into three parts including `year`, `month`, and `day`. But only the `year` part is used. 
I also stored a separate column for (`year`, `product`) and ((`year`, `product`),`company`). This allows counting the number of complaints for each combination of (`year`, `product`) and the number of complaints per company for each year and product ((`year`, `product`),`company`).

## Consumer complaint analysis
In the analysis the count for each combination of (`year`, `product`) and ((`year`, `product`),`company`) are calculated. Using the calculated amounts the final report is formed which has the following columns:
`product`,`year`,`number of companies receiving a complaint`,`company with max complaints`, `The highest percentage of complaints directed at a single company.`

# Testsuite
The testsuites coded in `test_complaint_analysis.py` are designed to check the input format and make sure the input is in the desired format. In addition, the tests check the output format and make sure it matches the desired format.

# Instructions for running the code
Here are the steps needed to be taken to run instructions:
1) run  `./run.sh` from the command line.
2) If you want to use any other input data than the one in the `input` directory.
3) `python3.8 src/run.py --ipath 'input/complaints.csv' --opath 'output/report.csv'` will be run inside `run.sh` file. So in case you are using a different name or folder for the input and output files, make sure you update this line and provide the correct input.

**Note**:
- The classes `complaint_analysis` and `preprocessing` are called inside the `run.py` file and this file will later be run from `run.sh` file.
- The code is tested using the provided link by `Insight` and it passes the tests.
- The directory structure is in the desired format.
- Python3.8 is used for this code.
- The lines in the output file should be sorted by product (alphabetically) and year (ascending) as requested.
- No Pandas or any other external libraries that must be installed using 'pip' is used in these codes.
