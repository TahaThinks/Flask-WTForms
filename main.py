from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Invalid email Address")])
    password = PasswordField(label='Password', validators=[DataRequired(message="Field must be atleast 8 characters long")])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "tah-secret-key"
correct_email = "admin@email.com"
correct_password = "123456789"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == correct_email and login_form.password.data == correct_password:
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)