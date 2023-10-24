from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("dark")
def buttonp_event():
    num=float(entry.get())
    ans=float(num/100)
    entry.delete(0,END)
    entry.insert(0,ans)
def buttonc_event():
    entry.delete(0,END)
def buttonb_event():
    num=float(entry.get())
    ans=10**num
    entry.delete(0,END)
    entry.insert(0,ans)
def buttondel_event():
    length=len(str(entry.get()))-1
    entry.delete(length)
def buttoninv_event():
    num=float(entry.get())
    ans=float(1/num)
    entry.delete(0,END)
    entry.insert(0,ans)
def buttonsq_event():
    num=float(entry.get())
    ans=num**2
    entry.delete(0,END)
    entry.insert(0,ans)
def buttonsr_event():
    num=float(entry.get())
    ans=float(num**0.5)
    entry.delete(0,END)
    entry.insert(0,ans)
def button9_event():
    num=entry.get()
    ans=num+"9"
    entry.delete(0,END)
    entry.insert(0,ans)
def button8_event():
    num=entry.get()
    ans=num+"8"
    entry.delete(0,END)
    entry.insert(0,ans)
def button7_event():
    num=entry.get()
    ans=num+"7"
    entry.delete(0,END)
    entry.insert(0,ans)
def button6_event():
    num=entry.get()
    ans=num+"6"
    entry.delete(0,END)
    entry.insert(0,ans)
def button5_event():
    num=entry.get()
    ans=num+"5"
    entry.delete(0,END)
    entry.insert(0,ans)
def button4_event():
    num=entry.get()
    ans=num+"4"
    entry.delete(0,END)
    entry.insert(0,ans)
def button3_event():
    num=entry.get()
    ans=num+"3"
    entry.delete(0,END)
    entry.insert(0,ans)
def button2_event():
    num=entry.get()
    ans=num+"2"
    entry.delete(0,END)
    entry.insert(0,ans)    
def button1_event():
    num=entry.get()
    ans=num+"1"
    entry.delete(0,END)
    entry.insert(0,ans)    
def button0_event():
    num=entry.get()
    ans=num+"0"
    entry.delete(0,END)
    entry.insert(0,ans)    
def buttondiv_event():
    f_num=entry.get()
    global first
    first=float(f_num)
    global math
    math="division"
    entry.delete(0,END)
def buttonmul_event():
    f_num=entry.get()
    global first
    first=float(f_num)
    global math
    math="multiplication"
    entry.delete(0,END)
def buttonplus_event():
    f_num=entry.get()
    global first
    first=float(f_num)
    global math
    math="addition"
    entry.delete(0,END)
def buttonmin_event():
    f_num=entry.get()
    global first
    first=float(f_num)
    global math
    math="subtraction"
    entry.delete(0,END)
def buttonpm_event():
    num=entry.get()
    if num[0] != "-" :
        ans="-"+num
    else :
        ans=num[1:]
    entry.delete(0,END)
    entry.insert(0,ans)    
def buttondot_event():
    num=entry.get()
    ans=num+"."
    entry.delete(0,END)
    entry.insert(0,ans) 
def buttoneq_event():
    s_num=entry.get()
    entry.delete(0,END)
    if math=="addition" :
        entry.insert(0,first+float(s_num))
    elif math=="subtraction" :
        entry.insert(0,first-float(s_num))
    elif math=="multiplication" :
        entry.insert(0,first*float(s_num))
    elif math=="division" :
        entry.insert(0,first/float(s_num))
    
root=customtkinter.CTk()
root.geometry("380x422")
root.resizable(False,False)
root.title("Calculator")
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=0)
entry = customtkinter.CTkEntry(master=root,placeholder_text=0,width=375,height=90,border_width=2,corner_radius=10,text_color="white",
                               fg_color="transparent",font=('times new roman',70,'bold'))
