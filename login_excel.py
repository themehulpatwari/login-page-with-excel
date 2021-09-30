import pandas as pd
workbook = pd.read_excel('login_python.xlsx') # Reading the excel sheet
n = len(workbook)
username = []
password = []

for i in range(n): # Appends the login info in 2 different list
    username.append(workbook['USERNAME'].loc[i])
    password.append(workbook['PASSWORD'].loc[i])

username_input = input('What is your username: ')

if username_input in username: # Checks whether the username is present in list or not
    username_password = input('What is your password: ')
    index = username.index(username_input)
    if username_password == password[index]: # Correct username and correct password will have same index in both the list
        print('You have logined successfully')
    else:
        print('Wrong Password')
else:
    print('wrong username')
    print('\nDo you want to create a new user id ') # This block imports the code for registering new username and password
    new = input('Reply with either yes or no: ')
    if new == 'yes':
        print()
        import login_info
    else:
        pass

