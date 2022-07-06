from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(executable_path = r"C:\Users\fitte\Downloads\scrapper\chromedriver.exe")

browser.get(start_url)
time.sleep(1)

def scrape():
    headers = ["Proper name", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0,4):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("td"):
            tr_tags = tr_tag.find_all("tr")
            temp_list = []
            for index, td_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
    with open("sutars.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()
