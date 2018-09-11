# Use loops to print a grid like this
# Grid rules :
# 1st row is 7 dashes (-)
# 2nd row is three pipes (|) in the 1st, 4th and 7th spot
# 3rd row is same as first row

string = ""
string2 = ""
for i in range(7):
    string = string+"-"

x = [0, 3, 6]
for i in range(0, 7):
    if i in x:
        string2 = string2 + "|"
    else:
        string2 = string2 + " "

print(string)
print(string2)
print(string)
# print("type 2")
# for i in range(7):
#   print("-", end="")
