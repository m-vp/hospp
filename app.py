from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    global inputs
    
    if request.method == 'POST':
        
        ip1 = request.form.get('username', '')
        ip2 = request.form.get('password', '')
    
        
        if  (ip1 == 'admin') and (ip2 == 'admin'):
                
                
                return render_template('dboard.html')
        else:
            return render_template('login.html', error="Invalid username or password.")

    return render_template('login.html')

@app.route('/dss')
def ind():
    return render_template('ds.html')

@app.route('/finale')
def indexx():
    user_agent = request.headers.get('User-Agent')
    if user_agent != 'pentabrowser':
        return '<body> Only pentabrowser is allowed </body>' 

    referer = request.headers.get('Referer')
    if referer not in {'http://localhost/',"http://localhost","127.0.0.1"}:
        return 'Access denied. You are not coming from our server.' 

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for != '169.172.18.9':
        return 'Access denied. Please use a proxy, your ip should originate from 169.172.18.9' 
    else:
        return 'affric{H3ad3rs_4r3_4w3s0m3!}' 



if __name__ == '__main__':
    app.run(debug=False)
