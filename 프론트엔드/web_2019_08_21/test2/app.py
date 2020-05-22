from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('map.html')


@app.route('/map2')
def optimal_location():
    return render_template('map2.html')


if __name__ == '__main__':
    app.run()
