from csv_operations import create_brands_dictionary

#create variables
file_path_cabinet="C:\\Users\\Claudia\\Documents\\SHSG code\\Cabinet.csv"
file_path_mock_cabinet='/Users/melinaehrat/Documents/International Affairs AT 21/SHSG Summer School/SHSG-Summer-School/Backend/Cabinet_Copy.csv'

class MedicalBox: #creates a medicine box and defines its property
    def __init__(self, gtin_number, purchase_date, expiry_date,instructions):
        self.gtin_number=gtin_number
        self._set_name()
        self._set_package_size()
        self._set_storage_info()
        self.purchase_date=purchase_date
        self.expiry_date=expiry_date
        self.instructions=instructions

    def _set_name(self):
        self.name=create_brands_dictionary()[str(self.gtin_number)][0]
        return self.name

    def _set_package_size(self):
        self.package_size=create_brands_dictionary()[str(self.gtin_number)][1]
        return self.package_size

    def _set_storage_info(self):
        self.storage_info=create_brands_dictionary()[str(self.gtin_number)][2]
        return self.storage_info

    def write_string(self):
        return str(self.gtin_number) + ";" + str(self.name) + ";" + str(self.package_size)  + ";" + str(self.storage_info) + ";" + str(self.purchase_date) + ";" + str(self.expiry_date) + ";" + str(self.instructions) + "\n"

def add_medical_box(gtin_number_input, purchase_date_input, expiry_date_input,instructions_input):
    representation = MedicalBox(gtin_number_input, purchase_date_input, expiry_date_input, instructions_input).write_string()
    open(file_path_cabinet,'a').write(representation)
    return representation