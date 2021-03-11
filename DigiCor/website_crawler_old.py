from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup, Doctype
import re
import pandas as pd
import glob
import os
import io
from urllib.request import Request, urlopen
from lxml import html, etree
import lxml.html
import lxml.html.soupparser
import requests
from more_itertools import flatten


class Txt_maker:
    def __init__(self):
        self.url = ""
        self.url_list = []

        self.driver = ""
        # self.product_desc_list = []
        self.html = ""
        self.txt_file = ""
        # self.supermicro_df = None
        self.intel_df = None
        # self.asus_df = None
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
        time.sleep(5)

        self.html = self.driver.page_source

        # with open("HTML.txt", "w", encoding="utf-8") as file:
        #     file.write(str(self.html))
        # print(re.findall(r"<span>(.+?)</span> <i class=\"fa fa-angle-up", self.html))
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

    def get_txt_supermicro(self, driver, boms_id, product_type, each_prod, partner, item_type): 
        self.driver = driver
        self.driver.get('http://www.google.com') 

        data_dict = {'boms_id': boms_id, 'partner': partner, 'desc': each_prod, 'type': item_type}
        data = pd.DataFrame(data_dict, index=[0])

        search = self.driver.find_element_by_name('q')
        search.send_keys("supermicro:" + each_prod)
        search.send_keys(Keys.RETURN)  # hit Enter after you enter search text
        time.sleep(2)  # sleep for 2 seconds so you can see the results

        def get_key_features(item_type):
            if item_type in ['D','S']:
                key_specs = driver.find_elements_by_class_name('key-feature-list')
            else:
                key_specs = driver.find_elements_by_class_name('spec-key-features')

            key_specs_data = [specs_data.text for specs_data in key_specs]
            key_specs_data = [specs_data.split('\n') for specs_data in key_specs_data]
            key_specs_data = [item for sublist in key_specs_data for item in sublist]
            key_specs_data = list(filter(None, key_specs_data))
            data_new = pd.DataFrame(key_specs_data, columns=['raw']) 
            key_features = {}
            try:
                key_features['pcl_express_x16_slots']= data_new.raw.str.extractall(r'(\d+\sPCI.*16)')[0][0]
            except:
                key_features['pcl_express_x16_slots']='NA'

            try:
                key_features['pcl_express_x8_slots']= data_new.raw.str.extractall(r'(\d+\sPCI.*8)')[0][0]
            except:
                key_features['pcl_express_x8_slots']='NA'

            try:
                key_features['pcl_express_slots_version']= [item.split(' ',1) for item in [''.join(i if re.search(r'[\d\.+]?(.*PCI-E.*)', i) else '' for i in key_specs_data)]][0][1]
            except:
                key_features['pcl_express_slots_version']='NA'

            try:
                key_features['maximum_internal_memory']= data_new.raw.str.extractall(r'([0-9.]+?TB)|([0-9.]+?tb)')[0][0]
            except:
                key_features['maximum_internal_memory']='NA'

            try:
                key_features['usb_3_0_type_a_ports_quantity']= data_new.raw.str.extractall(r'(\d+ USB 3.0)')[0][0]
            except:
                key_features['usb_3_0_type_a_ports_quantity']='NA'

            try:
                key_features['usb_2_0_type_a_ports_quantity']= data_new.raw.str.extractall(r'(\d+ USB 2.0)')[0][0]
            except:
                key_features['usb_2_0_type_a_ports_quantity']= 'NA'

            try:
                key_features['processor_socket']=[item.split(' ',1) for item in [''.join(i if re.search(r'(.*Socket.*)', i) else '' for i in key_specs_data)]][0][1]
            except:
                try:
                    key_features['processor_socket']= [item.split(' ',1) for item in [''.join(i if re.search(r'(.*socket.*)', i) else '' for i in key_specs_data)]][0][1]
                except:
                    key_features['processor_socket']= 'NA'
                    
            try:
                key_features['num_of_storage_drives_supported']= data_new.raw.str.extractall(r'(\d+ )Hot')[0][0]
            except:
                key_features['num_of_storage_drives_supported']= 'NA'
            
            try: 
                key_features['onboard_network_controllers'] = data_new.raw.str.extractall(r'(.*-T)')[0][0][3:]
            except:
                key_features['onboard_network_controllers'] = 'NA'
            
            try: 
                key_features['num_of_dimm_slots']= data_new.raw.str.extractall(r'(DD.*)')[0][0]
            except:
                key_features['num_of_dimm_slots']= 'NA'
                
            try:
                key_features['num_of_dimm_slots'] = data_new.raw.str.extractall(r'(.*;)')[0][0][3:]
            except:
                key_features['num_of_dimm_slots'] = 'NA'
                
            try:
                key_features['backplanes_support'] = data_new.raw.str.extractall(r'(SATA\d+)')[0][0]
            except:
                key_features['backplanes_support'] = 'NA'
                
            try:
                key_features['power_supply']= data_new.raw.str.extractall(r'(\d+W.*)')[0][0]
            except:
                key_features['power_supply']='NA'
                
            try:
                if data_new.raw.str.extractall(r'(ECC)')[0][0]: key_features['ecc'] = 'Y' 
                else: key_features['ecc'] = 'N'
            except:
                key_features['ecc'] = 'NA'
                
            return key_features

        def get_key_features_chassis_motherboard(item_type, product_type):
            key_specs = driver.find_elements_by_class_name('key-feature-list')
            key_specs_data = [specs_data.text for specs_data in key_specs]
            key_specs_data = [specs_data.split('\n') for specs_data in key_specs_data]
            key_specs_data = [item for sublist in key_specs_data for item in sublist]
            key_specs_data = list(filter(None, key_specs_data))
            data_new = pd.DataFrame(key_specs_data, columns=['raw']) 
            key_features = {}
            try:
                key_features['pcl_express_x16_slots']= data_new.raw.str.extractall(r'(\d+\sPCI.*16)')[0][0]
            except:
                key_features['pcl_express_x16_slots']='NA'

            try:
                key_features['pcl_express_x8_slots']= data_new.raw.str.extractall(r'(\d+\sPCI.*8)')[0][0]
            except:
                key_features['pcl_express_x8_slots']='NA'

            try:
                key_features['pcl_express_slots_version']= [item.split(' ',1) for item in [''.join(i if re.search(r'[\d\.+]?(.*PCI-E.*)', i) else '' for i in key_specs_data)]][0][1]
            except:
                key_features['pcl_express_slots_version']='NA'

            try:
                key_features['maximum_internal_memory']= data_new.raw.str.extractall(r'([0-9.]+?TB)|([0-9.]+?tb)')[0][0]
            except:
                key_features['maximum_internal_memory']='NA'

            try:
                key_features['usb_3_0_type_a_ports_quantity']= data_new.raw.str.extractall(r'(\d+ USB 3.0)')[0][0]
            except:
                key_features['usb_3_0_type_a_ports_quantity']='NA'

            try:
                key_features['usb_2_0_type_a_ports_quantity']= data_new.raw.str.extractall(r'(\d+ USB 2.0)')[0][0]
            except:
                key_features['usb_2_0_type_a_ports_quantity']= 'NA'

            try:
                key_features['processor_socket']=[item.split(' ',1) for item in [''.join(i if re.search(r'(.*Socket.*)', i) else '' for i in key_specs_data)]][0][1]
            except:
                try:
                    key_features['processor_socket']= [item.split(' ',1) for item in [''.join(i if re.search(r'(.*socket.*)', i) else '' for i in key_specs_data)]][0][1]
                except:
                    key_features['processor_socket']= 'NA'
            
            try: 
                key_features['onboard_network_controllers'] = data_new.raw.str.extractall(r'(.*-T)')[0][0][3:]
            except:
                key_features['onboard_network_controllers'] = 'NA'
            
            try: 
                key_features['num_of_dimm_slots']= data_new.raw.str.extractall(r'(DD.*)')[0][0]
            except:
                key_features['num_of_dimm_slots']= 'NA'
                
            try:
                key_features['num_of_dimm_slots'] = data_new.raw.str.extractall(r'(.*;)')[0][0][3:]
            except:
                key_features['num_of_dimm_slots'] = 'NA'
                
            try:
                key_features['backplanes_support'] = data_new.raw.str.extractall(r'(SATA\d+)')[0][0]
            except:
                key_features['backplanes_support'] = 'NA'
                
            try:
                if data_new.raw.str.extractall(r'(ECC)')[0][0]: key_features['ecc'] = 'Y' 
                else: key_features['ecc'] = 'N'
            except:
                key_features['ecc'] = 'NA'
                
            return key_features, data_new



        # Specifications data page
        def get_specifications(item_type):
            specs_data = {}
            specifications = ['spec-table-1', 'spec-table-2']
            for spec in specifications:
                tables1 = driver.find_element_by_class_name(spec).find_elements_by_tag_name('table')
                for table in tables1:
                    trs = table.find_elements_by_tag_name('tr')
                    if len(trs) > 4:
                        if trs[2].text != '':
                            specs_data['Power Supply'] = trs[2].text
                        for tr in trs[3:]:
                            tds = tr.find_elements_by_tag_name('td')
                            specs_data[tds[0].text] = tds[len(tds) - 1].text.replace('\n', ' ')
                    elif 0 < len(trs) <= 4:
                        try:
                            specs_data[trs[1].text] = trs[len(trs) - 1].text.replace('\n', ' ')
                        except:
                            print('Data Extracted but tag error')
                    else:
                        specs_data[trs[1].text] = trs[0].text.replace('\n', ' ') 
            
            # process the specs data
            specs_data_dict = {}
            temp_humid = {}
            weight_dict = {}
            m_2 = {}

            if not item_type in ['D','S']: 
                try:
                    temp_humid = dict([item.split(':') for item in list(filter(None, specs_data['Environmental Spec.'].strip().split(')')))])
                except:
                    temp_humid = dict([item.split(':') for item in list(
                        filter(None, [i for i in specs_data['Environmental Spec.'].split(') ') if ':' in i]))])

                pecs_data_dict['chassis']= specs_data[[col for col in specs_data.keys() if 'model' in col.lower()][0]]
            else:
                specs_data_dict = {**pd.DataFrame(specs_data, index=[0])[[col for col in specs_data.keys() if 'operating' in col.lower()]].to_dict('record')[0]}
                try:
                    specs_data_dict['chassis']= specs_data[[col for col in specs_data.keys() if 'sku' in col.lower()][0]].split()[0]
                except:
                    specs_data_dict['chassis']= specs_data[[col for col in specs_data.keys() if each_prod.lower() in col.lower()][0]].split()[0]
            
            try: 
                specs_data_dict['motherboard']=specs_data[[col for col in specs_data.keys() if 'motherboard' in col.lower()][0]]
            except: 
                try:
                    specs_data_dict['motherboard']=specs_data[[col for col in specs_data.keys() if 'x1' in col.lower()][0]]
                except:
                    specs_data_dict['motherboard'] = 'NA' 
            
            try: 
                specs_data_dict['CPU'] = specs_data['CPU']
            except: 
                try: 
                    specs_data_dict['CPU'] = specs_data['Processor/Cache']
                except: 
                    specs_data_dict['CPU'] = 'NA'
                
            specs_data_dict['form_factor']=specs_data[[col for col in specs_data.keys() if 'form factor' in col.lower()][0]]

            # if len(key_specs_data['power_supply'] == 'NA') > 0:
            #     try:
            #         if specs_data[[col for col in specs_data.keys() if 'power supply' in col.lower()][0]]:
            #             key_specs_data['power_supply']=specs_data[[col for col in specs_data.keys() if 'power supply' in col.lower()][0]]
            #         else:
            #             key_specs_data['power_supply']='NA'     
            #     except: 
            #         key_specs_data['power_supply']=key_specs_data['power_supply']
            
            try:
                specs_data_dict['chipset']=specs_data[[col for col in specs_data.keys() if 'chipset' in col.lower()][0]]
            except:
                specs_data_dict['chipset']='NA'
            try:
                specs_data_dict['cores']=specs_data[[col for col in specs_data.keys() if 'cores' in col.lower()][0]]
            except:
                specs_data_dict['cores']='NA'
            specs_data_dict['height_mm']=specs_data[[col for col in specs_data.keys() if 'height' in col.lower()][0]]
            specs_data_dict['width_mm']=specs_data[[col for col in specs_data.keys() if 'width' in col.lower()][0]]
            specs_data_dict['depth_mm']=specs_data[[col for col in specs_data.keys() if 'depth' in col.lower()][0]]
            try:
                specs_data_dict['product_colour']=specs_data[[col for col in specs_data.keys() if 'available colors' in col.lower()][0]]
            except:
                specs_data_dict['product_colour']='Black'

            try:
                key_specs_data['onboard_network_controllers'] = specs_data['Network Controllers']
            except:
                key_specs_data['onboard_network_controllers'] = 'NA'
                
            try: key_specs_data['num_of_dimm_slots']= re.search(r'(\d+)\sDIMM', specs_data['Memory Capacity'])[0]
            except: key_specs_data['num_of_dimm_slots']= 'NA'
            try:
                specs_data_dict['drive_bays'] = specs_data['Drive Bays']
            except:
                specs_data_dict['drive_bays'] = [value for key,value in specs_data.items() if key.startswith("Drive Bays")]
            specs_data_dict['Supported_memory_types']= specs_data['Memory Type']

            # specs_data_dict['maximum_supported_ram_clock_speed_mhz']= re.search(r'(\d+){1}', specs_data['Memory Type'])[0]

            try: 
                m_2_features = list(flatten([item.split(':') for item in list(filter(None, specs_data['M.2'].strip().split(')')))]))
                for item in m_2_features:
                    if '1x' in item:
                        m_2['num_of_m_2_supported'] = m_2_features[0].split('x')[0]
                    else:
                        m_2['num_of_m_2_supported'] = 1 
                    if 'pci' in item.lower():
                        m_2['m_2_interface'] = item
                    if ' key' in item.lower():
                        m_2['m_2_form_factor'] = item.split('Key')[0]

                    m_2['m_2_key'] = m_2_features[len(m_2_features) - 1]
            except:
                m_2['num_of_m_2_supported'] = 'NA'
                m_2['m_2_interface'] = 'NA'
                m_2['m_2_form_factor'] = 'NA'
                m_2['m_2_key'] = 'NA'

            try:
                if len(m_2['m_2_interface']) >0:
                    string = m_2['m_2_interface']
                    m_2['num_of_m_2_supported'] = re.search(r'(\d+)', string)[0]
            except:
                m_2['num_of_m_2_supported'] = 'NA'

            try:
                weight = specs_data[[col for col in specs_data.keys() if 'weight' in col.lower()][0]]
                try:
                    weight_dict = dict([item.split(':') for item in list(filter(None, weight.strip().split(')')))])
                except: 
                    specs_data_dict[' Gross Weight'] = weight
            except:         
                specs_data_dict['Net Weight'] = 'NA'
                specs_data_dict[' Gross Weight'] = 'NA'
            
            specs_data_dict = {**specs_data_dict, **m_2, **temp_humid, **weight_dict}
            
            if len(key_specs_data[key_specs_data.pcl_express_x16_slots == "NA"]) > 0:
                try: 
                    if specs_data[[col for col in specs_data.keys() if 'pci' in col.lower()][0]]:
                        key_specs_data['pcl_express_x16_slots'] = specs_data[[col for col in specs_data.keys() if 'pci express' in col.lower()][0]]
                except:
                    try:
                        key_specs_data['pcl_express_x16_slots'] = key_specs_data.pcl_express_slots_version[0].split(',')[0]
                    except:
                        key_specs_data['pcl_express_x16_slots'] = 'NA'
            try:          
                USB = specs_data['USB'].split(')')
                if len(key_specs_data[key_specs_data.usb_3_0_type_a_ports_quantity == "NA"]) > 0:
                    key_specs_data['usb_3_0_type_a_ports_quantity'] = USB[0]
                if len(key_specs_data[key_specs_data.usb_2_0_type_a_ports_quantity == "NA"]) > 0:
                    key_specs_data['usb_2_0_type_a_ports_quantity'] = USB[1]
            except: 
                pass

            try:
                specificationd_data = pd.DataFrame(specs_data_dict, index= [0])
            except: 
                specificationd_data = pd.DataFrame([specs_data_dict], index =[0])

            specs_data_dict = {**specs_data_dict, **m_2, **temp_humid, **weight_dict}

            return specs_data_dict, specs_data

        def get_specifications_chassis_motherboard(item_type, product_type):
            specs_data = {}
            specifications = ['spec-table-1', 'spec-table-2']
            for spec in specifications:
                tables1 = driver.find_element_by_class_name(spec).find_elements_by_tag_name('table')
                for table in tables1:
                    trs = table.find_elements_by_tag_name('tr')
                    if len(trs) > 4:
                        if trs[2].text != '':
                            specs_data['Power Supply'] = trs[2].text
                        for tr in trs[3:]:
                            tds = tr.find_elements_by_tag_name('td')
                            specs_data[tds[0].text] = tds[len(tds) - 1].text.replace('\n', ' ')
                    elif 0 < len(trs) <= 4:
                        try:
                            specs_data[trs[1].text] = trs[len(trs) - 1].text.replace('\n', ' ')
                        except:
                            print('Data Extracted but tag error')
                    else:
                        specs_data[trs[1].text] = trs[0].text.replace('\n', ' ')  
            
            specs_data_dict = {}
            temp_humid = {}
            m_2 = {}
            weight_dict = {}
            
            if item_type == 'D':
                if product_type == 'chassis':
                    if not item_type in ['D']: 

                        try:
                            temp_humid = dict([item.split(':') for item in list(filter(None, specs_data['Environmental Spec.'].strip().split(')')))])
                        except:
                            temp_humid = dict([item.split(':') for item in list(
                                filter(None, [i for i in specs_data['Environmental Spec.'].split(') ') if ':' in i]))])

                        specs_data_dict['chassis']= specs_data[[col for col in specs_data.keys() if 'model' in col.lower()][0]]
                    else:
                        temp_humid = {**pd.DataFrame(specs_data, index=[0])[[col for col in specs_data.keys() if 'operating' in col.lower()]].to_dict('record')[0]}
                        try:
                            specs_data_dict['chassis']= specs_data[[col for col in specs_data.keys() if 'sku' in col.lower()][0]].split()[0]
                        except:
                            specs_data_dict['chassis']= specs_data[[col for col in specs_data.keys() if each_prod.lower() in col.lower()][0]].split()[0]

                    try: 
                        specs_data_dict['CPU'] = specs_data['CPU']
                    except: 
                        try: 
                            specs_data_dict['CPU'] = specs_data['Processor/Cache']
                        except: 
                            try: 
                                specs_data_dict['CPU'] = specs_data['Processor Support']
                            except:
                                specs_data_dict['CPU'] = 'NA'

                    try:         
                        specs_data_dict['form_factor']=specs_data[[col for col in specs_data.keys() if 'form factor' in col.lower()][0]]
                    except: 
                        specs_data_dict['form_factor']= 'NA'

                    try:
                        specs_data_dict['product_colour']=specs_data[[col for col in specs_data.keys() if 'available colors' in col.lower()][0]]
                    except:
                        specs_data_dict['product_colour']='Black'

                    try: 
                        key_specs_data['num_of_dimm_slots']= re.search(r'(\d+)\sDIMM', specs_data['Memory Capacity'])[0]
                    except: 
                        key_specs_data['num_of_dimm_slots']= 'NA'

                    try:
                        specs_data_dict['drive_bays'] = specs_data['Drive Bays']
                    except:
                        specs_data_dict['drive_bays'] = [value for key,value in specs_data.items() if key.startswith("Drive Bays")]

                    try:
                        weight = specs_data[[col for col in specs_data.keys() if 'weight' in col.lower()][0]]
                        try:
                            weight_dict = dict([item.split(':') for item in list(filter(None, weight.strip().split(')')))])
                        except: 
                            specs_data_dict[' Gross Weight'] = weight
                    except:
                        specs_data_dict['Net Weight'] = 'NA'
                        specs_data_dict[' Gross Weight'] = 'NA'

                    try:
                        key_specs_data['power_supply']= data_new.raw.str.extractall(r'(\d+W.*)')[0][0]
                    except:
                        key_specs_data['power_supply']='NA'

                    specs_data_dict = {**specs_data_dict, **temp_humid, **weight_dict}

                elif product_type == 'motherboard':
                    try: 
                        specs_data_dict['motherboard']=specs_data[[col for col in specs_data.keys() if 'motherboard' in col.lower()][0]]
                    except: 
                        try:
                            specs_data_dict['motherboard']=specs_data[[col for col in specs_data.keys() if 'x1' in col.lower()][0]]
                        except:
                            specs_data_dict['motherboard'] =specs_data[[col for col in specs_data.keys() if 'product skus' in col.lower()][0]]

                    try:
                        specs_data_dict['chipset']=specs_data[[col for col in specs_data.keys() if 'chipset' in col.lower()][0]]
                    except:
                        specs_data_dict['chipset']='NA'

                    try:
                        specs_data_dict['cores']=specs_data[[col for col in specs_data.keys() if 'cores' in col.lower()][0]]
                    except:
                        specs_data_dict['cores']='NA'

                    try: 
                        specs_data_dict['Supported_memory_types'] = specs_data['Memory Type']
                        if specs_data_dict['Supported_memory_types'] == 'NA':
                            specs_data_dict['Supported_memory_types'] = specs_data['Memory Capacity']
                    except: 
                        specs_data_dict['Supported_memory_types']= 'NA'

                    try: 
                        m_2_features = list(flatten([item.split(':') for item in list(filter(None, specs_data['M.2'].strip().split(')')))]))
                        for item in m_2_features:
                            if '1x' in item:
                                m_2['num_of_m_2_supported'] = m_2_features[0].split('x')[0]
                            else:
                                m_2['num_of_m_2_supported'] = 1 
                            if 'pci' in item.lower():
                                m_2['m_2_interface'] = item
                            if ' key' in item.lower():
                                m_2['m_2_form_factor'] = item.split('Key')[0]

                            m_2['m_2_key'] = m_2_features[len(m_2_features) - 1]
                    except:
                        try:
                            if data2.raw.str.contains(r'(M.2.*)').item:
                                m_2['m_2_interface'] = data2.raw.str.extractall(r'(M.2.*)')[0][0].split(':')[1]
                                m_2['m_2_form_factor'] = data2.raw.str.extractall(r'(M.2.*)')[0][1].split(':')[1]
                                m_2['m_2_key']= data2.raw.str.extractall(r'(M.2.*)')[0][2].split(':')[1]
                        except:
                            m_2['num_of_m_2_supported'] = 'NA'
                            m_2['m_2_interface'] = 'NA'
                            m_2['m_2_form_factor'] = 'NA'
                            m_2['m_2_key'] = 'NA'

                    try:
                        if len(m_2['m_2_interface']) >0:
                            string = m_2['m_2_interface']
                            m_2['num_of_m_2_supported'] = re.search(r'(\d+)', string)[0]
                    except:
                        m_2['num_of_m_2_supported'] = 'NA'

                    try:
                        key_specs_data['onboard_network_controllers'] = specs_data['Network Controllers']
                    except:
                        key_specs_data['onboard_network_controllers'] = 'NA'

                    try: 
                        key_specs_data['num_of_dimm_slots']= re.search(r'(\d+)\sDIMM', specs_data['Memory Capacity'])[0]
                    except: 
                        key_specs_data['num_of_dimm_slots']= 'NA'

                    try: 
                        specs_data_dict['Supported_memory_types']= specs_data['Memory Type']
                    except: 
                        specs_data_dict['Supported_memory_types']= 'NA'

                    specs_data_dict = {**specs_data_dict, **m_2} 
                    
                specs_data_dict = {**specs_data_dict, **temp_humid, **weight_dict, **m_2}
            
            return specs_data_dict, specs_data

        def get_parts():
            result_components = []
            components = driver.find_element_by_class_name("part-list")
            for table in components.find_elements_by_tag_name('table'):
                trs = table.find_elements_by_tag_name('tr')
                try:
                    header = trs[1].get_attribute('innerText').lower()
                except:
                    print('broken')
                if 'parts list' in header and 'optional' not in header:
                    for i in range(len(trs)):
                        if i > 3:
                            tds = trs[i].find_elements_by_tag_name('td')
                            if len(tds) > 1:
                                result_components.append({'part': tds[0].get_attribute('innerText'),
                                                            'code': tds[1].get_attribute('innerText'),
                                                            'qty': tds[2].get_attribute('innerText'),
                                                            'description': tds[3].get_attribute('innerText')})
            return result_components

        partial_links = self.driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md']")
        for each_partial_link in partial_links:
            if "FAQ" not in each_partial_link.text:
                each_partial_link.click()
                time.sleep(2)  # sleep for 3 seconds so you can see the results

                if item_type == 'D':
                    key_features_dict = get_key_features(item_type)
                    key_specs_data = pd.DataFrame(key_features_dict, index=[0])
                    specs_data_dict, specs_data = get_specifications(item_type)
                    if len(key_specs_data[key_specs_data.pcl_express_x16_slots == "NA"]) > 0:
                        try: 
                            if specs_data[[col for col in specs_data.keys() if 'pci' in col.lower()][0]]:
                                key_specs_data['pcl_express_x16_slots'] = specs_data[[col for col in specs_data.keys() if 'pci express' in col.lower()][0]]
                        except:
                            try:
                                key_specs_data['pcl_express_x16_slots'] = key_specs_data.pcl_express_slots_version[0].split(',')[0]
                            except:
                                key_specs_data['pcl_express_x16_slots'] = 'NA'
                        try:          
                            USB = specs_data['USB'].split(')')
                            if len(key_specs_data[key_specs_data.usb_3_0_type_a_ports_quantity == "NA"]) > 0:
                                key_specs_data['usb_3_0_type_a_ports_quantity'] = USB[0]
                            if len(key_specs_data[key_specs_data.usb_2_0_type_a_ports_quantity == "NA"]) > 0:
                                key_specs_data['usb_2_0_type_a_ports_quantity'] = USB[1]
                        except: 
                            pass
                else:
                    key_features_dict = get_key_features(item_type, product_type)
                    key_specs_data = pd.DataFrame(key_features_dict, index=[0])
                    specs_data_dict, specs_data = get_specifications_chassis_motherboard(item_type, product_type)
                    if len(key_specs_data[key_specs_data.pcl_express_x16_slots == "NA"]) > 0:
                        try: 
                            if specs_data[[col for col in specs_data.keys() if 'pci' in col.lower()][0]]:
                                key_specs_data['pcl_express_x16_slots'] = specs_data[[col for col in specs_data.keys() if 'pci express' in col.lower()][0]]
                        except:
                            try:
                                key_specs_data['pcl_express_x16_slots'] = key_specs_data.pcl_express_slots_version[0].split(',')[0]
                            except:
                                key_specs_data['pcl_express_x16_slots'] = 'NA'
                        try:          
                            USB = specs_data['USB'].split(')')
                            if len(key_specs_data[key_specs_data.usb_3_0_type_a_ports_quantity == "NA"]) > 0:
                                key_specs_data['usb_3_0_type_a_ports_quantity'] = USB[1]
                            if len(key_specs_data[key_specs_data.usb_2_0_type_a_ports_quantity == "NA"]) > 0:
                                key_specs_data['usb_2_0_type_a_ports_quantity'] = USB[0]
                        except: 
                            pass

                try:
                    specificationd_data = pd.DataFrame(specs_data_dict, index= [0])
                except: 
                    specificationd_data = pd.DataFrame([specs_data_dict], index =[0])

                final_data = pd.concat([data, specificationd_data, key_specs_data],axis = 1, join = 'outer', ignore_index=False, sort=False)
                
                result_components = get_parts()
                result_parts_data = pd.DataFrame(result_components)
                
                final_data['nodes'] = 1
                try:
                    if [result_parts_data[result_parts_data.part == 'Motherboard / Chassis'].qty][0][0] == '11': final_data['nodes'] = 1
                except:
                    try:
                        if [result_parts_data[result_parts_data.part == 'Motherboard'].qty][0][0] == '1': final_data['nodes'] = 1
                    except:
                        final_data['nodes'] = 1
                    
                # if  product_type == 'motherboard':
                #     result_specs = {}
                #     key_specs = driver.find_elements_by_class_name('key-feature-list')
                #     key_specs_data = [specs_data.text for specs_data in key_specs]
                #     key_specs_data = [specs_data.split('\n') for specs_data in key_specs_data]
                #     key_specs_data = [item for sublist in key_specs_data for item in sublist]

                #     try:
                #         PCI_list = []
                #         for i in key_specs_data:
                #             if re.search(r'[\d?\.? ](\d+)[ PCI\-E].*x16.*', i):
                #                 PCI_list = i
                #         result_specs['PCI-E'] = PCI_list[0] if PCI_list else "NA"
                #         # result_specs['PCI-E'] = [i for i in key_specs_data if re.search(r'[\d?\.? ](\d+)[ PCI\-E].*x16.*', i)][0]
                #     except:
                #         key_specs = driver.find_elements_by_class_name('col-right')
                #         key_specs_data = [specs_data.text for specs_data in key_specs]
                #         key_specs_data = [specs_data.split('\n') for specs_data in key_specs_data]
                #         key_specs_data = [item for sublist in key_specs_data for item in sublist]
                #         PCI_list = []
                #         for i in key_specs_data:
                #             if re.search(r'[\d?\.? ](\d+)[ PCI\-E].*x16.*', i):
                #                 PCI_list = i
                #         result_specs['PCI-E'] = PCI_list[0] if PCI_list else "NA"
                #         # result_specs['PCI-E'] = [i if re.search(r'[\d?\.? ](\d+)[ PCI\-E].*x16.*', i) else 'NA' for i in key_specs_data][0]

                #     m_2_list = []
                #     for i in key_specs_data:
                #         if re.search(r'.*M.2', i):
                #             m_2_list = i
                #     result_specs['M.2'] = m_2_list if m_2_list else "NA"

                #     # print('M.2 Fix: ', result_specs['M.2'])
                #     result_specs['all_pce'] = [','.join(i if re.search(r'\d.?(.*PCI-E.*)', i) else 'NA' for i in key_specs_data)]

                #     socket_list = []
                #     for i in key_specs_data:
                #         if re.findall(re.compile('(.*Socket.*[,?])|(.*socket.*[,?])'), i):
                #             socket_list = i
                #     result_specs['socket'] = socket_list if socket_list else "NA"

                #     # result_specs['socket'] = [i if re.findall(re.compile('(.*Socket.*[,?])|(.*socket.*[,?])'), i,) else 'NA' for i in key_specs_data][0]

                #     key_specs_df = pd.DataFrame(result_specs, index=[0])
                #     if not key_specs_df['M.2'].empty:
                #         data['num_m2'] = key_specs_df['PCI-E'].str.extract('x(.*)')[0]
                #         # print(data['num_m2'])
                #         if not data['num_m2'].empty:
                #             data['m.2'] = 'Y'
                #         else:
                #             data['m.2'] = 'N'
                #     if not key_specs_df['PCI-E'].empty:
                #         data['pci'] = key_specs_df['PCI-E'].str.extract('(\d).?.*PCI-E.*')[0][0]
                #         # print('pci: ', data['pci'][0])

                #     if not key_specs_df['all_pce'].empty:
                #         data['all_pce'] = key_specs_df['all_pce'].str.extract(r'\d.?(.*PCI-E.*) {1}')[0][0]
                #         # print('all_pce: ', data['all_pce'][0])

                #     if not key_specs_df['socket'].empty:
                #         data['socket'] = key_specs_df['socket'][0]

                # if product_type == 'chassis' or product_type == 'chassis-s':
                    # result_components = []
                    # components = driver.find_element_by_class_name("part-list")
                    # for table in components.find_elements_by_tag_name('table'):
                    #     trs = table.find_elements_by_tag_name('tr')
                    #     try:
                    #         header = trs[1].get_attribute('innerText').lower()
                    #     except:
                    #         print('broken')
                    #     if 'parts list' in header and 'optional' not in header:
                    #         for i in range(len(trs)):
                    #             if i > 3:
                    #                 tds = trs[i].find_elements_by_tag_name('td')
                    #                 if len(tds) > 1:
                    #                     result_components.append({'part': tds[0].get_attribute('innerText'),
                    #                                               'code': tds[1].get_attribute('innerText'),
                    #                                               'qty': tds[2].get_attribute('innerText'),
                    #                                               'description': tds[3].get_attribute('innerText')})

                    # result_parts_data = pd.DataFrame(result_components)
                    # if [result_parts_data[result_parts_data.part == 'Motherboard / Chassis'].qty][0][0] == '11': final_data['nodes'] = 1

                    # if 'code' in result_parts_data.columns:
                    #     print('Extraction Working')

                    #     if not result_parts_data[result_parts_data['code'].str.startswith(('BPN', 'CSE'))]['code'].empty:
                    #         data['bp sku'] = result_parts_data[result_parts_data['code'].str.startswith(('BPN', 'CSE'))]['code'].values[0]
                    #     else:
                    #         data['bp sku'] = "NA"

                    #     data['num_fans'] = result_parts_data[result_parts_data['code'].str.startswith('FAN')].qty.sum()
                    #     data['fan_dims'] = str(','.join(result_parts_data[result_parts_data['code'].str.startswith('FAN')].description.tolist()))

                    #     if not result_parts_data[result_parts_data['code'].str.startswith('PWS')]['code'].empty:
                    #         data['pws'] = result_parts_data[result_parts_data['code'].str.startswith('PWS')]['code'].values[0]
                    #     else:
                    #         data['pws'] = "NA"

                    #     if not result_parts_data[result_parts_data['code'].str.startswith('PDB')]['code'].empty:
                    #         data['pdb'] = result_parts_data[result_parts_data['code'].str.startswith('PDB')]['code'].values[0]
                    #     else:
                    #         data['pdb'] = "NA"
                    # else:
                    #     print('Extraction Failed')

                    # if product_type == 'chassis-s':
                        # result_specs = {}
                        # key_specs = driver.find_elements_by_class_name('spec-key-features')
                        # key_specs_data = [specs_data.text for specs_data in key_specs]
                        # key_specs_data = [specs_data.split('\n') for specs_data in key_specs_data]
                        # key_specs_data = [item for sublist in key_specs_data for item in sublist]
                        # key_specs_data = list(filter(None, key_specs_data))
                        # data_new = pd.DataFrame(key_specs_data, columns=['raw'])
                        # key_features = {}
                        # result_specs['pcl_express_x16_slots']= data_new.raw.str.extractall(r'(\d+\sPCI.*16)')[0][0]
                        # result_specs['pcl_express_x8_slots']= data_new.raw.str.extractall(r'(\d+\sPCI.*8)')[0][0]
                        # result_specs['pcl_express_slots_version']= [item.split(' ',1) for item in [''.join(i if re.search(r'[\d\.+]?(.*PCI-E.*)', i) else '' for i in key_specs_data)]][0][1]
                        # result_specs['maximum_internal_memory']= data_new.raw.str.extractall(r'([0-9.]+?TB)|([0-9.]+?tb)')[0][0]
                        # result_specs['usb_3_0_type_a_ports_quantity']= data_new.raw.str.extractall(r'(\d+ USB 3.0)')[0][0]
                        # result_specs['usb_2_0_type_a_ports_quantity']= data_new.raw.str.extractall(r'(\d+ USB 2.0)')[0][0]
                        # result_specs['processor_socket'] =[item.split(' ',1) for item in [''.join(i if re.search(r'(.*Socket.*)', i) else '' for i in key_specs_data)]][0][1]
                        # if data_new.raw.str.extractall(r'(ECC)')[0][0]: result_specs['ecc'] = 'Y' 
                        # else: result_specs['ecc'] = 'N'

                        # key_specs_data = pd.DataFrame(data, index=[0])

                        # key_specs = driver.find_elements_by_class_name('spec-key-features')
                        # key_specs_data = [specs_data.text for specs_data in key_specs]
                        # key_specs_data = [specs_data.split('\n') for specs_data in key_specs_data]
                        # key_specs_data = [item for sublist in key_specs_data for item in sublist]
                        # PCI_list = []
                        # for i in key_specs_data:
                        #     if re.search(r'[\d?\.? ](\d+)[ PCI\-E].*x16.*', i):
                        #         PCI_list = i
                        # result_specs['PCI-E'] = PCI_list[0] if PCI_list else "NA"
                        # # result_specs['PCI-E'] = [i if re.search(r'[\d?\.? ](\d+)[ PCI\-E].*x16.*', i) else 'NA' for i in key_specs_data][0]

                        # m_2_list = []
                        # for i in key_specs_data:
                        #     if re.search(r'.*M.2', i):
                        #         m_2_list = i
                        # result_specs['M.2'] = m_2_list[0] if m_2_list else "NA"
                        # # result_specs['M.2'] = [i if re.search(r'.*M.2', i) else 'NA' for i in key_specs_data][0]

                        # result_specs['all_pce'] = [','.join(i if re.search(r'\d.?(.*PCI-E.*)', i) else 'NA' for i in key_specs_data)]

                        # socket_list = []
                        # for i in key_specs_data:
                        #     if re.search(r'(.*Socket.*[,?])', i):
                        #         socket_list = i
                        # result_specs['socket'] = socket_list[0] if socket_list else "NA"

                        # #result_specs['socket'] = [i
                        # #                          if re.findall(re.compile('(.*Socket.*[,?])'), i, )
                        # #                          else 'NA'
                        # #                         for i in key_specs_data][0]

                        # key_specs_df = pd.DataFrame(result_specs, index=[0])

                        # if not key_specs_df['M.2'].empty:
                        #     data['num_m2'] = key_specs_df['PCI-E'].str.extract('x(.*) M.2')[0][0]
                        #     if not data['num_m2'].empty:
                        #         data['m.2'] = 'Y'
                        #     else:
                        #         data['m.2'] = 'N'
                        # if not key_specs_df['PCI-E'].empty:
                        #     data['PCl_Express_x16_slots'] = key_specs_df['PCI-E'].str.extract('(\d).?.*PCI-E.*')[0][0]

                        # if not key_specs_df['all_pce'].empty:
                        #     data['all_pce'] = key_specs_df['all_pce'].str.extract(r'\d.?(.*PCI-E.*) {1}')[0][0]

                        # if result_parts_data[result_parts_data['code'].str.startswith('MBD')]['code'].values:
                        #     split_list = result_parts_data[result_parts_data['code'].str.startswith('MBD')]['code'].values[0].split('\n')
                        #     if split_list:
                        #         data['Motherboard'] = split_list[0]

                final_data.to_excel('Supermicro.xlsx')
                return final_data

    def get_txt_intel(self, driver,boms_id,  each_prod):
        self.driver = driver
        # for each in each_prod_parts_list:
        each_prod = re.sub('[Ii]ntel [Nn]utanix', '', each_prod)
        each_prod = each_prod.split("-")[0]
        self.driver.get('http://www.google.com')
        search = self.driver.find_element_by_name('q')
        search.send_keys("intel:" + each_prod)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        time.sleep(2)  # sleep for 2 seconds so you can see the results
        partial_links = self.driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md']")
        link_found = False

        if ("FAQ" not in partial_links[0].text) and ("Digicor" not in partial_links[0].text):
            partial_links[0].click()
            link_found = True
            time.sleep(2)  # sleep for 3 seconds so you can see the results
            # break
        if link_found:
            try:
                time.sleep(2)
                self.driver.find_element_by_partial_link_text("Download software and").click()
                time.sleep(2)
                self.driver.find_element_by_partial_link_text("Product specifications").click()
                time.sleep(2)
                print("hard intel")
            except:
                print("easy intel")
            self.driver.find_element_by_partial_link_text("Export specification").click()
            time.sleep(3)
            # get list of files from downloads directory
            list_of_files = glob.glob('/Users/mohsinkhan/Desktop/DigiCor/intel files/*.xls')  # * for all files
            latest_file = max(list_of_files, key=os.path.getctime)
            print(latest_file)
            # read the excel. it always reads in list, so picked the first element(df) and converted intel_df as df
            self.intel_df = pd.read_html(latest_file)[0]
            self.intel_df.set_index(self.intel_df.columns[0], inplace=True)
            self.intel_df = self.intel_df.T
            self.intel_df = self.intel_df.drop(self.intel_df.columns[0:1], 1)
            self.intel_df.rename(columns={self.intel_df.columns[0]: "Model"}, inplace=True)
            self.intel_df['boms_id'] = boms_id
            self.intel_df.to_excel("intel files/Intel_" + each_prod + ".xlsx")
        return self.intel_df, link_found

    def get_txt_asus(self, driver, each_prod):

        self.driver = driver

        self.driver.get('http://www.google.com')
        search = self.driver.find_element_by_name('q')
        search.send_keys("asus:" + each_prod)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        time.sleep(2)  # sleep for 2 seconds so you can see the results

        partial_links = self.driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md']")
        for each_partial_link in partial_links:
            if "FAQ" not in each_partial_link.text:
                each_partial_link.click()
                time.sleep(2)  # sleep for 3 seconds so you can see the results
                break

        self.driver.find_element_by_partial_link_text("Specifications").click()
        time.sleep(3)

        # create a proxy access
        req = Request(driver.current_url, headers={'User-Agent': 'Mozilla/5.0'})

        asus_txt = urlopen(req).read()
        asus_txt = str(asus_txt).replace("\n", "")
        asus_txt = re.sub(r'^[\s\S]*<html', '<html', asus_txt)
        asus_txt = str(asus_txt).replace("\\r\\n", "")
        asus_txt = re.sub(r'<', '\n<', asus_txt)
        asus_txt = re.sub(r'\n</', '</', asus_txt)

        # with open("ASUS files\output_" + each_prod + ".txt", "w", encoding="utf-8") as file:
        #     file.write(str(asus_txt))

        keys = re.findall(r"spec-item\">(.*)</", asus_txt)
        values = re.findall(r"spec-data\">([\s\S]+?)</div", asus_txt)

        values = [re.sub(r'\\xc2\\xae', '®', subs) for subs in values]
        values = [re.sub(r'\\xc2\\xa0', ' ', subs) for subs in values]
        values = [re.sub(r'\\xe2\\x84\\x83', '°C', subs) for subs in values]
        values = [sub.replace('\n<sup>', '').replace('</sup>', '') for sub in values]
        values = [sub.replace('<br>', '') for sub in values]

        dictionary_asus_data = dict(zip(keys, values))
        xml_content = ""
        for keys, values in dictionary_asus_data.items():
            xml_content = xml_content + "<" + keys + ">\n"
            if "<strong>" in values:
                values = values + "<strong>"
                result_keys = re.findall(r"strong>([\s\S]+?)<\/s", values)
                result_values = re.findall(r"\/strong>([\s\S]+?)<s", values)
                for k, v in zip(result_keys, result_values):
                    xml_content = xml_content + "\t<" + k + ">\n"
                    xml_content = xml_content + "\t\t<" + v.replace("\n", "\n\t\t").strip() + ">\n"

            else:
                xml_content = xml_content + "\t<" + values.replace("\n", "\n\t").strip() + ">\n"

        xml_content = re.sub(r"\n\s+\n", "\n", xml_content)
        with open("ASUS files\\xml_" + each_prod + ".txt", "w", encoding="utf-8") as file:
            file.write(str(xml_content))

        # dictionary_asus_data = dict(zip(keys, values))

        return xml_content
