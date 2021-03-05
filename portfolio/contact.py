from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flask_mail import Message

from portfolio.db import get_db
from portfolio import mail

bp = Blueprint('contact', __name__)


@bp.route('/')
def index():
    return render_template('contact/index.html')


@bp.route('/contactme', methods=['POST'])
def contactme():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        details = request.form['details']

        db = get_db()
        db.execute(
            'INSERT INTO Contacts'
            ' (firstName, lastName, email, phone, company, details)'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (first_name, last_name, email, phone, company, details)
        )
        msg = Message('Contact Info Received',
                      sender='michael@michaelkistler.net',
                      recipients=['michael@michaelkistler.net'])
        msg.body = f'''Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Company: {company}
Details: {details}
'''
        mail.send(msg)
        db.commit()

    return redirect(url_for('contact.index', _anchor='contact'))
