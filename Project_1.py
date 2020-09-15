#!/usr/bin/python
print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>Providers</title>")
print("</head>")
print("<body>")
 
import MySQLdb
import os
 
# Import modules for CGI handling 
import cgi, cgitb
 
def init():
    #read the query params
    params = os.environ.get('QUERY_STRING')
    findthis="="
 
    #find if there is an equal sign in the query param
    #use int to convert the variable to a number from a text value
    intEquals = int(params.find(findthis))
 
    #test for queryparam or first time you have arrived
    if intEquals > -1:
        #RECORD ALREADY EXISTS IN THE TABLE
        #slice notation like substr
        arg= params[3:]
        print ('show clicked record on form')
        print ('<br>')
        print ('<br>')
        sql = "SELECT * FROM tblProviders WHERE prv_id=" + arg
        print (sql)
        print ('<br>')
        print ('<br>')
        showtable()
        
    else:
        #CREATE THE NEW RECORD
 
        #get the field values
        
        form = cgi.FieldStorage() 
 
        # Get data from fields
        if form.getvalue('fname'):
           fname = form.getvalue('fname')
        else:
           fname = "Not set"
 
        if form.getvalue('city'):
           city = form.getvalue('city')
        else:
           city = "Not set"
           
        '''
        # Get data from fields
        fname = form.getvalue('fname')
        city = form.getvalue('city')
 
        print 'fname = ' + fname + '<br>'
        print 'city = ' + city + '<br>'
        '''
        #insert the contents of the form into the table
 
        print ("<h2>Enter New Provider:</h2>")
 
        print ('<strong>fname</strong> = ' + fname + '<br>')
        print ('<strong>city</strong> = ' + city + '<br>')
        
        print ("<form action = 'providers_add_form_values.py' method = 'post'>")
        
        print ("<table width='100%' border='0px' bgcolor=lightgreen>")
 
        print ("<tr>")
        print ("<td><strong>First Name:</strong></td>")        
        print ("<td><input type = 'text' name = 'fname' value='" + fname + "'></td>")
        print ("</tr>")
        print ("<tr>")
        print ("<td><strong>City:</strong></td>")    
        print ("<td><input type = 'text' name = 'city' value='" + city + "'></td>")
        print ("</tr>")
        print ("<tr>")
        print ("<td><input type = 'submit' value = 'Submit' /></td>")
        print ("</tr>")
        print ("</table>")
        print ("</form>")
 
        
        showtable()
        
def showtable():
    
    conn = MySQLdb.connect('localhost', 'username','pwd', 'erikloeb_med')
 
    cursor = conn.cursor()
 
    sql="SELECT * FROM tblProviders"
 
    cursor.execute(sql)
 
    # Get the number of rows in the result set
    numrows = cursor.rowcount
 
    print ("<table width='100%' border='1px'>")
    print ("<th>ID</th><th>First Name</th><th>City</th>")
    # Get and display all the rows
    for row in cursor:
 
        id = row[0]
        
        print ('<tr>')
        print ('<td>')
        print ("<a href='providers_add_form_values.py?id=" + str(id) + "'>" + str(id) + "</a>") #need to convert the index to a string
        print ('</td>')
        print ('<td>' + row[1] + '</td>')
        print ('<td>' + row[2] + '</td>')
        print ('</tr>')
    
    print ('</table>')
 
    # Close the connection
    conn.close()
    
#start here:
init()
 
 
print ("</body>")
print ("</html>")
