from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Invalid email Address")])
    password = PasswordField(label='Password', validators=[DataRequired(message="Field must be atleast 8 characters long")])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "tah-secret-key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)