
# python –m http.server --cgi 8080
# http://localhost:8080/cgi-bin/ex_cgi.py
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First MYSERVER Program</title>')
print ('</head>')
print ('<body>')
print ("<h1>ex_cgi</h1>")
print ('<h2>Hello World! This is my first MYSERVER program</h2>')
print ('</body>')
print ('</html>')