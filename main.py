from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import mysql.connector
from tkinter import messagebox

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose= StringVar()
        self.NumberofTablets= StringVar()
        self.Lot= StringVar()
        self.Issuedate= StringVar()
        self.ExpDate= StringVar()
        self.DailyDose= StringVar()
        self.NHSNumber = StringVar()
        self.sideEffect= StringVar()
        self.FurtherInformation= StringVar()
        self.StorageAdvice= StringVar()
        self.DrivingUsingMachine= StringVar()
        self.HowToUseMedication= StringVar()
        self.PatientId= StringVar()
        self.PatientName= StringVar()
        self.DateOfBirth= StringVar()
        self.PatientAddress= StringVar()





        labelTitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        labelTitle.pack(side=TOP,fill=X)

        # ______________________________________________DataFrame________________________________________________________

        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # _____________________________________________Button Frame____________________________________________________________
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # _____________________________________________Details Frame____________________________________________________________
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ________________________________________________DataframeLeft_________________________________________________________

        labelNameTablet = Label(DataframeLeft,text="Names of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        labelNameTablet.grid(row=0,column=0)

        comboNameTable = ttk.Combobox(DataframeLeft,font=("arial",12,"bold"),state="readonly",textvariable=self.Nameoftablets,width=33)
        comboNameTable["values"]=("Nice","Corona Vacacine","Eye Drop", "Adderall","Ativan","Acetaminophen")
        comboNameTable.current(0)
        comboNameTable.grid(row=0,column=1)

        labelRef = Label(DataframeLeft, text="Refence No:", font=("arial", 12, "bold"), padx=2)
        labelRef.grid(row=1, column=0,sticky=W)
        txtref = Entry(DataframeLeft,textvariable=self.ref, font=("arial", 13, "bold"),width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="No Of Tablets:", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft,textvariable=self.NumberofTablets ,font=("arial", 13, "bold"), width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft,textvariable=self.Lot, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=4)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft,textvariable=self.Issuedate, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=4)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft,textvariable=self.ExpDate, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft,textvariable=self.DailyDose ,font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft,textvariable=self.sideEffect ,font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="Further Info:", padx=20)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft,textvariable=self.FurtherInformation ,font=("arial", 13, "bold"), width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=20, pady=4)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, textvariable=self.DrivingUsingMachine, font=("arial", 13, "bold"), width=35)
        txtBloodPressure.grid(row=1, column=3)

        # lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        # lblDose.grid(row=2, column=0, sticky=W)
        # txtDose = Entry(DataframeLeft,textvariable=self.Dose ,font=("arial", 13, "bold"), width=35)
        # txtDose.grid(row=2, column=1)

        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage:", padx=20, pady=4)
        lblStorage.grid(row=2, column=2 ,sticky=W)
        txtStorage= Entry(DataframeLeft,textvariable=self.StorageAdvice, font=("arial", 13, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=20, pady=4)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, textvariable=self.HowToUseMedication, font=("arial", 13, "bold"), width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=20, pady=4)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft,textvariable=self.PatientId ,font=("arial", 13, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)

        lblNHS = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=20, pady=4)
        lblNHS.grid(row=5, column=2, sticky=W)
        txtNHS = Entry(DataframeLeft ,textvariable=self.NHSNumber,font=("arial", 13, "bold"), width=35)
        txtNHS.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=20, pady=4)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft,textvariable=self.PatientName, font=("arial", 13, "bold"), width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date Of Birth:", padx=20, pady=4)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft,textvariable=self.DateOfBirth, font=("arial", 13, "bold"), width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("arial", 12, "bold"), text="PatientAddress:", padx=20, pady=4)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft,textvariable=self.PatientAddress, font=("arial", 13, "bold"), width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ___________________________________________Data Frame Right_________________________________________________________

        self.txtPrscription = Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrscription.grid(row=0,column=0)

        # __________________________________________________Buttons__________________________________________________________________

        btnPrescription = Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), command=self.iPrescriptionData,
                                 width=23, height=0, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23,command=self.update_data, height=0, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, height=0, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, height=0, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, height=0, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # __________________________________________Table____________________________________________________

        # ____________________________________________ScrollBar________________________________________________________

        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","NHSNumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("NHSNumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        self.hospital_table["show"]="headings"



        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("NHSNumber",width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()


    # --------------------------------------------Functionality----------------------------------------------------------------

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() =="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="1234",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.NHSNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()
            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")


    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.NHSNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def update_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set Name_of_tablets=%s,dose=%s,Numbersoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where Reference_No=%s",(
                          self.Nameoftablets.get(),
                          self.Dose.get(),
                          self.NumberofTablets.get(),
                          self.Lot.get(),
                          self.Issuedate.get(),
                          self.ExpDate.get(),
                          self.DailyDose.get(),
                          self.StorageAdvice.get(),
                          self.NHSNumber.get(),
                          self.PatientName.get(),
                          self.DateOfBirth.get(),
                          self.PatientAddress.get(),
                          self.ref.get()
                          ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showerror("update", "Record has been updated Sucessfully")

root = Tk()
ob = Hospital(root)
root.mainloop()