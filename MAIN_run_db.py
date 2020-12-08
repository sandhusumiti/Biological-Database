#!/usr/local/Python-3.7/bin/python
# BF 768: Project
# group H
import pymysql
import sys
import cgi
import math
import matplotlib.pyplot as plt
# import mysql.connector
import operator
import cgitb

cgitb.enable()

# define mysql users and password
# --

# Get product list
# query = "SELECT id, name FROM Product;"
# cursor.execute(query)
# rows=cursor.fetchall()

# start the html output
print("""Content-type: text/html\n""")
print("""
<html>
<head>


<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://bioed.bu.edu/students_20/groupH/style.css">

</head>
<body>

<h2>Tabs</h2>
<p>Click on the buttons inside the tabbed menu:</p>

<div class="tab">
  <button class="tablinks" id="home_butt" onclick="openCity(event, 'Home')">Home</button>
  <button class="tablinks" onclick="openCity(event, 'About')">About</button>
  <button class="tablinks" onclick="openCity(event, 'Help')">Help</button>
</div>


<script src="https://code.jquery.com/jquery-3.4.1.js"></script>
<script src="https://bioed.bu.edu/students_20/groupH/table2CSV.js"></script>

<script>

function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
 $(document).ready(function(){             
    document.getElementById("home_butt").click();
});

</script>


""")

#####          need on document load to call the tab fcn
#####          something to direct to the tab i want after the search

# HTML code
print("""
<div id="Home" class="tabcontent">
  <h3>Home</h3>
  <p>This is the home page. Here you can query</p>

<head>
<title>Gene expression in REELER mice brains</title> """)
print("""
         </head>""")
# CSS template haven't done this part, can add later


# Begin body
# print(""" <body> """)

# Form
print("""
<hr/> 
<h1 class="header" style="text-align: left; font-family:verdana;">
<span style="background-color: #4485b8; color: black; padding: 0 5px;">
Search Genes</span></h1> <hr/>
<p>
<form name="Gene search form" class="form-wrapper" action="https://bioed.bu.edu/cgi-bin/students_20/groupH/MAIN_run_db.py" method="post"> 
""")

print("""<strong>Search by:</strong></br>""")

# Gene name
print (""" <!-- gene_name as text -->
<strong>Gene symbol:</strong>
	<input type="text" class="gene" name="gene" placeholder="Cxcl10">
<br /> """)

# ProbeSet ID
print(""" <!-- pid as text -->
<strong>ProbeSet ID:</strong> 
    <input type="text" class="pid" name="pid" placeholder="1418929_at">
<br /> """)

# Foldchange
# TODO: add min and max
print(""" <!-- Foldchange as text -->
<strong>OR search by other criteria:</strong><br />
<table style="height: 178px; width: 417px;">
<tbody>
<tr style="height: 9px;">
<td style="width: 325.2px; height: 9px;"><strong>
Fold Change:</strong></td>
<td style="width: 166.8px; height: 9px;">
    <input type="text" class="Foldchange" name="Foldchange" placeholder="1"/></td></tr>
<br /> """)

# Signal_
print(""" <!-- Signal_ as text -->
<tr style="height: 18px;">
<td style="width: 325.2px; height: 18px;"><strong>
Signal:</strong></td>
<td style="width: 166.8px; height: 18px;">
    <input type="text" class="Signal_" name="Signal_" placeholder="100">
</td>
</tr>
<br /> """)

# Detection
print(""" <!-- Detection as text -->
<tr style="height: 11px;">
<td style="width: 325.2px; height: 11px;"><strong>Detection:</strong></td>
<td style="width: 166.8px; height: 11px;">
<select name="Detection">
<option value="None">None</option>
　<option value="P">P</option>
　<option value="A">A</option>
  <option value="M">M</option>
</select></td></tr>
<br /> """)

# Change_direction
print(""" <!-- Change_direction as text -->
<tr style="height: 11px;">
<td style="width: 325.2px; height: 11px;"><strong>
Change Direction:</strong></td>
<td style="width: 166.8px; height: 11px;">
<select name="Direction">
<option value="None">None</option>
　<option value="NC">NC</option>
　<option value="I">I</option>
  <option value="D">D</option>
</select></td>
</tr>
<br /> """)

# Table name (different genetic variants)
print(""" <!-- tablename as text -->
<tr style="height: 21.2px;">
<td style="width: 325.2px; height: 21.2px;"><strong>
Select Variants:</strong></td><br />
<td style="width: 166.8px; height: 21.2px;">

<input type="checkbox" id="WT" name="WT" value="WT" checked> WT <br />
  <input type="checkbox" id="VLDLR" name="VLDLR" value="VLDLR"> VLDLR <br />
  <input type="checkbox" id="ApoER2" name="ApoER2" value="ApoER2"> ApoER2 <br />
  <input type="checkbox" id="Dabl" name="Dabl" value="Dabl"> Dabl <br />
  <input type="checkbox" id="ApoE_VLDLR" name="ApoE_VLDLR" value="ApoE_VLDLR"> ApoE_VLDLR <br />
  <input type="checkbox" id="Reln" name="Reln" value="Reln"> Reln <br />

</td>
</tr>
</tbody>
</table>
<br /> """)

