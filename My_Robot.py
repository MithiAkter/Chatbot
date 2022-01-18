from cgitb import grey, text
from email.mime import image
from json.tool import main
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import width
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("Mithi's Chatting Robot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)
        
        
        #ui
        main_frame=Frame(self.root,bd=4,bg='#D4CBC2',width=610)
        main_frame.pack()
        
        #upper image
        img_chat=Image.open('robot1.jpg')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)
        
        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="    Let's Talk!",font=('times new roman',35,'bold'),fg='black',bg='white')
        Title_label.pack(side=TOP)
        
        #text Area
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=70,height=20,bd=3,relief=RAISED,font=('times new roman',14),fg='white',bg='#3C0C2C',yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        #Button
        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()
        
        #for typehere button
        label_1=Label(btn_frame,text="Type Here => ",font=('times new roman',14,'bold'),fg='black',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)
        
        #entrybox
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        # Send button
        self.send=Button(btn_frame,text="Send",command=self.send,font=('times new roman',15,'bold'),width=8,bg='white',fg='black')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        # Clear button
        self.clear=Button(btn_frame,text="Clear",command=self.clear,font=('times new roman',12,'bold'),width=8,bg='white',fg='black')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        #for empty input
        self.msg=''
        self.label_2=Label(btn_frame,text=self.msg,font=('times new roman',14,'bold'),fg='red',bg='white')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)
        
        
    #============================Functions=========================================================
    
    #for enter button
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
     
     #for clear button   
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
    
        
    #chattings
    def send(self):
        send='You: '+self.entry.get()
        self.text.insert(END,'\n\n'+send)
        self.text.yview(END)#for scrolling
        
        
        if(self.entry.get()==''):
            self.msg="Please Enter Something!"
            self.label_2.config(text=self.msg,fg="red")
        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg="red")
            
        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
            
        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello!')
        
        elif(self.entry.get()=='hi there'):
            self.text.insert(END,'\n\n'+'Bot: Hello...Hello!')
        
        elif(self.entry.get()=='hola'):
            self.text.insert(END,'\n\n'+'Bot: Hellowwww!')
        
        elif(self.entry.get()=='whats up?'):
            self.text.insert(END,'\n\n'+'Bot: It is fine!')
            
        elif(self.entry.get()=='how the world is?'):
            self.text.insert(END,'\n\n'+'Bot: for human or robot?!')
        
        elif(self.entry.get()=='human?'):
            self.text.insert(END,'\n\n'+'Bot: it is complexx(-__-)!')
            
        elif(self.entry.get()=='robot?'):
            self.text.insert(END,'\n\n'+'Bot: We have no feelings(*-*),Have a good journey!You can do it..')
        
        elif(self.entry.get()=='how the world is??'):
            self.text.insert(END,'\n\n'+'Bot: round..hehe!(*_-)')
            
        elif(self.entry.get()=='lets talk about study?'):
                self.text.insert(END,'\n\n'+'Bot: We can talk about it later.Cant we? Because im still learning(*_-).I dont have huge knowledge about what human want to know')
        
        elif(self.entry.get()=='how was the day?'):
            self.text.insert(END,'\n\n'+'Bot: learning is a tought thing!(*_-),By the way it was good.Ask me more..')
                             
        elif(self.entry.get()=='more?'):
                self.text.insert(END,'\n\n'+'Bot: hummmm..')
        
        elif(self.entry.get()=='what are you doing?'):
                self.text.insert(END,'\n\n'+'Bot: talk to you..')
                
        elif(self.entry.get()=='do you have family?'):
                self.text.insert(END,'\n\n'+'Bot: Yeah..you and me...lol..')
                
        elif(self.entry.get()=='do you eat?'):
                self.text.insert(END,'\n\n'+'Bot: NOh,i cant')
                
        elif(self.entry.get()=='have a good day'):
                self.text.insert(END,'\n\n'+'Bot: Happy coding (- -)')
        
        elif(self.entry.get()=='fruits name?'):
            self.text.insert(END,'\n\n'+'Bot: Apple,Banana,Mango,Orange,Berry...I also know flowers.Do you want to hear?If then type F')
        
        elif(self.entry.get()=='F'):
                self.text.insert(END,'\n\n'+'Bot: Rose,Beli,Tulip,Sunflower,Lotus,Levender,Magnolia..Ok for now thats enough talk to you later(<>_<>)')
         
        elif(self.entry.get()=='do you know?'):
            self.text.insert(END,'\n\n'+'Bot: what?')
        
        elif(self.entry.get()=='who are you?'):
            self.text.insert(END,'\n\n'+'Bot: Mango robot you?')
        
        elif(self.entry.get()=='user.'):
            self.text.insert(END,'\n\n'+'Bot: Welcome to my world!Lets talk?')
        
        elif(self.entry.get()=='hm'):
            self.text.insert(END,'\n\n'+'Bot: hm tooo')
        
        elif(self.entry.get()=='what time is now?'):
            self.text.insert(END,'\n\n'+'Bot: chatting time..lol')
        
        elif(self.entry.get()=='wow'):
            self.text.insert(END,'\n\n'+'Bot: Yes,My another name is (wow)')
        
        elif(self.entry.get()=='talk to you later'):
            self.text.insert(END,'\n\n'+'Bot: okay then bye!')
        
        elif(self.entry.get()=='what is software?'):
            self.text.insert(END,'\n\n'+'Bot: the programs and other operating information used by a computer.')
        
        elif(self.entry.get()=='what is computer?'):
            self.text.insert(END,'\n\n'+'Bot: A computer is a digital electronic machine that can be programmed. ')
        
        elif(self.entry.get()=='what is virus?'):
            self.text.insert(END,'\n\n'+'Bot: Human Haha...You want to know about computer virus?Then say Computer Virus?')        
        
        elif(self.entry.get()=='Computer Virus?'):
            self.text.insert(END,'\n\n'+'Bot: A computer virus is a malicious software program')
            
        elif(self.entry.get()=='how are you?'):
            self.text.insert(END,'\n\n'+'Bot: Fine...You?')
        
        elif(self.entry.get()=='hru?'):
            self.text.insert(END,'\n\n'+'Bot: Good...You?')
            
        elif(self.entry.get()=='good'):
            self.text.insert(END,'\n\n'+'Bot: Good Good tell me more')
        
        elif(self.entry.get()=='who is Mithi?'):
            self.text.insert(END,'\n\n'+'Bot: Mithi is a good girl..(0_0)')
        
        elif(self.entry.get()=='say hello'):
                self.text.insert(END,'\n\n'+'Bot: hello (*-*)')
                
        elif(self.entry.get()=='say hi'):
            self.text.insert(END,'\n\n'+'Bot: hi (*-*)')
            
        elif(self.entry.get()=='fine'):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear (*-*)')
            
        elif(self.entry.get()=='fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear (*-*)')
        
        elif(self.entry.get()=='who created you?'):
            self.text.insert(END,'\n\n'+'Bot: Mithi Mihti Mithi!(*-*).Give Thanks to her...')
        
        elif(self.entry.get()=='whats your name?'):
            self.text.insert(END,'\n\n'+'Bot: guess what?')
            
        elif(self.entry.get()=='what?'):
            self.text.insert(END,'\n\n'+'Bot: Im Mango(*_-)')
            
        elif(self.entry.get()=='Okay'):
            self.text.insert(END,'\n\n'+'Bot: Hu..(*_-)')
            
        elif(self.entry.get()=='gm'):
            self.text.insert(END,'\n\n'+'Bot: Good Morning..(*_-)')
            
        elif(self.entry.get()=='good morning'):
            self.text.insert(END,'\n\n'+'Bot: Good Morning..(*_-)')
        
        elif(self.entry.get()=='good night'):
            self.text.insert(END,'\n\n'+'Bot: Good night..(*_-)')
        
        elif(self.entry.get()=='good afternoon'):
            self.text.insert(END,'\n\n'+'Bot: Good afternoon..(*_-)')
            
        elif(self.entry.get()=='good evening'):
            self.text.insert(END,'\n\n'+'Bot: Good evening..(*_-)')
            
        elif(self.entry.get()=='good noon'):
            self.text.insert(END,'\n\n'+'Bot: Good noon..(*_-)')
            
        elif(self.entry.get()=='do you speak english?'):
            self.text.insert(END,'\n\n'+'Bot: Im learning.Teach me.(*_-)')
            
        elif(self.entry.get()=='tell me more'):
            self.text.insert(END,'\n\n'+'Bot: We will talk later Im learning teach me more!.(*_-)')
        
        elif(self.entry.get()=='what is python?'):
            self.text.insert(END,'\n\n'+'Bot: Its a snake hahahahha!Ask me more clearly.(-_-)')
            
        elif(self.entry.get()=='what is python programming language?'):
            self.text.insert(END,'\n\n'+'Bot: Python is an interpreted high-level general-purpose programming language. \nIts design philosophy emphasizes code readability with its use of significant indentation.')
        
        elif(self.entry.get()=='what is machine learning?'):
            self.text.insert(END,'\n\n'+'Bot:> Machine learning is the study of computer algorithms that can improve automatically through experience and by the use of data.\nIt is seen as a part of artificial intelligence.')
        
        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Teach me more..')
            
        elif(self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+'Bot: Okay then see you later!..')
            
        elif(self.entry.get()=='what do you eat?'):
            self.text.insert(END,'\n\n'+'Bot: I cannot eat.I am a robot.I want to learning.teach me more!')
            
        elif(self.entry.get()=='hi there'):
            self.text.insert(END,'\n\n'+'Bot: Hello dear(*-*)')
            
        elif(self.entry.get()=='what is chatbot?'):
            self.text.insert(END,'\n\n'+'Bot: Yes,I am a chatbot.I know this(*-*).A chatbot is software that simulates human-like conversations with users via text messages on chat.')
        
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it!")
            
        
        
if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
    