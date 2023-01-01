from flask import Flask ,
render_template, redirect, url_for,
request
import sqlite3
import os

app = Flask(__name__)

def createDatabase():
    conn = sqlite3.connect("carrentDB.db")
    cur = conn.execute("""
                       CREATE TABLE IF NOT EXISTS CUSTOMER_DETAILES(
                         DLNumber INTEGER,
                         NAME TEXT,
                         PHONE_NUMBER INTEGER,
                         EMAIL_ID TEXT,
                         UNIQUE (DLNUMBER),
                         PRIMARY KEY(DLNUMBER)
                       );
                       """)
    cur = conn.execute("""
                       CREATE TABLE IF NOT EXISTS CAR(
                        REGISTRATIONNO INTEGER,
                        MODEL_NAME TEXT,
                        MILEAGE INTEGER,
                        COSTPERDAY INTEGER,
                        UNIQUE (REGISTRATIONNO)
                        PRIMARY KEY(REGISTRATIONO)
                        );
                       """)
    cur = conn.execute("""
                       CREATE TABLE IF NOT EXISTS BOOKING_DETAILS(
                        PICKUP_LOC TEXT,
                        DROP_LOC TEXT,
                        FROMDATE INTEGER,
                        RETURN DATE INTEGER,
                        DLNUM INTEGER,
                        FOREIGN KEY(DLNUM) REFERENCES CUSTOMER_DETAILS(DLNUMBER) 
                       );
                       """)
    
if __name__ == "__main__":
    if not os.path.exists("carrentDB.db"):
        createDatabase()
    app.run(debug==True)
    
    