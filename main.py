from flask import Flask, render_template, request, redirect, url_for
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<type>')
def crew_list(type):
    arr = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, ' \
          'специалист по радиационной защите, астрогеолог, ' \
          'гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода, киберинженер, ' \
          'штурман, пилот дронов'.split(', ')
    return render_template('crew_list.html', list=arr, type=type)


@app.route('/form', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        return redirect(url_for('answer'))


@app.route('/answer')
def answer():
    results = {
        'surname': 'Alina',
        'name': 'Alinova',
        'email': 'aaaa@gmail.com',
        'class': 'obychnoe',
        'sex': 'nonetype',
        'about': 'hihihahha',
        'accept': 'true'
    }
    return render_template('auto_answer.html', **results)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_form.html', title='Авторизация', form=form)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=age)

@app.route('/distribution')
def distribution():
    data = [
        'Джони Депп',
        'Леонардо Ди Каприо',
        'Бред Питт',
        'Кейт Уинслетт',
        'Том Круз'
    ]
    return render_template('distribution.html', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
