from flask import Flask, render_template, request

app = Flask(__name__,
            template_folder='/opt/app/templates',
            static_folder='/opt/app/static')

@app.route('/')
def home(): 
    base_url= request.base_url
    print("url==",base_url)
    return render_template('home.html', base_url=base_url)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("8050"), debug=True) 