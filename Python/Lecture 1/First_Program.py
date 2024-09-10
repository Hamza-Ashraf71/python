light = input("light color : ") #Example 1 conditional statement
if(light == "red") :
    print("stop")
elif(light == "yellow") :
    print("look")
elif(light == "green") :
    print("go")
else:
    print("light is broken") 

#Example 2 
marks = int(input("marks : "))
if(marks >=90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("c")
elif(marks >= 0 and marks < 40):
    print("fail")
else:
    print("D")
    