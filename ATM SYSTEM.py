#OM NAMAHSHYA SHIVAYA
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import database
from datetime import datetime
import smtplib as s
import random
class atm:

    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(120 * blank_space + "ATM GUI System")
        self.root.geometry("1045x750+400+0")
        self.root.configure(background ='cyan')
        
        self.balance = 1000
        self.change = ""
        self.name = ""
        self.rowid=int
        self.phone_no = ""
        self.email = ""
        self.otp = random.randint(1000,9999)
        self.amount = int
        self.num = int
        self.name2 = ""
        
        MainFrame = Frame(self.root, bd = 30 , width = 800, height = 800, background = 'purple', relief = GROOVE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd = 7 , width = 720, height = 400, background = 'purple', relief = GROOVE)
        TopFrame1.grid(row = 1, column = 0 ,padx = 10)
        
        TopFrame2 = Frame(MainFrame, bd = 7 , width = 720, height = 400, background = 'purple', relief = RIDGE)
        TopFrame2.grid(row = 0, column = 0 ,padx = 10)
        
        TopFrame2Left = Frame(TopFrame2, bd = 10 , width = 170, height = 250, background = 'darkblue', relief = RIDGE)
        TopFrame2Left.grid(row = 0, column = 0 ,padx = 10)

        TopFrame2Mid = Frame(TopFrame2, bd = 25 , width = 250, height = 250, background = 'cyan', relief = RIDGE)
        TopFrame2Mid.grid(row = 0, column = 1 ,padx = 1)
        
        TopFrame2Right = Frame(TopFrame2, bd = 10 , width = 170, height = 250, background = 'darkblue', relief = RIDGE)
        TopFrame2Right.grid(row = 0, column = 2 ,padx = 10)
#==============================================Functions================================================
        def debit1():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,"ENTER DEBIT CARD\n")
            self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = debit2,
            image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def debit2():
               self.rowid = self.txtReceipt.get("2.0","end-1c")
               rowid=str(self.rowid)
               self.change = str(database.search(rowid))
               self.name = str(database.name(rowid))
               self.balance = database.balance(rowid)
               self.phone_no = str(database.phone_no(rowid))
               self.email = str(database.email(rowid))
               if(self.name!= "None"):
                   enter_pin1()
               else:
                     self.txtReceipt.insert(END,"\nCARD MISMATCHED\n")
                     self.txtReceipt.insert(END,"PRESS ENTER")                   
                     self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = debit1,
                     image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)                                            
#========================================ABOUT PROJECT===================================================
        def system():
            self.txtReceipt.insert(END,"\t\tWELCOME\t\t"+"\n\n")
            self.txtReceipt.insert(END,"\tPresented by Group 7 members\t"+"\n\n")
            self.txtReceipt.insert(END," NAMES"+"\t\t\t\t   UID\n")
            self.txtReceipt.insert(END," AKASH "+"\t\t\t\t20BCS7377\n")
            self.txtReceipt.insert(END," OM ANIL GONADE"+"\t\t\t\t20BCS5975\n")
            self.txtReceipt.insert(END," SAKSHAM VATS"+"\t\t\t\t20BCS7370\n")
            self.txtReceipt.insert(END," SOHAM KR MODI"+"\t\t\t\t20BCS7352\n")
            self.txtReceipt.insert(END," MOHIT SHARMA"+"\t\t\t\t20BCS7350")
            self.txtReceipt.insert(END," MAYANK PRAKASH"+"\t\t\t\t20BCS7367")
            self.txtReceipt.insert(END," AYUSH KUMAR RAI"+"\t\t\t\t20BCS7391")
        def clear():
            self.txtReceipt.delete("end-2c")
