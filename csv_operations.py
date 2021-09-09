file_path_brands="C:\\Users\\Claudia\\Documents\\SHSG code\\Brands.csv"
file_path_cabinet="C:\\Users\\Claudia\\Documents\\SHSG code\\Cabinet.csv"

def create_brands_dictionary():
    brands_dictionary={}
    for line in open(file_path_brands,'r').readlines():
        brand=line.split(";")
        brands_dictionary[brand[0]]=[brand[1],brand[2],brand[3].strip()]
    return brands_dictionary

#print(create_brands_dictionary())

def create_cabinet():
    cabinet_list =[]
    for line in open(file_path_cabinet,'r').readlines():
        individual_box_dictionary={}
        cells = line.split(";")
        individual_box_dictionary["Name"]=cells[1]
        individual_box_dictionary["Expiry Date"]=cells[5]
        individual_box_dictionary["Purchase Date"]=cells[4]
        individual_box_dictionary["Storage"]="The medicine must be stored at a temperature of "+str(cells[3])+" Degrees Celsius."
        individual_box_dictionary["Package size"]=cells[2]
        individual_box_dictionary["Instructions"]=cells[6]
        cabinet_list.append(individual_box_dictionary)
    return cabinet_list

#print(create_cabinet())

def create_cabinet_dictionary():
    cabinet_dictionary={}
    for line in open(file_path_cabinet,'r').readlines():
        brand=line.split(";")
        cabinet_dictionary[brand[0]]=[brand[1],brand[2],brand[3],brand[4],brand[5],brand[6].strip()]
    return cabinet_dictionary

