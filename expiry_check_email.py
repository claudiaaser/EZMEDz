import time
import datetime
from push import email_push
from csv_operations import create_cabinet_dictionary

file_path_cabinet = "C:\\Users\\Claudia\\Documents\\SHSG code\\Cabinet.csv"

def check_expiry():
    cabinet=create_cabinet_dictionary()
    list_to_be_deleted=[]
    for gtin_number, value_list in cabinet.items():
        recorded_expiration_date=value_list[4]
        expiration_date = datetime.datetime.strptime(recorded_expiration_date, "%Y-%m-%d").date()
        if expiration_date <= datetime.date.today():
            list_to_be_deleted.append(gtin_number)
            email_push("Expired Medication","Hi George, \nYour medication expired! Please dispose of it safely as instructed on the box and purchase a new one if needed.\nMedicinal products do not belong in your household waste. In case of any doubt, please consult your local pharmacist. \nBest regards, \nYour team @EZMEDz","jasminramonabuerkler@gmail.com")
    return list_to_be_deleted

def delete_expired(list_to_be_deleted):
    cabinet=create_cabinet_dictionary()
    for key_to_delete in list_to_be_deleted:
        cabinet.pop(str(key_to_delete ))
    with open(file_path_cabinet,'w') as f: 
        pass
    for remaining_key, remaining_values in cabinet.items():
        representation= str(remaining_key) + ";" + str(remaining_values[0]) + ";" + str(remaining_values[1]) + ";" + str(remaining_values[2]) + ";" + str(remaining_values[3]) + ";" + str(remaining_values[4])+ ";" + str(remaining_values[5]) + "\n"
        open(file_path_cabinet,'a').write(representation) 


if __name__ == "__main__":
    while True:
        list_to_be_deleted =check_expiry()
        delete_expired(list_to_be_deleted)
        print(list_to_be_deleted)
        time.sleep(10)

while True:
   expired_barcodes = check_expiry()
   delete_required(expired_barcodes)
   sleep(10)