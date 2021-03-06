# Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies. For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

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
The testsuite's codes in `testDir` are designed to check the input format and make sure the input is in the desired format. In addition, the tests check the output format and make sure it matches the desired format. 
All the requested test data are located inside `insight_testsuite`.

# Instructions for running the code
Here are the steps needed to be taken to run instructions:
1) If you want to use any other input data than the one in the `input` directory make sure you provide the correct path in `run.sh` that requires the user to provide the path to the input and output files. The default are 'input/complaints.csv' for input file and 'output/report.csv' for output file.
2) `python3.8 src/run.py --ipath 'input/complaints.csv' --opath 'output/report.csv'` will be run inside `run.sh` file. 
3) execute `./run.sh` from the command line to run all the codes and produce the desired output.

# Notes:
- The classes `complaint_analysis` and `preprocessing` are called inside the `run.py` file and this file will later be run from `run.sh` file.
- The code is tested using the provided link by `Insight` and it passes the tests.
- The directory structure is in the desired format.
- Python3.8 is used for this code.
- The lines in the output file should be sorted by product (alphabetically) and year (ascending) as requested.
- No Pandas or any other external libraries that must be installed using 'pip' is used in these codes.
- The output data (`report.csv`) obtained from the input data provided [here](http://files.consumerfinance.gov/ccdb/complaints.csv.zip) is stored inside the `output` directory.
