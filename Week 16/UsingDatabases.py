# Contacts Program Using a Database
# Author: Thomas Preston

from tkinter import *
import sqlite3
import os.path

# Create Tkinter Window
root = Tk()
root.title('Contacts')
root.geometry("500x450")

# Create Database if it doesn't already exist
if not os.path.isfile('database.db'):
    conn = sqlite3.connect('database.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE contacts (
            first_name text,
            last_name text,
            contact text
            )""")

# Delete Contact
def delete():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE oid = " + delete_entry.get())
    conn.commit()
    conn.close()
    delete_entry.delete(0, END)

# Add Contact
def submit():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts VALUES (:f_name, :l_name, :contact)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'contact': contact_number.get(),
            })

    conn.commit()
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    contact_number.delete(0, END)
    
# Query Database for Contacts
def query():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM contacts")
    db = c.fetchall()
    print_oid = print_fname = print_lname = print_contact = ''

    key1 = Label(root, text = "Id:")
    key2 = Label(root, text = "First Name:")
    key3 = Label(root, text = "Last Name:")
    key4 = Label(root, text = "Mobile Number:")
    key1.grid(row = 6, column = 0)
    key2.grid(row = 6, column = 1)
    key3.grid(row = 6, column = 2)
    key4.grid(row = 6, column = 3)

    for data in db:
        print_oid += str(data[3]) + "\n"
        print_fname += str(data[0]) + "\n"
        print_lname += str(data[1]) + "\n"
        print_contact += str(data[2]) + "\n"

    query_label_oid = Label(root, text = print_oid)
    query_label_oid.grid(row = 7, column = 0)

    query_label_fname = Label(root, text = print_fname)
    query_label_fname.grid(row = 7, column = 1)

    query_label_lname = Label(root, text = print_lname)
    query_label_lname.grid(row = 7, column = 2)

    query_label_contact = Label(root, text = print_contact)
    query_label_contact.grid(row = 7, column = 3)

    conn.commit()
    conn.close()

# Entry Fields for Adding New Contact
f_name = Entry(root, width = 60)
f_name.grid(row = 0, column = 1, columnspan = 3, pady = (10, 0))
l_name = Entry(root, width = 60)
l_name.grid(row = 1, column = 1, columnspan = 3)
contact_number = Entry(root, width = 60)
contact_number.grid(row = 2, column = 1, columnspan = 3)

# Labels For Entry Fields
f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0, pady = (10, 0))
l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)
contact_number_label = Label(root, text = "Mobile Number")
contact_number_label.grid(row = 2, column = 0)

# Submit Button
submit_btn = Button(root, text = "Add Contact", command = submit)
submit_btn.grid(row = 3, column = 0, columnspan = 4, padx = 10, pady = 10, ipadx = 192)

# Search Database Button
query_button = Button(root, text = "Show Contacts", command = query)
query_button.grid(row = 4, column = 0, columnspan = 4, padx = 10, pady = 10, ipadx = 187)

# Delete Contact Button and Entry Field
delete_button = Button(root, text = "Delete ID", command = delete)
delete_button.grid(row = 5, column = 3, padx = 10, pady = 10, ipadx = 20)

delete_entry = Entry(root, width = 55)
delete_entry.grid(row = 5, column = 0, columnspan = 3, padx = 10)

# Tkinter Window
root.mainloop()