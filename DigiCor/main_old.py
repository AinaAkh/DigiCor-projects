from regexes import Regexer
from website_crawler import Txt_maker
from selenium import webdriver
import sqlalchemy
import re
import selenium
import pandas as pd
import time
import numpy as np
import openpyxl

pd.options.mode.chained_assignment = None  # default='warn'

system_info_df = pd.read_csv("/Users/mohsinkhan/Desktop/data_science/DigiCor/Data files/system info 5 oct 2020 - Original.csv")

# setting chrome driver and download location
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/Users/mohsinkhan/Downloads/"}
options.add_experimental_option('prefs', prefs)
PATH = "/Users/mohsinkhan/Desktop/data_science/DigiCor/chromedriver"
driver = webdriver.Chrome(executable_path=PATH, options=options)

txt_maker_obj = Txt_maker()
regexer_obj = Regexer()
models_done_list = []

def splitter(model_desc):
    splitter_model_list = model_desc.split("+")
    splitter_model_list = list(map(str.strip, splitter_model_list))
    splitter_model_list = list(filter(None, splitter_model_list))
    return splitter_model_list

def supermicro_models(each_model, product_type, boms_id, item_type):
    # regexer_obj = Regexer()
    supermicro_data = txt_maker_obj.get_txt_supermicro(driver,boms_id, product_type, each_model,"supermicro", item_type)
    # regexer_obj.run_regexes_supermicro(supermicro_data, boms_id, product_type, each_model, "supermicro", item_type)
    models_done_list.append(each_model)
    return supermicro_data

