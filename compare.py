import difflib
 
with open('b3.txt') as file_1:
    file_1_text = file_1.readlines()
 
with open('c7.txt') as file_2:
    file_2_text = file_2.readlines()

f= open("compared.txt","w+")


# Find and print the diff:

 #   f.write(line)
#f.close()
a=0
b=0
file1 = open("b3.txt",'r')
file2 = open("c7.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()

for i in range(len(file1_lines)):
    if file1_lines[i] != file2_lines[i] and "noPlate" not in file1_lines[i]:
            print("Line " + str(i+1) + " doesn't match.")
            print("------------------------")
            print("b3: " + file1_lines[i])
            print("c7: " + file2_lines[i])
            a=a+1
            string = "b3: " +file1_lines[i] + "c7: " +file2_lines[i]
            f.write(string)
            f.write("\n")
    else:
        b=b+1
f.close()
print(a)
print("no plates count ",b)
file1.close()
file2.close()