while True: #infinite loop until correct value
    password = input("Password: ").strip().lower()  #input cleaned and case sensitive
    if password ==  "cs50rocks": 
        print("Access Granted")
        break  #exit the loop if correct password is entered
    

