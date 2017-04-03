from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    name = request.args.get('name', None)
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
