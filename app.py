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
from flask import Flask, render_template


app = Flask(__name__)


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
    """Enter a new ticket via a form."""
    return 'enter_ticket'


@app.route('/ticket/<int:ticket_id>')
def display_ticket(ticket_id):
    """Display the details of the ticket with id *ticket_id*."""
    return 'display_ticket({ticket_id})'.format(ticket_id=ticket_id)


if __name__ == '__main__':
    app.run(debug=True)
