from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# url = "https://www.supermicro.com/products/system/1U/5019/SYS-5019A-FTN4.cfm"
url = "https://www.supermicro.com/products/system/4U/7049/SYS-7049GP-TRT.cfm"

driver.get(url)
# print(driver.title)



# try:
#     # parts_list = driver.find_element_by_link_text("Parts List")
#     # parts_list.click()
#     main = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "js"))
#     )
#
#
#
#     # articles = main.find_elements_by_tag_name("article")
#     # for article in articles:
#     #     header = article.find_element_by_class_name("feature border_b2")
#     #     # print(header.text)
#
#     with open("output.txt", "w", encoding="utf-8") as file:
#         file.write(str(main.text))
# except:
#     print("hello")
#     # driver.quit()

driver.find_element_by_css_selector("body > div.container.spec-container > div > div:nth-child(5) > span").click()
time.sleep(4)

txt = driver.find_element_by_class_name("js").text
# txt = driver.find_element_by_tag_name("html").text

# txt = driver.find_element_by_class_name("js").text
print(driver.find_element_by_xpath("/html/body/div[5]/div/div[6]").text)

desc = re.findall(r"Product SKUs.*\n(.*)", txt)[0]
# print("desc:"+desc)     # SYS-4029GP-TRT

with open("output"+desc+".txt", "w", encoding="utf-8") as file:
    file.write(str(txt))

driver.quit()

# desc
desc = re.findall(r"Product SKUs.*\n(.*)", txt)[0]
print("desc:"+desc)     # SYS-4029GP-TRT

# Chassis
Motherboard_Chassis = re.findall(r"Motherboard \/ Chassis ([\s\S]+?) \d\n", txt)[0]
print("Chassis:", Motherboard_Chassis.split("\n")[-1])

# Motherboard
# Motherboard_Chassis = re.findall(r"Motherboard / Chassis ([\s\S]*)? \d\n+", txt)[0]
print("Motherboard:", Motherboard_Chassis.split("\n")[:-1])

# Form_factor
Form_factor = re.findall(r"Form Factor\n(.*)", txt)[0]
print("Form_factor:", Form_factor)

# LED_indicators
LED_indicators = "Y" if "LEDs" in txt else "N"
print("LED_indicators:", LED_indicators)

# On_off_switch
On_off_switch = "Y" if "Power On/Off button" in txt else "N"
print("On_off_switch:", On_off_switch)

# Number_of_fans
result = re.findall(r"Fans\n(\d) ", txt)
Number_of_fans = result[0] if result else ""
print("Number_of_fans: " + Number_of_fans)

# Fan_Size
Fan_Size = re.findall(r"FAN .* (\w*) mm", txt)
print("Fan_Size", Fan_Size)

# Product_Colour
Product_Colour = re.findall(r"Product SKUs[\s\S]+? \((.*)\)", txt)[0]
print("Product_Colour", Product_Colour)

# RoHS_Compliance
RoHS_Compliance = "Y" if "RoHS Compliant" in txt else "N"
print("RoHS_Compliance:", RoHS_Compliance)

# Hot_swap_HDD_bays
Hot_swap_HDD_bays = "Y" if "Hot-swap" in txt else "N"
print("Hot_swap_HDD_bays:", Hot_swap_HDD_bays)

# Number_of_storage_drives_supported
Number_of_storage_drives_supported = re.findall(r"Key Features[\s\S]+? ([\d|\d\d]) Hot-swap", txt)[0]
print("Number_of_storage_drives_supported", Number_of_storage_drives_supported)

# Storage_drives_sizes_supported
Storage_drives_sizes_supported = re.findall(r"Key Features[\s\S]+? Hot-swap (\d.\d)", txt)[0]
print("Storage_drives_sizes_supported", Storage_drives_sizes_supported)


cols = ["product_id", "name", "desc", "Chassis", "Motherboard", "Form_factor", "LED_indicators", "On_off_switch",
        "Number_of_fans", "Fan_Size", "Product_Colour", "RoHS_Compliance", "Hot_swap_HDD_bays",
        "Number_of_storage_drives_supported", "Storage_drives_sizes_supported", "Backplane_SKU", "Backplanes_support",
        "Optional_rear_drive_bays", "Supporting_2_5_inch_NVMe", "Number_of_NVMe_Supported_by_Backplane",
        "Number_of_redundant_power_supplies_installed", "Power_Supply_SKU", "Power_Distributer_SKU", "Power_supply",
        "Height_mm", "Width_mm", "Depth_mm", "Chassis_Gross_weight_Kg", "Chassis_Net_Weight",
        "PCl_Express_slots_version", "PCl_Express_x16_slots", "On_Board_Graphics_adapter_model", "ECC",
        "Maximum_internal_memory", "Number_of_DIMM_slots", "Supported_memory_types", "Intel_Optane",
        "Maximum_supported_RAM_clock_speed_MHz", "M_2", "Number_of_M_2_Supported", "Operating_temperature",
        "Storage_temperature", "Operating_Relative_humidity", "Storage_relative_humidity", "PC_health_monitoring",
        "IPMl_LAN_port", "USB_3_0_Type_A_ports_quantity", "Built_in_processor", "Motherboard_chipset", "Lan_Ports",
        "Onboard_Connection", "GbE", "Onboard_Network_Controllers", "Onboard_SAS_Raid_Controller",
        "Supported_storage_drive_interfaces", "Number_of_processors_supported", "Processor_socket", "Quantity_of_Nodes",
        "Nodes", "Use_Cases", "CITRIX_COMPATIBLE", "VM_WARE_COMPATIBLE", "VIRTUALISATION_SERVER", "HyperV",
        "Vertical_Markets", "WINDOWS_OS", "RHEL_Ubuntu_SUSE", "VMWare", "Citrix", "GPU"]

df = pd.DataFrame(columns=cols)
# print(df)