def crawler():
    try:
        # i = 1

        # models_missed_list = []

        # models_skipped_list = ['1029GQ-TXRT','5039MS-H12NR', '414E-422', 'TRX40']

        # try:
        #     supermicro_output_df = pd.read_csv('result.csv')
        # except:
        #     # supermicro_output_df = pd.DataFrame(columns=list(Regexer().__dict__.keys()))
        #     supermicro_output_df = pd.DataFrame(columns=['boms_id','chassis','motherboard','CPU','form_factor','chipset','cores','height_mm','width_mm','depth_mm',
        #     'product_colour','drive_bays','Supported_memory_types','Operating Temperature',' Non-operating Temperature',' Operating Relative Humidity',
        #     ' Non-operating Relative Humidity','Gross Weight',' Net Weight','num_of_m_2_supported','m_2_key','m_2_interface','m_2_form_factor',
        #     'pcl_express_x16_slots','pcl_express_x8_slots','pcl_express_slots_version','maximum_internal_memory','usb_3_0_type_a_ports_quantity',
        #     'usb_2_0_type_a_ports_quantity','processor_socket','num_of_storage_drives_supported','onboard_network_controllers','num_of_dimm_slots',
        #     'backplanes_support','power_supply','ecc','nodes'])
        
        # # intel_output_df = pd.DataFrame()
        # # asus_output_df = pd.DataFrame(columns=list(Regexer().__dict__.keys()))

        # for row in system_info_df.itertuples():
        #     try:
        #         print(row.system, row.name)
        #         desc = row.name
        #     except: 
        #         print(row.system, row.desc)
        #         desc = row.desc
        #     boms_id = row.id

        #     if boms_id in supermicro_output_df.boms_id.tolist():
        #         continue
        #     else:
        #         0

        #     if '+' in desc:
        #         model_list = splitter(desc)
        #     else:
        #         model_list = [desc]

        #     coun = 0

        #     for each_model in model_list:
        #         if each_model in models_skipped_list or "SuperBlade 820L-822" in row.category:
        #             models_skipped_list.append(each_model)

        #         elif "DiGiCOR" in row.category and row.system.startswith("D"):
        #             print("in first")
        #             print(i, each_model, "supermicro", len(each_model))
        #             item_type = 'D'
        #             if len(each_model) >= 10:
        #                 # print('Chassis')
        #                 chassis_result = supermicro_models(each_model, 'chassis', boms_id, item_type)
        #                 chassis_result['boms_id'] = boms_id
        #             else:
        #                 # print('Motherboard')
        #                 mb_result = supermicro_models(each_model, 'motherboard', boms_id, item_type)

        #         elif "DiGiCOR" in row.category and row.system.startswith("S"):
        #             print("in second")
        #             print(i, each_model, "supermicro")
        #             item_type = 'S'
        #             chassis_result = supermicro_models(each_model, 'chassis-s', boms_id, item_type)
        #             chassis_result['boms_id'] = boms_id
        #             # print(chassis_result)
        #             # mb = chassis_result['Motherboard']
        #             # # print(mb)
        #             # if mb != "NA":
        #             #     mb_result = supermicro_models(mb, 'motherboard', boms_id, item_type)

        #         elif row.category.startswith("SUPERMICRO"):
        #             print("in third")
        #             print(i, each_model, "supermicro")
        #             item_type = 'SUPERMICRO'
        #             chassis_result = supermicro_models(each_model, 'chassis-s', boms_id, item_type)
        #             chassis_result['boms_id'] = boms_id
        #             # print(chassis_result)
        #             # mb = chassis_result['Motherboard']
        #             # # print(mb)
        #             # if mb != "NA":
        #             #     mb_result = supermicro_models(mb, 'motherboard', boms_id, item_type)


        #         elif "DiGiCOR" in row.category and row.system.startswith("IN"):
        #             print("in forth")
        #             print(i, each_model, "supermicro")
        #             # pass


        #         elif "DiGiCOR" in row.category and row.system.startswith("N"):
        #             print("in fifth")
        #             print(i, each_model, "supermicro")
        #             # pass

        #         # elif ("DiGiCOR" in row.category) and (row.system.startswith("I")) and ("AF" not in row.desc):
        #         #     print("in sixth")
        #         #     print(i, each_model, "intel")
        #         #     intel_df, link_found = txt_maker_obj.get_txt_intel(driver, boms_id, each_model)
        #         #     if link_found:
        #         #         intel_output_df = pd.concat([intel_output_df, intel_df], axis=0)
        #         #         models_done_list.append(each_model)
        #         #     else:
        #         #         models_missed_list.append(each_model)

        #         # elif (row.category.startswith("Intel")) and ("Nutanix" not in row.category) and ("AF" not in row.desc):
        #         #     print("in seventh")
        #         #     print(i, each_model, "intel")
        #         #     intel_df, link_found = txt_maker_obj.get_txt_intel(driver, boms_id, each_model)
        #         #     if link_found:
        #         #         intel_output_df = pd.concat([intel_output_df, intel_df], axis=0)
        #         #         models_done_list.append(each_model)
        #         #     else:
        #         #         models_missed_list.append(each_model)

        #         # elif ("ASUS" in row.category or "Asus" in row.category) and "DVT" not in row.desc:
        #         #     print("in eight")
        #         #     print(i, each_model, "asus")
        #         #     regexer_obj = Regexer()
        #         #     xml_asus_data = txt_maker_obj.get_txt_asus(driver, each_model)
        #         #     regexer_obj.run_regexes_asus(xml_asus_data, boms_id, each_model, "asus")
        #         #     asus_output_df = asus_output_df.append(regexer_obj.__dict__, ignore_index=True)
        #         #     models_done_list.append(each_model)

        #         else:
        #             # missed out models:
        #             if each_model not in models_done_list:
        #                 print("in ninth")
        #                 models_missed_list.append(each_model)

        #         print(i, "DONE: " + each_model)
        #         i = i + 1

        #     if ("DiGiCOR" in row.category and row.system.startswith("D")) or (
        #         "DiGiCOR" in row.category and row.system.startswith("S")) or (
        #             row.category.startswith("SUPERMICRO")):

        #         ## merge mb to chassis
        #         # convert pandas dataframe to dictionary, because the previous code works on dict
        #         try:
        #             chassis_result
        #         except NameError:
        #             print('chassis result not found')
        #             continue

        #         if ("DiGiCOR" in row.category and row.system.startswith("D")):
        #             # print(chassis_result.columns)
        #             for col in mb_result.columns:
        #                 if col in chassis_result.columns:
        #                     if "NA" in str(chassis_result.loc[0,col]):
        #                         chassis_result[col] = mb_result[col]
        #             supermicro_output_df = supermicro_output_df.append(chassis_result, ignore_index=True)
        #             supermicro_output_df.to_csv('result.csv')
        #         else: 
        #             supermicro_output_df = supermicro_output_df.append(chassis_result, ignore_index=True)
        #             supermicro_output_df.to_csv('result.csv')
                
        #         # print(supermicro_output_df)


        # driver.quit()

        # # intel columns rename
        # # intel_output_df.rename(columns={'Model': 'name',
        # #                                 'Chassis Form Factor': 'form_factor',
        # #                                 # 'Front Drive Form Factor': 'hot_swap_hdd_bays',   # if data present, "Y"
        # #                                 '# of Front Drives Supported': 'num_storage_drives_supported',
        # #                                 'Front Drive Form Factor': 'storage_drive_sizes_supported',
        # #                                 'integrated lan': 'gbe',
        # #                                 'Processor Graphics': 'on_board_graphics_adapter_model',
        # #                                 'Max Memory Size (dependent on memory type)': 'maximum_internal_memory',
        # #                                 'Max # of DIMMs': 'num_dimm_slots',
        # #                                 'Memory Types': 'supported_memory_types',
        # #                                 'Intel® Optane™ Memory Supported ‡': 'intel_optane',
        # #                                 # 'Integrated LAN': 'ipmi_lan_port',    # if data present, "Y"
        # #                                 '# of USB Ports': 'usb_3_0_type_a_ports_quantity',
        # #                                 'Board Chipset': 'motherboard_chipset',
        # #                                 '# of LAN Ports': 'lan_ports',
        # #                                 'Socket': 'processor_socket',
        # #                                 'Extended Warranty Available for Purchase (Select Countries)': 'extended_warranty_available_for_purchase',
        # #                                 'Riser Slot 1: Included Slot Configuration(s)': 'riser_slot_1',
        # #                                 'Riser Slot 2: Included Slot Configuration(s)': 'riser_slot_2',
        # #                                 'Intel® Virtualization Technology for Directed I/O (VT-d) ‡': 'intel_virtual_technology_for_directed_i/o'
        # #                                 })

        # # data = pd.read_excel('final files/specifications.xlsx', engine='openpyxl')
        # # data.drop([col for col in data.columns if "Unnamed" in col], axis=1, inplace=True)
        # # data = data.to_json()

        # supermicro_output_df.drop([col for col in supermicro_output_df.columns if "Unnamed" in col], axis=1, inplace=True)

        # def filltemp(row, pattern):
        #     for col in [col for col in row.index if pattern in col.lower()][1:]:
        #         if row[col] ==  row[col]:
        #             return row[col]

        # a = [' Non-operating Temperature', ' Operating Relative Humidity',' Non-operating Relative Humidity',
        # 'Net Weight', ' Gross Weight']
        # for pat in a:
        #     supermicro_output_df.loc[supermicro_output_df[pat].isna(), pat] = supermicro_output_df[supermicro_output_df[pat].isna()].apply(lambda row: filltemp(row, pat.lower().strip()), axis=1)
        
        # supermicro_output_df = supermicro_output_df.drop(columns=supermicro_output_df.columns[-10:], axis = 1)
        # supermicro_output_df.columns = supermicro_output_df.columns.str.replace(' ', '')

        # supermicro_output_df = supermicro_output_df.rename(columns= {'OperatingTemperature':'operating_temperature', 'Non-operatingTemperature':'storage_temperature', 
        #     'OperatingRelativeHumidity': 'operating_relative_humidity', 'Non-operatingRelativeHumidity':'storage_relative_humidity', 
        #     'GrossWeight': 'chassis_gross_weight_kg', 'NetWeight':'chassis_net_weight'})
        

        # supermicro_output_df.to_excel("final files/supermicro_final.xlsx")
        # # asus_output_df.to_excel("final files/asus_final.xlsx")
        # # intel_output_df.to_excel("final files/intel_final.xlsx")

        # models_missed_list = models_missed_list + models_skipped_list
        # models_missed_df = pd.DataFrame({'models_missed_list': models_missed_list})
        # models_missed_df.to_excel("models_missed_list.xlsx")
        # print("Crawler complete and all models are done")

        # data = supermicro_output_df

        # data.to_excel('new_supermicro.xlsx')
    
        data = pd.read_excel('/Users/mohsinkhan/Desktop/data_science/DigiCor/final files/specification_new.xlsx', engine = 'openpyxl')
        data.drop([col for col in data.columns if "Unnamed" in col], axis=1, inplace=True)
        status = 200
        error = ''
        return ({'status': status, 'data': data.to_json(), 'error': error})

    except ValueError:
        print('API Call not working')
        data = []
        status = 400
        error = ''
        return ({'status': status, 'data': data, 'error': ValueError})