#=======================================ENTER PIN=================================================
        def enter_pin1():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,"\t\tWELCOME  " + self.name)
            self.txtReceipt.insert(END,"\n---------------------------------ENTER PIN----------------------------------\n\n")
            self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = enter_pin2,
            image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)

        def enter_pin2():
                pinNo = self.txtReceipt.get("4.0","end-1c")
                if(pinNo == self.change):
                   self.txtReceipt.delete("1.0",END)
                   self.txtReceipt.insert(END,"\nWITHDRAW\t\t"+"\t\t       BALANCE ENQUIRY\n\n\n\n\n")
                   self.txtReceipt.insert(END," DEPOSIT"+"\t\t\t\t        PRINT STATEMENT\n\n\n\n\n")
                   self.txtReceipt.insert(END," TRANSFER "+"\t\t\t\t\t   PIN CHANGE\n\n\n\n\n")
                   self.txtReceipt.insert(END," ABOUT PROJECT"+"\t\t\t         CARDLESS TRANSACTION\n\n\n\n")
                   
                   self.btnlArrow1 = Button(TopFrame2Left, width = 160, height = 40, state = NORMAL,command = withdraw1,
                   image =self.image_arrow_Left).grid(row = 0, column = 0, padx = 2, pady = 2)
                   
                   self.btnlArrow2 = Button(TopFrame2Left, width = 160, height = 40, state = NORMAL,command = deposit1,
                   image =self.image_arrow_Left).grid(row = 1, column = 0, padx = 2, pady = 2)
                   
                   self.btnlArrow3 = Button(TopFrame2Left, width = 160, height = 40, state = NORMAL,command =  transfer1,
                   image =self.image_arrow_Left).grid(row = 2, column = 0, padx = 2, pady = 2)
                   
                   self.btnlArrow4 = Button(TopFrame2Left, width = 160, height = 40, state = NORMAL,command = system,
                   image =self.image_arrow_Left).grid(row = 3, column = 0, padx = 2, pady = 2)
                   
                   self.btnrArrow1 = Button(TopFrame2Right, width = 160, height = 40, state = NORMAL,command = Balance,
                   image =self.image_arrow_Right).grid(row = 0, column = 0, padx = 2, pady = 2)

                   self.btnrArrow2 = Button(TopFrame2Right, width = 160, height = 40, state = NORMAL,command = mini_statement,
                   image =self.image_arrow_Right).grid(row = 1, column = 0, padx = 2, pady = 2)

                   self.btnrArrow3 = Button(TopFrame2Right, width = 160, height = 40, state = NORMAL,command = pin_change1,
                   image =self.image_arrow_Right).grid(row = 2, column = 0, padx = 2, pady = 2)

                   self.btnrArrow4 = Button(TopFrame2Right, width = 160, height = 40, state = NORMAL,command = upi1,
                   image =self.image_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)

                else :
                   self.txtReceipt.delete("1.0",END) 
                   self.txtReceipt.insert(END,"--------------------------------WRONG PIN---------------------------------\nPRESS ENTER ")
                   self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = enter_pin1,
                   image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
