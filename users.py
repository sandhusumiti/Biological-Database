#!/usr/local/Python-3.7/bin/python
import pymysql
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()
if form:
        connection = pymysql.connect(host="bioed.bu.edu", user="wyueh", password="wyueh", db="groupH", port=4253)
        cursor = connection.cursor()
        submit = form.getvalue("submit")
        if submit:
                print('Content-type: text/html\n')
                name = form.getvalue("name")
                email = form.getvalue("email")
                message = form.getvalue("message")
                if name and email and message:
                        insert = '''insert into Users(username,email,message)   
                                    values("%s","%s","%s");''' % (name,email,message)
                        cursor.execute(insert)
                        connection.commit()
                cursor.close()
                connection.close()
else:
        print('Content-type: text/html\n')
        
        
        
        
        
