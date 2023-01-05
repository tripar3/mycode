#!/usr/bin/env python3
"""Script to demonstrate proficiency with the flask library.
    It is very simple program that asks you to record activities of a day.
    You can then print out the activity history"""

# Create table using sqlite3
import sqlite3
from flask import Flask, render_template, request

try:
    conn = sqlite3.connect('new.db')
    cur = conn.cursor()
    # Check if 'activity' table doesn't exist, create it
    cur.execute('''SELECT count(name) from sqlite_master WHERE type = 'table' AND name = 'activity' ''')

    if cur.fetchone()[0]==1:
        print('Activity table already exists')
    else:
        conn.execute("""CREATE TABLE activity
                     (NAMES TEXT NOT NULL,
                      DATES TEXT NOT NULL,
                      STEPS TEXT NOT NULL,
                      CALORIES TEXT NOT NULL);""")
        print("Activity table created successfully to record data")
        conn.close()
except:
    print("Failed to create activities table")


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
# function to take values from user and insert to 'activity' table
    info = []
    if request.method == 'POST' and 'name' in request.form:
        name = request.form.get('name')             # Name of the person
        date = request.form.get('date')             # Date of activity
        steps = request.form.get('steps')           # Number of steps in a day
        calories = request.form.get('calories')     # Number of calories burned in a day
        for i in (name,date,steps,calories):
            info.append(i)
    try:
        with sqlite3.connect("new.db") as con:
            cur = con.cursor()

            # Populate the table with information from the form activity.tracker.html
            cur.execute("INSERT INTO activity VALUES(?,?,?,?)", info)
            # Commit the transaction
            con.commit()
        msg = "Record successfully added"

    except:
        con.rollback()
        msg = "Insert failed"
    finally:
        return render_template('activity_tracker.html', msg=msg)

@app.route('/activity_history')
def history():
# function to display the activity records
    with sqlite3.connect('new.db') as con:
        cur = con.cursor()
    return render_template('activity_history.html', cur=cur)

app.run(debug=True)

