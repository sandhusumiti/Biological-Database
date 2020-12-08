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

          <li><a href="https://bioed.bu.edu/students_20/groupH/contact.html">Contact Us</a></li>
        </ul>
      </div>
    </div>
    <div id="site_content">
      <div class="sidebar">
        <h1>Latest News</h1>
        <h4>New Website Launched</h4>
        <h5>April 27, 2010</h5>
        <p> Take a look around and let us know what you think.<br /></p>
        <h1>Useful Database Links</h1>
        <ul>
          <li><a href="https://www.thermofisher.com/us/en/home/life-science/microarray-analysis/affymetrix.html">Affymatrix</a></li>
          <li><a href="https://www.ncbi.nlm.nih.gov/">NCBI</a></li>
          <li><a href="http://geneontology.org/">GeneOntology</a></li>
          <li><a href="https://www.genome.jp/kegg/pathway.html">KEGG Pathway</a></li>
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

print('''<br />''')

# Foldchange
# TODO: add min and max
print(""" <!-- Foldchange as text -->
<strong>OR search by other criteria:</strong>
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
  <input type="checkbox" id="Combined" name="Combined" value="Combined"> Combined <br />
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
<table id="order" style="border:3px #FFD382 dashed;" cellpadding="10" border='1'>
        <tr>
	<th> Variant </th>
        <th> Probe_set_ID </th>
        <th> Gene_symbol </th>
        <th> Foldchange </th>
	<th> Change_direction </th>
        <th> Signal </th>
        <th> Detection </th>
	<th> Process_ID </th>
	<th> Biological_process </th>
        </tr>''')

# Get form data
if form:
    # checkbox
    WT = str(form.getvalue("WT"))
    VLDLR = str(form.getvalue("VLDLR"))
    ApoER2 = str(form.getvalue("ApoER2"))
    Dabl = str(form.getvalue("Dabl"))
    ApoE_VLDLR = str(form.getvalue("ApoE_VLDLR"))
    Reln = str(form.getvalue("Reln"))
    Combined = str(form.getvalue("Combined"))
    # rest
    pid = str(form.getvalue("pid"))
    gene = str(form.getvalue("gene"))
    Signal_ = str(form.getvalue("Signal_"))
    Detection = str(form.getvalue("Detection"))
    Foldchange = str(form.getvalue("Foldchange"))
    Direction = str(form.getvalue("Direction"))

    # set colour palette for variant graphs
    var_color = {}

    # Select clause
    form_query = "SELECT Probe_Set_ID, Gene_Symbol, Foldchange, Change_direction, Signal_, Detection, Process_ID, Process_name "
    # From clause
    form_query += "FROM Biological_process JOIN Gene USING (Probe_Set_ID) "
    # Variant queries
    all_q = {}
    wt_q = ""
    if WT != "None":
        wt_q = form_query + "JOIN WT USING (Probe_Set_ID) "
        all_q[WT] = wt_q
        var_color[WT] = 'C0'
    vl_q = ""
    if VLDLR != "None":
        vl_q = form_query + "JOIN VLDLR USING (Probe_Set_ID) "
        all_q[VLDLR] = vl_q
        var_color[VLDLR] = 'C1'
    ap_q = ""
    if ApoER2 != "None":
        ap_q = form_query + "JOIN ApoER2 USING (Probe_Set_ID) "
        all_q[ApoER2] = ap_q
        var_color[ApoER2] = 'C4'
    ap_vl_q = ""
    if ApoE_VLDLR != "None":
        ap_vl_q = form_query + "JOIN ApoE_VLDLR USING (Probe_Set_ID) "
        all_q[ApoE_VLDLR] = ap_vl_q
        var_color[ApoE_VLDLR] = 'C6'
    rl_q = ""
    if Reln != "None":
        rl_q = form_query + "JOIN Reln USING (Probe_Set_ID) "
        all_q[Reln] = rl_q
        var_color[Reln] = 'C8'
    da_q = ""
    if Dabl != "None":
        da_q = form_query + "JOIN Dabl USING (Probe_Set_ID) "
        all_q[Dabl] = da_q
        var_color[Dabl] = 'C3'
    cm_q = ""
    if Combined != "None":
        cm_q = form_query + "JOIN Combined USING (Probe_Set_ID) "
        all_q[Combined] = cm_q
        var_color[Combined] = 'C9'

    # Values for query
    vals = []

    # Number of variants selected
    q_len = len(all_q)

    # Start Biological_process figure
    bp_fig, bp_sub = plt.subplots(1, q_len, sharey=True)
    bp_fig.subplots_adjust(bottom=0.35, wspace=0.3)
    bp_fig.suptitle('Biological_process', fontsize=14, fontweight='bold')

    # Start Fold_change figure
    fig_exp, exp_sub = plt.subplots(1, q_len, sharey=True)
    fig_exp.subplots_adjust(wspace=0.3)
    fig_exp.suptitle('Gene_expression', fontsize=14, fontweight='bold')

    # find max y for graphs
    max_bp = []
    max_fc = []

    # index
    i = 0

    # Loop through queries
    for nm, q in all_q.items():
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
            q += ";"
            # print(q, vals)
            vals = tuple(vals)
            cursor.execute(q, vals)
            records = cursor.fetchall()

            # Frequency of each Biological_process in query
            bp = {}

            exp = {}

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
                                     </tr>''' % (nm, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    print(mousedbsearch)
                    # print('''<br />''')
                mousedbresults()

            # taken from https: // github.com / OmbraDiFenice / table2csv / blob / master / src / table2csv.js
            # print("<button type='button' id='button'>Download "+nm+" Mouse Data</button> ")

            # TODO: Remove last 2 columns of table and display bp info only in graph
            # TODO:  plot 5 top Biological_processes associated with dataset

            # Create plots for variant
            #            fig, (bp_fig, fig_exp) = plt.subplots(2)
            #            fig.subplots_adjust(hspace=1)
            #            fig.suptitle(nm, fontweight='bold')

            # Plot 1: Top 10 Biological processes
            newbp = dict(sorted(bp.items(), key=operator.itemgetter(1), reverse=True)[:10])
            # bp_labels
            bp_labels = list(newbp.values())
            bp_labels = [item[0] for item in bp_labels]
            # bp_values
            bp_values = list(newbp.values())
            bp_values = [item[1] for item in bp_values]
            # generate plot 1
            bp_sub[i].bar(bp_labels, bp_values, color=var_color[nm])
            bp_sub[i].set_xticklabels(bp_labels, rotation=60)
            bp_sub[i].set_title(nm)  # ('Biological_process')
            # bp_fig.set_ylabel('Frequency')
            # TO DO: Sort position of plot or labels so that labels are completely visible

            # Plot 2: Top 20 genes according to FC
            if nm != "Combined":
                new_exp = dict(sorted(exp.items(), key=operator.itemgetter(1), reverse=True)[:20])
                genes_exp = list(new_exp.keys())
                FC_exp = list(new_exp.values())
                exp_sub[i].bar(genes_exp, FC_exp, color=var_color[nm])
                # track max fc for fig_exp
                if len(FC_exp) != 0:
                    max_fc.append(math.ceil(float(max(FC_exp)) / 5) * 5)
                    # exp_sub[i].set_ylim(0,y_upp)
                else:
                    max_fc.append(0)
                exp_sub[i].set_title(nm)  # "Fold_change")

        #            # save and show BP img
        #            bp_img_file = '/var/www/html/students_20/groupH/img/BP_'+nm+'.png'
        #            plt.savefig(bp_img_file)
        #            #print("<img src="+plt.show()+">")
        #            bp_src_loc = "https://bioed.bu.edu/students_20/groupH/img/BP_"+nm+".png"
        #            print("<img id='plots' src="+bp_src_loc+" />")
        #
        #            # save and show FC (exp) img
        #            fc_img_file = '/var/www/html/students_20/groupH/img/EXP_'+nm+'.png'
        #            plt.savefig(fc_img_file)
        #            #print("<img src="+plt.show()+">")
        #            fc_src_loc = "https://bioed.bu.edu/students_20/groupH/img/EXP_"+nm+".png"
        #            print("<img id='plots' src="+fc_src_loc+" />")
        #
        #
        # TODO: Sort out why two plot results are merging??
        #
        i += 1  # issue: can't use matplotlib.pyplot with this python3.7 version

    ## BP img
    # y axis settings
    bp_sub[0].set_ylabel('Frequency')
    # save and show BP img
    bp_img_file = '/var/www/html/students_20/groupH/img/BP.png'
    bp_fig.savefig(bp_img_file)
    # print("<img src="+plt.show()+">")
    bp_src_loc = "https://bioed.bu.edu/students_20/groupH/img/BP.png"
    print("<br><img id='plots' src=" + bp_src_loc + " /></br>")

    ## FC (exp) img
    # y axis settings
    exp_sub[0].set_ylabel('Fold_change')
    y_upp = max(max_fc)
    exp_sub[0].set_ylim(0, y_upp)
    # determine steps for y ticks
    steps = math.ceil(((y_upp + 0.00001) / (5 * 10)) * 5)
    y_nums = np.arange(0, y_upp + steps, steps)
    print(y_upp + 1, steps, y_nums)
    exp_sub[0].set_yticks(y_nums)
    exp_sub[0].set_yticklabels(y_nums)
    # save and show FC (exp) img
    fc_img_file = '/var/www/html/students_20/groupH/img/EXP.png'
    fig_exp.savefig(fc_img_file)

    # print("<img src="+plt.show()+">")
    fc_src_loc = "https://bioed.bu.edu/students_20/groupH/img/EXP.png"
    print("<br><img id='plots' src=" + fc_src_loc + " /></br>")

    # PRINT DOWNLOAD  BUTTONS

    ### Download Biological Process
    print("<button type='button'> <a href='" + bp_src_loc + "' download='reeler_bio_proc.png'>Download Biological_process plot</a></button></br>")
    ### Download Gene Expression
    print("<button type='button'> <a href='" + fc_src_loc + "' download='reeler_gene_exp.png'>Download Gene_expression plot</a></button></br>")
    ### Download Table as csv
    print("""<button type='button' id='button'>Download Mouse Table as csv</button>""")

    ## UPDATED IMG GENERATION

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



print("""
    </div>
  </div>

</body>
</html>
""")
