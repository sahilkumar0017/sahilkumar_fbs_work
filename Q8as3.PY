userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == "admin" and password == "1234":
    num = int(input("Enter any 4-digit number: "))
    user = int(input("Re-enter same number: "))
    
    if user == num:
        print("Success")
    else:
        print("Failed")
else:
    print("Wrong Login")