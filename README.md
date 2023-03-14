# MORNING_JOKES :sunny: 

<a href="https://www.linkedin.com/in/giuseppe-bonifati-738640261/"><img src="https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue"></a> 

### Description

The program will send an email with a random Joke to the user, every morning at 8:00 AM.



## Installation 🧊 

<img src="https://img.shields.io/badge/-Python-white?logo=python">

In order to run the program please follow the instructions 🏁:

### Files
We need to create 3 different files 

:black_small_square: **joke.py**      (Allows us to ask to the users to enter the data and save it in the database)

:black_small_square: **main.py**    (Will send an email with a random Joke to the users using smtplib and an api)
 
:black_small_square: **hidden.py**  (Containt the information about the database)

:heavy_exclamation_mark: IMPORTANT : Create a database connection in the file hidden with all info about the db , we will need this info in the main.py and joke.py

```python 

def db_connection():
    return {"database":"",
                        "host":"",
                        "user":"",
                        "password":"",
                        "port":""}

```
### Api

**Link to the api** https://official-joke-api.appspot.com/random_joke

### Email

Before to lunch the program we need to create an email ( the sender )

https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail

```python

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
smtp.mail.yahoo.com    

```
Then it is important to follow this example with gmail, steps by step to configure your email address


🔹**1.** _In Your gmail Webpage, after the login, on the top right of the screen click on the icon and then Manage your Google Account_

<p align="center">
<img width="287" alt="image" src="https://user-images.githubusercontent.com/110894389/220471922-99ea43d0-2599-4683-bd78-dd34bdd764c8.png">
</p>


🔹**2.** _Click on the Security/Safety_

<p align="center">
<img width="324" alt="image" src="https://user-images.githubusercontent.com/110894389/220472134-20f8508d-15d4-443f-a765-c7183b8a1252.png">
</p>

🔹**3.** _Enable two step verification and follow the instructions from gmail_

<p align="center">
<img width="340" alt="image" src="https://user-images.githubusercontent.com/110894389/220472533-b788ed6e-f74d-49a3-9a31-42922e03e765.png">
</p>


🔹**4.** _Then go back on Security/Safety and click on Add password_

<p align="center">
<img width="370" alt="image" src="https://user-images.githubusercontent.com/110894389/220472859-735c8fe5-a7b2-4ed1-8d59-bfab94f712e0.png">
</p>

🔹**5.** _After you add the password click on Select app and chose "Other" , type a name and click on Generate_


🔹**6.** _Copy the generated password and paste it into file joke.py in  test_password = ""_



### Python everywhere

To run the program everyday at 8:00, we need to run the program in the _could_ , in this case in **python everywhere** .

So in python everywhere add the file in the could , then start a new bash console and then schedule the task to be executed at the time that you want in this case at 8:00 AM



## GUI ▪️▫️  

The Graphical User Interface ( GUI ) will look like this:

<p align="center">
<img width="373" alt="image" src="https://user-images.githubusercontent.com/110894389/220474249-997b0c1e-7dd1-407b-95b2-4c518786213f.png">
</p>


## License

<a href=https://github.com/Giuseppe-Bonifati/Morning_Jokes/blob/main/LICENSE.md><img src="https://img.shields.io/badge/license-MIT-blue"></a>
