import re

class Regexer:

    def __init__(self):

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
        # self.result = "NA"

        # self.expand_type = ""

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
        # self.result = "NA"

        # self.expand_type = ""

    def run_regexes(self, txt, each_prod, expand_type, each_partner):

        self.initialise_vars()

        self.desc = each_prod
        self.level = expand_type
        self.partner = each_partner

        # counter_txt_list = 0

        # for each_expand_type in expand_type_list:
        # print(expand_type)
        # txt = str(txt_list[counter_txt_list])

        # expand_type = str(each_expand_type)

        # Chassis / Motherboard
        if "ompone" in expand_type:
            self.Chassis = re.findall(r"Product SKUs[\n]?(.*)", txt)[0]
            print("Chassis:", self.Chassis)
        else:
            self.Motherboard = re.findall(r"Product SKUs[\n]?(.*)", txt)[0]
            print("Motherboard:", self.Motherboard)

        # # Chassis
        # self.Chassis = re.findall(r""+expand_type+"[\s\S]+?\n(.*)\n\d+", txt)[0]
        #
        # # Motherboard
        # # Motherboard = re.findall(r"Parts List[\s\S]+?(.*) Motherboard[s]?[\n\d]", txt)[0]
        # result = re.findall(r"("+expand_type+"[\s\S]+? Motherboard[\s\S]+?Chassis)", txt)
        # self.Motherboard = re.findall(r"(.*) Motherboard", result[0]) if result else "NA"

        # Form_factor
        result = re.findall(r"Form Factor\n([\s\S]\D+?) ", txt)
        if self.Form_factor == "NA" and result:
            self.Form_factor = result[0]
        # print("Form_factor:", self.Form_factor)

        # LED_indicators
        if self.LED_indicators == "NA":
            self.LED_indicators = "Y" if "LEDs" in txt else "N"
        # print("LED_indicators:", self.LED_indicators)

        # On_off_switch
        if self.On_off_switch == "NA":
            self.On_off_switch = "Y" if "Power On/Off button" in txt else "N"
        # print("On_off_switch:", self.On_off_switch)

        # Number_of_fans
        result = re.findall(r"System Cooling\n?Fans\n(\d).? ", txt)
        if self.Number_of_fans == "NA" and result:
            self.Number_of_fans = result[0]
        else:
            self.Number_of_fans = "0"
        # print("Number_of_fans: " + self.Number_of_fans)

        # Fan_Size
        self.Fan_Size = re.findall(r"FAN .* (\w*) mm", txt)
        # print("Fan_Size", self.Fan_Size)

        # Product_Colour
        if self.Product_Colour == "NA":
            self.Product_Colour = re.findall(r"Product SKUs[\s\S]+? \((.*)\)", txt)[0]
        # print("Product_Colour", self.Product_Colour)

        # RoHS_Compliance
        if self.RoHS_Compliance == "NA":
            self.RoHS_Compliance = "Y" if "RoHS Compliant" in txt else "N"
        # print("RoHS_Compliance:", self.RoHS_Compliance)

        # Hot_swap_HDD_bays
        if self.Hot_swap_HDD_bays == "NA":
            self.Hot_swap_HDD_bays = "Y" if "Hot-swap" in txt else "N"
        # print("Hot_swap_HDD_bays:", self.Hot_swap_HDD_bays)

        # Number_of_storage_drives_supported
        result = re.findall(r"Key Features[\s\S]+? ([\d|\d\d]) Hot-swap", txt)
        self.Number_of_storage_drives_supported = result[0] if result else "0"
        # print("Number_of_storage_drives_supported:", self.Number_of_storage_drives_supported)

        # Storage_drives_sizes_supported
        result = re.findall(r"Key Features[\s\S]+? Hot-swap (\d.\d)", txt)
        self.Storage_drives_sizes_supported = result[0] if result else "0"
        # print("Storage_drives_sizes_supported:", self.Storage_drives_sizes_supported)

        # Backplane_SKU
        result = re.findall(r"Backplane\n?(BPN.*)", txt)
        if self.Backplane_SKU == "NA" and result:
            self.Backplane_SKU = result[0]
        # print("Backplane_SKU:", self.Backplane_SKU)

        # Backplanes_support
        # need to recheck this
        self.Backplanes_support = ""
        self.Backplanes_support = "SATA3" if "SATA3" in txt else self.Backplanes_support
        self.Backplanes_support = "SAS" if "SAS" in txt else self.Backplanes_support
        self.Backplanes_support = "SAS2" if "SAS2" in txt else self.Backplanes_support
        self.Backplanes_support = "SAS3" if "SAS3" in txt else self.Backplanes_support
        self.Backplanes_support = "SAS3/SATA3" if "SATA3" and "SAS3" in txt else self.Backplanes_support
        # print("Backplanes_support:", self.Backplanes_support)

        # Optional_rear_drive_bays
        # How to find "Optional_rear_drive_bays"

        # Supporting_2_5_inch_NVMe
        result = re.findall(r".*\s(2.5-inch)\s.*\s\dx\sNVMe.*", txt)
        if self.Supporting_2_5_inch_NVMe == "NA" and result:
            self.Supporting_2_5_inch_NVMe = "Y"
        else:
            self.Supporting_2_5_inch_NVMe = "N"

        print("Supporting_2_5_inch_NVMe:", self.Supporting_2_5_inch_NVMe)

        # Number_of_NVMe_Supported_by_Backplane
        result = re.findall(r".*\s2.5-inch\s.*\s(\d)x\sNVMe.*", txt)
        if self.Number_of_NVMe_Supported_by_Backplane == "NA" and result:
            self.Number_of_NVMe_Supported_by_Backplane = result[0]
        else:
            self.Number_of_NVMe_Supported_by_Backplane = 0
        print("Number_of_NVMe_Supported_by_Backplane:", self.Number_of_NVMe_Supported_by_Backplane)

        # Number_of_redundant_power_supplies_installed
        result = re.findall(r"W(.*)Redundant Power", txt)
        if self.Number_of_redundant_power_supplies_installed == "NA" and result:

            self.Number_of_redundant_power_supplies_installed = ("1" if result[0] == " " else result[0]).strip()
        else:
            self.Number_of_redundant_power_supplies_installed = "0"
        # print("Number_of_redundant_power_supplies_installed:", self.Number_of_redundant_power_supplies_installed)

        # Power_Supply_SKU
        result = re.findall(r"" + expand_type + "[\s\S]+?Power Supply\n?(.*)\n", txt)
        # result = re.findall("([0 - 9]{4}W\ / +?[0-9]{4}W\s\w * \sPower Supply){1}", txt)
        if self.Power_Supply_SKU == "NA" and result:
            self.Power_Supply_SKU = result[0]
        # print("Power_Supply_SKU:", self.Power_Supply_SKU)

        # Power_Distributer_SKU
        result = re.findall(r"" + expand_type + "[\s\S]+?Power Distributor\n?(.*)\n", txt)
        if self.Power_Supply_SKU == "NA" and result:
            self.Power_Supply_SKU = result[0]
        # print("Power_Supply_SKU:", self.Power_Supply_SKU)

        # Power_supply
        result = re.findall(
            r"Key Features[\s\S]+?\n[\d|\d\d]\.? ?(.*[Pp]ower.*(\n.*Titanium.*)?)[\s\S]+?Specifications", txt)
        if self.Power_supply == "NA" and result:
            self.Power_supply = result[0][0].replace("\n", " ")
        # print("Power_supply:", self.Power_supply)

        # Height_mm
        result = re.findall(r"Height[\s\S]+?(\d* ?mm)", txt)
        if self.Height_mm == "NA" and result:
            self.Height_mm = result[0]
        # print("Height_mm:", self.Height_mm)

        # Width_mm
        result = re.findall(r"Width\n[\s\S]+?(\d* ?mm)", txt)
        if self.Width_mm == "NA" and result:
            self.Width_mm = result[0]
        # print("Width_mm:", self.Width_mm)

        # Depth_mm
        result = re.findall(r"Depth\n[\s\S]+?(\d* ?mm)", txt)
        if self.Depth_mm == "NA" and result:
            self.Depth_mm = result[0]
        # print("Depth_mm:", self.Depth_mm)

        # Chassis_Gross_weight_Kg
        result = re.findall(r"Gross Weight.*\((.*)\)", txt)
        if self.Chassis_Gross_weight_Kg == "NA" and result:
            self.Chassis_Gross_weight_Kg = result[0]
        # print("Chassis_Gross_weight_Kg:", self.Chassis_Gross_weight_Kg)

        # Chassis_Net_Weight
        result = re.findall(r"Net Weight.*\((.*)\)", txt)
        if self.Chassis_Net_Weight == "NA" and result:
            self.Chassis_Net_Weight = result[0]
        # print("Chassis_Net_Weight:", self.Chassis_Net_Weight)

        # PCl_Express_slots_version
        result = re.findall(r"(Key Features[\s\S]+?Specifications)", txt)[0]
        result_1 = re.findall(r"(.*PCI.*)", result)
        if self.PCl_Express_slots_version == "NA" and result_1:
            self.PCl_Express_slots_version = result_1[0]
        # print("PCl_Express_slots_version:", self.PCl_Express_slots_version)

        # On_Board_Graphics_adapter_model
        result = re.findall(r"Graphics[\n]?(.*)", txt)
        if self.PCl_Express_slots_version == "NA" and result:
            self.On_Board_Graphics_adapter_model = result[0]
        # print("On_Board_Graphics_adapter_model:", self.On_Board_Graphics_adapter_model)

        # ECC
        self.ECC = "Y" if "ECC" in txt and self.ECC == "NA" else "N"
        # print("ECC:", self.ECC)

        # Maximum_internal_memory
        result = re.findall(r"Memory Capacity[\s\S]+? (\d*[TG]B).*ECC", txt)
        if self.Maximum_internal_memory == "NA" and result:
            self.Maximum_internal_memory = result[0]
        # print("Maximum_internal_memory:", self.Maximum_internal_memory)

        # Number_of_DIMM_slots
        result = re.findall(r"(\d*) DIMM slots", txt)
        if self.Number_of_DIMM_slots == "NA" and result:
            self.Number_of_DIMM_slots = result
        print("Number_of_DIMM_slots:", self.Number_of_DIMM_slots)

        # Supported_memory_types
        result = re.findall(r"Memory Type[\s\S]+?ECC (.*)", txt)
        if self.Supported_memory_types == "NA" and result:
            self.Supported_memory_types = result[0]
        # print("Supported_memory_types:", self.Supported_memory_types)

        # Intel_Optane
        result = re.findall(r"Intel.*Optane", txt)
        if self.Intel_Optane == "NA" and result:
            self.Intel_Optane = result[0]
        # print("Intel_Optane:", self.Intel_Optane)

        # Maximum_supported_RAM_clock_speed_MHz
        # needs re check
        # not consistent for "4029GP-TRT" and "826BE1C4-R1K23LPB"
        result = re.findall(r"Memory Type[\s\S]+?(\S*)MHz", txt)
        if result and self.Maximum_supported_RAM_clock_speed_MHz == "NA" and '' not in result:
            # result = re.findall(r"Memory Type[\s\S]+?(\S*)MHz", result_0[0])
            result = re.sub("[^0-9\/]", "", result[0])
            supported_RAM_clock_speed_MHz_list = result.split("/")
            # let convert all strings within the list to int
            supported_RAM_clock_speed_MHz_list = list(map(int, supported_RAM_clock_speed_MHz_list))
            self.Maximum_supported_RAM_clock_speed_MHz = max(supported_RAM_clock_speed_MHz_list)
            # print("Maximum_supported_RAM_clock_speed_MHz:", self.Maximum_supported_RAM_clock_speed_MHz)

        # M_2
        self.M_2 = "Y" if "M.2" in txt and self.M_2 == "NA" else "N"
        # print("M_2:", self.M_2)

        # Number_of_M_2_Supported
        result = re.findall(r"(?:.)*(\d) NVMe.*M\.2", txt)
        if result and self.Number_of_M_2_Supported == "NA":
            self.Number_of_M_2_Supported = result[0]
        else:
            result_1 = re.findall(r"(?:.)*(\d).*M\.2", txt)
            if result_1:
                self.Number_of_M_2_Supported = result_1[0]
        # print("Number_of_M_2_Supported:", self.Number_of_M_2_Supported)

        # Operating_temperature
        result = re.findall(r"Operating Temperature.*:?\n?(.*)", txt)
        if self.Operating_temperature == "NA" and result:
            self.Operating_temperature = result[0]
        # print("Operating_temperature:", self.Operating_temperature)

        # Storage_temperature
        result = re.findall(r"Non-operating Temperature.*:?\n?(.*)", txt)
        if self.Storage_temperature == "NA" and result:
            self.Storage_temperature = result[0]
        # print("Storage_temperature:", self.Storage_temperature)

        # Operating_Relative_humidity
        result = re.findall(r"Operating Relative Humidity.*:?\n?(.*)", txt)
        if self.Operating_Relative_humidity == "NA" and result:
            self.Operating_Relative_humidity = result[0]
        # print("Operating_Relative_humidity:", self.Operating_Relative_humidity)

        # Storage_relative_humidity
        result = re.findall(r"Non-operating Relative Humidity.*:?\n?(.*).*:?\n?(.*)", txt)
        if self.Storage_relative_humidity == "NA" and result:
            self.Storage_relative_humidity = result[0]
        # print("Storage_relative_humidity:", self.Storage_relative_humidity)

        # PC_health_monitoring
        # How come "PC Health Monitoring" for "SYS-4029GP-TRT" is Yes and "SYS-5019A-FTN4" is "No"

        # IPMl_LAN_port
        result = re.findall(r"(IPM.*over LAN)", txt)
        self.IPMl_LAN_port = "Y" if result and self.IPMl_LAN_port == "NA" else "N"
        # print("IPMl_LAN_port:", self.IPMl_LAN_port)

        # USB_3_0_Type_A_ports_quantity
        result = re.findall(r"(\d) USB 3\.0", txt)
        self.USB_3_0_Type_A_ports_quantity = result[0] if result and self.USB_3_0_Type_A_ports_quantity == "NA" \
            else "0"
        # print("USB_3_0_Type_A_ports_quantity:", self.USB_3_0_Type_A_ports_quantity)

        # Built_in_processor
        result = re.findall(r"Processor/Cache[\s\S]+?(.*[Pp]rocessor[s]?)", txt)
        if self.Built_in_processor == "NA" and result:
            self.Built_in_processor = result[0]
        # print("Built_in_processor:", self.Built_in_processor)

        # Motherboard_chipset
        result_0 = re.findall(r"On-Board Devices[\s\S]+?[\n](.*\d)", txt)
        if result_0 and self.Motherboard_chipset == "NA":
            result = result_0[0]
            self.Motherboard_chipset = "SOC" if "SOC" in result else result[0]
        # print("Motherboard_chipset:", self.Motherboard_chipset)

        # Lan_Ports
        result = re.findall(r"Input \/ Output[\s\S]+?LAN[\s\S]+?(\d).*RJ45", txt)
        if self.Lan_Ports == "NA" and result:
            self.Lan_Ports = result[0]
        # print("Lan_Ports:", self.Lan_Ports)

        # GbE
        # How to find GbE

        # Onboard_Network_Controllers
        result = re.findall(r"On-Board Devices[\s\S]+?Network Controllers\n?([\s\S]+?)\nIPMI", txt)
        if self.Onboard_Network_Controllers == "NA" and result:
            self.Onboard_Network_Controllers = result[0].replace("\n", " ")
        # print("Onboard_Network_Controllers:", self.Onboard_Network_Controllers)

        # Onboard_SAS_Raid_Controller
        result = re.findall(r"On-Board Devices[\s\S]+?\nSAS\n?([\s\S]*)\n?Network Controllers", txt)
        self.Onboard_SAS_Raid_Controller = result[0].replace("\n", "; ") if result else "NA"
        # print("Onboard_SAS_Raid_Controller:", self.Onboard_SAS_Raid_Controller)

        # Supported_storage_drive_interfaces
        # How to find Supported_storage_drive_interfaces

        # Number_of_processors_supported
        if self.Built_in_processor:
            comma_count = self.Built_in_processor.count(",")
            and_count = self.Built_in_processor.count("and")
            self.Number_of_processors_supported = 1 + comma_count + and_count
        else:
            self.Number_of_processors_supported = 0
        # print("Number_of_processors_supported:", self.Number_of_processors_supported)

        # Processor_socket
        result = re.findall(r"Processor\/Cache[\s\S]+?(.*GA.*)", txt)
        if self.Processor_socket == "NA" and result:
            self.Processor_socket = result[0]
        # print("Processor_socket:", self.Processor_socket)

        # Quantity_of_Nodes
        result = re.findall(r"(?:Key Features)?(.*) [hH]ot-plug(gable)? [sS]ystem", txt)
        if self.Quantity_of_Nodes == "NA" and result:
            self.Quantity_of_Nodes = result[0]
        # print("Quantity_of_Nodes:", self.Quantity_of_Nodes)

        # Nodes
        result = re.findall(r"(?:Key Features)?(.*ot-plug.*)\.? ?[Ee]ach node", txt)
        if self.Nodes == "NA" and result:
            self.Nodes = result[0]
        # print("Nodes:", self.Nodes)

        # Use_Cases
        # How to find Use Cases

        # CITRIX_COMPATIBLE
        # How to find CITRIX_COMPATIBLE

        # VM_WARE_COMPATIBLE
        # How to find VM_WARE_COMPATIBLE

        # VIRTUALISATION_SERVER
        # How to find VIRTUALISATION_SERVER

        # HyperV
        # How to find HyperV

        # How to find Vertical_Markets, WINDOWS_OS, RHEL/Ubuntu/SUSE, VMWare, Citrix, GPU

        # counter_txt_list = counter_txt_list + 1

    def run_regexes_supermicro_chassic(self, data,product_type, description, partner):

        self.initialise_vars()
        self.level = "NA"
        self.partner = partner
        self.desc = description

        if product_type == "chassic":
            '''
            Number of fans & Fan Dimensions
            '''
            Number_of_fans_list = [data['Systems Cooling'].str.extract(r'Fans\s(\d+)\sx{1}')[0][0]]
            fans_dimensions_list = [data['Systems Cooling'].str.extract(r'(\d\sx\s(\d+[cm|mm]+)).* {1}')[0][0]]
            if (len(Number_of_fans_list) > 1):
                Number_of_fans = sum(int(Number_of_fans_list))
                fans_dimensions = str(', '.join(i for i in fans_dimensions_list))
            else:
                Number_of_fans = int(''.join(str(i) for i in Number_of_fans_list))
                fans_dimensions = str(', '.join(i for i in fans_dimensions_list))

            '''
            Support 2.5-inch and Number of 2.5-inch supported
            '''
            Support2_5_inch = data['Backplane'].apply(lambda x: 'Y' if '2.5-inch' in x else 'N')[0][0]

            if Support2_5_inch == 'Y':
                Number_of_2_5_inch_supported = int(data['Backplane'].str.extract(r'.*\s2.5-inch\s.*\s(\d)x\sNVMe.*')[0][0])
            else:
                Number_of_2_5_inch_supported = 0

            self.Chassis = data['Product SKUs'].str.extract(r'([A-Za-z0-9-]+)\s')[0][0]
            self.Form_factor = data['Form Factor'].str.extract(r'([0-9]+U)\s')[0][0]
            self.LED_indicators = data['LEDs'].apply(lambda x: 'Y' if x else 'N')[0][0]
            self.On_off_switch = data['Buttons'].apply(lambda x: 'Y' if x else 'N')[0][0]
            self.Number_of_fans = Number_of_fans
            self.Fan_Size = fans_dimensions
            self.Product_Colour = data['Available Color'][0]
            self.RoHS_Compliance = data['Backplane'].apply(lambda x: 'Y' if 'rohs' in x.lower() else 'N')[0][0]
            self.Hot_swap_HDD_bays = data['Drive Bays'].apply(lambda x: 'Y' if 'hot-swap drive bay' in x.lower() else 'N')[0][0]
            self.Number_of_storage_drives_supported = data['Drive Bays'].str.extract('([0-9]+)\sx\s([0-9."]+) {1}')[0][0]
            self.Storage_drives_sizes_supported = data['Drive Bays'].str.extract('[0-9]+\sx\s([0-9."]+) {1}')[0][0]
            self.Backplane_SKU = "NA"
            self.Backplanes_support = data['Backplane'].str.extract(r'(SAS[0-9]?\/SATA[0-9]?\/NVMe[0-9]?|SAS[0-9]?\/SATA[0-9]?|SAS[0-9]?|SATA[0-9]?|NVMe)')[0][0]
            self.Optional_rear_drive_bays = data['Form Factor'].apply(lambda x: 'Y' if 'rear' in x.lower() else 'N')[0][0]
            self.Supporting_2_5_inch_NVMe = Support2_5_inch
            self.Number_of_NVMe_Supported_by_Backplane = Number_of_2_5_inch_supported
            self.Number_of_redundant_power_supplies_installed = "NA"
            self.Power_Supply_SKU = "NA"
            self.Power_Distributer_SKU = "NA"
            self.Power_supply = "NA"
            self.Height_mm = data['Height'].str.extract(r'([0-9]+)\smm{1}')[0][0]
            self.Width_mm = data['Width'].str.extract(r'([0-9]+)\smm{1}')[0][0]
            self.Depth_mm = data['Depth'].str.extract(r'([0-9]+)\smm{1}')[0][0]
            self.Chassis_Gross_weight_Kg = data['Gross Weight'].str.extract(r'\((\d.+)\skg\){1}')[0][0]
            self.Chassis_Net_Weight = data['Gross Weight'].str.extract(r'(\d+)\slbs{1}')[0][0]
            self.Operating_temperature = data['Operating Temperature Range'][0]
            self.Storage_temperature = data['Non-Operating Temperature Range'][0]
            self.Operating_Relative_humidity = data['Operating Relative Humidity Range'][0]
            self.Storage_relative_humidity = data['Non-Operating Relative Humidity Range'][0]
            self.PC_health_monitoring = 'Y'

        elif product_type == "motherboard":

            print(data['Memory Capacity'].str.extract(r'(\d+\s?TB)|(\d+\s?GB)|(\d.+\s?TB)')[0][0])

            self.Motherboard = data['Product SKUs'].str.extract(r'([A-Za-z0-9-]+)\s')[0][0]
            self.Form_factor = data['Form Factor'][0]
            self.PCl_Express_slots_version = "NA"
            self.PCl_Express_x16_slots = "NA"
            self.On_Board_Graphics_adapter_model = data['Graphics'][0]
            self.ECC = data['Memory Type'].apply(lambda x: 'Y' if 'ecc' in x.lower() else 'N')[0][0]
            self.Maximum_internal_memory = data['Memory Capacity'].str.extract(r'(\d+\s?TB)|(\d+\s?GB)|(\d.+\s?TB)')[0][0]
            self.Number_of_DIMM_slots = data['Memory Capacity'].str.extract(r'(\d+)\sDIMM')[0][0]
            self.Supported_memory_types = data['Memory Type'][0]
            self.Intel_Optane = data['Memory Capacity'].str.extract(r'(\d+TB)\sIntel® Optane™.*(\(.*\))')[0][0]
            self.Maximum_supported_RAM_clock_speed_MHz = data['Memory Type'].str.extract(r'(\d+){1}')[0][0]
            self.M_2 = "NA"
            self.Number_of_M_2_Supported = "NA"
            self.IPMl_LAN_port = data['Management'].apply(lambda x: 'Y' if 'ipmi' in x.lower() else 'N')[0][0]
            self.USB_3_0_Type_A_ports_quantity = data['USB'].str.extract(r'([0-9]+)\sUSB\s3\.[0-9]+')[0][0]
            self.Built_in_processor = "N"
            self.Motherboard_chipset = data['Chipset'][0]
            self.Lan_Ports = data['LAN'].str.extract(r'(\d+){1}')[0][0]
            self.Onboard_Connection = data['LAN'].str.extract(r'\d+\s(.*)')[0][0]
            self.GbE = data['Network Controllers'].str.extract(r'(\d+)GbE')[0][0]
            self.Onboard_Network_Controllers = data['Network Controllers'][0]
            self.Onboard_SAS_Raid_Controller = "NA"
            self.Supported_storage_drive_interfaces = data['SATA'].str.extract(r'(SATA.*)\(')[0][0]
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


        # chassic_columns_list = ['Product SKUs', 'Form Factor', 'Processor Support', 'Height', 'Width',
        #                         'Depth', 'Net Weight', 'Gross Weight', 'Packaging (W x H x L)',
        #                         'Available Color', 'Expansion Slots', 'Drive Bays', 'Backplane',
        #                         'Peripheral Drives', 'Buttons', 'LEDs', 'Ports', 'Systems Cooling',
        #                         'Operating Temperature Range', 'Non-Operating Temperature Range',
        #                         'Operating Relative Humidity Range',
        #                         'Non-Operating Relative Humidity Range', 'Power Supply']

        # motherboard_columns_list = ['Product SKUs', 'Form Factor', 'Dimensions', 'CPU', 'Cores / Cache',
        #                             'Note', 'Memory Capacity', 'Memory Type', 'DIMM Sizes',
        #                             'Memory Voltage', 'Error Detection', 'Chipset', 'SATA', 'IPMI',
        #                             'Network Controllers', 'Graphics', 'LAN', 'USB', 'Video Output',
        #                             'Serial Port / Header', 'TPM', '', 'System BIOS', 'Management',
        #                             'Voltage', 'FAN', 'Temperature', 'LED', 'Other Features',
        #                             'Operating Temperature Range', 'Non-Operating Temperature Range',
        #                             'Operating Relative Humidity Range',
        #                             'Non-Operating Relative Humidity Range']
        #
        # for column in data.columns:
        #     if column in chassic_columns_list:
        #         print('chassic', True)
        #     elif column in motherboard_columns_list:
        #         print('Motherboard', False)


        # self.level = "NA"
        # self.partner = partner
        # self.desc = description
        # self.product_id = "NA"
        # self.name = "NA"
        # self.Chassis = data['Product SKUs'].str.extract(r'([A-Za-z0-9-]+)\s')[0][0]
        # self.Motherboard = "NA"
        # self.Form_factor = data['Form Factor'].str.extract(r'([0-9]+U)\s')[0][0]
        # self.LED_indicators = data['LEDs'].apply(lambda x: 'Y' if x else 'N')[0][0]
        # self.On_off_switch = data['Buttons'].apply(lambda x: 'Y' if x else 'N')[0][0]
        # self.Number_of_fans = Number_of_fans
        # self.Fan_Size = fans_dimensions
        # self.Product_Colour = data['Available Color'][0]
        # self.RoHS_Compliance = data['Backplane'].apply(lambda x: 'Y' if 'rohs' in x.lower() else 'N')[0][0]
        # self.Hot_swap_HDD_bays = data['Drive Bays'].apply(lambda x: 'Y' if 'hot-swap drive bay' in x.lower() else 'N')[0][0]
        # self.Number_of_storage_drives_supported = data['Drive Bays'].str.extract('([0-9]+)\sx\s([0-9."]+) {1}')[0][0]
        # self.Storage_drives_sizes_supported = data['Drive Bays'].str.extract('[0-9]+\sx\s([0-9."]+) {1}')[0][0]
        # self.Backplane_SKU = "NA"
        # self.Backplanes_support = data['Backplane'].str.extract(r'(SAS[0-9]?\/SATA[0-9]?\/NVMe[0-9]?|SAS[0-9]?\/SATA[0-9]?|SAS[0-9]?|SATA[0-9]?|NVMe)')[0][0]
        # self.Optional_rear_drive_bays = data['Form Factor'].apply(lambda x: 'Y' if 'rear' in x.lower() else 'N')[0][0]
        # self.Supporting_2_5_inch_NVMe = Support2_5_inch
        # self.Number_of_NVMe_Supported_by_Backplane = Number_of_2_5_inch_supported
        # self.Number_of_redundant_power_supplies_installed = "NA"
        # self.Power_Supply_SKU = "NA"
        # self.Power_Distributer_SKU = "NA"
        # self.Power_supply = "NA"
        # self.Height_mm = data['Height'].str.extract(r'([0-9]+)\smm{1}')[0][0]
        # self.Width_mm = data['Width'].str.extract(r'([0-9]+)\smm{1}')[0][0]
        # self.Depth_mm = data['Depth'].str.extract(r'([0-9]+)\smm{1}')[0][0]
        # self.Chassis_Gross_weight_Kg = data['Gross Weight'].str.extract(r'\((\d.+)\skg\){1}')[0][0]
        # self.Chassis_Net_Weight = data['Gross Weight'].str.extract(r'(\d+)\slbs{1}')[0][0]

        # self.PCl_Express_slots_version = "NA"
        # self.PCl_Express_x16_slots = "NA"
        # self.On_Board_Graphics_adapter_model = "NA"
        # self.ECC = "NA"
        # self.Maximum_internal_memory = "NA"
        # self.Number_of_DIMM_slots = "NA"
        # self.Supported_memory_types = "NA"
        # self.Intel_Optane = "NA"
        # self.Maximum_supported_RAM_clock_speed_MHz = "NA"
        # self.M_2 = "NA"
        # self.Number_of_M_2_Supported = "NA"

        # self.Operating_temperature = data['Operating Temperature Range'][0]
        # self.Storage_temperature = data['Non-Operating Temperature Range'][0]
        # self.Operating_Relative_humidity = data['Operating Relative Humidity Range'][0]
        # self.Storage_relative_humidity = data['Non-Operating Relative Humidity Range'][0]
        # self.PC_health_monitoring = 'Y'

        # self.IPMl_LAN_port = "NA"
        # self.USB_3_0_Type_A_ports_quantity = "NA"
        # self.Built_in_processor = "NA"
        # self.Motherboard_chipset = "NA"
        # self.Lan_Ports = "NA"
        # self.Onboard_Connection = "NA"
        # self.GbE = "NA"
        # self.Onboard_Network_Controllers = "NA"
        # self.Onboard_SAS_Raid_Controller = "NA"
        # self.Supported_storage_drive_interfaces = "NA"
        # self.Number_of_processors_supported = "NA"
        # self.Processor_socket = "NA"
        # self.Quantity_of_Nodes = "NA"
        # self.Nodes = "NA"
        # self.Use_Cases = "NA"
        # self.CITRIX_COMPATIBLE = "NA"
        # self.VM_WARE_COMPATIBLE = "NA"
        # self.VIRTUALISATION_SERVER = "NA"
        # self.HyperV = "NA"
        # self.Vertical_Markets = "NA"
        # self.WINDOWS_OS = "NA"
        # self.RHEL_Ubuntu_SUSE = "NA"
        # self.VMWare = "NA"
        # self.Citrix = "NA"
        # self.GPU = "NA"

        return True


    def run_regexes_intel(self, intel_df_list):

        self.initialise_vars()

        counter_df_list = 0
        for each_df in intel_df_list:
            # read the df data

            counter_df_list = counter_df_list + 1
