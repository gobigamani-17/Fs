# file=open("student.txt","w")
# file.write("hello python")
# file.close()

# file=open("student.txt","r")
# data=file.read()
# print(data)
 
file=open("student name.txt","w")
file.write("priyanka\n""jayarani\n""ezhil\n""rexc\n")
file.close()
file=open("student name.txt","r")
data=file.read()
print(data)
file.close()

# try:
#     a=10
#     b=20
#     print(a+b)
# except Exception as e:
#     print(e)
# finally:
#     print("program Ended")