from flask import Flask
from flask import request
from flask import render_template
import json
#  форма для обратной сзвязи
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()

    return render_template("index.html",
                           title="index page",
                           form=form)


@app.route('/send', methods=['POST'])
def send():
    form = ContactForm()
    if request.method == "POST":
        if form.validate_on_submit():
            #  отправить почту, записать в БД и т. д.
            return json.dumps({'success': 'true', 'msg': 'Ждите звонка!'})
        else:
            #  обработать ошибку
            return json.dumps({'success': 'false', 'msg': 'Ошибка на сервере!'})

if __name__ == '__main__':
    app.run(debug=True)
