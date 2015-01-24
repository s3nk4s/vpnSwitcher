import urllib2
import geoip2.database

reader = geoip2.database.Reader('./geoIP/GeoLite2-City.mmdb')

ip = urllib2.urlopen('http://icanhazip.com').read()
ip = ip.rstrip()

georesp = reader.city(ip)

print 'iso code: ' + georesp.country.iso_code
print 'country: ' + georesp.country.name
print 'city: ' + georesp.city.name
