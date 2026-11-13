from tkinter import*
r=Tk();e=Entry(r);e.grid(columnspan=4);s=''
def a(x):
 global s
 if x=='=':e.delete(0,END);e.insert(0,eval(s));s=''
 elif x=='C':s='';e.delete(0,END)
 else:s+=x;e.delete(0,END);e.insert(0,s)
for i,x in enumerate('789/456*123-0.+C='):Button(r,text=x,width=5,command=lambda x=x:a(x)).grid(row=i//4+1,column=i%4)
r.mainloop()
