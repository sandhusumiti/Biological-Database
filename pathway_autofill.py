#!/usr/local/Python-3.7/bin/python
#!/Users/wyueh/anaconda/bin/python
import pymysql
import sys
import cgi
import operator
import cgitb
import mysql.connector

cgitb.enable()
form = cgi.FieldStorage()

print("Content-type: text/html\n")

if form:
    connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
    cursor = connection.cursor()


    path = str(form.getvalue("pathway"))
    autofill_query = "SELECT  distinct(Process_name) FROM Biological_process where Process_name regexp '" + path + "';"

    cursor.execute(autofill_query)
    rows = cursor.fetchall()

    for row in rows:
        print(row[0]+",")


