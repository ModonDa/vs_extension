d={}
def dictionary_add(key,value):
    d[key]=value
    print("New Word Added Successfully !")
def dictionary_delete(key):
    d.pop(key)
    print("Word deleted successfully !")
def dictionary_update(key,value):
    d.update({key:value})
    print("Word updated successfully !")
def display():
    print(d)
while True:
    k=input("Press \n1.To Insert New Word\n2.To Delete a Word\n3.To Update a word\n4.To Display\nAnything else to exit\n")
    if k=='1':
        key=input("Enter the word")
        value=input("Enter the meaning")
        dictionary_add(key,value)
    elif k=='2':
        key=input("Enter the word to delete")
        dictionary_delete(key)
    elif k=='3':
        key=input("Enter an existing word")
        if key not in d:
            print("Word Not Found")
        else:
            value=input("Enter new meaning:")
            dictionary_update(key,value)
    elif k=='4':
        for i in d:
            print(i ,':' ,d[i])
    else:
        exit(0)
'''Output:

Press 
1.To Insert New Word
2.To Delete a Word
3.To Update a word
4.To Display
Anything else to exit
1
Enter the wordEndeavour
Enter the meaningTry
New Word Added Successfully !
Press 
1.To Insert New Word
2.To Delete a Word
3.To Update a word
4.To Display
Anything else to exit
1
Enter the wordDefend
Enter the meaningProtect
New Word Added Successfully !
Press 
1.To Insert New Word
2.To Delete a Word
3.To Update a word
4.To Display
Anything else to exit
1
Enter the wordSuspect
Enter the meaningMisdoubt
New Word Added Successfully !
Press 
1.To Insert New Word
2.To Delete a Word
3.To Update a word
4.To Display
Anything else to exit
1
Enter the wordOrifice
Enter the meaningHole
New Word Added Successfully !
Press 
1.To Insert New Word
2.To Delete a Word
3.To Update a word
4.To Display
Anything else to exit
4
Endeavour : Try
Defend : Protect
Suspect : Misdoubt
Orifice : Hole
Press 
1.To Insert New Word
2.To Delete a Word
3.To Update a word
4.To Display
Anything else to exit
3
Enter an existing wordOrifice
Enter new meaning:cleft
Word updated successfully !
Press 
1.To Insert New Word
2.To Delete a Word
3.To Update a word
4.To Display
Anything else to exit
4
Endeavour : Try
Defend : Protect
Suspect : Misdoubt
Orifice : cleft
Press 
1.To Insert New Word
2.To Delete a Word
3.To Update a word
4.To Display
Anything else to exit
'''
