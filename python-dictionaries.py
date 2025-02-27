
# created first dictionary
dict1= {}
letter = input ("enter dict 1 letter: ")
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

    letter = input ("enter dict 1 letter: ")
print(dict1)
print(merge)


# created second dictionary
dict2={}
letter = input ("enter dict 2 letter: ")

while letter != "stop":
    # letter = input ("enter letter: ")
    number = int(input("enter corresponding no.: "))
    # print (letter,number)
    # dict1= {letter:number}
    # print(dict1)
    dict2[f"{letter}"]=number
    # print(dict2)
    merge [f"{letter}"]= number

    letter = input ("enter dict2 letter: ")
print(dict2)



def merge_dictionaries():
    print(merge)

merge_dictionaries()