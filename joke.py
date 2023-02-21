import requests  # type: ignore
import psycopg2  # type: ignore
from hidden import db_connection
import smtplib


db_connection = db_connection()

conn = psycopg2.connect(
    database=db_connection["database"],
    host=db_connection["host"],
    user=db_connection["user"],
    password=db_connection["password"],
    port=db_connection["port"],
)

cursor = conn.cursor()


def funny_joke():
    '''return a string representing the random jokes from the API  https://official-joke-api.appspot.com/random_joke'''
    joke_request = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_json = joke_request.json()
    return f'{joke_json["setup"]} {joke_json["punchline"]}'


# Assign to the var the email and the password (app password) README file for more information

# test_email = ""
# test_password = ""


cursor.execute("SELECT email, user_name FROM users")
list_of_email = cursor.fetchall()
conn.commit()

with smtplib.SMTP("smtp.gmail.com",587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_password)

        for i in list_of_email:
            connection.sendmail(
                from_addr=test_email,
                to_addrs=i[0],
                msg=f"Subject:Funny Jokes\n\nHi {i[1]} :)\nWhat up today ? \nHere a funny joke to start your Day :)) \n\n{funny_joke()}",
            )




conn.close()