#=========================================Withdraw function===================================
        def withdraw1():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,"\n----------------------------ENTER AMOUNT------------------------------\n")
            self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = withdraw2,
            image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)      
        def withdraw2():
                self.amount = int(self.txtReceipt.get("3.0","end-1c"))
                if (self.amount%100==0):
                     self.txtReceipt.delete("1.0",END)
                     if(self.amount<=self.balance):
                           self.balance = self.balance - self.amount
                           balance= str(self.balance)
                           rowid = str(self.rowid)
                           database.update(balance,rowid)
                           c = datetime.now()
                           d = c.strftime("%d/%m/%Y %H:%M:%S")
                           self.txtReceipt.insert(END,"\n----------------------------------------------------------------------------------\n")
                           self.txtReceipt.insert(END,"\t\t\t\t"+ d)
                           self.txtReceipt.insert(END,"\nNAME: "+self.name+"             WITHDRAW = "+str(self.amount) + "\n")
                           self.txtReceipt.insert(END,"\n__________YOUR TRANSACTION IS COMPLETE__________\n")
                           self.txtReceipt.insert(END,"\nAVAILABLE BALANCE = ")
                           self.txtReceipt.insert(END,self.balance)
                           self.txtReceipt.insert(END,"\n---------------------------------------------------------------------------------\n")
                           self.txtReceipt.insert(END,"\n\t\t\t               DO YOU WANT RECEIPT\n\n\t\t\tYES\n\n\n\n\t\t\tNO")
                         
                           self.btnrArrow3 = Button(TopFrame2Right, width = 225, height = 70, state = NORMAL,command = withdraw3,
                           image =self.image_arrow_Right).grid(row = 2, column = 0, padx = 1, pady = 2)

                           self.btnrArrow4 = Button(TopFrame2Right, width = 225, height = 70, state = NORMAL,command = delete,
                           image =self.image_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)
                     else :
                              self.txtReceipt.delete("1.0",END)
                              self.txtReceipt.insert(END,"INSUFFICEIENT BALANCE\n")
                              self.txtReceipt.insert(END,"PRESS ENTER")
                              self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = withdraw1,
                              image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
                else:
                   self.txtReceipt.delete("1.0",END)
                   self.txtReceipt.insert(END,"\nENTER AMOUNT IN MULTIPLE OF 100\n")
                   self.txtReceipt.insert(END,"PRESS ENTER")
                   self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = withdraw1,
                   image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def withdraw3():
               text = self.txtReceipt.get("1.0","end-40c")
               f = open ("abc.txt","a")
               f.write(text)
               f.close()
               num = str("You have withdrawn Rs." + str(self.amount)  + " through ATM SYSTEM OF GROUP 7 "  + "\nAVAILABLE BALANCE = Rs." + str(self.balance))
               email(num)
               add_record()
               self.txtReceipt.delete("1.0",END)
               self.txtReceipt.insert(END,"\n\n\n__________YOUR TRANSACTION IS COMPLETE__________\n")
               self.txtReceipt.insert(END,"\n\n______________THANK YOU FOR USING ATM____________\n")
            
#===========================================Balance==========================================
        def Balance():
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,"AVAILABLE BALANCE: ")
                self.txtReceipt.insert(END,self.balance)
#============================================Deposit==========================================
        def deposit1():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,"\n------------------------------ENTER AMOUNT--------------------------\n")
            self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = deposit2,
            image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def deposit2():
                self.amount = int(self.txtReceipt.get("3.0","end-1c"))
                if (self.amount%100==0):
                     self.txtReceipt.delete("1.0",END)
                     self.balance = self.balance + self.amount
                     balance= str(self.balance)
                     rowid = str(self.rowid)
                     database.update(balance,rowid)
                     c = datetime.now()
                     d = c.strftime("%d/%m/%Y %H:%M:%S")
                     self.txtReceipt.insert(END,"\n----------------------------------------------------------------------------------\n")
                     self.txtReceipt.insert(END,"\t\t\t\t"+ d)
                     self.txtReceipt.insert(END,"\nNAME: "+self.name+"     " + "        DEPOSIT = "+str(self.amount) + "\n") 
                     self.txtReceipt.insert(END,"\n__________YOUR TRANSACTION IS COMPLETE__________\n")
                     self.txtReceipt.insert(END,"\nAVAILABLE BALANCE = ")
                     self.txtReceipt.insert(END,self.balance)
                     self.txtReceipt.insert(END,"\n---------------------------------------------------------------------------------\n")
                     self.txtReceipt.insert(END,"\n\t\t\t               DO YOU WANT RECEIPT\n\n\t\t\tYES\n\n\n\n\t\t\tNO")
                         
                     self.btnrArrow3 = Button(TopFrame2Right, width = 225, height = 70, state = NORMAL,command = deposit3,
                     image =self.image_arrow_Right).grid(row = 2, column = 0, padx = 1, pady = 2)

                     self.btnrArrow4 = Button(TopFrame2Right, width = 225, height = 70, state = NORMAL,command = delete,
                     image =self.image_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)
                else:
                   self.txtReceipt.delete("1.0",END)
                   self.txtReceipt.insert(END,"ENTER AMOUNT IN MULTIPLE OF 100\n")
                   self.txtReceipt.insert(END,"PRESS ENTER")
                   self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = deposit1,
                   image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)

        def deposit3():
                text = self.txtReceipt.get("1.0","end-40c")
                f = open ("abc.txt","a")
                f.write(text)
                f.close()
                num = str("You have deposited  Rs." + str(self.amount)  + " through ATM SYSTEM OF GROUP 7 "  + "\nAVAILABLE BALANCE = Rs." + str(self.balance))
                email(num)
                add_record()
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,"\n\n\n__________YOUR TRANSACTION IS COMPLETE__________\n")
                self.txtReceipt.insert(END,"\n\n______________THANK YOU FOR USING ATM____________\n")
    
