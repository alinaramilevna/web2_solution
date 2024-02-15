from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
