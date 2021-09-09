import push
import time
import csv_operations
import datetime
from push import email_push
from csv_operations import create_cabinet_dictionary

file_path_cabinet = "C:\\Users\\Claudia\\Documents\\SHSG code\\Cabinet_1.csv"

def check_expiry():
    cabinet=create_cabinet_dictionary()
    list_to_be_deleted=[]
    for gtin_number, value_list in cabinet.items():
        recorded_expiration_date=value_list[4]
        expiration_date = datetime.datetime.strptime(recorded_expiration_date, "%Y-%m-%d").date()
        if expiration_date <= datetime.date.today():
            list_to_be_deleted.append(gtin_number)
            email_push()
    return list_to_be_deleted


            #send_mail()

def delete_expired(list_to_be_deleted):
    cabinet=create_cabinet_dictionary()
    for key_to_delete in list_to_be_deleted:
        cabinet.pop(str(key_to_delete ))
    with open(file_path_cabinet,'w') as f: ##change to real cabinet
        pass
    for remaining_key, remaining_values in cabinet.items():
        representation= str(remaining_key) + ";" + str(remaining_values[0]) + ";" + str(remaining_values[1]) + ";" + str(remaining_values[2]) + ";" + str(remaining_values[3]) + ";" + str(remaining_values[4])+ ";" + str(remaining_values[5]) + "\n"
        open(file_path_cabinet,'a').write(representation) ##change to w command ##change to real cabinet


        

  


if __name__ == "__main__":
    while True:
        list_to_be_deleted =check_expiry()
        delete_expired(list_to_be_deleted)
        #check_expiry()
        #delete_line()
        time.sleep(120)
