import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

specification_applicator_df = pd.read_excel("get_partner.xlsx")
product_desc = specification_applicator_df['components'].tolist()
partial_links = []

for each_partner in product_desc:

    driver.get('http://www.google.com')
    search = driver.find_element_by_name('q')

    search.send_keys(each_partner)
    search.send_keys(Keys.RETURN) # hit return after you enter search text
    time.sleep(2) # sleep for 5 seconds so you can see the results

    partial_links.append(driver.find_element_by_xpath("//h3[@class='LC20lb DKV0Md']").text)
    # print(partial_link)
    # specification_applicator_df.append({'partner': partial_link}, ignore_index=True)

specification_applicator_df.loc[:, 'partner'] = partial_links
print(specification_applicator_df)
specification_applicator_df.to_excel("partners file.xlsx")