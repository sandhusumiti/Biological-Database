#!/usr/local/Python-3.7/bin/python
# BF 768: Project
# group H
import pymysql
import sys
import cgi
# import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
# import mysql.connector
import operator
import cgitb
import math
import numpy as np

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
  <link rel="stylesheet" type="text/css" href="https://bioed.bu.edu/students_20/groupH/style/style.css" />
  <script src="https://code.jquery.com/jquery-3.4.1.js"></script>
  <script src="https://bioed.bu.edu/students_20/groupH/table2CSV.js"></script>

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

          <li class="selected"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupH/search.py">Search</a></li>
          
          <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupH/pathway.py">Pathway</a></li>

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
# # =============================================================================
# # =============================================================================
# # =============S=T=A=R=T=====M=A=R=K=E=R======P=A=S=T=E========================
# # =============================================================================
# # =============================================================================

# Form
print("""
<hr/> 
<h1 class="header" style="text-align: left; font-family:verdana;">
<span style="background-color: #4485b8; color: black; padding: 0 5px;">
Search Genes</span></h1> <hr/>
<p>
<form name="Gene search form" class="form-wrapper" action="https://bioed.bu.edu/cgi-bin/students_20/groupH/search.py" method="post"> 
""")

#print("""<strong>Search by:</strong></br>""")


# Gene name
print (""" <!-- gene_name as text -->
<strong>Search by Gene: </strong>
	<input type="text" class="gene" name="gene" placeholder="Cxcl10"> """)
#<br /> """)

#print('''<br />''')

# Foldchange
# TODO: add min and max
print(""" <!-- Foldchange as text -->
<table style="height: 178px; width: 60%;">
<tbody>
<tr style="height: 9px;">
<td style="width: 25%; height: 9px;"><strong>Fold Change:</strong></td>
<td style="width: 35%; height: 9px;">
    <input type="number" class="Foldchange" name="Foldchange" placeholder="Enter a value of 1.5 to 1360.00" min="0" max="1360" step="0.01" style="width: 80%;"/></td></tr>
<br /> """)

# Signal_
print(""" <!-- Signal_ as text -->
<tr style="height: 18px;">
<td style="width: 325.2px; height: 18px;"><strong>
Signal:</strong></td>
<td style="width: 166.8px; height: 18px;">
    <input type="number" class="Signal_" name="Signal_" placeholder="Enter a value of 100 to 10820.0" min="0" max="10820" step="0.1" style="width:80%;"/>
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
　<option value="P">Prevalent</option>
　<option value="A">Absent</option>
  <option value="M">Marginal</option>
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
　<option value="NC">No Change</option>
　<option value="I">Increase</option>
  <option value="D">Decrease</option>
</select></td>
</tr>
<br /> """)

print('''<p><h4><b>OR search by any combination of the below Criteria:</b></h4></p><br />''')
print('''<b><i>*Please select <u>at least one</u> of the below variants to compare with WT:</i></b>''')

