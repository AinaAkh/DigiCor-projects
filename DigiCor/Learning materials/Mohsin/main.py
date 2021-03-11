from regexes import Regexer
from website_crawler import Txt_maker
from selenium import webdriver
import re
import pandas as pd
import numpy as np

specification_applicator_df = pd.read_excel("get_partner.xlsx")
# specification_applicator_df = pd.read_excel("specification_applicator_data.xlsx", header=1, sheet_name="Specs")
# specification_applicator_df = pd.read_excel("Custom_spec.xlsx", sheet_name="Sheet2")
product_desc_list = specification_applicator_df['components'].tolist()
partner_list = specification_applicator_df['partner'].tolist()
desc_partner_dict = dict(zip(product_desc_list, partner_list))


# setting chrome driver and download location
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/Users/mohsinkhan/Downloads/"}
options.add_experimental_option('prefs', prefs)
# PATH = "C:\Program Files (x86)\chromedriver.exe"
PATH = "/Users/mohsinkhan/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=PATH, options=options)

txt_maker_obj = Txt_maker()
regexer_obj = Regexer()

product_desc_list = ["743TQ-1200B-SQ", "826BE1C4-R1K23LPB", "216BE1C4-R1K23LPB",
                     "745BAC-R1K28B2","745TQ-R920B", "X11DPi-N"]
partner_list = ["supermicro", "supermicro", "supermicro", "supermicro", "supermicro", "supermicro"]

# product_desc_list = ["X11DPi-N"]
# partner_list = ["supermicro"]

df = pd.DataFrame(columns=list(regexer_obj.__dict__.keys()))

i = 1

for each_prod, each_partner in list(zip(product_desc_list, partner_list)):

    if "supermicro" in each_partner:
        print(i, each_prod, each_partner)
        supermicro_data = txt_maker_obj.get_txt_supermicro(driver, each_prod)
        # supermicro_data = supermicro_data.replace(np.nan, '', regex=True)
        # supermicro_data.to_excel('supermicro_chassic.xls')
        supermicro_data.to_excel('supermicro_motherboard.xls')
        if len(each_prod) >= 10:
            product_type = "chassic"
            regexer_obj.run_regexes_supermicro_chassic(supermicro_data, product_type,  each_prod, each_partner)
        else:
            product_type = "motherboard"
            regexer_obj.run_regexes_supermicro_chassic(supermicro_data, product_type, each_prod, each_partner)


    if "intel" in each_partner:
        print(i, each_prod, each_partner)
        intel_df = txt_maker_obj.get_txt_intel(driver, each_prod)
        regexer_obj.run_regexes_intel(intel_df)

    if "Seagate" in each_partner:
        print("seagate is digicor")

    df = df.append(regexer_obj.__dict__, ignore_index=True)
    print(i, "DONE: "+each_prod)
    i = i + 1

driver.quit()
df.to_excel("final.xlsx")