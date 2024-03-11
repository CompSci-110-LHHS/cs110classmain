################ Python Context Manager and Working With Img Files #################

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 

#Opens an img file and reads and writes bytes in 254byte chunks
with open("LHHS_IMG.jpg", "rb") as ri:  #the 'b' indicates 'byte mode'
    with open("LHHS_IMG_copy.jpg", "wb") as wi:
        #reading a specific number of bytes
        buffer_size = 254
        img_read = ri.read(buffer_size)
        while len(img_read) > 0:
            wi.write(img_read)
            img_read = ri.read(buffer_size)

################ EXAMPLE 1 - End ##################