#===============================================Delete==========================================
        def delete():
                self.txtReceipt.delete("8.0",END)
#=============================================Print Statement=====================================
        def mini_statement():
                self.txtReceipt.delete("1.0",END)
                id = str(self.rowid)
                a = str(database.showdata(id))
                self.txtReceipt.insert(END,(self.name +"\t\tSTATEMENT"+"\n"+"   Date"+"\t        "+"Time"+"\t                "+"Withdraw/Deposit" + "\t         " + "Balance\n"))
                self.txtReceipt.insert(END,a)
                self.txtReceipt.insert(END,"\n----------------------------------------------------------------------------------\n")
                text = self.txtReceipt.get("1.0",END)
                f = open ("statement.txt","a")
                f.write((self.name +"\t\tSTATEMENT"+"\n"+"   Date"+"\t\t\t"+"Time"+"\t \t  "+"Withdraw/Deposit" + "\t   \t    " + "Balance\n" +a))
                f.write("\n-----------------------------------------------------------------------------------------\n")
                f.close()
#=========================================Pin Change============================================
        def pin_change1():
                 self.txtReceipt.delete("1.0",END)
                 self.txtReceipt.insert(END,"ENTER YOUR PREVIOUS PIN\n")
                 self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = pin_change2,
                 image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def  pin_change2():
                pin_no = str(self.txtReceipt.get("2.0","end-1c"))
                if(pin_no == self.change):
                        self.txtReceipt.delete("1.0",END)
                        self.txtReceipt.insert(END,"ENTER NEW PIN\n")
                        self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = pin_change3,
                        image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def pin_change3():
               self.change = self.txtReceipt.get("2.0","end-1c")
               pin_no = str(self.change)
               rowid = str(self.rowid)
               database.update_pin(pin_no,rowid)
               self.txtReceipt.delete("1.0",END)
               self.txtReceipt.insert(END,"YOUR PIN IS SUCCESSFULLY CHANGE\n")
               self.txtReceipt.insert(END,"\n______________THANK YOU FOR USING ATM____________\n")
#=========================================Banking===============================================
        def add_record():
                now = datetime.now()
                a = now.strftime("%d/%m/%Y")
                b = now.strftime("%H:%M:%S")
                amount = str(self.amount)
                balance = str(self.balance)
                id = str(self.rowid)
                database.mini_statement(a,b,amount,balance,id)
