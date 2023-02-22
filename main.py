from hidden import db_connection
from tkinter import messagebox
from tkinter import *
import tkinter
import re
import psycopg2  #type: ignore

BLUE = "#03b1d6"
FONT_NAME = "Courier"

# connect to the db
db_connection = db_connection()

conn = psycopg2.connect( database=  db_connection["database"],
                         host = db_connection["host"],
                         user = db_connection["user"],
                        password=db_connection["password"],
                        port=db_connection["port"])


cursor = conn.cursor()



# function to validate the emails
def check_email(email):
    '''Check the email address and return the email address if everything is correct otherwise return an error'''
    try:
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror(
            title="Error email", message="Invalid Email Address"
        )
    else:
        return email    
        
        


# check the name
def check_name(name):
    '''check and return the user name with min 2 char otherwise return an error'''
    try:
        if not name or len(name) < 2:
            raise ValueError
        for _ in name:
            if not _.isalpha():
                raise ValueError
            else:
                return name.capitalize()    
    except ValueError:
        tkinter.messagebox.showerror(
            title="Error name", message="Invalid Username"
        )
    


# db Create a table and add information into the table 
def database(name,email):
        '''This function creates a table and insert the user information into the database if something went wrong will give an error'''
        try:
            cursor.execute('CREATE EXTENSION  IF NOT EXISTS "uuid-ossp";')
            cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id uuid default uuid_generate_v4() PRIMARY KEY, user_name text not null ,email text not null , registration_date TIMESTAMPTZ default now());')
            cursor.execute('INSERT INTO users (user_name,email) VALUES (%s, %s);',(name,email),)
            conn.commit()
        except Exception as e:
            tkinter.messagebox.showerror(
            title="Error", message=f"Something went wrong {e}"
        )
        
        else:
            tkinter.messagebox.showinfo(title="Saved", message="Thank you to use our service" )



# check function will be called by the confirmation button from tkinter , once user click on confirmation , check function will call all the other function to check the name the email and save info into db
def check():
    ''' The function collect the user input and use check_name() and check_email()  and if everything is fine after the user confirmation call the function database() '''
    name_user = name_input.get()
    email_user = email_input.get()
    name_checked =  check_name(name_user)
    email_checked = check_email(email_user)

    x = {"name": name_checked, "email": email_checked}

    for value in x.values():
        if not value:
            return False
        
    yes = tkinter.messagebox.askquestion(title="Confirmation", message="Do you want to confirm your data ?", )
    if yes == "yes":
        database(name_checked,email_checked)





# delete function will be called by tkinter delete button and will delete user info from db
def delete():
    '''Allows the user to delete the user information from the database'''

    #get the input from the Entry tkinter delete_input
    email_to_delete =  delete_input.get()
    if email_to_delete_checked := check_email(email_to_delete):
        cursor.execute("SELECT  EMAIL FROM users WHERE email = %s LIMIT 1",(email_to_delete_checked,))
        #fetchone returns a single result form the query 
        if em := cursor.fetchone():
            try:
                y = tkinter.messagebox.askquestion(title="Confirmation", message="Are you sure, no more Joke in the morning :(?", )
                if y == "yes":
                    cursor.execute('DELETE  FROM users WHERE email = %s;', (email_to_delete_checked,))
                    conn.commit()
                    tkinter.messagebox.showinfo(title="Canceled", message="Thank you to use our service, Your date has been canceled" )
            except Exception as e:
                tkinter.messagebox.showerror(title="Error", message=f"Something went wrong {e}" )
        else:
            tkinter.messagebox.showerror(
                title="Error", message="Your email is not in our System"
            )





# Initialize Tk
window = Tk()
window.title("Morning_Jokes")
window.geometry("500x400")
window.configure(bg=BLUE)


#Welcome to the user
title_label = Label(text="Welcome to Morning_Jokes ☺",font = ( FONT_NAME,20, "bold"),highlightthickness=0,bg=BLUE)
title_label.pack()

#Description of the program
description = Label(text="Everyday at 8:00 Am You will get a joke to start your day\n\n",font = ( FONT_NAME,10, "bold"),highlightthickness=0,bg=BLUE)
description.pack()

#Label to ask the email 
email = Label(text="Type here Your email",highlightthickness=0,bg=BLUE)
email.pack()
#Field to type the email address
email_input = Entry(window, width=40)
email_input.focus_set()
email_input.pack()

# Label to ask the name
name = Label(text="Your Name",highlightthickness=0,bg=BLUE)
name.pack()
#field to type the name 
name_input = Entry(window, width=40)
name_input.pack()

#button to call the function check 
confirmation = Button(text="Okay", highlightthickness=0,bg=BLUE,command=check)
confirmation.pack()


#label and ENtry space to delete  data from the system
delete_date = Label(text="\n\n\n\nEnter your email if you want to stop the service and delete your data from the database",highlightthickness=0,bg=BLUE)
delete_date.pack()
delete_input = Entry(window, width=40)
delete_input.pack() 


#button to click to delete the date from the database
delete_button = Button(text="Delete", highlightthickness=0,bg=BLUE,command=delete)
delete_button.pack()



window.mainloop()


cursor.close()
