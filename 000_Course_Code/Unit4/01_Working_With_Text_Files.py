################ Python Context Manager and Working With Files #################

#Python uses the open() method to open files in read "r", write "w" or append "a" mode

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 

# #Opens a text file and reads its contents
# with open("input.txt", "r") as f:  
#     file_read = f.read()
#     print(file_read)

# print("\n*******Reading Bytes Below********\n")

# with open("input.txt", "r") as f:  
#     #reading a specific number of bytes
#     buffer_size = 10
#     file_read = f.read(buffer_size)
#     while len(file_read) > 0:
#         print(file_read, end="*") #adds a * every 10 bytes read
#         file_read = f.read(buffer_size)

################ EXAMPLE 1 - End ##################
    

################ EXAMPLE 2 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 

# with open("input.txt", "r") as f:  
#     read_first = f.readline()  #Reads only first line
#     print(read_first)

#     line_array = f.readlines() #Converts each line into list element
#     print(line_array)

################ EXAMPLE 2 - End ##################
    
################ EXAMPLE 3 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 

# #Opens a text file and reads its contents line by line in a loop
# with open("input.txt", "r") as f:  
#     for line in f:
#         print(line, end="")

################ EXAMPLE 3 - End ##################
        
################ EXAMPLE 4 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 
 
# #Opens (or creates) a text file and writes (or overwrites) the first line
# with open("writefile.txt", "w") as f:  
#     f.write("Hello World")

################ EXAMPLE 4 - End ##################
    
################ EXAMPLE 5 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 
 
#Copies the contents of input.txt to a new file called output.txt
with open("input.txt", "r") as rf:  
    with open("output.txt", "w") as wf:
        text_list = rf.readlines()
        print(text_list)
        text_list.reverse()
        print(text_list)
        for line in text_list:
            pass
        #DO SOMETHING HERE TO WRITE TO NEW OUTPUT.TXT FILE
       
        
################ EXAMPLE 5 - End ##################