#============================================transfer=============================================
        def transfer1():
              self.txtReceipt.delete("1.0",END)
              self.txtReceipt.insert(END,"Enter ACCOUNT NUMBER in which you want to transfer\n")
              self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = transfer2,
              image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def transfer2():
              self.num = self.txtReceipt.get("2.0","end-1c")
              self.txtReceipt.insert(END,"\n------------------------------ENTER AMOUNT--------------------------\n")
              self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = transfer3,
              image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def transfer3():
              self.amount  = int(self.txtReceipt.get("4.0","end-1c"))
              if (self.amount%100==0):
                     self.txtReceipt.delete("1.0",END)
                     if(self.amount<=self.balance):
                           self.balance = self.balance - self.amount
                           balance= str(self.balance)
                           rowid = str(self.rowid)
                           database.update(balance,rowid)
                           account_no = str(self.num)
                           self.name2 = database.transfer(balance,account_no)
                           c = datetime.now()
                           d = c.strftime("%d/%m/%Y %H:%M:%S")
                           self.txtReceipt.insert(END,"\n----------------------------------------------------------------------------------\n")
                           self.txtReceipt.insert(END,"\t\t\t\t"+ d)
                           self.txtReceipt.insert(END,"\nNAME : "+self.name+"    TRANSFER = "+str(self.amount) + " to " + str(self.name2)+"\n")
                           self.txtReceipt.insert(END,"\n__________YOUR TRANSACTION IS COMPLETE__________\n")
                           self.txtReceipt.insert(END,"\nAVAILABLE BALANCE = ")
                           self.txtReceipt.insert(END,self.balance)
                           self.txtReceipt.insert(END,"\n---------------------------------------------------------------------------------\n")
                           self.txtReceipt.insert(END,"\n\t\t\t               DO YOU WANT RECEIPT\n\n\t\t\tYES\n\n\n\n\t\t\tNO")
                         
                           self.btnrArrow3 = Button(TopFrame2Right, width = 225, height = 70, state = NORMAL,command = transfer4,
                           image =self.image_arrow_Right).grid(row = 2, column = 0, padx = 1, pady = 2)

                           self.btnrArrow4 = Button(TopFrame2Right, width = 225, height = 70, state = NORMAL,command = delete,
                           image =self.image_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)
                     else :
                              self.txtReceipt.delete("1.0",END)
                              self.txtReceipt.insert(END,"INSUFFICEIENT BALANCE\n")
                              self.txtReceipt.insert(END,"PRESS ENTER")
                              self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = transfer2,
                              image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
              else:
                   self.txtReceipt.delete("1.0",END)
                   self.txtReceipt.insert(END,"\nENTER AMOUNT IN MULTIPLE OF 100\n")
                   self.txtReceipt.insert(END,"PRESS ENTER")
                   self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = transfer2,
                   image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def transfer4():
                text = self.txtReceipt.get("1.0","end-40c")
                f = open ("abc.txt","a")
                f.write(text)
                f.close()
                num = str("You have transfer  Rs." + str(self.amount)  + " through ATM SYSTEM OF GROUP 7 "  +" to " + str(self.name2) +  "\nAVAILABLE BALANCE = Rs." + str(self.balance))
                email(num)
                add_record()
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,"\n\n\n__________YOUR TRANSACTION IS COMPLETE__________\n")
                self.txtReceipt.insert(END,"\n\n______________THANK YOU FOR USING ATM____________\n")
            
              
              
#=================================Card less transaction==============================================
        def upi1():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,"Enter phone no.\n")
            self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = upi2,
            image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def upi2():
                Upi_id =self.txtReceipt.get("2.0","end-1c")
                if (Upi_id == self.phone_no):
                    self.txtReceipt.delete("1.0",END)
                    num = str("OTP for ATM transaction is " + str(self.otp))
                    email(num)
                    self.txtReceipt.insert(END,"OTP send successfully on your email \n Enter OTP\n")
                    self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = upi3,
                    image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
                    self.txtReceipt.focus_set()
                else :
                    self.txtReceipt.delete("1.0",END)
                    self.txtReceipt.insert(END,"PHONE NO. DOESN'T MATCH\nPRESS ENTER")
                    upi1()
        def upi3():
            pas = self.txtReceipt.get("3.0","end-1c")        
            if((pas == str(self.otp))) :
                   self.txtReceipt.delete("1.0",END)
                   self.txtReceipt.insert(END,"\n----------------------------ENTER AMOUNT------------------------------\n")
                   self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = upi4,
                   image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
            else :
                   self.txtReceipt.delete("1.0",END) 
                   self.txtReceipt.insert(END,"--------------------------------WRONG OTP---------------------------------\nPRESS ENTER ")
                   self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = upi1,
                   image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def upi4():
                self.amount = int(self.txtReceipt.get("3.0","end-1c"))
                if (self.amount%100==0):
                     self.txtReceipt.delete("1.0",END)
                     if(self.amount<=self.balance):
                           self.balance = self.balance - self.amount
                           balance= str(self.balance)
                           rowid = str(self.rowid)
                           database.update(balance,rowid)
                           c = datetime.now()
                           d = c.strftime("%d/%m/%Y %H:%M:%S")
                           self.txtReceipt.insert(END,"\n----------------------------------------------------------------------------------\n")
                           self.txtReceipt.insert(END,"\t\t\t\t"+ d)
                           self.txtReceipt.insert(END,d+"\nNAME : "+self.name+"          WITHDRAW = "+str(self.amount)+"\n")
                           self.txtReceipt.insert(END,"\n__________YOUR TRANSACTION IS COMPLETE__________\n")
                           self.txtReceipt.insert(END,"\nAVAILABLE BALANCE = ")
                           self.txtReceipt.insert(END,self.balance)
                           self.txtReceipt.insert(END,"\n---------------------------------------------------------------------------------\n")
                           self.txtReceipt.insert(END,"\n\t\t\t               DO YOU WANT RECEIPT\n\n\t\t\tYES\n\n\n\n\t\t\tNO")
                         
                           self.btnrArrow3 = Button(TopFrame2Right, width = 225, height = 70, state = NORMAL,command = upi5,
                           image =self.image_arrow_Right).grid(row = 2, column = 0, padx = 1, pady = 2)

                           self.btnrArrow4 = Button(TopFrame2Right, width = 225, height = 70, state = NORMAL,command = delete,
                           image =self.image_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)
                     else :
                              self.txtReceipt.insert(END,"INSUFFICEIENT BALANCE\n")
                              self.txtReceipt.insert(END,"PRESS ENTER")
                              self.btn12 = Button(TopFrame1, width = 160, height = 50, state = NORMAL,command = insertCE,
                              image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)
        def upi5():
                text = self.txtReceipt.get("1.0","end-40c")
                f = open ("abc.txt","a")
                f.write(text)
                f.close()
                num = str("You have withdrawn Rs." + str(self.amount)  + " through ATM SYSTEM OF GROUP 7 "  + "\nAVAILABLE BALANCE = Rs." + str(self.balance))
                email(num)
                add_record()
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,"\n\n\n__________YOUR TRANSACTION IS COMPLETE__________\n")
                self.txtReceipt.insert(END,"\n\n______________THANK YOU FOR USING ATM____________\n")