def OS_compatibility_data():
    driver.get('https://www.supermicro.com/en/support/faqs/os')
    link_headers = driver.find_elements_by_xpath("//ul[@class='os-list']//a")

    df = pd.DataFrame(columns=['OS'])

    for i in range(len(link_headers)):

        # need to write below 2 lines because the link elements are lost while traversing through website
        driver.get('https://www.supermicro.com/en/support/faqs/os')
        link_headers = driver.find_elements_by_xpath("//ul[@class='os-list']//a")

        header = link_headers[i].text
        print(i, header)
        time.sleep(2)

        try:
            link_headers[i].click()
        except selenium.common.exceptions.StaleElementReferenceException:
            link_headers[i].click()

        except:
            driver.execute_script("arguments[0].click();", link_headers[i])
        time.sleep(2)

        current_url = driver.current_url
        os_df = pd.read_html(driver.page_source)[0]

        # delete first row of multilevel header
        os_df.columns = os_df.columns.droplevel(0)
        # reformat headers
        os_df = os_df.rename_axis(None, axis=1)

        # get the NaNs from first columun
        nans = os_df.loc[pd.isna(os_df[os_df.columns[0]]), :].index
        # drop top useless rows
        os_df = os_df.iloc[max(nans) + 1:]

        # boolean check if values a row is same for all columns or not? And store boolean result in a list
        common_list = (os_df.eq(os_df.iloc[:, 0], axis=0).all(1)).tolist()
        # add that list as a column in the df
        os_df["new"] = common_list

        # rename first column
        os_df = os_df.rename(columns={os_df.columns[0]: "OS_Type"})

        # create data for os_name for each os_type
        new_column_data = []
        OS_name = ""
        for row in os_df.itertuples():
            if row.new is True:
                OS_name = row.OS_Type
            new_column_data.append(OS_name)

        # merge the list of os_name into the database
        os_df["OS_name"] = new_column_data

        # delete the rows with same values across all the columns
        os_df = os_df.drop(os_df[os_df['new'] == True].index)

        # drop last few rows
        os_df = os_df[:-6]

        # delete the columns that starts with unnamed. we dont need them
        cols = [c for c in os_df.columns if not c.startswith('Unnamed')]
        os_df = os_df[cols]

        # remove unnecessary text from the data from os_name column
        os_df['OS_name'] = os_df['OS_name'].str.replace("\(There are CPU/Memory limitations, please see legend below\)",
                                                        '')
        # concat two columns
        os_df['OS'] = os_df.OS_Type.map(str) + "_" + os_df.OS_name

        # delete the boolean column from df
        os_df.drop(['new', 'OS_Type', 'OS_name'], axis=1, inplace=True)

        # reorder columns
        cols = list(os_df.columns)
        cols = [cols[-1]] + cols[:-1]
        os_df = os_df[cols]

        os_df.to_excel("OS Tables\\" + str(i) + "_" + ".xlsx", index=False)

        df = pd.merge(df, os_df, how='outer', on='OS')

        if i == 3:
            break

    df.to_excel("OS Tables\\OS_final.xlsx", index=False)

