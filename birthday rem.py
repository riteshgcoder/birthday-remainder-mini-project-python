dict={}
while True:
    print('@@@@@Birthday ramainder app@@@@@@')
    print('1. Show birthday')
    print('2. Add to birthday list')
    print('3. Exit')
    choice=int(input('Enter the choice'))
    if choice==1:
        if len(dict.keys())==0:
            print('Nothing to show')
        
        else:
            name=input('Enter name look for')
            birthday=dict.get(name,'No data found')
            print(name,date,'birthday')
    elif choice==2:
        name=input('Enter friends name')
        date=input('Enter birthdate')
        dict[name]=date
        print('birthday added')
    elif choice==3:
        break
    else:
        print('Choose a valid option')


OUTPUT:-

@@@@@Birthday ramainder app@@@@@@
1. Show birthday
2. Add to birthday list
3. Exit
Enter the choice2
Enter friends nameojha
Enter birthdate 23 aug
birthday added
@@@@@Birthday ramainder app@@@@@@
1. Show birthday
2. Add to birthday list
3. Exit
Enter the choice2
Enter friends name amit
Enter birthdate 23 jul
birthday added
@@@@@Birthday ramainder app@@@@@@
1. Show birthday
2. Add to birthday list
3. Exit
Enter the choice1
Enter name look for amit
 amit  23 jul birthday
@@@@@Birthday ramainder app@@@@@@
1. Show birthday
2. Add to birthday list
3. Exit
Enter the choice3
 
