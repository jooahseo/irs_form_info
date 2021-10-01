from bs4 import BeautifulSoup
import requests
import json

BASE_URL = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"

def prompt_input():
    try:
        query = [ q.strip() for q in input("Enter the form names separated by comma(,) >> ").split(",")]
        get_all_data(query)
    except Exception as e:
        print(e)

def get_all_data(query):
    try:
        result = []
        for input in query:
            data = get_data(input)
            if data:
                result.append(data)
        print(json.dumps(result))
    except Exception as e:
        print(e)

def get_data(input):
    try:
        form_number = ""
        years = []
        title = ""

        start = 0
        while True:
            response = requests.get(f"{BASE_URL}?indexOfFirstRow={start}&sortColumn=sortOrder&value={input}&criteria=formNumber&resultsPerPage=200&isDescending=false")
            soup = BeautifulSoup(response.text, "lxml")

            if is_error(soup):
                break

            product_numbers = soup.find_all("td", class_="LeftCellSpacer")

            for product_number in product_numbers:
                product_text = product_number.a.text.strip()
                if product_text.lower() == input.lower():
                    title_td = product_number.findNext("td")
                    year_td = title_td.findNext("td")

                    form_number = product_text
                    title = title_td.text.strip()
                    years.append(year_td.text.strip())
            start += 200

        if form_number or len(years) or title: 
            years.sort()
            return {"form_number": form_number, "form_title":title, "min_year":years[0], "max_years":years[len(years)-1]}

        return {"result": f"No result for {input}"}
    except Exception as e:
        print(e)

def is_error(soup):
    if soup.find("div", class_="errorBlock"):
        return True
    return False

prompt_input()

