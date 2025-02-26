
dict1= {}
letter = ""
while letter != "stop":
    letter = input ("enter letter: ")
    number = int(input("enter corresponding no.: "))
    print (letter,number)
    # dict1= {letter:number}
    # print(dict1)
    dict1[f"{letter}"]=number
    print(dict1)
