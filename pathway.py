#!/usr/local/Python-3.7/bin/python
#!/Users/wyueh/anaconda/bin/python
import pymysql
import sys
import cgi

import operator
import cgitb

cgitb.enable()

# set the content type to html
print("Content-type: text/html\n")

print("""
<!DOCTYPE HTML>
<html>

<head>
<title>Search database</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=windows-1252" />
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" type="text/css" href="https://bioed.bu.edu/students_20/groupH/style/style.css" />
  <script src="https://code.jquery.com/jquery-3.4.1.js"></script>
  <script src="https://bioed.bu.edu/students_20/groupH/table2CSV.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

</head>

<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <div id="logo_text">
          <!-- class="logo_colour", allows you to change the colour of the text -->
          <h1><a href="https://bioed.bu.edu/students_20/groupH/indexdata.html">Gene expression in <span class="logo_colour">REELER mice brains</span></a></h1>

        </div>
      </div>
      <div id="menubar">
        <ul id="menu">
          <!-- put class="selected" in the li tag for the selected page - to highlight which page you're on -->
          <li ><a href="https://bioed.bu.edu/students_20/groupH/indexdata.html">Home</a></li>
            
          <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupH/about.py">About</a></li>

          <li><a href="https://bioed.bu.edu/students_20/groupH/help.html">Help</a></li>
          
          <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupH/search.py">Search</a></li>

          <li class="selected"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupH/pathway.py">Pathway</a></li>

          <li><a href="https://bioed.bu.edu/students_20/groupH/contact.html">Contact Us</a></li>
        </ul>
      </div>
    </div>
    <div id="site_content">
      <div class="sidebar">
        <h1>Latest News</h1>
        <h4>New Website Launched</h4>
        <h5>April 27, 2020</h5>
        <p> Take a look around and let us know what you think.<br /></p>
        <h1>Useful Database Links</h1>
        <ul>
          <li><a href="https://www.thermofisher.com/us/en/home/life-science/microarray-analysis/affymetrix.html" target="_blank">Affymatrix</a></li>
          <li><a href="https://www.ncbi.nlm.nih.gov/" target="_blank">NCBI</a></li>
          <li><a href="http://geneontology.org/" target="_blank">GeneOntology</a></li>
          <li><a href="https://www.genome.jp/kegg/pathway.html" target="_blank">KEGG Pathway</a></li>
        </ul>
      </div>
    """)

# Form
print("""
<hr/> 
<h1 class="header" style="text-align: left; font-family:verdana;">
<span style="background-color: #4485b8; color: black; padding: 0 5px;">
Search Pathways</span></h1> <hr/>
<p>
<form name="pathway search form" class="form-wrapper" action="https://bioed.bu.edu/cgi-bin/students_20/groupH/pathway.py" method="post"> 
""")

# Pathway name
print (""" <!-- pathway as text -->
<strong>Pathway: </strong>
	<input type="text" class="pathway" id="pathway" name="pathway" placeholder="tRNA processing">
<br /> """)

# Submit button
print(""" <!-- Submit Button-->
<p style="text-align: left; padding-left: 3px;">  
<input type="submit" value="Go" class="submit"> </p>
<br /> """)

form = cgi.FieldStorage()

connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
cursor = connection.cursor()
# ============================================================================


print('''
<h2>List</h2>
<table class="sortable" id="order" style="border:3px #FFD382 dashed;" cellpadding="10" border='1'>
	<thead>
        <tr>
        <th> Gene Symbol </th>
        <th> Title </th>
        <th> Process name </th>
        </tr></thead>''')

# Get form data
if form:
    path = str(form.getvalue("pathway"))
    
    if path!="None":
        form_query = "SELECT Gene_Symbol, Title, Process_name from Gene  JOIN Biological_process USING (Probe_Set_ID) where Process_name regexp '%s';"%(path) 

        #print(form_query)
        cursor.execute(form_query)
        records = cursor.fetchall()
        
        for row in records:
        
            print('''<tr><td>%s</td><td>%s</td><td>%s</td></tr>''' % (row[0], row[1],row[2]))
        
        print("""<button type='button' id='button'>Download Pathway Table as csv</button>""")

        cursor.close()    
        connection.close()


        
print("</table>")


# CSV file
print("""

    <script type="text/javascript">
    $(document).ready(function(){
        $('#pathway').on('input', function(){
            $.ajax({
                url: 'https://bioed.bu.edu/cgi-bin/students_20/groupH/pathway_autofill.py',
                type: 'get',
                data: {'pathway': $("#pathway").val()},
                success: function(response){
                    $("#TesterDiv").empty();
                    var lines = response.trim().split(",");
                    lines.forEach(function(value){
                        $("#pathway").autocomplete({
                          source: lines
                        });
                    });
                }
            });
        });
        $('#button').on('click', function(){
            $('#order').table2csv({
                filename:'reelermousetable.csv'
            });
        });
    });
    </script>


""")

#Sort tables by clicking on column
print("""<script src="https://kryogenix.org/code/browser/sorttable/sorttable.js"></script>""")

print("""
    </div>
  </div>""")

print("""
  <footer>
      <p>2020 © BF-768@Boston University, All Rights Reserved.</p>
  </footer>
  <style>

      footer{
      padding: 10px 20px;
      background: #0D0301;
      color: white;
      }

  </style>
    </body>
</html>
</body></html>""")
