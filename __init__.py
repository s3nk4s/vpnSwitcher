from flask import Flask, render_template, session, redirect, url_for, escape, request, jsonify
from os import listdir
import subprocess
import ConfigParser
import urllib2
import geoip2.database

app = Flask(__name__)
app.debug = True
Config = ConfigParser.ConfigParser()
Config.read("config.ini")
OVPNFLDER = Config.get('config','ovpnFolder')

def getCountry():

    reader = geoip2.database.Reader('./geoIP/GeoLite2-City.mmdb')

    ip = urllib2.urlopen('http://icanhazip.com').read()
    ip = ip.rstrip()

    georesp = reader.city(ip)
    
    return georesp.country.name

def getovpnFiles():
	ovpnFiles = []
	pia = OVPNFLDER
	files = listdir(pia)
	for file in files:
		if file[-4:] == 'ovpn':
			ovpnFiles.append(file)
	return ovpnFiles
	
@app.route('/')
def homepage():
    country = getCountry()
    ovpnFiles = getovpnFiles()
    return render_template("index.html", ovpnFiles=ovpnFiles, country=country)
    
if __name__ == "__main__":
	app.run(host='0.0.0.0')
