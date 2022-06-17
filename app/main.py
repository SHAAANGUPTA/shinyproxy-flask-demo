from flask import Flask, render_template, request

app = Flask(__name__,
            template_folder='/opt/app/templates',
            static_folder='/opt/app/static')

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/about')
def about():
    full_path= request.full_path  
    origin= request.origin
    referrer= request.referrer
    base_url= request
    endpoint= request.endpoint
    print("full_path==",full_path)
    print("origin==",origin)
    print("referrer==",referrer)
    print("request==",request)
    print("endpoint", endpoint)
    return render_template('about.html',full_path= full_path , origin= origin, referrer= referrer ,endpoint=endpoint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("8050"), debug=True) 