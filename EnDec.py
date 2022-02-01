#Idea404 Hackathon
import cryptocode#Importing cryptocodeHAI
print("Welcome to calculator,Press Enter to continue")
code=input()#Take input code from user 
passone="ONE"#Save password for user one
passtwo="TWO"#Save password for user two
if(code=="HAIL SPIES"):#If code matches secret pass than Endec else calculator
    string=input("Enter Operation Mode:")#Whether to Encrypt or Decrypt
    string=string.upper()#Change Input to all upper case
    if(string=="ENCRYPT"):#If input matches ENCRYPT
        print("Message to encrypt")#Enter message to encrypt
        message=input()#Take input message
        print("Enter Key for encryption")#Enter key for encryption
        key=input()#Take input key from user
        encoded=cryptocode.encrypt(message,key)#Encode the message along with key
        user=input("Enter Passcode:")#Enter passcode of user
        user=user.upper()#Convert passcode to upper cases
        if(user==passone):#User is equal to passone
            import smtplib #Simple Mail Tranfser Protocol Library
            from email.mime.multipart import MIMEMultipart #Mime is multipurpose internet mail extension
            from email.mime.text import MIMEText 
            mail_content = encoded+" Key is "+key
            sender_address = 'idea404hackathon@gmail.com'
            sender_pass = 'Password'
            receiver_address = 'naitikjkapadia@gmail.com'
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Encrypted.'  
            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587) 
            session.starttls() 
            session.login(sender_address, sender_pass) 
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
        elif(user==passtwo):
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            mail_content = message+"Key is "+key
            sender_address = 'idea404hackathon@gmail.com'
            sender_pass = 'Password'
            receiver_address = 'naitikjkapadia@gmail.com'
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Encrypted.'   
            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587) 
            session.starttls() 
            session.login(sender_address, sender_pass) 
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
        else:
            import smtplib
            import os
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            mail_content = '''SOMEONE TRIED UNAUTHORIZED ACCESS WE DELETED ALL DATA FROM THAT COMPUTER BUT KEEP IN MIND WE ARE UNDER SUSPICION'''
            sender_address = 'idea404hackathon@gmail.com'
            sender_pass = 'Password'
            receiver_address = 'naitikjkapadia@gmail.com'
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'ALERT'   
            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587) 
            session.starttls() 
            session.login(sender_address, sender_pass) 
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            print("TASK FAILED")
            os.remove(r"C:\Users\naiti\OneDrive\Desktop\a.txt")
            session.quit()
    else:
        print("Message to decrypt")
        message=input()
        print("Enter Key for decryption")
        key=input()
        decoded=cryptocode.decrypt(message,key)
        user=input("Enter password:")
        user=user.upper()
        if(user==passone):
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            mail_content = decoded
            sender_address = 'idea404hackathon@gmail.com'
            sender_pass = 'Password'
            receiver_address = 'naitikjkapadia@gmail.com'
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Decrypted.'   
            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587) 
            session.starttls() 
            session.login(sender_address, sender_pass) 
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
        elif(user==passtwo):
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            mail_content = decoded
            sender_address = 'idea404hackathon@gmail.com'
            sender_pass = 'Password'
            receiver_address = 'naitikjkapadia@gmail.com'
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Decrypted.'   
            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587) 
            session.starttls() 
            session.login(sender_address, sender_pass) 
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
        else:
            import smtplib
            import os
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            mail_content = '''SOMEONE TRIED UNAUTHORIZED ACCESS WE DELETED ALL DATA FROM THAT COMPUTER BUT KEEP IN MIND WE ARE UNDER SUSPICION'''
            sender_address = 'idea404hackathon@gmail.com'
            sender_pass = 'Password'
            receiver_address = 'naitikjkapadia@gmail.com'
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'ALERT'   
            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587) 
            session.starttls() 
            session.login(sender_address, sender_pass) 
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            print("TASK FAILED")
            os.remove(r"C:\Users\naiti\OneDrive\Desktop\a.txt")
            session.quit()
else:
    print("Enter Number 1")
    a=float(input())
    print("Enter Number 2")
    b=float(input())
    print("Enter the operand")
    oper=input()
    if(oper=="+"):
        print(a+b)
    elif(oper=="-"):
        print(a-b)
    elif(oper=="*"):
        print(a*b)
    elif(oper=="/"):
        print(a/b)
    else:
        print(a%b)
    import smtplib
    import os
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    mail_content = '''SOMEONE TRIED UNAUTHORIZED ACCESS WE DELETED ALL DATA FROM THAT COMPUTER BUT KEEP IN MIND WE ARE UNDER SUSPICION'''
    sender_address = 'idea404hackathon@gmail.com'
    sender_pass = 'Password'
    receiver_address = 'veerpkatrodia@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'ALERT'   
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls() 
    session.login(sender_address, sender_pass) 
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    #print("TASK FAILED")
    os.remove(r"C:\Users\naiti\OneDrive\Desktop\a.txt")
    session.quit()