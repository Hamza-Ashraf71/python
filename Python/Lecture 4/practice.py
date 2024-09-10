#Store following words meaning in a python dictionary.
myDict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"

}
print(myDict)

#You are given a list of subjects for students.Assume one classroom is required for 1 class.
#How many class rooms are needed by all students.

#make the set
subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}

print(len(subjects))

#Enter marks of 3 subjects from the user and store them in a dictionary.
#start with empty dictionary and add one by one.Use subject name as key and marks as value.

marks = {} 

x = int(input("phy :"))
marks.update({"phy" : x})

x = int(input("chem :"))
marks.update({"chem" : x})

x = int(input("math :"))
marks.update({"math" : x})

print(marks)


#figure out a way to store 9 & 9.0 as a seprate value in set.
#you can use built in data types.

values = {
    ("int", 9),
    ("float", 9.0)
}
print(values)