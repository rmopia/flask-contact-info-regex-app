from flask import Flask, render_template, request, redirect, url_for
from forms import UploadForm
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = # generate your own secret key


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
@app.route('/home', methods=['POST'])
def home_regex():
    text_block = request.form['text']
    contacts = regex_find(text_block)
    results = 'Results:<br/>' + '<br/>'.join(contacts)
    return results


def regex_find(text_block):
    result = ['Numbers:']
    phone_regex = re.compile(r'(((\(\d\d\d\))|(\d\d\d))?(\s|-)(\d\d\d)(-)(\d\d\d\d))')
    email_regex = re.compile(r'[a-zA-Z0-9._+"-]+@[a-zA-Z0-9]+\.[a-zA-Z]+')
    result_phone = phone_regex.findall(text_block)
    result_email = email_regex.findall(text_block)
    result_email.insert(0, 'Emails:')
    for item in result_phone:
        result.append(item[0].strip(' '))
    result = result + result_email
    return result


if __name__ == '__main__':
    app.run(debug=True)
