# CS5293SP23-Project0

Name: Siddartha Sodum
Sooner ID: 113581755
Description:
The project aims to extract data from a PDF file containing summaries of arrests, cases, and incident reports in the Norman, which is available on the Police Department Website. In this project, we use python to process the downloaded file and extract the relevant data. The extracted data is then stored in SQLite3 database, enabling the retrieval of unique incident types and their frequency in the Norman area. The project involves the use of Python, GIT, Linux and SQLite3.
The following packages are installed:
1. Urlib
2. Requests 3. Argparse 4. re
5. PyPDF2 6. SQLite3 7. Io
8. Pytest
9. pandas
Structure:
  cs5293sp23-project0/
├── COLLABORATORS
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── docs
│   └── demo.gif
├── incidents.db
├── project0
│   ├── incidents.db
│ └── main.py
 ├── setup.cfg
├── setup.py
└── tests
    └── test_case.py
    
 Installment Procedure:
• To start the project, first, create a new directory named “project”: mkdir project
• Change the directory path to “project”: cd project
• Download the project file from git using the command: “https://github.com/siddu7999
/cs5293sp23-project0 “

• Navigate to the downloaded project directory and install pipenv by using the command “pip install pipenv“
• Install all the necessary packages required for the project using the command “pip install <packpagename>“
Execution:
• Inorder to execute the main.py we use the following command:
Pipenv run python3 project0/main.py –incidents <paste the url here>
• To run the unit test cases: pipenv run python -m pytest
External Links:
https://www.geeksforgeeks.org/write-regular-expressions/ https://docs.python.org/3.10/library/sqlite3.html
Assumptions:
• The code has been designed to handle PDF files that adhere to a particular format used by the Oklahoma Police Department website.
• It may not be able to effectively process PDF files with data spanning multiple lines, as it assumes that each line of text represents a single incident record.
Function Description:
The main.py consists of the following methods:
extractpdfpages():
• The extractpdfpages() method extracts the text from a PDF file located at a given URL using the PyPDF2 library.
• The function takes URL as an argument and returns a list of strings, where each string represents the text extracted from PDF file.
get_data():
• The function get_data() extracts data from each line of the input text by splitting the line on whitespace.
• It uses regular expressions to identify patterns in the strings.
• The extracted data includes the date, time, incidentnumber, location, nature of the incident, and
ORI number.
• The function uses Pandas DataFrame to store the extracted data and returns the dataframe.
Insertion():
• The function initially establishes a connection to the database using the sqlite3 module in Python.
• If the table “incidents” already exists in the database, it is dropped to avoid the conflicts, and then a
new table is created with columns for date, time, incident number, location, nature and ORI.
• Next, the data from the DataFrame is inserted into the table using to_sql() method.
  
• After, the data has been inserted, a query is executed to count the number of occurences of each unique value in the “nature” column.
Database Development:
A database is created to store the incident records using the database() method, which is defined in func.py and used by main.py. We build a table called "Incident data" in this database to store the records.
A table is created using:
CREATE TEABLE Incident_table (date TEXT, time TEXT, incident_nature TEXT, address TEXT, nature TEXT, ORI_number TEXT)

