import os
import csv

def read_txt_file(path,file_object):
    """ reads file data """
    file = open(path + file_object, "r")
    print(file.read())


def read_all_items():
    """ grabs files from folders and extracts/converts to csv """
    folder_path = input("Enter full folder path of txt files")
    dir_file = folder_path
    file_list = os.listdir(dir_file)
    master_list = []
    for item in file_list:
       e_data =  extract_data(dir_file,item)
       master_list.append(e_data)
    csv_file = open("receipt.csv", "w+")
    fieldnames = ["Transaction_number", "Date", "Total"]
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    for item in master_list:
        writer.writerow({'Transaction_number':item["Transaction_number"],'Date':item["Date"],'Total':item["Total"] })
    print("Done")
    return 


def extract_data(path,file_object):
    """ extracts data from file """   
    file = open(path + file_object, "r")
    data = {}
    for line in file:
        new_line = line.split(" ")
        #print(new_line[0],new_line[2])
        data.update({new_line[0]:new_line[2]})
    print(data["Total"])
    return(data)




if __name__=='__main__':
    read_all_items()
