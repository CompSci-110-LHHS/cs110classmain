################ Python csv modul - working with large collection of data #################

#Python has a module called 'csv' for working with comma seperated value (.csv) files
#which are commonly used to store date
#The first line of a csv are normally column names, the following lines are the data entries
#look at the LHHS staff directory csv as an example (install the csv rainbow extension to help with readability - optional)

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 

# import csv #import the csv module

# #uses a context manager to open our csv file
# with open("LHHS_Staff_Directory_2023-11-01.csv", "r") as csv_file: 
#     read_csv = csv.reader(csv_file)   

#     next(read_csv) #uncomment to skip the header row
#     num_staff = 0   

#     for line in read_csv:
#         num_staff += 1
#         print(line) 
#         #returns a series of lists corresponding to each line in the csv file
#         #note the first list printed is the header row that has the column names

#         #print(line[1]) #Running this line will print only the last name
    
#     print("\n**********************************************************")
#     print(f"There are currently {num_staff} staff listed at Leo Hayes\n")

################ EXAMPLE 1 - End ##################


################ EXAMPLE 2 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 

# import csv #import the csv module

# #uses a context manager to open our csv file
# with open("LHHS_Staff_Directory_2023-11-01.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)  
#     with open("LHHS_Staff_Directory_backup.csv", "w") as new_csv:
#         csv_writer = csv.writer(new_csv)           
#         for line in csv_reader:            
#             csv_writer.writerow(line)             
    
# print("**********************************************************")
# print("New backup created!")
# print("**********************************************************")

################ EXAMPLE 2 - End ##################

################ EXAMPLE 3 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############

# import csv

# with open("LHHS_Staff_Directory_2023-11-01.csv") as r_csv:
#     csv_reader = csv.DictReader(r_csv)    
#     with open("csv_backup.csv", "w", newline="") as w_csv:
#         fieldnames = ["First Name", "Last Name", "Position", "Email"]
#         csv_writer = csv.DictWriter(w_csv, fieldnames=fieldnames)
#         csv_writer.writeheader()
#         for row in csv_reader:
#             firstname = row["First Name"]
#             lastname = row["Last Name"]
#             position = row["Position"]
#             email = firstname.upper() + "." + lastname.upper() + "@nbed.nb.ca"
#             csv_writer.writerow({"First Name":firstname, "Last Name":lastname, "Position":position, "Email":email})             
    
# print("**********************************************************")
# print("New reformated csv created!")
# print("**********************************************************")

################ EXAMPLE 3 - End ##################