# Submit button
print(""" <!-- Submit Button-->
<p style="text-align: left; padding-left: 3px;">  
<input type="submit" value="Go" class="submit"> </p>
<br /> """)

form = cgi.FieldStorage()
# the query is based on the table's name
#tablename = form.getvalue("tablename")
#pid = str(form.getvalue("pid"))
#gene = str(form.getvalue("gene"))

connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
cursor = connection.cursor()
# =============================================================================

print('''
<h2>List</h2>
<table id="order" style="border:3px #FFD382 dashed;" cellpadding="10" border='1'>
        <tr>
	<th> Variant </th>
        <th> Probe_set_ID </th>
        <th> Gene_symbol </th>
        <th> Foldchange </th>
        <th> Signal </th>
        <th> Detection </th>
        <th> Change_direction </th>
	<th> Process_ID </th>
	<th> Biological_process </th>
        </tr>''')

# Get form data
if form:
	#checkbox
	WT = str(form.getvalue("WT"))
	VLDLR = str(form.getvalue("VLDLR"))
	ApoER2 = str(form.getvalue("ApoER2"))
	Dabl = str(form.getvalue("Dabl"))
	ApoE_VLDLR = str(form.getvalue("ApoE_VLDLR"))
	Reln = str(form.getvalue("Reln"))
	print(WT)
	# rest
	pid = str(form.getvalue("pid"))
	gene = str(form.getvalue("gene"))
	Signal_ = str(form.getvalue("Signal_"))
	Detection = str(form.getvalue("Detection"))
	Foldchange = str(form.getvalue("Foldchange"))
	Direction = str(form.getvalue("Direction"))
	
	# Select clause
	form_query = "SELECT Probe_Set_ID, Gene_Symbol, Foldchange, Signal_, Detection, Change_direction, Process_ID, Process_name "
	# From clause
	form_query += "FROM Biological_process JOIN Gene USING (Probe_Set_ID) "
	# Variant queries
	all_q = {}
	wt_q = ""
	if WT!="None":
		wt_q = form_query + "JOIN WT USING (Probe_Set_ID) "
		all_q[WT]=wt_q
	vl_q = ""
	if VLDLR!="None":
		vl_q = form_query + "JOIN VLDLR USING (Probe_Set_ID) "
		all_q[VLDLR]=vl_q
	ap_q = ""
	if ApoER2!="None":
		ap_q = form_query + "JOIN ApoER2 USING (Probe_Set_ID) "
		all_q[ApoER2]=ap_q
	ap_vl_q = ""
	if ApoE_VLDLR!="None":
		ap_vl_q = form_query + "JOIN ApoE_VLDLR USING (Probe_Set_ID) "
		all_q[ApoE_VLDLR]=ap_vl_q
	rl_q = ""
	if Reln!="None":
		rl_q = form_query + "JOIN Reln USING (Probe_Set_ID) "
		all_q[Reln]=rl_q
	da_q = ""
	if Dabl!="None":
		da_q = form_query + "JOIN Dabl USING (Probe_Set_ID) "
		all_q[Dabl]=da_q

	# Values for query
	vals = []
	
	# Loop through queries
	for nm,q in all_q.items():
		# check that variant chosen
		if q != "":
			# add where
			q += "WHERE "
			
			# Add conditions based on form input
			if pid != "None":
				q += "Probe_Set_ID=%s AND  "
				if pid not in vals:
					vals.append(pid)
			if gene != "None":
				q += "Gene_Symbol=%s AND  "
				if gene not in vals:
					vals.append(gene)
			if Foldchange != "None":
				q += "Foldchange>=%s AND  "
				if Foldchange not in vals:
					vals.append(Foldchange)
			if Signal_ != "None":
				q += "Signal_>=%s AND  "
				if Signal_ not in vals:
					vals.append(Signal_)
			if Detection != "None":
				q += "Detection=%s AND  "
				if Detection not in vals:
					vals.append(Detection)
			if Direction != "None":
				q += "Change_direction=%s AND  "
				if Direction not in vals:
					vals.append(Direction)
			
			# Clean query
			q = q[:-6]
			q += "ORDER BY Foldchange DESC LIMIT 20;"
			print(q, vals)
			vals = tuple(vals)
			cursor.execute(q, vals)
			records = cursor.fetchall()
			
			# Frequency of each Biological_process in query
			bp = {}

			exp ={}

			# iterate through results
			for row in records:
				##genes and FC in query
				exp[row[1]] = row[2]
				# count frequency of Biological_process
				if row[6] not in bp:
					bp[row[6]] = [row[7],1]
				else:
					bp[row[6]][1] += 1
				# make table
				def mousedbresults():
					mousedbsearch = '''<tr>
					<td> %s </td>
					<td> %s </td>
					<td> %s </td>
					<td> %s </td>
					<td> %s </td>
					<td> %s </td>
					<td> %s </td>
					<td> %s </td>
					<td> %s </td>
					</tr>''' % (nm,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
					print(mousedbsearch)
				mousedbresults()
			# taken from https: // github.com / OmbraDiFenice / table2csv / blob / master / src / table2csv.js
			print("""<button type='button' id='button'>Download Mouse Data</button> """)

			# print('''<tr>
				# 	<td> %s </td>
				# 	<td> %s </td>
				# 	<td> %s </td>
				# 	<td> %s </td>
				# 	<td> %s </td>
				# 	<td> %s </td>
				# 	<td> %s </td>
				# 	<td> %s </td>
				# 	<td> %s </td>
				# 	</tr>''' % (nm,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

			#TODO: Remove last 2 columns of table and display bp info only in graph
			#TODO:  plot 5 top Biological_processes associated with dataset
			
			# Create plots for variant
			fig, (bp_fig, fig_exp) = plt.subplots(2)
			fig.subplots_adjust(hspace=1)
			fig.suptitle(nm, fontweight='bold')
			
			# Plot 1: Top 10 Biological processes 
			newbp = dict(sorted(bp.items(), key=operator.itemgetter(1), reverse=True)[:10])
			
			# bp_labels
			bp_labels =list(newbp.values())
			bp_labels=[item[0] for item in bp_labels]
			# bp_values
			bp_values =list(newbp.values())
			bp_values = [item[1] for item in bp_values]
			# generate plot 1
			bp_fig.bar(bp_labels,bp_values)
			bp_fig.set_xticklabels(bp_labels, rotation='vertical')
			bp_fig.set_title('Biological_process')
			#bp_fig.set_ylabel('Frequency')
			#TO DO: Sort position of plot or labels so that labels are completely visible
			
			# Plot 2: Top 20 genes according to FC
			new_exp = dict(sorted(exp.items(), key=operator.itemgetter(1), reverse=True)[:20])
			genes_exp = list(new_exp.keys())
			FC_exp = list(new_exp.values())
			fig_exp.bar(genes_exp, FC_exp, color='orange')
			y_upp = math.ceil(float(max(FC_exp))/5)*5
			fig_exp.set_ylim(0,y_upp)
			fig_exp.set_title("Fold_change")
			
			# save and show img
			img_file = '/var/www/html/students_20/groupH/img/'+nm+'.png'
			plt.savefig(img_file)
			#print("<img src="+plt.show()+">")
			src_loc = "https://bioed.bu.edu/students_20/groupH/img/"+nm+".png"
			print("<img id='plots' src="+src_loc+" />")
			
			#TO DO: Sort out why two plot results are merging??
			# issue: can't use matplotlib.pyplot with this python3.7 version

	cursor.close()
	connection.close()

print("</table></p>")

# =============================================================================
# CSV file
# =============================================================================

print("""

    <script type="text/javascript">
    $(document).ready(function(){
        $('#button').on('click', function(){
            $('#order').table2csv({
                filename:'reelermousetable.csv'
            });
        });
    });
    </script>


    """)

# # =============================================================================

# =============================================================================

# end Home tab
#
# =============================================================================
# # About tab
# print("""
# </div>
# <div id="About" class="tabcontent">
#   <h3>About</h3>
#   <p>This is the about page.</p>
#
# </div>
#
#
#
# """)
# =============================================================================
# Help tab
# print("""
# <div id="Help" class="tabcontent">
#   <h1>Key</h1>
#   <hr>
#   <hr>
#   <p>
#
#
#   <b>Gene symbol:</b>
#   This is the short name of your gene of interest.										</br></br>
#   short name = Xpo7																		</br>
#   long name = exportin 7																</br> </br>
#   <hr>
#
#  </br>
#  <b>ProbeSet ID:</b>
#  This is the unique ID from the Affymetrix ID.											</br></br>
#  Note: One gene may be associated with several ProbeSet ID's.							</br></br>
#   		If using this search, the ProbeSet ID must be an exact match					</br></br>
#   <hr>
#
#  </br>
#  <b>Fold Change:</b>
#   This is the ratio of the variant signal compared to the wt signal.					</br> </br>
#   Search by a fold change of at least 1.5 for significant results.						</br>
#   To search by negative fold change see "Change Direction".								</br> </br>
#   <hr>
#
#   </br>
#   <b>Signal:</b>
#   A signal is high or "intense" if the gene you are targeting is prevalent. 			</br> </br>
#   The data is negligible if the signal is below 100.									</br> </br>
#
#   <hr>
#
#   </br>
#   <b>Detection:</b>																		</br> </br>
#   P = Prevalent																			</br>
#   A = 																					</br>
#   M = Marginal																			</br> </br>
#   <hr>
#
#   </br>
#   <b>Change Direction:</b>																</br> </br>
#   NC = No Change																		</br>
#   I = Increased			- select this to see a positive fold change						</br>
#   D = Decreased			- select this to see a negative fold change						</br> </br>
#   <hr>
#
#   </br>
#   <b>Select variants:</b>
#
#   </br> </br>
#
#   </br>
#
#
#
#
#
#
#
#   </p>
# </div>
#
#
# </body>
# </html>
# """)
