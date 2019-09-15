from tkinter import *
import backend

def view_command():
    result_listbox.delete(0,END)
    for row in backend.view():
        result_listbox.insert(END,row)
def add_command():
    result_listbox.delete(0,END)
    backend.add(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    result_listbox.insert(END,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def search_command():
    result_listbox.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        result_listbox.insert(END,row)

def get_selected_row(event):
    index=result_listbox.curselection()
    print(index)

def delete_command():
    return



window=Tk()
window.geometry("800x300+900+400")
window.title("BookStore")

title_label=Label(window,text="Title")
title_label.grid(row=0,column=0)
title_text=StringVar()
title_entry=Entry(window,textvariable=title_text)
title_entry.grid(row=0,column=1)

author_label=Label(window,text="Author")
author_label.grid(row=0,column=2)
author_text=StringVar()
author_entry=Entry(window,textvariable=author_text)
author_entry.grid(row=0,column=3)

year_label=Label(window,text="Year")
year_label.grid(row=1,column=0)
year_text=StringVar()
year_entry=Entry(window,textvariable=year_text)
year_entry.grid(row=1,column=1)


isbn_label=Label(window,text="ISBN")
isbn_label.grid(row=1,column=2)
isbn_text=StringVar()
isbn_entry=Entry(window,textvariable=isbn_text)
isbn_entry.grid(row=1,column=3)


result_listbox=Listbox(window,width=30)
result_listbox.grid(row=3,column=0,rowspan=7,columnspan=2)
scrol=Scrollbar(window)
scrol.grid(row=3,column=2,rowspan=7)
result_listbox.configure(yscrollcommand=scrol.set)
scrol.configure(command=result_listbox.yview)

result_listbox.bind("<<Listbox>>",get_selected_row)

####Buttons

addAll_btn=Button(window,text="Add All",height=1,width=12,command=add_command)
addAll_btn.grid(row=2,column=3)

viewAll_btn=Button(window,text="View All",height=1,width=12,command=view_command)
viewAll_btn.grid(row=3,column=3)


search_btn=Button(window,text="Search",height=1,width=12,command=search_command)
search_btn.grid(row=4,column=3)

update_btn=Button(window,text="Update",height=1,width=12)
update_btn.grid(row=5,column=3)

delete_btn=Button(window,text="Delete",height=1,width=12,command=delete_command)
delete_btn.grid(row=6,column=3)

close_btn=Button(window,text="Close",height=1,width=12)
close_btn.grid(row=7,column=3)


window.mainloop()