entry.grid(row=1,column=0,rowspan=2,columnspan=4,padx=1,pady=1)
buttonp = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="%",command=buttonp_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonp.grid(row=3,column=0,columnspan=1,padx=2,pady=2,rowspan=1)
buttonc = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="C",command=buttonc_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonc.grid(row=3,column=1,padx=2,pady=2,columnspan=1,rowspan=1)
buttonb = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="10ˣ",command=buttonb_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonb.grid(row=3,column=2,padx=2,pady=2,columnspan=1,rowspan=1)
buttondel = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="DEL",command=buttondel_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttondel.grid(row=3,column=3,padx=2,pady=2,columnspan=1,rowspan=1)
buttoninv = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="1/x",command=buttoninv_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttoninv.grid(row=4,column=0,columnspan=1,padx=2,pady=2,rowspan=1)
buttonsq = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="x²",command=buttonsq_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonsq.grid(row=4,column=1,padx=2,pady=2,columnspan=1,rowspan=1)
buttonsr = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="√x",command=buttonsr_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonsr.grid(row=4,column=2,padx=2,pady=2,columnspan=1,rowspan=1)
buttondiv = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="÷",command=buttondiv_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttondiv.grid(row=4,column=3,padx=2,pady=2,columnspan=1,rowspan=1)
button7 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="7",command=button7_event,fg_color="transparent",font=('times new roman',25,'bold'))
button7.grid(row=5,column=0,columnspan=1,padx=2,pady=2,rowspan=1)
button8 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="8",command=button8_event,fg_color="transparent",font=('times new roman',25,'bold'))
button8.grid(row=5,column=1,padx=2,pady=2,columnspan=1,rowspan=1)
button9 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="9",command=button9_event,fg_color="transparent",font=('times new roman',25,'bold'))
button9.grid(row=5,column=2,padx=2,pady=2,columnspan=1,rowspan=1)
buttonmul = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="x",command=buttonmul_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonmul.grid(row=5,column=3,padx=2,pady=2,columnspan=1,rowspan=1)
button4 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="4",command=button4_event,fg_color="transparent",font=('times new roman',25,'bold'))
button4.grid(row=6,column=0,columnspan=1,padx=2,pady=2,rowspan=1)
button5 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="5",command=button5_event,fg_color="transparent",font=('times new roman',25,'bold'))
button5.grid(row=6,column=1,padx=2,pady=2,columnspan=1,rowspan=1)
button6 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="6",command=button6_event,fg_color="transparent",font=('times new roman',25,'bold'))
button6.grid(row=6,column=2,padx=2,pady=2,columnspan=1,rowspan=1)
buttonmin = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="-",command=buttonmin_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonmin.grid(row=6,column=3,padx=2,pady=2,columnspan=1,rowspan=1)
button1 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="1",command=button1_event,fg_color="transparent",font=('times new roman',25,'bold'))
button1.grid(row=7,column=0,columnspan=1,padx=2,pady=2,rowspan=1)
button2 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="2",command=button2_event,fg_color="transparent",font=('times new roman',25,'bold'))
button2.grid(row=7,column=1,padx=2,pady=2,columnspan=1,rowspan=1)
button3 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="3",command=button3_event,fg_color="transparent",font=('times new roman',25,'bold'))
button3.grid(row=7,column=2,padx=2,pady=2,columnspan=1,rowspan=1)
buttonplus = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="+",command=buttonplus_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonplus.grid(row=7,column=3,padx=2,pady=2,columnspan=1,rowspan=1)
buttonpm = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="+/-",command=buttonpm_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttonpm.grid(row=8,column=0,columnspan=1,padx=2,pady=2,rowspan=1)
button0 = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="0",command=button0_event,fg_color="transparent",font=('times new roman',25,'bold'))
button0.grid(row=8,column=1,padx=2,pady=2,columnspan=1,rowspan=1)
buttondot = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text=".",command=buttondot_event,fg_color="transparent",font=('times new roman',25,'bold'))
buttondot.grid(row=8,column=2,padx=2,pady=2,columnspan=1,rowspan=1)
buttoneq = customtkinter.CTkButton(master=root,width=90,height=50,border_width=2,corner_radius=8,text="=",text_color="black",command=buttoneq_event,fg_color="light blue",font=('times new roman',25,'bold'))
buttoneq.grid(row=8,column=3,padx=2,pady=2,columnspan=1,rowspan=1)
root.mainloop()
