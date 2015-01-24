from flask import Flask, render_template, session, redirect, url_for, escape, request, jsonify
from os import listdir
import subprocess
import ConfigParser

app = Flask(__name__)
app.debug = True
Config = ConfigParser.ConfigParser()
Config.read("config.ini")
OVPNFLDER = Config.get('config','ovpnFolder')

def getovpnFiles():
	ovpnFiles = []
	pia = OVPNFLDER
	files = listdir(pia)
	for file in files:
		if file[-4:] == 'ovpn':
			ovpnFiles.append(file)
	return ovpnFiles
	
@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
	#do post stuff
	for f in request.form:
	    print f
	return "posted stuff"
    title = 'Private Internet Access Files:'
    files = getovpnFiles()
    return render_template("index.html",title=title, paragraph=files)
	
@app.route('/test')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
    
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
