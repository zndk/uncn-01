from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('thread.html', url='https://github.com/zndk/')

if __name__ == '__main__':
    app.run()
