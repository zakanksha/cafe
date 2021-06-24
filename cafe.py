from tkinter import *
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk
import mysql.connector
import mysql.connector as mysql
from PIL import ImageTk, Image
from sys import exit
import os
import time
class cafe:
	def __init__(self,root):
		def login():
			con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
			z=con.cursor(buffered=True)
			z.execute("CREATE DATABASE IF NOT EXISTS cafe")
			z.execute("use cafe")
			u=username_entry.get()
			p=pass_entry.get()
			if (u=="" and p==""):
				msgbox.showinfo("Login status","You need to enter Username and Password")
				return
			if (u==""):
				msgbox.showinfo("Login status","You need to enter Username")
				return
			if (p==""):
				msgbox.showinfo("Login status","You need to enter Password")
				return
			z.execute("SELECT * FROM user where user= '"+u+"' AND password='"+p+"'")
			rowcount=z.rowcount
			if z.rowcount==1:
				msgbox.showinfo("Login status","Login Successfully Done.")
				self.root.iconify()
				root2=Toplevel()
				root2.geometry("1250x635+7+7")
				root2.title("cafe management system")
				root2["bg"] = "khaki3"
				root2.resizable(False,False)
				root2.iconbitmap(r'D:\\cafe\\images\\browncoffee.ico')
				img = ImageTk.PhotoImage(file="D:\\cafe\\images\\beans.png")
				panel = Label(root2, image = img,bg="khaki3")
				panel.place(x=0,y=0)
				panel.image=img
				def cust(Win1_class):
					global win3
					win3 = Toplevel(root)
					Win1_class(win3)
				def menu(Win2_class):
					global win4
					win4 = Toplevel(root)
					Win2_class(win4)
				def order(Win3_class):
					global win5
					win5= Toplevel(root)
					Win3_class(win5)	
				def payment(Win4_class):
					global win6
					win6= Toplevel(root)
					Win4_class(win6)
				def report(Win5_class):
					global win7
					win7= Toplevel(root)
					Win5_class(win7)
				z=Label(root2,text="WELCOME TO THE CAFE",fg="black",bg="khaki3",font=("Consolas","60","bold"))
				z.place(x=240,y=30)
				a=Button(root2,text="CUSTOMER DETAILS",fg="Beige",bg="black",font=("Consolas","15","bold"))
				a.place(x=1000,y=200,width=230)
				a['command']=lambda:cust(cust_class)
				a2=Button(root2,text="MENU DETAILS",fg="Beige",bg="black",font=("Consolas","15","bold"))
				a2.place(x=1000,y=440,width=230)
				a2['command']=lambda:menu(menu_class)
				a3=Button(root2,text="ORDER & BILL DETAILS",fg="Beige",bg="black",font=("Consolas","15","bold"))
				a3.place(x=1000,y=280,width=230)
				a3['command']=lambda:order(order_class)
				a4=Button(root2,text="PAYMENT DETAILS",fg="Beige",bg="black",font=("Consolas","15","bold"))
				a4.place(x=1000,y=360,width=230)
				a4['command']=lambda:payment(payment_class)
				a5=Button(root2,text="REPORT",fg="Beige",bg="black",font=("Consolas","15","bold"))
				a5.place(x=1000,y=520,width=230)
				a5['command']=lambda:report(report_class)
			else:
				msgbox.showinfo("Login status","Please enter correct Username and Password")
				return
			con.close();
		class cust_class:
			def __init__(self, root):
				def insert():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					cust_id=id1.get()
					cust_name=name1.get()
					cno=contactno1.get()
					cust_add=add1.get()
					if (cust_id=="" or cust_name=="" or cno=="" or cust_add==""):
						msgbox.showinfo("customer status","You need to enter all details")
					else:
						if con.is_connected()==False: 
							con.connect()
						z.execute("create table if not exists customers(cust_id INT AUTO_INCREMENT NOT NULL,cust_name CHAR(20),cno INTEGER(100),cust_add CHAR(20), PRIMARY KEY(cust_id))")
						z.execute("insert into customers values('"+cust_id+"','"+cust_name+"','"+cno+"','"+cust_add+"')")
						z.execute("commit");
						msgbox.showinfo("insert customer status","details inserted!!")
						
						con.close();		
				def update():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					cust_id=id1.get()
					cust_name=name1.get()
					cno=contactno1.get()
					cust_add=add1.get()
					if (cust_id=="" or cust_name=="" or cno=="" or cust_add==""):
						msgbox.showinfo("customer status","You need to enter all details")
					else:
						if con.is_connected()==False:
							con.connect()
						#z.execute("create table if not exists customers(cust_id INT AUTO_INCREMENT NOT NULL,cust_name CHAR(20),cno INTEGER(12),cust_add CHAR(20),PRIMARY KEY(cust_id))")
						z.execute(""" UPDATE customers SET cust_name=%s,cno=%s,cust_add=%s WHERE cust_id=%s """,(cust_name,cno,cust_add,cust_id))
						z.execute("commit");
						msgbox.showinfo("update customer status","details updated!!")
						con.close();
				def delete():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					cust_id=id1.get()
					if (cust_id==""):
						msgbox.showinfo("delete customer status","please enter customer id")
					else:
						if con.is_connected()==False:
							con.connect()
						#z.execute("create table if not exists customers(cust_id INT AUTO_INCREMENT NOT NULL,cust_name CHAR(20),cno INTEGER(12),cust_add CHAR(20),PRIMARY KEY(cust_id))")
						if msgbox.askyesno("confirm delete?","are you sure you want to delete this customer?"):	
							z.execute("DELETE FROM customers WHERE cust_id=%s "%(cust_id))
							z.execute("commit");
							msgbox.showinfo("delete customer status","details deleted!!")
							con.close();
				def clear(): 
					global expression 
					expression = "" 
					equation1.set("") 
					equation2.set("") 
					equation3.set("") 
					equation4.set("") 
				def get_selected_row(event):
					try:
						global selected_tuple
						index = cust_list.curselection()[0]
						selected_tuple = cust_list.get(index)
						id1.delete(0, END)
						id1.insert(END, selected_tuple[0])
						name1.delete(0, END)
						name1.insert(END, selected_tuple[1])
						contactno1.delete(0, END)
						contactno1.insert(END, selected_tuple[2])
						add1.delete(0, END)
						add1.insert(END, selected_tuple[3])
					except IndexError:
						pass	
				def view_command():
					cust_list.delete(0, END)
					for row in view():
						cust_list.insert(END, row)
				self.root = root
				self.root.geometry("550x550+300+50")
				self.root["bg"] = "khaki3"
				root.title("CUSTOMER")
				self.root.resizable(False,False)
				root.iconbitmap(r'D:\\cafe\\images\\customer.ico')
				img = ImageTk.PhotoImage(file="D:\\cafe\\images\\custcup.png")
				panel = Label(root, image = img,width=100,height=100,bg="khaki3")
				panel.place(x=400,y=260)
				panel.image=img
				equation1 = StringVar()
				equation2 = StringVar()
				equation3 = StringVar()
				equation4 = StringVar()
				aid=Label(self.root,text="Enter Customer Details Below",fg="black",bg="khaki3",font=("Consolas","16","bold"))
				aid.place(x=110,y=3)
				id=Label(self.root,text="CUSTOMER ID:",fg="black",bg="khaki3",font=("Consolas","13","bold"))
				id.place(x=110,y=35)
				id1=Entry(self.root,width=150,bg="Beige",fg="black",font=("Consolas","13","bold"),textvariable=equation1) 
				id1.place(x=110,y=70,width=130) 
				name=Label(self.root,text="CUSTOMER NAME:",fg="black",bg="khaki3",font=("Consolas","13","bold"))
				name.place(x=320,y=35)
				name1=Entry(self.root,width=150,bg="Beige",fg="black",font=("Consolas","13","bold"),textvariable=equation2) 
				name1.place(x=320,y=70,width=130) 
				contactno=Label(self.root,text="CONTACT NUMBER:",fg="black",bg="khaki3",font=("Consolas","13","bold"))
				contactno.place(x=110,y=115)
				contactno1=Entry(self.root,width=150,bg="Beige",fg="black",font=("Consolas","13","bold"),textvariable=equation3 )
				contactno1.place(x=110,y=150,width=130) 
				add=Label(self.root,text="ADDRESS:",fg="black",bg="khaki3",font=("Consolas","13","bold"))
				add.place(x=320,y=115)
				add1=Entry(self.root,width=150,bg="Beige",fg="black",font=("Consolas","13","bold"),textvariable=equation4) 
				add1.place(x=320,y=150,width=130) 
				insert=Button(self.root,text="ADD CUSTOMER",bg="black",fg="Beige",font=("Consolas","13","bold"),command=insert)
				insert.place(x=30,y=200,width=115)
				update=Button(self.root,text="UPDATE CUSTOMER",bg="black",fg="Beige",font=("Consolas","13","bold"),command=update)
				update.place(x=150,y=200,width=150)
				delete=Button(self.root,text="DELETE CUSTOMER",bg="black",fg="Beige",font=("Consolas","13","bold"),command=delete)
				delete.place(x=305,y=200,width=150)
				clear=Button(self.root,text="CLEAR",bg="black",fg="Beige",font=("Consolas","13","bold"),command=clear)
				clear.place(x=460,y=200,width=60)
				view=Button(self.root,text="VIEW ALL",bg="black",fg="Beige",font=("Consolas","13","bold"),command=view_command)
				view.place(x=410,y=365,width=90)
				cust_list = Listbox(self.root, height=11, width=30,selectmode=SINGLE,font=("Consolas","15","bold"), border=3,bg="black",fg="Beige")
				cust_list.place(x=32,y=250)
				cust_list.bind('<<ListboxSelect>>', get_selected_row)
				scrollbary = Scrollbar(self.root,orient='vertical')
				scrollbary.place(x=371,y=250,height=289)
				scrollbarx = Scrollbar(self.root,orient='horizontal')
				scrollbarx.place(x=32,y=523,width=338)
				cust_list.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
				scrollbary.configure(command=cust_list.yview)
				scrollbarx.configure(command=cust_list.xview)
				def view():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="cafe",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					z.execute("SELECT * FROM customers")
					rows=z.fetchall()
					con.close()
					return rows
		class menu_class:
			def __init__(self, root):
				def insert():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					item_id=id1.get()
					item_name=name1.get()
					item_type=type1.get()
					item_price=price1.get()
					if (item_id=="" or item_name=="" or item_type=="" or item_price==""):
						msgbox.showinfo("menu status","You need to enter all details")
					else:
						if con.is_connected()==False:
							con.connect()
						z.execute("create table if not exists menu(item_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,item_name CHAR(50),item_type CHAR(50),item_price INT(20))")
						z.execute("insert into menu values('"+item_id+"','"+item_name+"','"+item_type+"','"+item_price+"')")
						z.execute("commit");
						msgbox.showinfo("insert item status","details inserted!!")
						con.close();		
				def update():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					item_id=id1.get()
					item_name=name1.get()
					item_type=type1.get()
					item_price=price1.get()
					if (item_id=="" or item_name=="" or item_type=="" or item_price==""):
						msgbox.showinfo("menu status","You need to enter all details")
					else:
						if con.is_connected()==False:
							con.connect()
						z.execute(""" UPDATE menu SET item_name=%s,item_type=%s,item_price=%s WHERE item_id=%s """,(item_name,item_type,item_price,item_id))
						z.execute("commit");
						msgbox.showinfo("update item status","details updated!!")
						con.close();
				def delete():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					item_id=id1.get()
					if (item_id==""):
						msgbox.showinfo("delete item status","please enter item id")
					else:
						if con.is_connected()==False:
							con.connect()
						if msgbox.askyesno("confirm delete?","are you sure you want to delete this item?"):	
							z.execute("DELETE FROM menu WHERE item_id='%s' "%(item_id))
							z.execute("commit");
							msgbox.showinfo("delete item status","details deleted!!")
							con.close();
				def clear(): 
					global expression 
					expression = "" 
					equation1.set("") 
					equation2.set("") 
					equation3.set("") 
					equation4.set("")
				def get_selected_row(event):
					try:
						global selected_tuple
						index = menu_list.curselection()[0]
						selected_tuple = menu_list.get(index)
						id1.delete(0, END)
						id1.insert(END, selected_tuple[0])
						name1.delete(0, END)
						name1.insert(END, selected_tuple[1])
						type1.delete(0, END)
						type1.insert(END, selected_tuple[2])
						price1.delete(0, END)
						price1.insert(END, selected_tuple[3])
					except IndexError:
						pass	
				def view_command():
					menu_list.delete(0, END)
					for row in view():
						menu_list.insert(END, row)
				self.root = root
				self.root.geometry("550x550+300+50")
				self.root["bg"] = "khaki3"
				root.title("MENU")
				self.root.resizable(False,False)
				root.iconbitmap(r'D:\\cafe\\images\\menu.ico')
				img = ImageTk.PhotoImage(file="D:\\cafe\\images\\menucup.png")
				panel = Label(root, image = img,width=100,height=100,bg="khaki3")
				panel.place(x=400,y=260)
				panel.image=img
				equation1 = StringVar()
				equation2 = StringVar()
				equation3 = StringVar()
				equation4 = StringVar()
				aid=Label(self.root,text="Enter Menu Details Below",fg="Black",bg="khaki3",font=("Consolas","16","bold"))
				aid.place(x=140,y=3)
				id=Label(self.root,text="ITEM ID:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				id.place(x=110,y=35)
				id1=Entry(root,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation1) 
				id1.place(x=110,y=70,width=130) 
				name=Label(self.root,text="ITEM NAME:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				name.place(x=320,y=35)
				name1=Entry(root,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation2) 
				name1.place(x=320,y=70,width=130) 
				type=Label(self.root,text="ITEM TYPE:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				type.place(x=110,y=115)
				type1=Entry(root,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation3) 
				type1.place(x=110,y=150,width=130) 
				price=Label(self.root,text="PRICE:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				price.place(x=320,y=115)
				price1=Entry(root,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation4) 
				price1.place(x=320,y=150,width=130) 
				insert=Button(self.root,text="ADD ITEM",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=insert)
				insert.place(x=30,y=200,width=115)
				update=Button(self.root,text="UPDATE ITEM",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=update)
				update.place(x=150,y=200,width=150)
				delete=Button(self.root,text="DELETE ITEM",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=delete)
				delete.place(x=305,y=200,width=150)
				clear=Button(self.root,text="CLEAR",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=clear)
				clear.place(x=460,y=200,width=60)
				view=Button(self.root,text="VIEW ALL",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=view_command)
				view.place(x=400,y=370,width=90)
				menu_list = Listbox(self.root, height=11, width=30,selectmode=SINGLE,font=("Consolas","15","bold"), border=3,bg="black",fg="Beige")
				menu_list.place(x=32,y=250)
				menu_list.bind('<<ListboxSelect>>', get_selected_row)
				scrollbary = Scrollbar(self.root,orient='vertical')
				scrollbary.place(x=371,y=250,height=289)
				scrollbarx = Scrollbar(self.root,orient='horizontal')
				scrollbarx.place(x=32,y=523,width=338)
				menu_list.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
				scrollbary.configure(command=menu_list.yview)
				scrollbarx.configure(command=menu_list.xview)
				def view():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="cafe",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					z.execute("SELECT * FROM menu")
					rows=z.fetchall()
					con.close()
					return rows		
		class payment_class:
			def __init__(self, root):
				def insert():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					order_id=oid1.get()
					payment_id=pid1.get()
					total_price=total_price1.get()
					amount_given=amount_given1.get()
					amount_returned=amount_returned1.get()
					if (payment_id=="" or amount_given=="" or amount_returned==""):
						msgbox.showinfo("payment status","You need to enter all details")
					else:
						if con.is_connected()==False:
							con.connect()
						z.execute("create table if not exists payment(order_id INT(20),payment_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,amount_given INTEGER(20),amount_returned INTEGER(20), CONSTRAINT order_id FOREIGN KEY(order_id) REFERENCES order1(order_id)ON DELETE CASCADE ON UPDATE CASCADE)ENGINE=InnoDB");
						z.execute("insert into payment values('"+order_id+"','"+payment_id+"','"+amount_given+"','"+amount_returned+"')")
						z.execute("commit");
						msgbox.showinfo("payment status","details inserted!!")
						con.close();		
				def update():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					order_id=oid1.get()
					payment_id=pid1.get()
					total_price=total_price1.get()
					amount_given=amount_given1.get()
					amount_returned=amount_returned1.get()
					if (payment_id=="" or amount_given=="" or amount_returned==""):
						msgbox.showinfo("payment status","You need to enter all details")
					else:
						if con.is_connected()==False:
							con.connect()
						z.execute(""" UPDATE payment SET amount_given=%s,amount_returned=%s,order_id=%s WHERE payment_id=%s """,(amount_given,amount_returned,order_id,payment_id))
						z.execute("commit");
						msgbox.showinfo("payment status","details updated!!")
						con.close();
				def delete():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					payment_id=pid1.get()
					if (payment_id==""):
						msgbox.showinfo("payment status","please enter item id")
					else:
						if con.is_connected()==False:
							con.connect()
						if msgbox.askyesno("confirm delete?","are you sure you want to delete this payment?"):	
							z.execute("DELETE FROM payment WHERE payment_id='%s' "%(payment_id))
							z.execute("commit");
							msgbox.showinfo("payment status","details deleted!!")
							con.close();
				def clears(): 
					global expression 
					expression = "" 
					equation4.set("")
					equation1.set("") 
					equation2.set("") 
					equation3.set("")
					 
				def get_selected_row(event):
					try:
						global selected_tuple
						index = payment_list.curselection()[0]
						selected_tuple = payment_list.get(index)
						oid1.delete(0, END)
						oid1.insert(END, selected_tuple[0])
						pid1.delete(0, END)
						pid1.insert(END, selected_tuple[1])
						amount_given1.delete(0, END)
						amount_given1.insert(END, selected_tuple[2])
						amount_returned1.delete(0, END)
						amount_returned1.insert(END, selected_tuple[3])
						
					except IndexError:
						pass	
				def view_command():
					payment_list.delete(0, END)
					for row in view():
						payment_list.insert(END, row) 
				self.root = root
				self.root.geometry("700x600+230+40")
				self.root["bg"] = "khaki3"
				root.title("payment")
				self.root.resizable(False,False)
				root.iconbitmap(r'D:\\cafe\\images\\payment.ico')
				equation1 = StringVar()
				equation2 = StringVar()
				equation3 = StringVar()
				equation4 = StringVar()
				id=Label(self.root,text="Enter Payment Details Below",fg="Black",bg="khaki3",font=("Consolas","16","bold"))
				id.place(x=170,y=3)
				oid=Label(self.root,text="ORDER ID:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				oid.place(x=50,y=50)
				oid1=Entry(root,width=150,bg="Beige",fg='Black',font=("Consolas","13","bold"),textvariable=equation4) 
				oid1.place(x=50,y=85,width=130)
				pid=Label(self.root,text="PAYMENT ID:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				pid.place(x=270,y=50)
				pid1=Entry(self.root,width=150,bg="Beige",fg='Black',font=("Consolas","13","bold"),textvariable=equation1) 
				pid1.place(x=270,y=85,width=130) 
				total_price=Label(self.root,text="TOTAL PRICE:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				total_price.place(x=490,y=50)
				total_price1=Entry(self.root,width=150,bg="Beige",fg='Black',font=("Consolas","13","bold")) 
				total_price1.place(x=490,y=85,width=130) 
				amount_given=Label(self.root,text="AMOUNT RECEIVED:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				amount_given.place(x=50,y=135)
				amount_given1=Entry(root,width=150,bg="Beige",fg='Black',font=("Consolas","13","bold"),textvariable=equation2) 
				amount_given1.place(x=50,y=170,width=130)
				amount_returned=Label(self.root,text="AMOUNT RETURNED:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				amount_returned.place(x=270,y=135)
				amount_returned1=Entry(root,width=150,bg="Beige",fg='Black',font=("Consolas","13","bold"),textvariable=equation3) 
				amount_returned1.place(x=270,y=170,width=130)
				insert=Button(self.root,text="ADD PAYMENT",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=insert)
				insert.place(x=20,y=220,width=110)
				update=Button(self.root,text="UPDATE PAYMENT",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=update)
				update.place(x=185,y=220,width=140)
				delete=Button(self.root,text="DELETE PAYMENT",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=delete)
				delete.place(x=380,y=220,width=140)
				clear=Button(self.root,text="CLEAR",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=clears)
				clear.place(x=570,y=220,width=70)
				view=Button(self.root,text="VIEW ALL",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=view_command)
				view.place(x=142,y=260,width=90)
				payment_list = Listbox(self.root, height=11, width=30,selectmode=SINGLE,font=("Consolas","15","bold"), border=3,bg="black",fg="Beige")
				payment_list.place(x=20,y=300)
				payment_list.bind('<<ListboxSelect>>', get_selected_row)
				scrollbary = Scrollbar(self.root,orient='vertical')
				scrollbary.place(x=359,y=300,height=290)
				scrollbarx = Scrollbar(self.root,orient='horizontal')
				scrollbarx.place(x=20,y=573,width=339)
				payment_list.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
				scrollbary.configure(command=payment_list.yview)
				scrollbarx.configure(command=payment_list.xview)
				def view():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="cafe",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					z.execute("SELECT * FROM payment")
					rows=z.fetchall()
					con.close()
					return rows
				def press(num): 
					global expression
					expression = expression + str(num) 
					equation.set(expression) 
				def equalpress(): 
					try: 
						global expression 
						total = str(eval(expression)) 
						equation.set(total) 
						expression = "" 
					except: 
						equation.set(" error ") 
						expression = "" 
				def clear(): 
					global expression 
					expression = "" 
					equation.set("")
				cal_frame = Frame(self.root,bd=8, bg="black", relief=GROOVE)
				cal_frame.place(x=380,y=300,height=300,width=297)
				equation = StringVar()
				expression_field = Entry(cal_frame,textvariable=equation,bg='white',fg='black',font=("Consolas","15","bold")) 
				expression_field.place(x=0,y=0,width=280,height=40) 
				equation.set('ENTER YOUR EXPRESSION:')
				plus = Button(cal_frame, text=' + ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press("+")) 
				plus.place(x=0,y=40,height=50,width=70)
				minus = Button(cal_frame, text=' - ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press("-")) 
				minus.place(x=0,y=90,height=50,width=70)  
				multiply = Button(cal_frame, text=' * ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press("*"))  
				multiply.place(x=0,y=140,height=50,width=70)
				divide = Button(cal_frame, text=' / ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press("/")) 
				divide.place(x=0,y=190,height=50,width=70)
				button7 = Button(cal_frame, text=' 7 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(7)) 
				button7.place(x=70,y=40,height=50,width=70)
				button8 = Button(cal_frame, text=' 8 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(8)) 
				button8.place(x=140,y=40,height=50,width=70)
				button9 = Button(cal_frame, text=' 9 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(9)) 
				button9.place(x=210,y=40,height=50,width=70) 
				button4 = Button(cal_frame, text=' 4 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(4)) 
				button4.place(x=70,y=90,height=50,width=70) 
				button5 = Button(cal_frame, text=' 5 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(5)) 
				button5.place(x=140,y=90,height=50,width=70)  
				button6 = Button(cal_frame, text=' 6 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(6)) 
				button6.place(x=210,y=90,height=50,width=70)  
				button1 = Button(cal_frame, text=' 1 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(1)) 
				button1.place(x=70,y=140,height=50,width=70)
				button2 = Button(cal_frame, text=' 2 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(2)) 
				button2.place(x=140,y=140,height=50,width=70) 
				button3 = Button(cal_frame, text=' 3 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(3)) 
				button3.place(x=210,y=140,height=50,width=70) 
				Decimal= Button(cal_frame, text='.', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press('.')) 
				Decimal.place(x=70,y=190,height=50,width=70)
				button0 = Button(cal_frame, text=' 0 ', fg='white', bg='black', font=("Consolas","20","bold"),command=lambda: press(0)) 
				button0.place(x=140,y=190,height=50,width=70) 
				clear = Button(cal_frame, text='CLEAR', fg='white', bg='black', font=("Consolas","17","bold"),command=clear) 
				clear.place(x=210,y=190,height=50,width=70)
				equal = Button(cal_frame, text=' = ', fg='white', bg='black', font=("Consolas","20","bold"),command=equalpress) 
				equal.place(x=210,y=240,height=45,width=70)
		class order_class:
			def __init__(self, root):
				order_dict = {}
				def load_order():
					menu_tabel1.delete(*menu_tabel1.get_children())
					menu_tabel1.insert('',END,values=lis)
					update_total_price()
				def insert():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					order_id=orderid1.get()
					cust_id=custid1.get()
					item_name=name1.get()
					item_type=type1.get()
					item_price=price1.get()
					quantity=quantity1.get()
					if (order_id=="" or cust_id=="" or item_name=="" or item_type=="" or item_price=="" or quantity==""):
						msgbox.showinfo("order status","You need to enter all details")
					else:
						if con.is_connected()==False:
							con.connect()
						z.execute("create table if not exists order1(order_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,cust_id INT(20),item_name CHAR(50),item_type CHAR(50),item_price INT(20),quantity INT(10),CONSTRAINT cust_id FOREIGN KEY(cust_id) REFERENCES customers(cust_id)ON DELETE CASCADE ON UPDATE CASCADE)ENGINE=InnoDB")
						z.execute("insert into order1 values('"+order_id+"','"+cust_id+"','"+item_name+"','"+item_type+"','"+item_price+"','"+quantity+"')")
						z.execute("commit");
						msgbox.showinfo("insert order status","details inserted!!")
						con.close();
							
				def update():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					order_id=orderid1.get()
					cust_id=custid1.get()
					item_name=name1.get()
					item_type=type1.get()
					item_price=price1.get()
					quantity=quantity1.get()
					if (order_id=="" or cust_id=="" or item_name=="" or item_type=="" or item_price=="" or quantity==""):
						msgbox.showinfo("order status","You need to enter all details")
					else:
						if con.is_connected()==False:
							con.connect()
						z.execute(""" UPDATE order1 SET cust_id=%s,item_name=%s,item_type=%s,item_price=%s,quantity=%s WHERE order_id=%s """,(cust_id,item_name,item_type,item_price,quantity,order_id))
						z.execute("commit");
						msgbox.showinfo("update order status","details updated!!")
						con.close();
				def delete():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					order_id=orderid1.get()
					if (order_id==""):
						msgbox.showinfo("delete order status","please enter order id")
					else:
						if con.is_connected()==False:
							con.connect()
						if msgbox.askyesno("confirm delete?","are you sure you want to delete this item?"):	
							z.execute("DELETE FROM order1 WHERE order_id='%s' "%(order_id))
							z.execute("commit");
							msgbox.showinfo("delete order status","details deleted!!")
							con.close()
				def clear(): 
					global expression 
					expression = "" 
					equation1.set("")
					equation2.set("") 
					equation3.set("") 
					equation4.set("")
					equation5.set("")
					equation6.set("")
				def get_selected_row(event):
					try:
						global selected_tuple
						index = order_list.curselection()[0]
						selected_tuple = order_list.get(index)
						orderid1.delete(0, END)
						orderid1.insert(END, selected_tuple[0])
						name1.delete(0, END)
						name1.insert(END, selected_tuple[1])
						type1.delete(0, END)
						type1.insert(END, selected_tuple[2])
						price1.delete(0, END)
						price1.insert(END, selected_tuple[3])
						quantity1.delete(0, END)
						quantity1.insert(END, selected_tuple[4])
					except IndexError:
						pass
				def view_command():
					order_list.delete(0, END)
					order_list.insert(ACTIVE,"order customer name type price quantity")
					for row in view():
						order_list.insert(END, row)

				def load_item_from_menu(event):
					cursor_row = menu_tabel.focus()
					contents = menu_tabel.item(cursor_row)
					row = contents["values"]
					equation3.set(row[0])
					equation5.set(row[1])
					equation4.set(row[2])
					equation6.set("1")
				def load_item_from_order(event):
					cursor_row = menu_tabel1.focus()
					contents = menu_tabel1.item(cursor_row)
					row = contents["values"]
					equation3.set(row[0])
					equation5.set(row[1])
					equation6.set(row[2])

				self.root = root
				self.root.geometry("1000x645+0+0")
				root.title("order & bill")
				self.root["bg"] = "khaki3"
				self.root.resizable(False,False)
				root.iconbitmap(r'D:\\cafe\\images\\bill.ico')
				frames = Frame(self.root,bd=8, bg="khaki3", relief=GROOVE)
				frames.place(x=0,y=0,height=645,width=1000)
				order_frame = Frame(frames,bd=8, bg="khaki3", relief=GROOVE)
				order_frame.place(x=3,y=5,height=550,width=550)
				order_label = Label(order_frame, text="Enter Order Details Below",font=("times new roman", 16, "bold"),bg = "khaki3", fg="Black", pady=0)
				order_label.pack(side=TOP,fill="x")
				equation1 = StringVar()
				equation2 = StringVar()
				orderid=Label(order_frame,text="ORDER ID:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				orderid.place(x=30,y=35)
				orderid1=Entry(order_frame,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation1) 
				orderid1.place(x=30,y=70,width=130) 
				custid=Label(order_frame,text="CUSTOMER ID:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				custid.place(x=200,y=35)
				custid1=Entry(order_frame,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation2) 
				custid1.place(x=200,y=70,width=130)
				name=Label(order_frame,text="ITEM NAME:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				name.place(x=370,y=35)
				equation3 = StringVar()
				equation3.set("")
				name1=Entry(order_frame,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation3,state=DISABLED) 
				name1.place(x=370,y=70,width=130) 
				type=Label(order_frame,text="ITEM TYPE:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				type.place(x=30,y=115)
				equation4 = StringVar()
				equation4.set("")
				type1=Entry(order_frame,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation4,state=DISABLED) 
				type1.place(x=30,y=150,width=130) 
				price=Label(order_frame,text="ITEM PRICE:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				price.place(x=200,y=115)
				equation5 = StringVar()
				equation5.set("")
				price1=Entry(order_frame,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation5,state=DISABLED) 
				price1.place(x=200,y=150,width=130) 
				quantity=Label(order_frame,text="ITEM QUANTITY:",fg="Black",bg="khaki3",font=("Consolas","13","bold"))
				quantity.place(x=370,y=115)
				equation6 = StringVar()
				equation6.set("")
				quantity1=Entry(order_frame,width=150,bg="Beige",fg="Black",font=("Consolas","13","bold"),textvariable=equation6) 
				quantity1.place(x=370,y=150,width=130) 
				insertbtn=Button(order_frame,text="ADD ITEM",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=insert)
				insertbtn.place(x=30,y=200,width=115)
				updatebtn=Button(order_frame,text="UPDATE ITEM",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=update)
				updatebtn.place(x=150,y=200,width=150)
				deletebtn=Button(order_frame,text="DELETE ITEM",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=delete)
				deletebtn.place(x=305,y=200,width=150)
				clearbtn=Button(order_frame,text="CLEAR",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=clear)
				clearbtn.place(x=460,y=200,width=60)
				viewbtn=Button(order_frame,text="VIEW ALL",bg="Black",fg="Beige",font=("Consolas","13","bold"),command=view_command)
				viewbtn.place(x=400,y=370,width=90)
				order_list = Listbox(order_frame, height=11, width=30,selectmode=SINGLE,font=("Consolas","15","bold"), border=3,bg="black",fg="Beige")
				order_list.place(x=32,y=244)
				order_list.bind('<<ListboxSelect>>', get_selected_row)
				scrollbary = Scrollbar(order_frame,orient='vertical')
				scrollbary.place(x=371,y=244,height=289)
				scrollbarx = Scrollbar(order_frame,orient='horizontal')
				scrollbarx.place(x=32,y=517,width=338)
				order_list.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
				scrollbary.configure(command=order_list.yview)
				scrollbarx.configure(command=order_list.xview)
				def view():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="cafe",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					z.execute("SELECT * FROM order1")
					rows=z.fetchall()
					con.close()
					return rows
				def view_menu():
					con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="cafe",auth_plugin='mysql_native_password') 
					z=con.cursor(buffered=True)
					z.execute("CREATE DATABASE IF NOT EXISTS cafe")
					z.execute("use cafe")
					menu_tabel.set("")
					z.execute("""SELECT * FROM menu""")
					for row in z:
						menu_tabel.insert('','end',values=(row[1],row[3],row[2]))	
				heading=Button(frames,text="VIEW MENU",fg="Beige",bg="black",font=("Consolas","15","bold"),command=view_menu)
				heading.place(x=740,y=0)
				scrollbar_menu_x = Scrollbar(frames,orient=HORIZONTAL)
				scrollbar_menu_y = Scrollbar(frames,orient=VERTICAL)
				style = ttk.Style()
				style.configure("Treeview.Heading",font=("Consolas",12, "bold"))
				style.configure("Treeview",font=("Consolas",12,"bold"),rowheight=25)

				menu_tabel = ttk.Treeview(frames,style = "Treeview",columns =("name","price","type"),xscrollcommand=scrollbar_menu_x.set,yscrollcommand=scrollbar_menu_y.set)
				menu_tabel.heading("name",text="NAME")
				menu_tabel.heading("price",text="PRICE")
				menu_tabel.heading("type",text="TYPE")
				menu_tabel["displaycolumns"]=("name", "price","type")
				menu_tabel["show"] = "headings"
				menu_tabel.column("name",width=150)
				menu_tabel.column("price",width=100)
				scrollbar_menu_x.place(x=557,y=385,width=417)
				scrollbar_menu_y.place(x=957,y=35,height=349)
				scrollbar_menu_x.configure(command=menu_tabel.xview)
				scrollbar_menu_y.configure(command=menu_tabel.yview)
				menu_tabel.place(x=557,y=35,width=400,height=350)
				menu_tabel.insert('',END,values=["Black coffee","50","coffee"])
				menu_tabel.bind("<ButtonRelease-1>",load_item_from_menu)

				def bill():
					z=Toplevel(root)
					z.geometry("550x550+600+50")
					z.title("bill")
					z["bg"] = "khaki3"
					z.resizable(False,False)
				def cancel_order():
					z=Toplevel(root)
				'''billbtn=Button(frames,text="BILL",bg="Black",fg="Beige",font=("Consolas","15","bold"),command=bill)
				billbtn.place(x=800,y=580,width=150)'''
				total_price_label=Label(frames,text="TOTAL PRICE:",fg="Black",bg="khaki3",font=("Consolas","15","bold"))
				total_price_label.place(x=410,y=580)
				totalPrice = StringVar()
				totalPrice.set("")
				totalprice=Entry(frames,text="",bg="khaki3",fg="black",font=("Consolas","15","bold"),textvariable=totalPrice)
				totalprice.place(x=557,y=580,width=150)
				#cancelbtn=Button(frames,text="CANCEL ORDER",bg="Black",fg="Beige",font=("Consolas","15","bold"),command=cancel_order)
				#cancelbtn.place(x=150,y=570,width=150)

		class report_class:
			def __init__(self, root):
				self.root = root
				self.root.geometry("550x550+300+50")
				root.title("report")
				self.root["bg"] = "khaki3"
				self.root.resizable(False,False)
				root.iconbitmap(r'D:\\cafe\\images\\report.ico')
		def new_window(win_class):
			global win2
			try:
				if win2.state()=="normal":win2.focus()
			except NameError as e:
				print(e)
			win2=Toplevel(root)
			win_class(win2)
		def new_window1(win_class):
			global win2
			try:
				if win2.state()=="normal":win2.focus()
			except NameError as e:
				print(e)
			win2=Toplevel(self.root)
			win_class(win2)
		class registerpage:
			def __init__(self,root1):
				def r():
					fn=firstname_entry.get()
					ln=lastname_entry.get()
					u=username_entry1.get()
					p=pass_entry1.get()
					if (fn=="" and ln=="" and u=="" and p==""):
						msgbox.showinfo("Registration Status","You need to enter all details")
						return
					if (fn==""):
						msgbox.showinfo("Registration Status","You need to enter First Name")
						return
					if (ln==""):
						msgbox.showinfo("Registration Status","You need to enter Last Name")
						return
					if (u==""):
						msgbox.showinfo("Registration Status","You need to enter Username")
						return
					if (p==""):
						msgbox.showinfo("Registration Status","You need to enter Password")
						return
					elif not re.fullmatch(r'[A-Za-z]+',fn):
						msgbox.showinfo("Registration Status","First Name must contain only characters")
						return
					elif not re.fullmatch(r'[A-Za-z]+',ln):
						msgbox.showinfo("Registration Status","Last Name must contain only characters")
						return
					elif not re.fullmatch(r'[A-Za-z]+',u):
						msgbox.showinfo("Registration Status","Username must contain only characters")
						return
					elif not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}',p):
						msgbox.showinfo("Registration Status","Password must contain characters, numbers and should be at least 8 characters!")
						return
					else:
						con=mysql.connect(host ="localhost",user = "root",password ="zakanksha",db ="",auth_plugin='mysql_native_password') 
						z=con.cursor()
						z.execute("CREATE DATABASE IF NOT EXISTS cafe")
						z.execute("use cafe")
						if con.is_connected()==False:
							z.execute("CREATE DATABASE IF NOT EXISTS cafe")
							z.execute("use cafe")
							con.connect()
						z.execute("create table if not exists user(firstname CHAR(20),lastname CHAR(20),user CHAR(20),password VARCHAR(20))")
						z.execute("insert into user values('"+fn+"','"+ln+"','"+u+"','"+p+"')")
						z.execute("commit");
						msgbox.showinfo("Registration status","Registration Successfully Done")
						con.close();
				root.iconify()
				root1.title("REGISTRATION PAGE")
				root1["bg"] = "khaki3"
				root1.geometry("500x500+100+100")
				root1.resizable(False,False)
				root1.iconbitmap(r'D:\\cafe\\images\\cutecup.ico')
				label = Label(root1, text="Enter Details To Register",font=("times new roman", 20, "bold"),bg = "khaki3", fg="black", pady=0)
				label.place(x=100,y=10)
				firstname_label = Label(root1, text="Enter Firstname:",font=("times new roman", 20, "bold"),bg = "khaki3", fg="Black", pady=0)
				firstname_label.place(x=30,y=80)
				firstname_entry=Entry(root1,text="",font=("times new roman", 20, "bold"),bg="khaki3",fg="black")
				firstname_entry.place(x=250,y=80,width=190)
				lastname_label = Label(root1, text="Enter Lastname:",font=("times new roman", 20, "bold"),bg = "khaki3", fg="Black", pady=0)
				lastname_label.place(x=30,y=150)
				lastname_entry=Entry(root1,text="",font=("times new roman", 20, "bold"),bg="khaki3",fg="black")
				lastname_entry.place(x=250,y=150,width=190)
				username_label1 = Label(root1, text="Enter Username:",font=("times new roman", 20, "bold"),bg = "khaki3", fg="black", pady=0)
				username_label1.place(x=30,y=220)
				username_entry1=Entry(root1,text="",font=("times new roman", 20, "bold"),bg="khaki3",fg="black")
				username_entry1.place(x=250,y=220,width=190)
				pass_label1 = Label(root1, text="Enter Password:",font=("times new roman", 20, "bold"),bg = "khaki3", fg="black", pady=0)
				pass_label1.place(x=30,y=290)
				pass_entry1=Entry(root1,text="",font=("times new roman", 20, "bold"),bg="khaki3",fg="black")
				pass_entry1.place(x=250,y=290,width=190)
				register_button1 = Button(root1, text="REGISTER",width=26,fg="khaki3",bg="black",font=("Consolas","16","bold"),command=r)
				register_button1.place(x=70,y=360)
				exitbutton = Button(root1, text="exit",width=20,fg="khaki3",bg="black",font=("Consolas","10","bold"))
				exitbutton.place(x=70,y=440)
				exitbutton['command']=lambda:new_window1(cafe)
		self.root=root
		root.title("CAFE LOGIN")
		root["bg"] = "khaki3"
		self.root.geometry("1250x635+7+7")
		self.root.resizable(False,False)
		icon=PhotoImage(file="D:\\cafe\\images\\feuser.png")
		root.iconphoto(False,icon)
		C = Canvas(root, height = 700, width = 700,bg="khaki3") 
		imageFile = Image.open("D:\\cafe\\images\\coffee3.png")
		imageFile = ImageTk.PhotoImage(imageFile)
		C.image = imageFile
		C.create_image(350, 350, anchor=CENTER, image=imageFile, tags="bg_img")
		C.place(x=0,y=0)
		lbl=Label(root,text="THE  LIGHTNING  CAFE",bg="khaki3",fg="black",font=("times new roman", 60, "bold"))
		lbl.place(x=200,y=0)
		login_frame = Frame(self.root,bd=8, bg="khaki3", relief=GROOVE)
		login_frame.place(x=735,y=120,height=480,width=480)
		login_label = Label(login_frame, text="LOGIN HERE",font=("times new roman", 25, "bold"),bg = "black", fg="Beige", pady=0)
		login_label.pack(side=TOP,fill="x")
		username_label = Label(login_frame, text="Enter Username:",font=("times new roman", 20, "bold"),bg = "khaki3", fg="black", pady=0)
		username_label.place(x=30,y=120)
		username_entry=Entry(login_frame,text="",font=("times new roman", 20, "bold"),fg = "Beige",bg="black")
		username_entry.place(x=240,y=120,width=190)
		pass_label = Label(login_frame, text="Enter Password:",font=("times new roman", 20, "bold"),bg = "khaki3", fg="black", pady=0)
		pass_label.place(x=30,y=170)
		pass_entry=Entry(login_frame,text="",font=("times new roman", 20, "bold"),fg = "Beige",bg="black")
		pass_entry.place(x=240,y=170,width=190)
		login_button = Button(login_frame, text="LOGIN",width=17,fg="Beige",bg="black",font=("Consolas","20","bold"),command=login)
		login_button.place(x=100,y=230)
		register_button = Button(login_frame, text="NEW? REGISTER",width=21,fg="Beige",bg="black",font=("Consolas","16","bold"))
		register_button.place(x=100,y=300)
		register_button['command']=lambda:new_window(registerpage)
		exit_button = Button(login_frame, text="EXIT",width=15,fg="black",bg="Beige",font=("Consolas","10","bold"),command=self.kill)
		exit_button.place(x=340,y=430)
		def pop(message):
			root=Tk()
			root.title("welcome")
			root.geometry("530x50+250+150")
			root.resizable(False,False)
			m=message
			a=Label(root,text=m,fg="khaki3",bg="black",font=("Consolas","30","bold"))
			a.pack()
		pop("Welcome to the Cafeteria")
	def kill(self):
			self.root.destroy()
			exit(0)
root=Tk()
z=cafe(root)
root.mainloop()