def database():
    # function to read data from excel
    def read_file(path, item_type):
        if item_type == 'csv':
            data = pd.read_csv(path)
        elif item_type == 'excel':
            data = pd.read_excel(path, engine='openpyxl')
        data.drop([col for col in data.columns if "Unnamed" in col], axis=1, inplace=True)
        return data

    # function to connect to database
    def connection():
        database_username = 'root'  # database username
        database_password = '123456789'  # database password
        database_ip = 'localhost'  # database server
        database_name = 'digicor_partner'  # database name
        # connection object to database
        database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                       format(database_username, database_password,
                                                              database_ip, database_name))
        return database_connection, database_name

    # function to store data
    def write_table_db(connection, data, table_name):
        # drop the table if it exists
        drop_table(connection, table_name)
        # write table to database
        print('Created table: {}'.format(table_name))
        data.to_sql(con=connection, name=table_name, if_exists='replace')

    # function to drop table
    def drop_table(connection, table_name):
        sql = "DROP TABLE IF EXISTS {};".format(table_name)
        connection.execute(sql)
        print('Dropped table: {}'.format(table_name))

    # function to extact boms table from database
    def get_boms(connection):
        sql = 'SELECT * FROM digicor_partner.boms'
        boms = pd.read_sql(sql, connection)
        return boms

    # function to combine data with boms from db
    def combine_with_boms(df, boms):
        df = df.rename(columns={'boms_id': 'id'})
        df = df.merge(boms, on='id')
        df = df.rename(columns={'name_y': 'name', 'id': 'boms_id'})
        return df

    # function to create applicator table
    def create_applicator_data(boms, applicator_df):
        applicator_with_boms_df = pd.merge(applicator_df, boms, on=['desc'])
        applicator_with_boms_df = applicator_with_boms_df.iloc[:, :8]
        applicator_with_boms_df = applicator_with_boms_df.rename(columns={'id_x': 'id', 'id_y': 'boms_id',
                                                                          'vendor_x': 'vendor', 'mpn_x': 'mpn'})
        cols = applicator_with_boms_df.columns.tolist()
        applicator_with_boms_df = applicator_with_boms_df[cols[:1] + cols[-1:] + cols[2:len(cols) - 1]].head()
        return applicator_with_boms_df

    def get_desc(df):
        df['desc'] = df.Chassis.apply(lambda x:
                                      x.split('-', 1)[1] if '-' in x else x) + ' + ' + \
                     df.Motherboard.apply(lambda x:
                                          x.split('-', 1)[1] if '-' in str(x) else str(x))
        return df
    try:
        # Read files
        supermicro_df = read_file('/Users/mohsinkhan/Desktop/DigiCor/final files/supermicro_final.xlsx', 'excel')
        asus_df = read_file('/Users/mohsinkhan/Desktop/DigiCor/final files/asus_final.xlsx', 'excel')
        intel_df = read_file('/Users/mohsinkhan/Desktop/DigiCor/final files/intel_final.xlsx', 'excel')
        applicator_df = read_file('/Users/mohsinkhan/Desktop/DigiCor/Data files/system info 5 oct 2020.csv', 'csv')

        # Create DB connection
        connection, db_name = connection()

        # Extract boms tables from DB
        boms = get_boms(connection)

        # Create applicator table
        applicator_df_new = create_applicator_data(boms, applicator_df)

        # intel columns rename
        intel_df = intel_df.rename(columns={'Model': 'name',
                                            'Chassis Form Factor': 'form_factor',
                                            # 'Front Drive Form Factor': 'hot_swap_hdd_bays',   # if data present, "Y"
                                            '# of Front Drives Supported': 'num_storage_drives_supported',
                                            'Front Drive Form Factor': 'storage_drive_sizes_supported',
                                            # 'maximum_supported_ram_clock_speed_mhz': 'power_supply',
                                            # 'Chassis Dimensions': 'height',
                                            # 'Chassis Dimensions': 'width',
                                            # 'Chassis Dimensions': 'depth',
                                            'integrated lan': 'gbe',
                                            'Processor Graphics': 'on_board_graphics_adapter_model',
                                            'Max Memory Size (dependent on memory type)': 'maximum_internal_memory',
                                            'Max # of DIMMs': 'num_dimm_slots',
                                            'Memory Types': 'supported_memory_types',
                                            'Intel® Optane™ Memory Supported ‡': 'intel_optane',
                                            # 'Internal Drive Form Factor': 'm2',   # if data present, "Y"
                                            # 'Integrated LAN': 'ipmi_lan_port',    # if data present, "Y"
                                            '# of USB Ports': 'usb_3_0_type_a_ports_quantity',
                                            'Board Chipset': 'motherboard_chipset',
                                            '# of LAN Ports': 'lan_ports',
                                            'Socket': 'processor_socket',
                                            'Extended Warranty Available for Purchase (Select Countries)': 'extended_warranty_available_for_purchase',
                                            'Riser Slot 1: Included Slot Configuration(s)': 'riser_slot_1',
                                            'Riser Slot 2: Included Slot Configuration(s)': 'riser_slot_2',
                                            'Intel® Virtualization Technology for Directed I/O (VT-d) ‡': 'intel_virtual_technology_for_directed_i/o',
                                            'riser slot 3: included slot configuration(s)': 'riser_slot_3'})

        boms = boms[['id', 'name']]

        supermicro_df = get_desc(supermicro_df)

        supermicro_df = combine_with_boms(supermicro_df, boms)
        asus_df = combine_with_boms(asus_df, boms)
        intel_df = combine_with_boms(intel_df, boms)

        # Create a single table for all partners [supermicro, intel, asus]
        combined_df = pd.concat([supermicro_df, asus_df])

        combined_df.columns = map(str.lower, combined_df.columns)
        combined_df.columns = combined_df.columns.str.replace('number', 'num')
        combined_df['name_x'] = combined_df['name']
        combined_df = combined_df.drop(['level', 'name'], axis=1)
        combined_df = combined_df.rename(columns={'name_x': 'name'})

        combined_df2 = pd.concat([combined_df, intel_df])

        combined_df2 = combined_df2.iloc[:, :-1]
        # writing to excel (just for viewing purpose)
        combined_df2.to_excel('/Users/mohsinkhan/Desktop/DigiCor/final files/specifications.xlsx')

        # Write file to database
        '''
        param: connection: A connection to the database server.
        param: data: dataframe to write to database (combined_df).
        param: table_name: name of the new table in database.
        '''
        write_table_db(connection, combined_df2, 'specifications')

        # Writing all three partners to database into three tables

        # write_table_db(connection, supermicro_df, 'supermicro_specifications')
        # write_table_db(connection, asus_df, 'asus_specifications')
        # write_table_db(connection, applicator_df_new, 'applicator_table')
        # write_table_db(connection, intel_test_df, 'intel_specifications')

        return ({ 'Database state' : 'Sucessfull'})
    except:
        return ({'Database state': 'Unsucessfull'})

# crawler()
# database()
# OS_compatibility_data()
# dashboard()
