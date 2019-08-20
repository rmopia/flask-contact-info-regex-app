from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, validators


class ContactForm(FlaskForm):
    full_name = StringField("Name", [validators.DataRequired("Please enter your name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email."),
                                  validators.Email("Please enter your email.")])
    subject = StringField("Subject")
    message = TextAreaField("Message", [validators.DataRequired("Please enter a message.")])
    submit = SubmitField("Send")
