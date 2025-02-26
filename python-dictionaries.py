
# created first dictionary
dict1= {}
letter = input ("enter letter: ")
merge ={}

while letter != "stop":
    # letter = input ("enter letter: ")
    number = int(input("enter corresponding no.: "))
    # print (letter,number)
    # dict1= {letter:number}
    # print(dict1)
    dict1[f"{letter}"]=number
    # print(dict1)
    merge [f"{letter}"]= number

    letter = input ("enter letter: ")
print(dict1)
print(merge)


# created second dictionary
dict2={}
letter = input ("enter letter: ")

while letter != "stop":
    # letter = input ("enter letter: ")
    number = int(input("enter corresponding no.: "))
    # print (letter,number)
    # dict1= {letter:number}
    # print(dict1)
    dict2[f"{letter}"]=number
    # print(dict2)
    merge [f"{letter}"]= number

    letter = input ("enter letter: ")
print(dict2)

print(merge)

    
