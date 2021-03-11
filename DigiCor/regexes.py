import re
import math

## Depreciated, used only for asus
class Regexer:

    def __init__(self):

        self.boms_id = 0000
        self.level = "NA"
        self.partner = "NA"
        self.desc = "NA"
        self.product_id = "NA"
        self.name = "NA"
        self.desc = "NA"
        self.Chassis = "NA"
        self.Motherboard = "NA"
        self.Form_factor = "NA"
        self.LED_indicators = "NA"
        self.On_off_switch = "NA"
        self.Number_of_fans = "NA"
        self.Fan_Size = "NA"
        self.Product_Colour = "NA"
        self.RoHS_Compliance = "NA"
        self.Hot_swap_HDD_bays = "NA"
        self.Number_of_storage_drives_supported = "NA"
        self.Storage_drives_sizes_supported = "NA"
        self.Backplane_SKU = "NA"
        self.Backplanes_support = "NA"
        self.Optional_rear_drive_bays = "NA"
        self.Supporting_2_5_inch_NVMe = "NA"
        self.Number_of_NVMe_Supported_by_Backplane = "NA"
        self.Number_of_redundant_power_supplies_installed = "NA"
        self.Power_Supply_SKU = "NA"
        self.Power_Distributer_SKU = "NA"
        self.Power_supply = "NA"
        self.Height_mm = "NA"
        self.Width_mm = "NA"
        self.Depth_mm = "NA"
        self.Chassis_Gross_weight_Kg = "NA"
        self.Chassis_Net_Weight = "NA"
        self.PCl_Express_slots_version = "NA"
        self.PCl_Express_x16_slots = "NA"
        self.On_Board_Graphics_adapter_model = "NA"
        self.ECC = "NA"
        self.Maximum_internal_memory = "NA"
        self.Number_of_DIMM_slots = "NA"
        self.Supported_memory_types = "NA"
        self.Intel_Optane = "NA"
        self.Maximum_supported_RAM_clock_speed_MHz = "NA"
        self.M_2 = "NA"
        self.Number_of_M_2_Supported = "NA"
        self.Operating_temperature = "NA"
        self.Storage_temperature = "NA"
        self.Operating_Relative_humidity = "NA"
        self.Storage_relative_humidity = "NA"
        self.PC_health_monitoring = "NA"
        self.IPMl_LAN_port = "NA"
        self.USB_3_0_Type_A_ports_quantity = "NA"
        self.Built_in_processor = "NA"
        self.Motherboard_chipset = "NA"
        self.Lan_Ports = "NA"
        self.Onboard_Connection = "NA"
        self.GbE = "NA"
        self.Onboard_Network_Controllers = "NA"
        self.Onboard_SAS_Raid_Controller = "NA"
        self.Supported_storage_drive_interfaces = "NA"
        self.Number_of_processors_supported = "NA"
        self.Processor_socket = "NA"
        self.Quantity_of_Nodes = "NA"
        self.Nodes = "NA"
        self.Use_Cases = "NA"
        self.CITRIX_COMPATIBLE = "NA"
        self.VM_WARE_COMPATIBLE = "NA"
        self.VIRTUALISATION_SERVER = "NA"
        self.HyperV = "NA"
        self.Vertical_Markets = "NA"
        self.WINDOWS_OS = "NA"
        self.RHEL_Ubuntu_SUSE = "NA"
        self.VMWare = "NA"
        self.Citrix = "NA"
        self.GPU = "NA"

    def initialise_vars(self):
        self.level = "NA"
        self.partner = "NA"
        self.desc = "NA"
        self.product_id = "NA"
        self.name = "NA"
        self.desc = "NA"
        self.Chassis = "NA"
        self.Motherboard = "NA"
        self.Form_factor = "NA"
        self.LED_indicators = "NA"
        self.On_off_switch = "NA"
        self.Number_of_fans = "NA"
        self.Fan_Size = "NA"
        self.Product_Colour = "NA"
        self.RoHS_Compliance = "NA"
        self.Hot_swap_HDD_bays = "NA"
        self.Number_of_storage_drives_supported = "NA"
        self.Storage_drives_sizes_supported = "NA"
        self.Backplane_SKU = "NA"
        self.Backplanes_support = "NA"
        self.Optional_rear_drive_bays = "NA"
        self.Supporting_2_5_inch_NVMe = "NA"
        self.Number_of_NVMe_Supported_by_Backplane = "NA"
        self.Number_of_redundant_power_supplies_installed = "NA"
        self.Power_Supply_SKU = "NA"
        self.Power_Distributer_SKU = "NA"
        self.Power_supply = "NA"
        self.Height_mm = "NA"
        self.Width_mm = "NA"
        self.Depth_mm = "NA"
        self.Chassis_Gross_weight_Kg = "NA"
        self.Chassis_Net_Weight = "NA"
        self.PCl_Express_slots_version = "NA"
        self.PCl_Express_x16_slots = "NA"
        self.On_Board_Graphics_adapter_model = "NA"
        self.ECC = "NA"
        self.Maximum_internal_memory = "NA"
        self.Number_of_DIMM_slots = "NA"
        self.Supported_memory_types = "NA"
        self.Intel_Optane = "NA"
        self.Maximum_supported_RAM_clock_speed_MHz = "NA"
        self.M_2 = "NA"
        self.Number_of_M_2_Supported = "NA"
        self.Operating_temperature = "NA"
        self.Storage_temperature = "NA"
        self.Operating_Relative_humidity = "NA"
        self.Storage_relative_humidity = "NA"
        self.PC_health_monitoring = "NA"
        self.IPMl_LAN_port = "NA"
        self.USB_3_0_Type_A_ports_quantity = "NA"
        self.Built_in_processor = "NA"
        self.Motherboard_chipset = "NA"
        self.Lan_Ports = "NA"
        self.Onboard_Connection = "NA"
        self.GbE = "NA"
        self.Onboard_Network_Controllers = "NA"
        self.Onboard_SAS_Raid_Controller = "NA"
        self.Supported_storage_drive_interfaces = "NA"
        self.Number_of_processors_supported = "NA"
        self.Processor_socket = "NA"
        self.Quantity_of_Nodes = "NA"
        self.Nodes = "NA"
        self.Use_Cases = "NA"
        self.CITRIX_COMPATIBLE = "NA"
        self.VM_WARE_COMPATIBLE = "NA"
        self.VIRTUALISATION_SERVER = "NA"
        self.HyperV = "NA"
        self.Vertical_Markets = "NA"
        self.WINDOWS_OS = "NA"
        self.RHEL_Ubuntu_SUSE = "NA"
        self.VMWare = "NA"
        self.Citrix = "NA"
        self.GPU = "NA"

    def run_regexes_supermicro(self, data, boms_id, product_type, description, partner, type):

        self.initialise_vars()
        self.boms_id = boms_id
        self.type = type
        self.partner = partner
        self.desc = description

        if "chassis" in product_type:
            for col in data.columns:
                if 'product sku' in col.lower():
                    self.Chassis = data[col].str.extract(r'([A-Za-z0-9-]+)\s')[0][0]

                elif 'backplane' in col.lower():
                    self.Supporting_2_5_inch_NVMe = data[col].apply(lambda x: 'Y' if '2.5-inch' in x else 'N')[0][0]
                    self.RoHS_Compliance = data[col].apply(lambda x: 'Y' if 'rohs' in x.lower() else 'N')[0][0]
                    self.Backplanes_support = data[col].str.extract(
                        r'(SAS[0-9]?\/SATA[0-9]?\/NVMe[0-9]?|SAS[0-9]?\/SATA[0-9]?|SAS[0-9]?|SATA[0-9]?|NVMe)')[0][0]

                    try:
                        self.Number_of_NVMe_Supported_by_Backplane = int(data[col].str.extract(r'.*\s2.5-inch\s.*\s(\d)x\sNVMe.*')[0][0])
                    except:
                        if self.Supporting_2_5_inch_NVMe == 'Y' and not math.isnan(data[col].str.extract(r'.*\s2.5-inch\s.*\s(\d)x\sNVMe.*')[0][0]):
                            self.Number_of_NVMe_Supported_by_Backplane = int(data[col].str.extract(r'.*\s2.5-inch\s.*\s(\d)x\sNVMe.*')[0][0])
                        else:
                            self.Number_of_NVMe_Supported_by_Backplane = 0

                elif 'available color' in col.lower():
                    self.Product_Colour = data[col][0]

                elif 'drive bay' in col.lower():
                    self.Number_of_storage_drives_supported = data[col].str.extract('([0-9]+)\sx\s([0-9."]+){1}')[0][0]
                    self.Storage_drives_sizes_supported = data[col].str.extract('[0-9]+\sx\s([0-9."]+) {1}')[0][0]
                    self.Hot_swap_HDD_bays = data[col].apply(lambda x: 'Y' if 'hot-swap drive bay' in x.lower() else 'N')[0][0]

                elif 'bays' in col.lower():
                    self.Number_of_storage_drives_supported = data[col].str.extract(r'.*\s(\d+)x{1}')[0][0]
                    self.Storage_drives_sizes_supported = data[col].str.extract('.*(\d.\d"){1}')[0][0]
                    self.Hot_swap_HDD_bays = data[col].apply(lambda x: 'Y' if 'hot-swap drive bay' in x.lower() else 'N')[0][0]

                elif 'height' in col.lower():
                    self.Height_mm = data[col].str.extract(r'([0-9]+)\s?mm{1}')[0][0]

                elif 'width' in col.lower():
                    self.Width_mm = data[col].str.extract(r'([0-9]+)\s?mm{1}')[0][0]

                elif 'depth' in col.lower():
                    self.Depth_mm = data[col].str.extract(r'([0-9]+)\s?mm{1}')[0][0]

                elif 'gross weight' in col.lower():
                    self.Chassis_Gross_weight_Kg = data[col].str.extract(r'\((\d.+)\s?kg\){1}')[0][0]
                    self.Chassis_Net_Weight = data[col].str.extract(r'(\d+)\s?lbs{1}')[0][0]

                elif 'temperature' in col.lower() and 'opera' in col.lower():
                    if 'non-' in col.lower():
                        self.Storage_temperature = data[col][0]
                    else:
                        self.Operating_temperature = data[col][0]

                elif 'humidity' in col.lower() and 'opera' in col.lower():
                    if 'non-' in col.lower():
                        self.Operating_Relative_humidity = data[col][0]
                    else:
                        self.Storage_relative_humidity = data[col][0]

                elif 'environmental' in col.lower():
                    temp = data[col].str.split(')').values[0]
                    try:
                        self.Storage_temperature = temp[0].split(': ')[1] + ')'
                        self.Operating_temperature = temp[1].split(': ')[1] + ')'
                        self.Operating_Relative_humidity = temp[2].split(': ')[1] + ')'
                        self.Storage_relative_humidity = temp[3].split(': ')[1] + ')'
                    except:
                        self.Storage_temperature = 'NA'
                        self.Operating_temperature = 'NA'
                        self.Operating_Relative_humidity = 'NA'
                        self.Storage_relative_humidity = 'NA'


                elif 'motherboard' in col.lower() and product_type == 'chassis-s':
                    self.Motherboard = data[col][0]

                elif 'Power Supply' in data.columns:
                    self.Power_supply = data['Power Supply'][0]

                elif 'redundant' in col.lower() or 'titanium' in col.lower() or 'power supply' in col.lower():
                    self.Power_supply = data[col][0]

                elif 'all_pce' in col.lower():
                    self.PCl_Express_slots_version = data[col][0]

                elif 'pci_Express_x16_slots' in col.lower():
                    self.PCl_Express_x16_slots = data[col][0]

                elif 'num_of_M_2_Supported' in col.lower():
                    self.Number_of_M_2_Supported = data[col][0]

                elif 'm.2' in col.lower():
                    self.M_2 = data[col][0]

                elif 'led' in col.lower():
                    self.LED_indicators = data[col].apply(lambda x: 'Y' if x else 'N')[0][0]

                elif 'buttons' in col.lower():
                    self.On_off_switch = data[col].apply(lambda x: 'Y' if x else 'N')[0][0]


            self.Form_factor = data['Form Factor'].str.extract(r'([0-9]+U)\s')[0][0]
            self.Number_of_fans = data['num_fans'][0]
            self.Fan_Size = data['fan_dims'].str.extract(r'(\d.*\s[m|c]m)')[0][0]
            self.Backplane_SKU = data['bp sku'][0]
            self.Optional_rear_drive_bays = data['Form Factor'].apply(lambda x: 'Y' if 'rear' in x.lower() else 'N')[0][0]
            self.Number_of_redundant_power_supplies_installed = "NA"
            self.Power_Supply_SKU = data['pws'][0]
            self.Power_Distributer_SKU = data['pdb'][0]
            self.PC_health_monitoring = 'Y'

        elif product_type == "motherboard":

            for col in data.columns:
                if 'graphics' in col.lower():
                    self.On_Board_Graphics_adapter_model = data[col][0]
                elif 'memory type' in col.lower():
                    self.Supported_memory_types = data[col][0]
                    self.ECC = data[col].apply(lambda x: 'Y' if 'ecc' in x.lower() else 'N')[0][0]
                    self.Maximum_supported_RAM_clock_speed_MHz = data[col].str.extract(r'(\d+){1}')[0][0]
                elif 'memory capacity' in col.lower():
                    self.Maximum_internal_memory = data[col].str.extract(r'(\d+\s?TB)|(\d+\s?GB)|(\d.+\s?TB)')[0][0]
                    self.Number_of_DIMM_slots = data[col].str.extract(r'(\d+)\sDIMM')[0][0]
                elif 'management' in col.lower():
                    self.IPMl_LAN_port = data[col].apply(lambda x: 'Y' if 'ipmi' in x.lower() else 'N')[0][0]
                elif 'usb' in col.lower():
                    self.USB_3_0_Type_A_ports_quantity = data[col].str.extract(r'([0-9]+)\sUSB\s3\.[0-9]+')[0][0]
                elif 'lan' in col.lower():
                    self.Lan_Ports = data[col].str.extract(r'(\d+){1}')[0][0]
                    self.Onboard_Connection = data[col].str.extract(r'\d+\s(.*)')[0][0]
                elif 'chipset' in col.lower():
                    self.Motherboard_chipset = data[col][0]
                elif 'network controllers' in col.lower():
                    self.GbE = data[col].str.extract(r'(\d+)GbE')[0][0]
                    self.Onboard_Network_Controllers = data[col][0]
                elif 'sata' in col.lower():
                    self.Supported_storage_drive_interfaces = data[col].str.extract(r'(SATA.*)\(')[0][0]
                elif 'product skus' in col.lower():
                    self.Motherboard = data[col].str.extract(r'([A-Za-z0-9-]+)\s')[0][0]
                elif 'all_pce' in col.lower():
                    self.PCl_Express_slots_version = data[col][0]
                elif 'pci' in col.lower():
                    self.PCl_Express_x16_slots = data[col][0]
                elif 'num_m2' in col.lower():
                    self.Number_of_M_2_Supported = data[col][0]
                elif 'm.2' in col.lower():
                    self.M_2 = data[col][0]
                elif 'socket' in col.lower():
                    self.Processor_socket = data[col][0]
                    if self.Processor_socket:
                        try:
                            self.Number_of_processors_supported = data[col].apply(lambda x: 2 if 'dual' in x.lower() else (1 if 'single' in data[col].lower() else 0))[0]
                        except:
                            self.Number_of_processors_supported = "NA"

            self.Built_in_processor = "N"
            self.Onboard_SAS_Raid_Controller = "NA"
            self.Quantity_of_Nodes = "NA"
            self.Nodes = "NA"

        return True

    def run_regexes_intel(self, intel_df, each_prod, each_partner):
        self.initialise_vars()
        self.partner = each_partner
        self.product_id = "NA"
        self.name = "NA"
        self.desc = each_prod

    def run_regexes_asus(self, xml_asus_data, boms_id, each_prod, each_partner):
        self.initialise_vars()
        self.boms_id = boms_id
        self.partner = each_partner
        self.product_id = "NA"
        self.name = "NA"
        self.desc = each_prod

        self.Processor_socket = re.findall(r"rocessor[\s\S]+?<[\dx ]+(.*)", xml_asus_data)[0]

        self.Motherboard_chipset = re.findall(r"Core Logic[\s\S]+?<(.*)>", xml_asus_data)[0]

        self.Number_of_DIMM_slots = re.findall(r"Total Slots[\s\S]+?<(\d).*>", xml_asus_data)[0]

        result = list(set(re.findall(r" ([\w]*DIMM)", xml_asus_data)))
        self.Supported_memory_types = ', '.join(result) if result else "NA"

        result = re.findall(r"emory Siz[\s\S]+?<([\s\S]+?)>", xml_asus_data)
        if result:
            size_list = re.findall(r"(\d*)GB", result[0])
            if len(size_list) > 0:
                self.Maximum_internal_memory = max(list(map(int, size_list)))

        if "NVMe" or "NVME" in xml_asus_data:
            self.Supporting_2_5_inch_NVMe = "Y"
            result = re.findall(r"(\d) x.+?(?:NVM)[\w\/]+? ", xml_asus_data)
            if result:
                self.Number_of_NVMe_Supported_by_Backplane = result[0]
        else:
            self.Supporting_2_5_inch_NVMe = "N"

        if "M.2" in xml_asus_data:
            self.M_2 = "Y"
            result = re.findall(r"(\d) ?x ?(?:M.2)", xml_asus_data)
            if result:
                result_2 = list(set(result))
                self.Number_of_processors_supported = ', '.join(result_2) if result_2 else "NA"
        else:
            self.M_2 = "N"

        result = re.findall(r"HDD Bays>\n?([\s\S]+?)>\n<", xml_asus_data)
        if result:
            result_2 = (re.findall(r"(\d) ?x.*", result[0]))
            self.Number_of_storage_drives_supported = sum(list(map(int, result_2))) if result_2 else "NA"
        else:
            self.Number_of_storage_drives_supported = "NA"

        # result = re.findall(r"(\d+.?\d\").*(?:HDD|SSD).+?Bays", xml_asus_data)
        if result:
            result_2 = (re.findall(r'(\d.\d\").*', result[0]))
            self.Storage_drives_sizes_supported = ', '.join(list(set(result_2))) if result_2 else "NA"
        else:
            self.Storage_drives_sizes_supported = "NA"

        if "Hot-swap" in xml_asus_data:
            self.Hot_swap_HDD_bays = "Y"
        else:
            self.Hot_swap_HDD_bays = "N"

        result = re.findall(r"(\d) ?x.*(?:LAN|RJ.*45)", xml_asus_data)
        self.Lan_Ports = result[0] if result else "NA"
        self.Onboard_Connection = "RJ45" if result else "NA"

        if "LED" in xml_asus_data:
            self.LED_indicators = "Y"
        else:
            self.LED_indicators = "N"

        result = re.findall(r"Dimensions[\s\S]+?<(.*)", xml_asus_data)
        result_2 = re.findall(r"([\d]+?)[ m>]", result[0])
        self.Height_mm = result_2[0] if result_2 else "NA"
        self.Width_mm = result_2[1] if result_2 else "NA"
        self.Depth_mm = result_2[2] if result_2 else "NA"

        result = re.findall(r"Net Weight.+?([\d.]*) ?[Kk][Gg]", xml_asus_data)
        self.Chassis_Net_Weight = result[0] if result else "NA"

        result = re.findall(r"Gross Weight.+?([\d.]*) ?[Kk][Gg]", xml_asus_data)
        self.Chassis_Gross_weight_Kg = result[0] if result else "NA"

        result = re.findall(r"Power Supply[\s\S]+?<([\s\S]+?)>", xml_asus_data)
        self.Power_supply = result[0] if result else "NA"

        result = re.findall(r"Operation temperature: ?(.*)", xml_asus_data)
        self.Operating_temperature = str(str(result[0]).split("/")[0]) if result else "NA"

        result = re.findall(r"Form Factor>\n?.+?<(.*)>", xml_asus_data)
        self.Form_factor = result[0] if result else "NA"

        if "Power Switch" in xml_asus_data:
            self.On_off_switch = "Y"
        else:
            self.On_off_switch = "N"

        result = re.findall(r"Backplane [Ss]upports(.*)", xml_asus_data)
        if result:
            result_2 = (re.findall(r"((?:SATA|SAS|NVM)[\w\/]*)", result[0]))
            self.Backplanes_support = result_2[0] if result_2 else "NA"
        else:
            self.Backplanes_support = "NA"

        result = re.findall(r"(\d\+?\w).+?(?:edundant.+?ower.+?uppl)", xml_asus_data)
        if result:
            result_2 = result[0].split("+")
            self.Number_of_redundant_power_supplies_installed = sum(list(map(int, result_2)))
        else:
            self.Backplanes_support = "NA"

        result = re.findall(r"Expansion Slots[\s\S]+?<([\s\S]+?)>", xml_asus_data)
        self.PCl_Express_slots_version = (', '.join(result[0].split("\n"))).replace("\t", "") if result else "NA"

        result = re.findall(r"Graphic[\s\S]+?<([\s\S]+?)>", xml_asus_data)
        self.On_Board_Graphics_adapter_model = result[0] if result else "NA"

        if "ECC" in xml_asus_data:
            self.ECC = "Y"
        else:
            self.ECC = "N"

        result = re.findall(r"(\d).*USB.*ype[ -]A", xml_asus_data)
        self.USB_3_0_Type_A_ports_quantity = result[0] if result else "NA"

        result = re.findall(r"(\d).*GbE LAN", xml_asus_data)
        self.GbE = result[0] if result else "NA"

        result = re.findall(r"Networking[\s\S]+?<([\s\S]+?)>", xml_asus_data)
        self.Onboard_Network_Controllers = result[0] if result else "NA"

        result = re.findall(r"<Drive Bays[\s\S]+?<([\s\S]+?)>\n<", xml_asus_data)
        if result:
            pass
        else:
            result = re.findall(r"<Storage[\s\S]+?<([\s\S]+?)>\n<", xml_asus_data)
        result_2 = re.findall(r"\d x.+?((?:SATA|SAS|NVM)[\w\/]+?) ", result[0])
        self.Supported_storage_drive_interfaces = ', '.join(result_2) if result_2 else "NA"

        result = re.findall(r"OS Suppo[\s\S]+?[Cc]itrix", xml_asus_data)
        self.CITRIX_COMPATIBLE = "Y" if result else "N"

        result = re.findall(r"OS Suppo[\s\S]+?VMware", xml_asus_data)
        self.VM_WARE_COMPATIBLE = "Y" if result else "N"

        result = re.findall(r"OS Suppo[\s\S]+?indows.*10", xml_asus_data)
        self.WINDOWS_OS = "Y" if result else "N"

        if "Ubuntu" in xml_asus_data or "SuSE" in xml_asus_data:
            self.RHEL_Ubuntu_SUSE = "Y"
        else:
            self.RHEL_Ubuntu_SUSE = "N"
