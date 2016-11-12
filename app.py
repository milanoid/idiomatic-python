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

from flask import Flask

app = Flask(__name__)

app.add_url_rule()


@app.route('/', methods=['GET'])
def list_tickets():
    """Display a list of tickets in the system."""


@app.route('/ticket', methods=['GET', 'POST'])
def enter_ticket():
    """Enter a new ticket via a form."""


@app.route('/ticket/<ticket_id>')
def display_ticket(ticket_id):
    """Display the details of the ticket with id *ticket_id*."""