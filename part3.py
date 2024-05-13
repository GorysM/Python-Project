"""
SOURCES
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
https://www.w3schools.com/python/python_file_write.asp
https://www.geeksforgeeks.org/python-program-convert-string-list/
https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/
"""

answers = {'1':[], '2':[], '3':[], '4':[]}

while True:
    while True:
        try:
            pass_cred = int(input('Give pass:\n')) # Input() return str so we transform out value to int
            defer_cred = int(input('Give defer:\n'))
            fail_cred = int(input('Give fail:\n'))
        except ValueError:
            print('Integer required\n')
            continue
        else:
            break
        

    if pass_cred not in range(0,140,20) and defer_cred not in range(0,140,20) and fail_cred  not in range(0,140,20):
        print('Out of range\n')
        continue
    if pass_cred + defer_cred + fail_cred != 120:
            print('Total incorrect\n')
            continue
        
        
    if pass_cred == 120:
        print('Progress\n')
        
        #progress.append('*')
        answers['1'].append('Progress - '  + str(pass_cred) + ' ' + str(defer_cred) + ' ' + str(fail_cred))
        
        print('Would you like to enter another set of data?\n')
        user_inp = input("Enter 'y' for yes or 'q' to quit and view results: ")
        
        while(user_inp != 'q' and user_inp != 'y'):
            print('Try again\n')
            user_inp = input("Enter 'y' for yes or 'q' to quit and view results: ")
        
        if user_inp == 'q':
            break 
        elif user_inp == 'y':
            continue
        
    elif pass_cred == 100:
        print('Progress (module trailer)')
        
        #trailer.append('*')
        answers['2'].append('Progress (module trailer) - '  + str(pass_cred) + ' ' + str(defer_cred) + ' ' + str(fail_cred))
        
        print('Would you like to enter another set of data?\n')
        user_inp = input("Enter 'y' for yes or 'q' to quit and view results: ")
        
        while(user_inp != 'q' and user_inp != 'y'):
            print('Try again\n')
            user_inp = input("Enter 'y' for yes or 'q' to quit and view results: ")
        
        if user_inp == 'q':
            break 
        elif user_inp == 'y':
            continue
        
    elif ((pass_cred in range(40, 100, 20) and defer_cred in range(0, 100, 20)) or  
         (pass_cred == 20 and defer_cred in range(40, 120, 20)) or 
         (pass_cred == 0 and defer_cred in range(60, 140, 20))):
            print('Do not progress – module retriever')
            
            #retriever.append('*')
            answers['3'].append('Module Retriever - '  + str(pass_cred) + ' ' + str(defer_cred) + ' ' + str(fail_cred))
            
            print('Would you like to enter another set of data?\n')
            user_inp = input("Enter 'y' for yes or 'q' to quit and view results: ")
            
            while(user_inp != 'q' and user_inp != 'y'):
                print('Try again\n')
                user_inp = input("Enter 'y' for yes or 'q' to quit and view results: ")
            
            if user_inp == 'q':
                break 
            elif user_inp == 'y':
                continue
    else:
        print('Exclude')
        
        #excluded.append('*')
        answers['4'].append('Exclude - '  + str(pass_cred) + ' ' + str(defer_cred) + ' ' + str(fail_cred))
        
        print('Would you like to enter another set of data?\n')
        user_inp = input("Enter 'y' for yes or 'q' to quit and view results: ")
        
        while(user_inp != 'q' and user_inp != 'y'):
            print('Try again\n')
            user_inp = input("Enter 'y' for yes or 'q' to quit and view results: ")
        
        if user_inp == 'q':
            break 
        elif user_inp == 'y':
            continue
        
        
        
        
        


print('-------------------------------------------')
for key in answers:
    if answers[key]:
        for ans in answers[key]:
            print(ans)
    

print('-------------------------------------------')












