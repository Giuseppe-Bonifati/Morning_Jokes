# MORNING_JOKES

The program will send an email with a random Joke to the user, every morning at 8:00 AM.



## Installation

In order to run the program please follow the instructions:

it is important to create a database connection in the file hidden 

```
def db_connection():
    return {"database":"",
                        "host":"",
                        "user":"",
                        "password":"",
                        "port":""}

```

then we need to create 2 different file 

**joke.py and main.py**

**main.py** allows us to ask the user to enter the dates and save them in the database.

**joke.py** will send an email with a random Joke to the user using """import smtplib""" and this api:

https://official-joke-api.appspot.com/random_joke

before to lunch the program we need to create an email ( the sender )

https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail

``` 
with smtplib.SMTP("smtp.gmail.com",587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_password)

SMTP host for different email addresses:


smtp.aol.com
smtp.mail.att.net
smtp.comcast.net
smtp.mail.me.com
smtp.gmail.com
smtp-mail.outlook.com
smtp.mail.yahoo.com    ```

then it is important to follow this example with gmail steps by step to configure your email address

1. On the top right of the screen click on the icon
image.png

and then Manage your Google Account

2. Click on the Security/Safety
image.png

3. Enable two step verification and follow the instructions from gmail
image.png

4. Then go back on Security/Safety and click on Add password
image.png

5. After you add the password click on Select app and chose "Other" , type a name and click on Generate.


6. Copy the generated password and paste it into fille joke.py in  test_password = ""




At the end to run the program everyday at 8:00 we run the program in the could  for ex in python everywhere or something similar . Add the file in the could , start a new bash console and then schedule the task to be executed at the time that you want in this case at 8:00 AM



##Usage

The Graphical User Interface  ( GUI ) will look like this:

image.png





