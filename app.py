"""
sqlite> .dump
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Ticket (id INT PRIMARY KEY,
change TEXT NOT NULL,
title TEXT NOT NULL,
description TEXT NOT_NULL,
submitter_name TEXT NOT NULL,
submitter_email TEXT NOT NULL,
submitter_website TEXT NOT NULL,
file TEXT NOT NULL,
date_created DATE NOT NULL);
COMMIT;
"""

import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
INSERT_STATEMENT = """INSERT INTO Ticket VALUES ({id}, "{change}", "{title}", "{description}", "{submitter_name}", "{submitter_email}", "{submitter_website}","{file}", "{date_created}")"""


@app.route('/', methods=['GET'])
def list_tickets():
    """Display a list of tickets in the system."""
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Ticket')
    all_tickets = cursor.fetchall()
    return render_template('index.html', tickets=all_tickets)


@app.route('/ticket', methods=['GET', 'POST'])
def enter_ticket():
    if request.method == 'GET':
        return render_template('edit.html')
    else:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute(INSERT_STATEMENT.format(
            id=request.form.get('id'),
            change=request.form.get('change'),
            title=request.form.get('title'),
            description=request.form.get('description'),
            submitter_name=request.form.get('submitter_name'),
            submitter_email=request.form.get('submitter_email'),
            submitter_website=request.form.get('submitter_website'),
            file=request.form.get('file'),
            date_created=request.form.get('date_created')
        ))
        connection.commit()
        return redirect(url_for('list_tickets'))


@app.route('/ticket/<int:ticket_id>')
def display_ticket(ticket_id):
    """Display the details of the ticket with id *ticket_id*."""
    return 'display_ticket({ticket_id})'.format(ticket_id=ticket_id)


if __name__ == '__main__':
    app.run(debug=True)
