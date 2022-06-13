from flask import Flask, render_template

app = Flask(__name__,
            template_folder='/opt/app/templates',
            static_folder='/opt/app/static')

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/heartbeat')
def heartbeat():
    return True

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("8050"), debug=True) 