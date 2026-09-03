from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField, IntegerField, BooleanField
from generator import generate_password

app = Flask(__name__)
app.secret_key = "qwerty123"
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)
class GeneratorForm(FlaskForm):
    password_length = IntegerField("Длина пароля")
    use_special_symbols = BooleanField("Использовать спец. символы")
    ignore_similar_symbols = BooleanField("Не использовать похожие символы")
    submit = SubmitField("Отправить")


@app.route("/", methods = ["GET", "POST"])
def generator():
    password = None
    form = GeneratorForm()
    if form.validate_on_submit():
        password = generate_password(form.password_length.data, form.use_special_symbols.data, form.ignore_similar_symbols.data)
    # else:
    #     print("jkjkll")
    #     password = 123
    return render_template("index.html", form_template=form, password=password)

@app.route("/user/<userid>")
def user(userid):
    return f"{userid}"



