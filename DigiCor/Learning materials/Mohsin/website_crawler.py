import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
import glob
import os
import csv

class Txt_maker:
    def __init__(self):
        self.url = ""
        self.url_list = []

        self.driver = ""
        # self.product_desc_list = []
        self.html = ""
        self.txt_file = ""
        self.intel_df = None
        self.expand_type = ""

    def get_txt(self, driver, each_prod, each_partner):

        self.driver = driver

        # self.expand_type = []
        # self.txt = []

        # for each in each_prod_parts_list:

        self.driver.get('http://www.google.com')
        search = self.driver.find_element_by_name('q')
        search.send_keys("supermicro:" + each_prod)
        search.send_keys(Keys.RETURN)  # hit Enter after you enter search text
        time.sleep(2)  # sleep for 2 seconds so you can see the results

        partial_links = self.driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md']")
        for each_partial_link in partial_links:
            if "FAQ" not in each_partial_link.text:
                each_partial_link.click()
                time.sleep(2)  # sleep for 3 seconds so you can see the results
                break

        # Checking if part lists/components is expanded or collapsed. Expand if collapsed
        expander = driver.find_elements_by_xpath("//div[@class='more']")
        if expander:
            # print(len(info))
            expander[-1].click()
        time.sleep(2)

        self.html = self.driver.page_source

        # with open("HTML.txt", "w", encoding="utf-8") as file:
        #     file.write(str(self.html))
        print(re.findall(r"<span>(.+?)</span> <i class=\"fa fa-angle-up", self.html))
        self.expand_type = re.findall(r"<span>(.+?)</span> <i class=\"fa fa-angle-up", self.html)[1]

        soup = BeautifulSoup(self.html, features="html.parser")
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out
        txt = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in txt.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        # self.txt = '\n'.join(chunk for chunk in chunks if chunk)
        self.txt_file = '\n'.join(chunk for chunk in chunks if chunk)

        # print(self.expand_type_list)
        return self.txt_file, self.expand_type

    def get_txt_supermicro(self, driver, each_prod):
        self.driver = driver
        self.driver.get('http://www.google.com')
        
        search = self.driver.find_element_by_name('q')
        search.send_keys(each_prod)
        search.send_keys(Keys.RETURN)  # hit Enter after you enter search text
        time.sleep(2)  # sleep for 2 seconds so you can see the results

        partial_links = self.driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md']")
        for each_partial_link in partial_links:
            if "FAQ" not in each_partial_link.text:
                each_partial_link.click()
                time.sleep(2)  # sleep for 3 seconds so you can see the results
                break

        result = {}
        specifications = ['spec-table-1', 'spec-table-2']
        for spec in specifications:
            tables1 = self.driver.find_element_by_class_name(spec).find_elements_by_tag_name('table')
            for table in tables1:
                trs = table.find_elements_by_tag_name('tr')
                if len(trs) > 4:
                    for tr in trs[3:]:
                        tds = tr.find_elements_by_tag_name('td')
                        result[tds[0].text] = tds[1].text.replace('\n', ' ')
                else:
                    result[trs[1].text] = trs[3].text.replace('\n', ' ')

        result_components = {}
        components = driver.find_element_by_class_name("part-list")
        for table in components.find_elements_by_tag_name('table'):
            trs = table.find_elements_by_tag_name('tr')
            if 'parts list' in trs[1].text.lower():
                for i in range(len(trs)):
                    if i > 3 :
                        tds = trs[i].find_elements_by_tag_name('td')
                        result_components[tds[0].text] = {'part': tds[0].text, ' value': tds[1].text, 'qty': tds[2].text, 'description': tds[3].text}
        data = pd.DataFrame(result, index=[0])
        return data

    def get_txt_intel(self, driver, each_prod):

        self.driver = driver

        # for each in each_prod_parts_list:

        self.driver.get('http://www.google.com')
        search = self.driver.find_element_by_name('q')
        search.send_keys("intel:" + each_prod)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        time.sleep(2)  # sleep for 2 seconds so you can see the results

        partial_links = self.driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md']")
        for each_partial_link in partial_links:
            if "FAQ" not in each_partial_link.text:
                each_partial_link.click()
                time.sleep(2)  # sleep for 3 seconds so you can see the results
                break
        try:
            self.driver.find_element_by_partial_link_text("Download software and").click()
            self.driver.find_element_by_partial_link_text("Product specifications").click()
            print("hard intel")
        except:
            print("easy intel")

        self.driver.find_element_by_partial_link_text("Export specification").click()
        time.sleep(3)

        # get list of files from downloads directory
        list_of_files = glob.glob('/Users/mohsinkhan/Downloads/*.xls')  # * for all files
        latest_file = max(list_of_files, key=os.path.getctime)
        latest_file = latest_file.replace("/", "\\")
        print(latest_file)

        self.intel_df = pd.read_html(latest_file)

        return self.intel_df