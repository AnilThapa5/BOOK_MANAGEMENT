from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Book_Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Book Management System")
        self.root.geometry("1350x690+0+0")


        

        #title
        lbl_title=Label(self.root,text="Dashboard", font=("arial",20,"bold"),bg="green",fg="red",bd=4)
        lbl_title.place(x=0,y=0,width=1350,height=40)


        #frame

        lbl_frame=LabelFrame(self.root,bd=5,text="Add Book Details",relief=RIDGE,font=("arial",15,"bold"),padx=15)
        lbl_frame.place(x=5,y=45,width=435,height=640)


        #book name
        lbl_title=Label(lbl_frame,text="Book Name", font=("arial",12,"bold"),padx=2,pady=6)
        lbl_title.grid(row=0,column=0,sticky=W)

        lbl_title=ttk.Entry(lbl_frame,width=29, font=("arial",12,"bold"))
        lbl_title.grid(row=0,column=1)


        # book publisher
        cname=Label(lbl_frame,text="Book Publisher",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(lbl_frame,width=29,font=("arial",12,"bold"))
        txtcname.grid(row=1,column=1)


         # book price
        bprice=Label(lbl_frame,text="Book Price",font=("arial",12,"bold"),padx=2,pady=6)
        bprice.grid(row=2,column=0,sticky=W)

        txtbprice=ttk.Entry(lbl_frame,width=29,font=("arial",12,"bold"))
        txtbprice.grid(row=2,column=1)


         # book description
        bprice=Label(lbl_frame,text="Book Description",font=("arial",12,"bold"),padx=2,pady=6)
        bprice.grid(row=3,column=0,sticky=W)

        txtbprice=ttk.Entry(lbl_frame,width=29,font=("arial",12,"bold"))
        txtbprice.grid(row=3,column=1)


        # frame for image
        #lblimage=Label(lbl_frame,bd=4,relief=RIDGE)
        #lblimage.place(x=0,y=700,height=100,width=435)

        image1=Image.open(r"C:\Users\DELL\Desktop\BOOK_MANAGEMENT\image\book.jpg")
        image1=image1.resize((400,400),Image.ANTIALIAS)
        self.image11=ImageTk.PhotoImage(image1)

        lblimage=Label(lbl_frame,image=self.image11,bd=4,relief=RIDGE)
        lblimage.place(x=0,y=150,height=300,width=400)



        #buttons frame
        btn_frame=Frame(lbl_frame,bd=2,relief=RIDGE,bg="orange")
        btn_frame.place(x=-10,y=455,width=410,height=150)

        # buttons 
        
        lbl_btn=Button(btn_frame,bd=2,width=15,height=1,relief=RIDGE,text="SAVE",font=("arial",12,"bold"),cursor="hand1")
        lbl_btn.grid(row=0,column=0)

        lbl_btn1=Button(btn_frame,bd=2,width=15,height=1,relief=RIDGE,text="UPDATE",font=("arial",12,"bold"),cursor="hand1")
        lbl_btn1.grid(row=0,column=1,pady=10)

        lbl_btn2=Button(btn_frame,bd=2,width=15,height=1,relief=RIDGE,text="DELETE",font=("arial",12,"bold"),cursor="hand1")
        lbl_btn2.grid(row=1,column=0,pady=10,padx=10)

        lbl_btn3=Button(btn_frame,bd=2,width=15,height=1,relief=RIDGE,text="RESET",font=("arial",12,"bold"),cursor="hand1")
        lbl_btn3.grid(row=1,column=1,pady=10,padx=10)

        # frame for data display lables


        lbl_frame1=Label(self.root,bd=4,relief=RIDGE)
        lbl_frame1.place(x=450,y=55,width=895,height=150)

        #search button

        lbl_seachcombo=ttk.Combobox(lbl_frame1,font=("arial",10,"bold"),state="readonly")
        lbl_seachcombo["value"]=["Name",["Publisher"]]
        lbl_seachcombo.grid(row=0,column=0,sticky=W,padx=2)

        lbl_searchbtn=Button(lbl_frame1,bd=1,width=20,text="Search",font=("arial",10,"bold"))
        lbl_searchbtn.grid(row=0,column=2,sticky=W)




       


        
        

        




      
root=Tk()
ob=Book_Details(root)
root.mainloop()

