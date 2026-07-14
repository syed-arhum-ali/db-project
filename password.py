def email_checker():
    while True:
    
        user = input("enter your email: ")
        email_splitter = user.split("@")
    
        if len(email_splitter) < 2 or not email_splitter[0] or not email_splitter[1]:
            print("Please enter a complete email address.")
            continue

        if email_splitter[1] != "gmail.com":
            print("put the write email address extension is not riemail_splittert")  
            continue
        return user

def pass_checker():
    while True:
        pswd = input("enter your password: ")
        symbols = "!@#$%^&*()~?/\|"
        have_symbols = False
        if len(pswd) <= 7:
            print("passsword is too short")
            continue
        for char in pswd:
            if char  in symbols:
                have_symbols = True
                break
        if not have_symbols:
            print("password is too simple add symbols please")
            continue
        return pswd


