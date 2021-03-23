from tkinter import*
from tkinter import ttk



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

        #buttons
        btn_frame=Frame(lbl_frame,bd=2,relief=RIDGE,bg="orange")
        btn_frame.place(x=0,y=350,width=410,height=250)


        lbl_btn=Button(btn_frame,bd=2,width=15,relief=RIDGE,text="SAVE",font=("arial",12,"bold"),cursor="hand1")
        lbl_btn.grid(row=0,column=0)

        lbl_btn1=Button(btn_frame,bd=2,width=15,relief=RIDGE,text="UPDATE",font=("arial",12,"bold"),cursor="hand1")
        lbl_btn1.grid(row=0,column=1)

        lbl_btn2=Button(btn_frame,bd=2,width=15,relief=RIDGE,text="DELETE",font=("arial",12,"bold"),cursor="hand1")
        lbl_btn2.grid(row=1,column=0,pady=1)

        lbl_btn3=Button(btn_frame,bd=2,width=15,relief=RIDGE,text="RESET",font=("arial",12,"bold"),cursor="hand1")
        lbl_btn3.grid(row=1,column=1,pady=1)

        ####




       


        
        

        




      
root=Tk()
ob=Book_Details(root)
root.mainloop()

