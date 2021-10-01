=========================================================================
Python Version 3.7.9
=========================================================================

Requirements:
    Python version 3.X

Recommended:
    Please activate the virtual environment using following commands:
        python3 -m venv venv
        source venv/bin/activate

How to run: 
    1. download required packages in the requirements.txt file
        pip install -r requirements.txt
    2. Run the app
        python app.py
    3. Enter the name of files separated by comma(,) and JSON formatted result will be returned. 
        input example: Form W-2, Form 1095-C 
        output example: 
            [
                {
                    "form_number": "Form W-2", 
                    "form_title": "Wage and Tax Statement (Info Copy Only)", 
                    "min_year": "1954", 
                    "max_years": "2021"
                }, 
                {
                    "form_number": "Form 1095-C", 
                    "form_title": "Employer-Provided Health Insurance Offer and Coverage", 
                    "min_year": "2014", 
                    "max_years": "2020"
                }
            ]

        If user enter an invalid form name, it will return {"result": "No reuslt for {input}"} for only invalid form name. 
