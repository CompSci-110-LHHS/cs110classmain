# # Triangle - Solid
# sideA = 8
# sideB = 8

# for i in range(0, sideA):
#     for j in range(0, sideB):
#         print("* ", end="")        
#     sideB -= 1
#     print()


#Rectangle - Hollow
sideA = 8
sideB = 8

for i in range(0, sideA):
    if i == 0 or i == sideA-1:
        for j in range(0, sideB):
            print("* ", end="")
    else:
        print("* ", end="")
        for j in range(1, sideB-1):
            print("  ", end="")
        print("* ", end="")
    print()

#Triangle - Hollow
sideA = 8
sideB = 8

for i in range(0, sideA):
    if i == 0 or i == sideA-1:
        for j in range(0, sideB):
            print("* ", end="")
    else:
        print("* ", end="")
        for j in range(1, sideB-1):
            print("  ", end="")
        print("* ", end="")
    sideB -= 1
    print()