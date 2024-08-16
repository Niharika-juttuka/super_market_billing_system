from tkinter import*
import math,random,os
from tkinter import messagebox
class bill_App:
    def _init_(self,root):
         self.root=root
         self.root.geometry("1350x700+0+0")
         self.root.title("Billing System")
         bg_color='#2F4F4F'
         
         title=Label(self.root,text="Billing Software",bd=5,relief=RAISED,bg=bg_color,fg="black",font=("jokerman 30 bold"),pady=2).pack(fill=X)
         #===============variables================
        #  ===============cosmetics================
         self.soap=IntVar()
         self.face_cream=IntVar()
         self.face_wash=IntVar()
         self.spray=IntVar()
         self.gell=IntVar()
         self.lotion=IntVar()
        #  #==================grocery===============
         self.rice=IntVar()
         self.salt=IntVar()
         self.sugar=IntVar()
         self.food_oil=IntVar()
         self.daal=IntVar()
         self.wheat=IntVar()
         self.tea=IntVar()
         #==================cold drinks===============
         self.maaza=IntVar()
         self.thumbsup=IntVar()
         self.sprite=IntVar()
         self.magic_moments=IntVar()
         self.marinda=IntVar()
         self.mountain_dew=IntVar()
         #================Total product price an dtax service=======
         self.cosmetic_price=StringVar()
         self.grocery_price=StringVar()
         self.cold_drink_price=StringVar()

         self.cosmetic_tax=StringVar()
         self.grocery_tax=StringVar()
         self.cold_drink_tax=StringVar()
         #==========================customer================
         self.c_name=StringVar()
         self.c_phone=StringVar()
         
         self.bill_no=StringVar()
         x=random.randint(1000,9999)
         self.bill_no.set(str(x))
         self.search_bill=StringVar()

         
         #==============customer detail frame
         f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman" ,15, "bold"),fg="gold",bg=bg_color)
         f1.place(x=0,y=80,relwidth=1)

         cname_lbl=Label(f1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=3)
         cname_txt=Entry(f1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN ).grid(row=0,column=1,pady=5,padx=10)


         cphone_lbl=Label(f1,text="Customer Phone",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=3)
         cphone_txt=Entry(f1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN ).grid(row=0,column=3,pady=5,padx=10)


         cbill_lbl=Label(f1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=3)
         cbill_txt=Entry(f1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN ).grid(row=0,column=5,pady=5,padx=10)

         Bill_btn=Button(f1,text="Search",command=self.find_bill,bg="cadetblue",fg="white",bd=7,width=10,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
        #  bill_btn=Button(f1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
         #=============cosmetic frame
         f2=LabelFrame(self.root,text="Cosmetic",bd=10,relief=GROOVE,font=("times new roman" ,15, "bold"),fg="gold",bg=bg_color)
         f2.place(x=5,y=180,width=325,height=380)

         bath_lbl=Label(f2,text="Bath soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
         bath_txt=Entry(f2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

         face_cream_lbl=Label(f2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
         face_cream_txt=Entry(f2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

         bath_w_lbl=Label(f2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
         bath_w_txt=Entry(f2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
         
         hair_s_lbl=Label(f2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
         hair_s_txt=Entry(f2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
         

         hair_g_lbl=Label(f2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
         hair_g_txt=Entry(f2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
         
         body_lbl=Label(f2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
         body_txt=Entry(f2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



         #=============Grocery frame
         f3=LabelFrame(self.root,text="Groceries",bd=10,relief=GROOVE,font=("times new roman" ,15, "bold"),fg="gold",bg=bg_color)
         f3.place(x=335,y=180,width=325,height=380)

         g1_lbl=Label(f3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
         g1_txt=Entry(f3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

         g2_lbl=Label(f3,text="Salt",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
         g2_txt=Entry(f3,width=10,textvariable=self.salt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

         g3_lbl=Label(f3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
         g3_txt=Entry(f3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
         
         g4_lbl=Label(f3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
         g4_txt=Entry(f3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
         

         g5_lbl=Label(f3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
         g5_txt=Entry(f3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
         
         g6_lbl=Label(f3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
         g6_txt=Entry(f3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



         #========== cool drink frame
         f4=LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE,font=("times new roman" ,15, "bold"),fg="gold",bg=bg_color)
         f4.place(x=665,y=180,width=325,height=380)

         c1_lbl=Label(f4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
         c1_txt=Entry(f4,width=10,textvariable=self.maaza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

         c2_lbl=Label(f4,text="Thumbs-Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
         c2_txt=Entry(f4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

         c3_lbl=Label(f4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
         c3_txt=Entry(f4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
         
         c4_lbl=Label(f4,text="Magic moments",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
         c4_txt=Entry(f4,width=10,textvariable=self.magic_moments,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
         

         c5_lbl=Label(f4,text="Mirinda",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
         c5_txt=Entry(f4,width=10,textvariable=self.marinda,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
         
         c6_lbl=Label(f4,text="Mountain-Dew",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
         c6_txt=Entry(f4,width=10,textvariable=self.mountain_dew,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #=========billing 
         f5=Frame(self.root,bd=10,relief=GROOVE)
         f5.place(x=995,y=180,width=350,height=380)
         bill_title=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
         scrol_y=Scrollbar(f5,orient=VERTICAL)
         self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
         scrol_y.pack(side=RIGHT,fill=Y)
         scrol_y.config(command=self.txtarea.yview)
         self.txtarea.pack(fill=BOTH,expand=1)



         #==========Button frame

         f6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill menu",font=("times new roman" ,15, "bold"),fg="gold",bg=bg_color)
         f6.place(x=0,y=560,relwidth=1,height=140)
         m1=Label(f6,text="Total cosmetic price",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")        
         m1_txt=Entry(f6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

         m2=Label(f6,text="Total Groceries price",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")        
         m2_txt=Entry(f6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
         
         m3=Label(f6,text="Total Cold Drinks price",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
         m3_txt=Entry(f6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


         c1=Label(f6,text="Cosmetic Tax",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")        
         c1_txt=Entry(f6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

         c2=Label(f6,text="Groceries Tax",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")        
         c2_txt=Entry(f6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
         
         c3=Label(f6,text="Cold Drinks Tax",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
         c3_txt=Entry(f6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


         btn_F=Frame(f6,bd=7,relief=GROOVE)
         btn_F.place(x=740,width=585,height=105)

         total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 12 bold").grid(row=0,column=0,padx=5)
         Bill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 12 bold").grid(row=0,column=1,padx=5)
         clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 12 bold").grid(row=0,column=2,padx=5)
         Exit_btn=Button(btn_F,text="Exit",command=self.exit,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 12 bold").grid(row=0,column=3,padx=5)


         
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*240
        self.c_fw_p=self.face_wash.get()*140
        self.c_hs_p=self.spray.get()*450
        self.c_hg_p=self.gell.get()*350
        self.c_bl_p=self.lotion.get()*240

        self.total_cosmetic_price=float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_hs_p+
            self.c_hg_p+
            self.c_bl_p
            )
        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs."+str(self.c_tax))
        

        self.g_r_p=self.rice.get()*240
        self.g_f_p=self.food_oil.get()*80
        self.g_d_p=self.daal.get()*140
        self.g_w_p=self.wheat.get()*200
        self.g_s_p=self.sugar.get()*140
        self.g_t_p=self.tea.get()*180
        self.g_ss_p=self.salt.get()*30
        self.total_grocery_price=float(
            self.g_r_p+
            self.g_f_p+
            self.g_d_p+
            self.g_w_p+
            self.g_s_p+
            self.g_ss_p+
            self.g_t_p
            )
        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.d_m_p=self.maaza.get()*40
        self.d_t_p=self.thumbsup.get()*50
        self.d_s_p=self.sprite.get()*40
        self.d_mm_p=self.magic_moments.get()*400
        self.d_mnd_p=self.marinda.get()*20
        self.d_mnt_p=self.mountain_dew.get()*40
        self.total_cold_drink_price=float(
            self.d_m_p+
            self.d_mm_p+
            self.d_t_p+
            self.d_s_p+
            self.d_mnd_p+
            self.d_mnt_p
            )
        self.cold_drink_price.set("Rs."+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                            self.total_grocery_price+
                            self.total_cold_drink_price+
                            self.c_tax+
                            self.g_tax+
                            self.cd_tax
                            )


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome to HRL Retail\n")
        self.txtarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.txtarea.insert(END,f"\n================================")
        self.txtarea.insert(END,f"\nProduct\t   Quantity\t\tPrice")
        self.txtarea.insert(END,f"\n================================")
        
        

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone=="":
            messagebox.showerror("Error","Please enter Customer details")
        elif self.cosmetic_price.get()=='Rs.0.0' and self.grocery_price.get()=="Rs.0.0" and self.cold_drink_price.get()=="Rs.0.0":
            messagebox.showerror("Error","No Products are purchased")
        
        else:
            self.welcome_bill()
            #========Cosmetics=======
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\nFace Cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\nFace Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\nSpray\t\t{self.spray.get()}\t{self.c_hs_p}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\nBody Lotion\t\t{self.lotion.get()}\t{self.c_bl_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\nGell\t\t{self.gell.get()}\t{self.c_hg_p}")


        #==========Groceries==========================
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\nRice\t\t{self.rice.get()}\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\nFood Oil\t\t{self.face_cream.get()}\t{self.g_f_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\nDaal\t\t{self.face_wash.get()}\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\nWheat\t\t{self.spray.get()}\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nSugar\t\t{self.lotion.get()}\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\nTea\t\t{self.gell.get()}\t{self.g_t_p}")
            if self.salt.get()!=0:
                self.txtarea.insert(END,f"\nSalt\t\t{self.salt.get()}\t{self.g_s_p}")

            #============Cold Drinks========
            if self.maaza.get()!=0:
                self.txtarea.insert(END,f"\nMaaza\t\t{self.maaza.get()}\t{self.d_m_p}")
            if self.thumbsup.get()!=0:
                self.txtarea.insert(END,f"\nThumbs-Up\t\t{self.thumbsup.get()}\t{self.d_t_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t{self.d_s_p}")
            if self.marinda.get()!=0:
                self.txtarea.insert(END,f"\nMarinda\t\t{self.marinda.get()}\t{self.d_mnd_p}")
            if self.magic_moments.get()!=0:
                self.txtarea.insert(END,f"\nMagic-moments\t\t{self.magic_moments.get()}\t{self.d_mm_p}")
            if self.mountain_dew.get()!=0:
                self.txtarea.insert(END,f"\nMountain-Dew\t\t{self.mountain_dew.get()}\t{self.d_mnt_p}")

            self.txtarea.insert(END,f"\n--------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCosmetic Tax \t\t\t {self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nGrocery Tax \t\t\t {self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
             self.txtarea.insert(END,f"\nCold Drink Tax \t\t\t {self.cold_drink_tax.get()}")
            self.txtarea.insert(END,f"\n\nTotal Bill \t\t\t {self.Total_bill}")
            self.txtarea.insert(END,f"\n--------------------------------")
            self.save_bill()
    def save_bill(self):
        opt=messagebox.askyesno("Save Bill","Do you want to save the bill ?")
        if opt>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("C:\\Users\\byas\\Desktop\\bills\\"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill number: {self.bill_no.get()} saved successfully")

        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("C:\\Users\\byas\\Desktop\\bills\\"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"\\Users\\byas\\Desktop\\bills\\{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                 self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.")

    def clear_data(self):
        opt=messagebox.askyesno("CLEAR","Do you Really want to Clear?")
        if opt>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)
            #  #==================grocery===============
            self.rice.set(0)
            self.salt.set(0)
            self.sugar.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.tea.set(0)
            #==================cold drinks===============
            self.maaza.set(0)
            self.thumbsup.set(0)
            self.sprite.set(0)
            self.magic_moments.set(0)
            self.marinda.set(0)
            self.mountain_dew.set(0)
            #================Total product price an dtax service=======
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #==========================customer================
            self.c_name.set("")
            self.c_phone.set("")
    
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def exit(self):
        opt=messagebox.askyesno("EXIT","Do you Really want to Exit?")
        if opt>0:
            self.root.destroy()
root=Tk()
obj=bill_App(root)
root.mainloop()