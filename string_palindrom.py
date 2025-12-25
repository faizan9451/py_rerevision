# str = "faizan"
# i = 1
# store = ""
# while len(str)-1>=i:
#  store = store[i]
#  i = i + 1

# check if a string contain volwels or nnot

# volwel = 0
# name = "faizan"
# for i in range(len(name)):
#     print(name[i])
#     if name[i] == "a":
#         volwel +=1
#         print("1 found")
#     if name[i] == "e":
#         volwel +=1
#         print("2 found")
#     if name[i] == "i":
#         volwel +=1
#         print("3 found")
#     if name[i] == "o":
#         volwel +=1
#         print("4 found") 
#     if name[i] == "u":
#         volwel +=1
#         print("5 found")
# print("Total vowels count: ", volwel)        



str1 =  "listen"
str2 =  "hilent"

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            print("found")
            continue
        