# Table name (different genetic variants)
print(""" <!-- tablename as text -->
<tr style="height: 21.2px;">
<td style="width: 325.2px; height: 21.2px;"><strong>
Select Variants:</strong></td><br />
<td style="width: 166.8px; height: 21.2px;">

<label class="tooltip">
  <input type="checkbox" id="VLDLR" name="VLDLR" value="VLDLR">
  <a href="https://bioed.bu.edu/students_20/groupH/help.html#variants" target="_blank"> VLDLR </a><br />
  <span class="tooltiptext">Click for info!</span></label> <br />
  <input type="checkbox" id="ApoER2" name="ApoER2" value="ApoER2"> 
  <a href="https://bioed.bu.edu/students_20/groupH/help.html#variants">ApoER2</a> <br />
  <input type="checkbox" id="Dabl" name="Dabl" value="Dabl"> 
  <a href="https://bioed.bu.edu/students_20/groupH/help.html#variants">Dabl </a><br />
  <input type="checkbox" id="ApoE_VLDLR" name="ApoE_VLDLR" value="ApoE_VLDLR"> 
  <a href="https://bioed.bu.edu/students_20/groupH/help.html#variants">ApoE_VLDLR </a><br />
  <input type="checkbox" id="Reln" name="Reln" value="Reln"> 
  <a href="https://bioed.bu.edu/students_20/groupH/help.html#variants">Reln</a> <br />
  <input type="checkbox" id="Combined" name="Combined" value="Combined"> 
  <a href="https://bioed.bu.edu/students_20/groupH/help.html#variants">Combined </a><br />
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
# tablename = form.getvalue("tablename")
# pid = str(form.getvalue("pid"))
# gene = str(form.getvalue("gene"))

connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
cursor = connection.cursor()
# =============================================================================

print('''
<h2>List</h2>
<table class="sortable" id="order" style="border:3px #FFD382 dashed; overflow: auto;" cellpadding="10" border='1'>
	<thead>
        <tr>
	<th> Variant </th>
        <th> ProbeSet_ID </th>
        <th style="width:10px;"> Symbol </th>
        <th style="width:20px;"> Gene </th>
        <th> Foldchange </th>
	<th> Direction </th>
        <th> Signal </th>
        <th> Detection </th>
	<th> Process_ID </th>
	<th> Biol_process </th>
        </tr></thead>''')

# Get form data
if form:
    # checkbox
    WT = "WT"              #str(form.getvalue("WT"))
    VLDLR = str(form.getvalue("VLDLR"))
    ApoER2 = str(form.getvalue("ApoER2"))
    Dabl = str(form.getvalue("Dabl"))
    ApoE_VLDLR = str(form.getvalue("ApoE_VLDLR"))
    Reln = str(form.getvalue("Reln"))
    Combined = str(form.getvalue("Combined"))
    # rest
    #pid = str(form.getvalue("pid"))
    gene = str(form.getvalue("gene"))
    Signal_ = str(form.getvalue("Signal_"))
    Detection = str(form.getvalue("Detection"))
    Foldchange = str(form.getvalue("Foldchange"))
    Direction = str(form.getvalue("Direction"))

    # set colour palette for variant graphs
    var_color = {}

    # Select clause
    form_query = "SELECT Probe_Set_ID, Gene_Symbol, Foldchange, Change_direction, Signal_, Detection, Process_ID, Process_name, Title "
    # From clause
    form_query += "FROM Biological_process JOIN Gene USING (Probe_Set_ID) "
    # Variant queries
    all_q = {}
    # WT
    wt_q = ""
#    if WT != "None":
    wt_q = form_query + "JOIN WT USING (Probe_Set_ID) "
    all_q[WT] = wt_q
    var_color[WT] = 'C0'
    # VLDLR
    vl_q = ""
    vl_q = form_query + "JOIN VLDLR USING (Probe_Set_ID) "
    if VLDLR != "None":
        all_q[VLDLR] = vl_q
        var_color[VLDLR] = 'C1'
    # ApoeER2
    ap_q = ""
    ap_q = form_query + "JOIN ApoER2 USING (Probe_Set_ID) "
    if ApoER2 != "None":
        all_q[ApoER2] = ap_q
        var_color[ApoER2] = 'C4'
    # ApoE_VLDLR
    ap_vl_q = ""
    ap_vl_q = form_query + "JOIN ApoE_VLDLR USING (Probe_Set_ID) "
    if ApoE_VLDLR != "None":
        all_q[ApoE_VLDLR] = ap_vl_q
        var_color[ApoE_VLDLR] = 'C6'
    # Reln
    rl_q = ""
    rl_q = form_query + "JOIN Reln USING (Probe_Set_ID) "
    if Reln != "None":
        all_q[Reln] = rl_q
        var_color[Reln] = 'C8'
    # Dabl
    da_q = ""
    da_q = form_query + "JOIN Dabl USING (Probe_Set_ID) "
    if Dabl != "None":
        all_q[Dabl] = da_q
        var_color[Dabl] = 'C3'
    # Combined
    cm_q = ""
    cm_q = form_query + "JOIN Combined USING (Probe_Set_ID) "
    if Combined != "None":
        all_q[Combined] = cm_q
        var_color[Combined] = 'C9'
        # if Dabl not in all_q.keys():
        all_q["Dabl_c"] = da_q
        var_color["Dabl_c"] = 'C3'
        # if Reln not in all_q.keys():
        all_q["Reln_c"] = rl_q
        var_color["Reln_c"] = 'C8'
        # if ApoE_VLDLR not in all_q.keys():
        all_q["ApoE_VLDLR_c"] = ap_vl_q
        var_color["ApoE_VLDLR_c"] = 'C6'

    # Number of variants selected
    q_len = len(all_q)
    if Combined in all_q.keys():
        q_len -=4
#    print(q_len)
    
    # Values for query
    vals = []

    # Start Biological_process figure
#    bp_fig, bp_sub = plt.subplots(1, q_len, sharey=True)
#    bp_fig.subplots_adjust(bottom=0.35, wspace=0.25)
#    bp_fig.suptitle('Biological_process', fontsize=14, fontweight='bold')

    # Start Fold_change figure
    fig_exp, exp_sub = plt.subplots(1, q_len-1, sharey=True)
    #print(len(exp_sub))
    fig_exp.subplots_adjust(bottom=0.35, wspace=0.3)
    fig_exp.suptitle('Gene_expression compared to WT', fontsize=14, fontweight='bold')

    # find max y for graphs
    max_bp = []
    max_fc = []

    # Gene not found msg
    no_gene_msg = "Gene not found. Please try again."
    no_gene = 0

    # No rows found message
    no_rows_msg = "No results for search criteria in the following variants: "
    miss_rows = False
    
    # index
    i = -1
    
    try:
        # Loop through queries
        for nm, q in all_q.items():
            # check that variant chosen
            if q != "":
                # add where
                q += "WHERE "

                # Add conditions based on form input
                if gene != "None":
                    q += "(Title LIKE '%"+gene+"%' OR Gene_Symbol LIKE '%"+gene+"%') AND  "
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
                q += ";"
                vals = tuple(vals)

                if len(vals)==0:
                    cursor.execute(q)
                    records = cursor.fetchall()
                else:
                    cursor.execute(q,vals)
                    records = cursor.fetchall()

                # Frequency of each Biological_process in query
                bp = {}
                exp = {}
            
                # Update variant name if needed
                nm_u = nm
                if nm=="Dabl_c" or nm=="ApoE_VLDLR_c" or nm=="Reln_c":
                    nm_u = nm[:-2]
                elif len(records)==0:
                    no_gene += 1 
                    if nm!=WT:
                        miss_rows = True
                        no_rows_msg = no_rows_msg + nm + ', '
###                    print('<h3 style="color:red;"><b><i> No results for search criteria in '+nm+'.</i></b></h3>')
                if (nm=="Dabl_c" and Dabl in all_q) or (nm=="ApoE_VLDLR_c" and ApoE_VLDLR in all_q) or (nm=="Reln_c" and Reln in all_q):
                    pass
                else:
                    # iterate through results
                    for row in records:
                        ##genes and FC in query
                        exp[row[1]] = row[2]
                        # count frequency of Biological_process
                        if row[6] not in bp:
                            bp[row[6]] = [row[7], 1]
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
                                        <td> %s </td>
                                     </tr>''' % (nm_u, row[0], row[1], row[8], row[2], row[3], row[4], row[5], row[6], row[7])
                            print(mousedbsearch)
                            # print('''<br />''')
                        mousedbresults()

                # taken from https: // github.com / OmbraDiFenice / table2csv / blob / master / src / table2csv.js
                # print("<button type='button' id='button'>Download "+nm+" Mouse Data</button> ")

                # Plot 2: Top 5 genes according to FC
                if nm!=Combined and nm!=WT and nm!="Dabl_c" and nm!="ApoE_VLDLR_c" and nm!="Reln_c":
                    new_exp = dict(sorted(exp.items(), key=operator.itemgetter(1), reverse=True)[:5])
                    genes_exp = list(new_exp.keys())
                    FC_exp = list(new_exp.values())
                    this_expsub = exp_sub
                    if q_len-1>1:
                        this_expsub = exp_sub[i]
                    if FC_exp:  # and max(FC_exp)>0:
                        this_expsub.bar(genes_exp, FC_exp, color=var_color[nm])
                        # track max fc for fig_exp
                        max_fc.append(math.ceil(float(max(FC_exp)) / 5) * 5)
                        # exp_sub[i].set_ylim(0,y_upp)
                    else:
                        genes_exp=list(" ")
                        FC_exp=[0.001]
                        this_expsub.bar(genes_exp, FC_exp, color=var_color[nm])
                        #exp_sub[i].set_xticklabels(gene_exp)
                        max_fc.append(0)
                    this_expsub.set_title(nm)  # "Fold_change")
                    this_expsub.set_xticklabels(genes_exp, rotation=90)
                # Append 0 to list if Combined was selected
                if nm==Combined:
                    max_fc.append(0)

            # increment i for subplots
            i += 1

        # PRINT QUERY ERROR MSG
        if no_gene==q_len and gene!="None":
            print('<h3 style="color:red;"><b><i>'+no_gene_msg+'</i></b></h3>')
        elif miss_rows == True:
            no_rows_msg = no_rows_msg[:-2] + '.'
            print('<h3 style="color:red;"><b><i>'+no_rows_msg+'</i></b></h3>')
        
        ## FC (exp) img
        # y axis settings
        if fig_exp.get_axes():
            this_expsub = exp_sub
            if q_len-1>1:
               this_expsub = exp_sub[0]
            this_expsub.set_ylabel('Fold_change')
            y_upp = max(max_fc)
            if y_upp<=0:
               y_upp = 1
               print('''<h3 style="color:red;"><b><i> <u>Empty graph:</u> No gene expression detected for search criteria. Please try again.</i></b></h3>''')
            this_expsub.set_ylim(0, y_upp)
            # determine steps for y ticks
            steps = math.ceil(((y_upp + 0.00001) / (5 * 10)) * 5)
            y_nums = np.arange(0, y_upp + steps, steps)
            this_expsub.set_yticks(y_nums)
            this_expsub.set_yticklabels(y_nums)
            # save and show FC (exp) img
            fc_img_file = '/var/www/html/students_20/groupH/img/EXP.png'
            fig_exp.savefig(fc_img_file)
         

            # PRINT GRAPH IMG
            fc_src_loc = "https://bioed.bu.edu/students_20/groupH/img/EXP.png"
            print("<br><img id='plots' src=" + fc_src_loc + " style='width:95%;'/></br>")

            # PRINT DOWNLOAD  BUTTONS

            ### Download Gene Expression
            print("<button type='button'> <a href='" + fc_src_loc + "' download='reeler_gene_exp.png'>Download Gene_expression plot</a></button></br>")
        ### Download Table as csv
        print("""<button type='button' id='button'>Download Mouse Table as csv</button>""")

        ## UPDATED IMG GENERATION
    
    # catch error
    except:
        print('''<h3 style="color:red;"><b><i> Invalid query. Please try again.</i></b></h3>''')

    cursor.close()
    connection.close()

print("</table></p>")



# CSV file
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


#Sort tables by clicking on column
print("""<script src="https://kryogenix.org/code/browser/sorttable/sorttable.js"></script>""")

#Hover over text
print("""
<style>
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  
  /* Position the tooltip */
  position: absolute;
  z-index: 1;
  top: -5px;
  left: 105%;
  
  /* Fade in tooltip - takes 1 second to go from 0% to 100% opac: */
  opacity: 0;
  transition: opacity 1s;
}
.tooltip .tooltiptext::after {
  content: "";
  position: absolute;
  top: 50%;
  right: 100%;
  margin-top: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: transparent black transparent transparent;
}
.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}
</style>
""")

print("""
    </div>
  </div>

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
""")
