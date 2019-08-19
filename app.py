from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '2090cdcebc9658f5eefd810a80096273'


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
    text_area = request.form['text']
    if text_area is '':
        flash('The text box below is empty! Please fill it in.')
        return redirect(url_for('home'))
    else:
        phone_nums = regex_find_phone_num(text_area)
        emails = regex_find_email(text_area)
        return render_template('results.html', phone_nums=phone_nums, emails=emails, title='Results')


def regex_find_phone_num(text_block):
    result = []
    phone_regex = re.compile(r'(((\(\d\d\d\))|(\d\d\d))?(\s|-)(\d\d\d)(-)(\d\d\d\d))')
    result_phone = phone_regex.findall(text_block)
    for item in result_phone:
        result.append(item[0].strip(' '))
    return result


def regex_find_email(text_block):
    email_regex = re.compile(r'[a-zA-Z0-9._+"-]+@[a-zA-Z0-9]+\.[a-zA-Z]+')
    result_email = email_regex.findall(text_block)
    return result_email


if __name__ == '__main__':
    app.run(debug=True)
