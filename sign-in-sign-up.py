#___________________________________________________________________________________________________________________________________________________
def attacker():
    import cv2
    from ListOfUsers import user

    pic = cv2.imread('%s%d.jpg' % (user[i] , i))
    cv2.imshow('Picture of attacker' , pic)
    k = cv2.waitKey(300)
    cv2.destroyWindow('Picture of attacker')
    
#___________________________________________________________________________________________________________________________________________________
def SendPic():
    import os
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
    img_data = open('%s%d.jpg' %(user[i] , i) , 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'auto.email.python1@gmail.com'
    msg['To'] = ('%s' % email[i])

    text = MIMEText("Login attemp!!!")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('masiha0.jpg'))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('auto.email.python1@gmail.com', 'prnxkayqigoznywl')
    s.sendmail('auto.email.python1@gmail.com', '%s' %email[i], msg.as_string())
    s.quit()


#___________________________________________________________________________________________________________________________________________________
def takePic():
    import numpy as np
    import time 
    import cv2
    import datetime
    camera_port = 2
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)
    return_value, image = camera.read()
    #Now lets write a text on the pic that tells us what have happened
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (50,300)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2

    
 
    dt= datetime.datetime.now()
    dateANDtime = str('%d-%d-%d   %d:%d:%d' %(dt.year , dt.month , dt.day , dt.hour , dt.minute , dt.second))

    cv2.putText(image,'Login attemp from this person at   %s' % (dateANDtime) , 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
    
    cv2.imwrite("%s%d.jpg" %(user[i] , i) , image)
    del(camera)
#__________________________________________________________________________________________________________________________________________________

def RecoveryPass():
    recovery = int(input('You enter wrong password three times.\nFor getting a password recovery enter "1"\nFor answering security questions enter "2"\n'))
    if recovery == 1:
    #The code from this line to the "End tag" ,is the code fore sending email 


        RecoveryEmail()


    #End tag
        print("we've send a recovery link to",email[i])
        exit()
    if recovery == 2:


        SecurityQuestion()

                        
        exit()


#________________________________________________________________________________________________________________________________________________________
#CALCULATOR

def summ():
    x = int(input('\nEnter two numbers : '))
    y = int(input())
    print('\n%s + %s = %s' %(x,y,x+y))
    sumlog = open('ListOfUsers.py','a')
    sumlog.write("\nLogMath[%s].append('%s + %s = %s')"  % (i,x,y,x+y))
    sumlog.close()

def mult():
    x = int(input('\nEnter two numbers : '))
    y = int(input())
    print('\n%s X %s = %s' %(x,y,x*y))
    multlog = open('ListOfUsers.py','a')
    multlog.write("\nLogMath[%s].append('%s X %s = %s')" % (i,x,y,x*y))
    multlog.close()

def div():
    x = int(input('\nEnter two numbers : '))
    y = int(input())
    print('\n%s / %s = %s' %(x,y,float(x/y)))
    divlog = open('ListOfUsers.py','a')
    divlog.write("\nLogMath[%s].append('%s / %s = %s')" % (i,x,y,float(x/y)))
    divlog.close()

def integral():
    import webbrowser
    webbrowser.open('https://www.integral-calculator.com')
    
def deriative():
    import webbrowser
    webbrowser.open('https://www.derivative-calculator.net')

def matrix():
    import webbrowser
    webbrowser.open('https://matrixcalc.org/en/')

#___________________________________________________________________________________________________________________________________________________________

def AfterLogin():
    print('What do you want to do?\n\n1.Calculate the summation of two numbers\n\n2.Calculate the multiple of two numbers\n\n3.Calculate the division of\
two number\n\n4.Integral CalCulator\n\n5.Deriative Calculator\n\n6.Matrix Calculator\n\n7.See the log of wrong passwords\n\n\
8.See the picture of the person who attempted to login\n\n9.See the log of previous calculations\n\n10.EXIT \n')
    choice = input('Enter the number of your choice : ')
    if choice == '1':
        summ()
    elif choice == '2':
        mult()
    elif choice =='3':
        div()
    elif choice =='4':
        integral()
    elif choice =='5':
        deriative()
    elif choice == '6':
        matrix()
    elif choice == '7':
        from ListOfUsers import Log
        print(Log[i])
    elif choice == '8':
        attacker()
    elif choice == '9':
        from ListOfUsers import LogMath
        print(LogMath[i])
    elif choice == '10':
        exit()
    else:
        print("Please enter a valid number!")

    nextStep = input('\nDo you want to continue?(y/n)\n')
    if nextStep == 'y':
        AfterLogin()
    elif nextStep == 'n':
        print('Good Bye')
        exit()


#________________________________________________________________________________________________________________________________
def SecurityQuestion():
    answer1 = input('Where did your parents meet?')
    answer2 = input('What is your favorite color?')
    if answer1 == secques1[i] and answer2 == secques2[i]:
        print('The password that you forgot is :' , Pass[i],'\n','Welcome ',user[i])
        exit()
    else:
        print('Due to security terms , unfortunately this account is blocked.')
#_________________________________________________________________________________________________________________________________
def SignUp():
    emptyTest = 0
        #emptyTest is an identifire to know from which argument we don't have user and we should add our new user to it
        #The code lines from the 'while' below to the next tag are code lines for adding new user to our ListOfusers
    while user[emptyTest] != 'empty':
        emptyTest = emptyTest + 1

    newuser = open('ListOfUsers.py','a')
        
    nUser = input('\nEnter your Username :')
    newuser.write("\nuser[%s] = '%s';" % (emptyTest , nUser))
        
    nPass = input('\nEnter your Password :')
    newuser.write("Pass[%s] = '%s';" % (emptyTest , nPass))
        
    nEmail = input('\nEnter your email address :')
    newuser.write("email[%s] = '%s';" % (emptyTest , nEmail))
        
    print('\nFor more security ,please answer these 2 security questions.')

    nsecques1 = input('\nWhere did your parents meet ?')
    newuser.write("secques1[%s] = '%s';" % (emptyTest , nsecques1))
        
    nsecques2 = input('\nWhat is your favorite color ?')
    newuser.write("secques2[%s] = '%s';" % (emptyTest , nsecques2))
    #The end of code lines of adding new user 
    print('\nThanks for signing up :)')
    newuser.close()
#_________________________________________________________________________________________________________________________________
def RecoveryEmail():
    import smtplib
    from ListOfUsers import email
    from ListOfUsers import Pass
    content = ('Hi\nThis is a password recovery email\nYour password is : %s' % (Pass[i]))
    mail = smtplib.SMTP('smtp.gmail.com:587')
    mail.ehlo()
    mail.starttls()
    mail.login('auto.email.python1@gmail.com','statdesigner')
    mail.sendmail('auto.email.python1@gmail.com',email[i],content)
    mail.close()
#_________________________________________________________________________________________________________________________________   
###########
###########
###########

from ListOfUsers import user
from ListOfUsers import Pass
from ListOfUsers import email
from ListOfUsers import secques1
from ListOfUsers import secques2


name = input('Enter your username : ')
fchecker = 1
emptyval_checker = 0
for i in range(len(user)):
    if name == user[i]:
        for password in range(3):
            
            password = input('Enter your password :')
            
            if password == Pass[i]:
                print('Welcome',user[i],'\n')
                AfterLogin()
                exit()
            elif password == '':

                if emptyval_checker < 3:
                    print("\nYou can't enter empty value , try again.")
                else:

                    takePic()

                    SendPic()
                    
                    RecoveryPass()

            else:
                log = open('ListOfUsers.py','a')
                log.write("\nLog[%s].append('%s')" %(i,password))
                log.close()
                if fchecker < 3:
                    print('Wrong password , try agin.')
                    fchecker = fchecker + 1
                else:

                    takePic()

                    SendPic()
                    
                    RecoveryPass()
                        
else:
    SignUpQ = input("\nYou don't have an account yet.\nDo you want to sign up?\n\nYes?(Enter 'y')\nNo?(Enter anything but 'y')\n")
    if SignUpQ == 'y':


        SignUp()


        exit()
    else:
        print('\nGood Bye')
        exit()
