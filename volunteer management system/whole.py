from tkinter import*
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import ttk
#from volunteer import Database
#from PIL import ImageTk,Image

root=Tk()
root.title("Login")

#image=Image.open('back_image.png')


def click():
    root=Tk()
    root.title("Volunteer Managment System")
    frame=Frame(root, bg="steelblue3", width=300,height=1000)
    frame.place(x=0,y=0)

    myfont=Font(root,family="times",size=20,weight="bold")
    Label(root,text="Enter the Details",font=myfont).place(x=500,y=50)

    letter=Font(root,family="times",size=12,weight="bold")

    Label(root,text="Name",font=letter).place(x=500,y=150)
    Label(root,text="Degree",font=letter).place(x=500,y=300)
    Label(root,text="Year of study",font=letter).place(x=500,y=350)
    Label(root,text="Section",font=letter).place(x=500,y=200)
    Label(root,text="Date of birth",font=letter).place(x=500,y=250)
    Label(root,text="Contact Number",font=letter).place(x=500,y=400)
    Label(root,text="Alternate Number",font=letter).place(x=500,y=450)
    Label(root,text="Address",font=letter).place(x=500,y=500)
    Entry(root,width=25).place(x=650,y=150)
    combobox=Combobox(root)
    combobox['values']=('A','B','C','D',"Others")
    combobox.place(x=650,y=200)
    #txt.place(x=650,y=200)
    #sectioncombo
    #Entry(root,width=25).place(x=650,y=200)    #section
    Entry(root,width=25).place(x=650,y=250)#dob

    combobox=Combobox(root)
    combobox['values']=('Ug','Pg','Diploma',"Others")
    combobox.place(x=650,y=300)

    #Entry(root,width=25).place(x=650,y=300)     #degree

    combobox=Combobox(root)
    combobox['values']=('I','II','III')
    combobox.place(x=650,y=350)


    #Entry(root,width=25).place(x=650,y=350)   #year of studying
    Entry(root,width=25).place(x=650,y=400)   #contact number     
    Entry(root,width=25).place(x=650,y=150)  #name
    Entry(root,width=25).place(x=650,y=450)  #alternative number
    Text(root,width=20,height=5).place(x=650,y=500)
    
         

         
    Label(root,text="Menu",font="times",relief="raised",width=30).place(x=15,y=5)
    Button(root,text="Add  Details",font="times",fg="black").place(x=50,y=180)
    Button(root,text="Update Details",font="times",fg="black").place(x=50,y=240)
    Button(root,text="Delete Details",font="times",fg="black").place(x=50,y=300)
    Button(root,text="Clear Details",font="times",fg="black").place(x=50,y=370)
    root.geometry('1234x1234')
    root.mainloop()

    #view
    

    
#head frame title

Frame(root,width=1400,height=130,bg='steelblue3').pack()
Label(root,text=" \"Volunteer Management System\" ",width=50,bg='steelblue3',fg='white',font=('times',30,'bold')).place(x=80,y=20)
Label(root,text="  ***Give your time, make a difference.  Volunteers plant seeds of kindness that grow into forests of gratitude***",width=100,bg='steelblue3',fg='white',font=('times',16)).place(x=100,y=75)


img=PhotoImage(file='login_pic.png')
Label(root,image=img,border=0).place(x=290,y=200)
root.configure(bg='white')

Frame(root,width=380,height=390,bg='white').place(x=800,y=180)

Label(root,text="Sign in",bg='white',fg='#57a1f8',font=('Microsoft YaHei UI Light','22','bold')).place(x=930,y=200)

#username label

#function for the temporary text

def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,"Username")

user=Entry(root,width=20,fg='#57a1f8',bg='white',border=0,font=('Microsoft YaHei UI Light',14))
user.place(x=870,y=285)
user.insert(0,"Username")
Frame(root,border=2,width=295,height=2,bg='black').place(x=870,y=315)

user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

#password made by coopy of username


def access(e):
    secure.delete(0,"end")
def inaccess(e):
    password=secure.get()
    if password=='':
        secure.insert(0,"Password")

secure=Entry(root,width=20,fg='#57a1f8',bg='white',border=0,font=('Microsoft YaHei UI Light',14))
secure.place(x=870,y=360)
secure.insert(0,"Password")
Frame(root,border=2,width=295,height=2,bg='black').place(x=870,y=388)

secure.bind("<FocusIn>",access)
secure.bind("<FocusOut>",inaccess)


#submit button



Button(root,text="submit",command=click,width=10,bg='steelblue3',font=('times',14,'bold')).place(x=930,y=440)

root.geometry('1234x1234')

root.mainloop()