#============================================EMAIL FUNCTION=====================================
        def email(num):
             ob = s.SMTP("smtp.gmail.com",587)
             ob.starttls()
             ob.login("atmguisystem@gmail.com","ATM@system1")
             subject = "ATM SYSTEM"
             body = num
             mail = self.email
             message="Subject:{}\n\n{}".format(subject,body)
             ob.sendmail("atmguisystem@gmail.com",mail,message)
             ob.quit()

#============================================Button fuction==========================================                   
        def insert0():
                value0 = 0
                self.txtReceipt.insert(END,value0)
        def insert1():
                value1 = 1
                self.txtReceipt.insert(END,value1)
        def insert2():
                value2 = 2
                self.txtReceipt.insert(END,value2)
        def insert3():
                value3 = 3
                self.txtReceipt.insert(END,value3)
        def insert4():
                value4 = 4
                self.txtReceipt.insert(END,value4)
        def insert5():
                value5 = 5
                self.txtReceipt.insert(END,value5)
        def insert6():
                value6 = 6
                self.txtReceipt.insert(END,value6)
        def insert7():
                value7 = 7
                self.txtReceipt.insert(END,value7)
        def insert8():
                value8 = 8
                self.txtReceipt.insert(END,value8)
        def insert9():
                value9 = 9
                self.txtReceipt.insert(END,value9)
        def insertCE():
                Cancel = tkinter.messagebox.askyesno("ATM","Confirm if you want to exit")
                if Cancel > 0 :
                    self.root.destroy()
                    return
        
#======================================Widgets================================================================================
        self.txtReceipt = Text(TopFrame2Mid, height = 18, width = 55, bd = 10, font = ('Times New Roman' ,9, 'bold'),background = 'lightblue')
        self.txtReceipt.grid(row = 0, column = 0)

        self.image_arrow_Left = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/lArrow.png")
        self.btnlArrow1 = Button(TopFrame2Left, width = 225, height = 70, state = DISABLED,
        image =self.image_arrow_Left).grid(row = 0, column = 0, padx = 1, pady = 2)

        self.btnlArrow2 = Button(TopFrame2Left, width = 225, height = 70, state = DISABLED,
        image =self.image_arrow_Left).grid(row = 1, column = 0, padx = 1, pady = 2)

        self.btnlArrow3 = Button(TopFrame2Left, width = 225, height = 70, state =DISABLED,
        image =self.image_arrow_Left).grid(row = 2, column = 0, padx = 1, pady = 2)

        self.btnlArrow4 = Button(TopFrame2Left, width = 225, height = 70, state =DISABLED,
        image =self.image_arrow_Left).grid(row = 3, column = 0, padx = 1, pady = 2)
