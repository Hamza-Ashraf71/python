#---------------------File I/O-------------------

#Create a new file "practice.txt" using python
with open("lec7practice.txt", "w") as f:
    f.write("Hi everyone\nWe are learning File I/O\n")
    f.write("using Java\nI like programming in Java.")
   

#WAF that replace all occurrence of "Java" with "python"
with open("lec7practice2.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "python") 
print(new_data)

with open("lec7practice2.txt", "w") as f:
    f.write(new_data)


#Search if the word "learning" exist in the file or not.

def check_for_word(): #make the function
    word = "learning"
    with open("lec7practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")
        
check_for_word()


# WAF to find in which line of the file does the word "learning"
# occur first print -1 if word not found.

def check_for_line():
    word = "Java"
    data = True
    line_no = 1
    with open("lec7practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    
    return -1
check_for_line()

#From a file containg numbers separated by comma, print the count of even no.
count = 0
with open("lec7practice3.txt", "r") as f:
        data = f.read()

        nums = data.split(",")
        for val in nums:
                if(int(val) % 2 == 0):
                    count += 1
print(count)

 
 