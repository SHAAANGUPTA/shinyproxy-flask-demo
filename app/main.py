from flask import Flask, render_template, request

app = Flask(__name__,
            template_folder='/opt/app/templates',
            static_folder='/opt/app/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    print(url_for('shaan'))
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("8050"), debug=True) 