#==============================================================================================================================
        self.image_arrow_Right = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/rArrow.png")
        self.btnrArrow1 = Button(TopFrame2Right, width = 225, height = 70, state = DISABLED,
        image =self.image_arrow_Right).grid(row = 0, column = 0, padx = 1, pady = 2)

        self.btnrArrow2 = Button(TopFrame2Right, width = 225, height = 70, state = DISABLED,
        image =self.image_arrow_Right).grid(row = 1, column = 0, padx = 1, pady = 2)

        self.btnrArrow3 = Button(TopFrame2Right, width = 225, height = 70, state = DISABLED,
        image =self.image_arrow_Right).grid(row = 2, column = 0, padx = 1, pady = 2)

        self.btnrArrow4 = Button(TopFrame2Right, width = 225, height = 70, state = DISABLED,
        image =self.image_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)

#=================================================PIN NUMBER BUTTONS================================================================
        
        self.image1 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/one.png")
        self.btn1 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert1,
        image =self.image1).grid(row = 2, column = 0, padx =2, pady = 2)

        self.image2 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/two.png")
        self.btn2 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert2,
        image =self.image2).grid(row = 2, column = 1, padx = 2, pady = 2)

        self.image3 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/three.png")
        self.btn3 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert3,
        image =self.image3).grid(row = 2, column = 2, padx = 2, pady = 2)

        self.imageCE = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/cancel.png")
        self.btn4 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insertCE,
        image =self.imageCE).grid(row = 2, column = 3, padx = 2, pady = 2)
#===================================================================================================================================
        self.image4 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/four.png")
        self.btn5 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert4,
        image =self.image4).grid(row = 3, column = 0, padx = 2, pady = 2)

        self.image5 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/five.png")
        self.btn6 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert5,
        image =self.image5).grid(row = 3, column = 1, padx = 2, pady = 2)

        self.image6 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/six.png")
        self.btn7 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert6,
        image =self.image6).grid(row = 3, column = 2, padx = 2, pady = 2)

        self.imagecl = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/clear.png")
        self.btn8 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = clear,
        image =self.imagecl).grid(row = 3, column = 3, padx = 2, pady = 2)

#=====================================================PIN number buttons=============================================================
        self.image7 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/seven.png")
        self.btn9 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert7,
        image =self.image7).grid(row = 4, column = 0, padx = 2, pady = 2)

        self.image8 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/eight.png")
        self.btn10 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert8,
        image =self.image8).grid(row = 4, column = 1, padx = 2, pady = 2)

        self.image9 = PhotoImage(file ="C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/nine.png")
        self.btn11 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert9,
        image =self.image9).grid(row = 4, column = 2, padx = 2, pady = 2)

        self.image10 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/enter.png")
        self.btn12 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = debit1,
        image =self.image10).grid(row = 4, column = 3, padx = 2, pady = 2)

#==================================================PIN NUMBER BUTTONS===========================================================
        self.imageSp1 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/empty.png")
        self.btnSp1 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command=email,
        image =self.imageSp1).grid(row = 5, column = 0, padx = 2, pady = 2)

        self.image0 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/zero.png")
        self.btn0 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = insert0,
        image =self.image0).grid(row = 5, column = 1, padx = 2, pady = 2)

        self.imageSp2 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/empty.png")
        self.btnSp2 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,
        image =self.imageSp2).grid(row = 5, column = 2, padx = 2, pady = 2)

        self.imageSp3 = PhotoImage(file = "C:/Users/mayank prakash/OneDrive/Desktop/ATM project/ATM_Icon/empty.png")
        self.btnSp3 = Button(TopFrame1, width = 225, height = 70, state = NORMAL,command = system, 
        image =self.imageSp3).grid(row = 5, column = 3, padx = 2, pady = 2)
        

    

if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()


