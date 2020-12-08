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
          <li><a href="https://bioed.bu.edu/students_20/groupH/indexdata.html">Home</a></li>

          <li class="selected"><a href="https://bioed.bu.edu/cgi-bin/students_20/groupH/about.py">About</a></li>

          <li><a href="https://bioed.bu.edu/students_20/groupH/help.html">Help</a></li>

          <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupH/search.py">Search</a></li>
          
          <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupH/pathway.py">Pathway</a></li>
          
          <li><a href="https://bioed.bu.edu/students_20/groupH/contact.html">Contact Us</a></li>
        </ul>
      </div>
    </div>
    <div id="site_content">
      <div class="sidebar">
        
      </div>
  
      """)
print("""<h3> To Make these: Each mutant mouse was sequenced with the same probes.                      </br>
                            Each probe targets a gene or part of a gene which has a biological process.  </br>
                             Only probes with statistically significant values were included in these charts. </br>
                             Out of ~1700 biological processes the top 25 "hit" are represented in pie charts. </br>
                             Only statistically significant results were included.                      </br>
            </h3>""")
# #############################################################################################################
# ################ APOE    #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in ApoER2 KO Compared to WT</h1>""")

# Retrieve data for chart
connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
cursor = connection.cursor()

# apoI_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN ApoER2 USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 AND Process_name <> 'Unknown'"+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(apoI_pie_query)
# apoI_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_apoI = []
# labels_apoI = []
# for apoI_label in apoI_labels:
#     sizes_apoI.append(apoI_label[0])
#     labels_apoI.append(str(apoI_label[1]))
#
# # Figures and axes
# pie_fig_apoI, ax = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#32c1be',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# y = sizes_apoI
# y = np.around(y)
# y = y.astype(int)
# x = labels_apoI
# porcent = 100.* y/y.sum()
#
# # Colors & Labels
# # figure.figsize=[4, 5]
# patches, texts = plt.pie(y, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, y), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax.set_title("Top 25 Biological Processes Effected in ApoER2 Compared to WT", fontsize=7)
#
# Store & Print Image
# apoI_img_file = '/var/www/html/students_20/groupH/img/about_pie_Ifc_Apo.png'
# pie_fig_apoI.savefig(apoI_img_file, bbox_inches='tight', pad_inches=0)
apoI_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Ifc_Apo.png"
print("<br><img id='plots' src=" + apoI_img_loc + " /></br>")

# cursor.close()
# connection.close()
#
# #############################################################################################################
# ################ Reelin   #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in Reln KO Compared to WT</h1>""")

# Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()

# rlnI_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN Reln USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 AND Process_name <> 'Unknown'"+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(rlnI_pie_query)
# rlnI_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_rlnI = []
# labels_rlnI = []
# for rlnI_label in rlnI_labels:
#     sizes_rlnI.append(rlnI_label[0])
#     labels_rlnI.append(str(rlnI_label[1]))
#
# # Figures and axes
# pie_fig_rlnI, ax2 = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#32c1be',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# yb = sizes_rlnI
# yb = np.around(yb)
# yb = yb.astype(int)
# xb = labels_rlnI
# porcent = 100.* yb/yb.sum()
#
# # Colors & Labels
# patches, texts = plt.pie(yb, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xb, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, yb), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax2.set_title("Top 10 Increased Genes in Reln Compared to WT", fontsize=7)
#
# # Store & Print Image
# rlnI_img_file = '/var/www/html/students_20/groupH/img/about_pie_Ifc_Rln.png'
# pie_fig_rlnI.savefig(rlnI_img_file, bbox_inches='tight', pad_inches=0)
rlnI_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Ifc_Rln.png"
print("<br><img id='plots' src=" + rlnI_img_loc + " /></br>")

# cursor.close()
# connection.close()

# #############################################################################################################
# ################ Dab1     UNKNOWN INCLUDED #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in Dab1 KO Compared to WT</h1>""")

# Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()
#
# dabI_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN Dabl USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 AND Process_name <> 'Unknown'"+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(dabI_pie_query)
# dabI_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_dabI = []
# labels_dabI = []
# for dabI_label in dabI_labels:
#     sizes_dabI.append(dabI_label[0])
#     labels_dabI.append(str(dabI_label[1]))
#
# # Figures and axes
# pie_fig_dabI, ax3 = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#32c1be',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# yc = sizes_dabI
# yc = np.around(yc)
# yc = yc.astype(int)
# xc = labels_dabI
# porcent = 100.* yc/yc.sum()
#
# # Colors & Labels
# patches, texts = plt.pie(yc, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xc, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, yc), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax2.set_title("Top 10 Increased Genes in Reln Compared to WT", fontsize=7)
#
# # Store & Print Image
# dabI_img_file = '/var/www/html/students_20/groupH/img/about_pie_Ifc_Dab.png'
# pie_fig_dabI.savefig(dabI_img_file, bbox_inches='tight', pad_inches=0)
dabI_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Ifc_Dab.png"
print("<br><img id='plots' src=" + dabI_img_loc + " /></br>")

# cursor.close()
# connection.close()

# #############################################################################################################
# ################ DKO    #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in VLDLR/ApoER2 DKO Compared to WT</h1>""")

# Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()

# dkoI_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN ApoE_VLDLR USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 AND Process_name <> 'Unknown'"+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(dkoI_pie_query)
# dkoI_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_dkoI = []
# labels_dkoI = []
# for dkoI_label in dkoI_labels:
#     sizes_dkoI.append(dkoI_label[0])
#     labels_dkoI.append(str(dkoI_label[1]))
#
# # Figures and axes
# pie_fig_dkoI, ax5 = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#32c1be',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# ye = sizes_dkoI
# ye = np.around(ye)
# ye = ye.astype(int)
# xe = labels_dkoI
# porcent = 100.* ye/ye.sum()
#
# # Colors & Labels
# patches, texts = plt.pie(ye, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xe, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, ye), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax2.set_title("Top 10 Increased Genes in Reln Compared to WT", fontsize=7)
#
# # Store & Print Image
# dkoI_img_file = '/var/www/html/students_20/groupH/img/about_pie_Ifc_Dko.png'
# pie_fig_dkoI.savefig(dkoI_img_file, bbox_inches='tight', pad_inches=0)
dkoI_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Ifc_Dko.png"
print("<br><img id='plots' src=" + dkoI_img_loc + " /></br>")

# cursor.close()
# connection.close()

# #############################################################################################################
# ################ VLDLR   #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in VLDLR KO Compared to WT</h1>""")

# Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()
#
# vldI_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN VLDLR USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 AND Process_name <> 'Unknown'"+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(vldI_pie_query)
# vldI_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_vldI = []
# labels_vldI = []
# for vldI_label in vldI_labels:
#     sizes_vldI.append(vldI_label[0])
#     labels_vldI.append(str(vldI_label[1]))
#
# # Figures and axes
# pie_fig_vldI, ax4 = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#32c1be',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# yd = sizes_vldI
# yd = np.around(yd)
# yd = yd.astype(int)
# xd = labels_vldI
# porcent = 100.* yd/yd.sum()
#
# # Colors & Labels
# patches, texts = plt.pie(yd, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xd, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, yd), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax2.set_title("Top 10 Increased Genes in Reln Compared to WT", fontsize=7)
#
# # Store & Print Image
# vldI_img_file = '/var/www/html/students_20/groupH/img/about_pie_Ifc_Vld.png'
# pie_fig_vldI.savefig(vldI_img_file, bbox_inches='tight', pad_inches=0)
vldI_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Ifc_Vld.png"
print("<br><img id='plots' src=" + vldI_img_loc + " /></br>")

# cursor.close()
# connection.close()




















# #############################################################################################################
# ################ APOE     UNKNOWN INCLUDED #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in ApoER2 KO Compared to WT - including unknown</h1>""")

# Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()

# apoIu_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN ApoER2 USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 "+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(apoIu_pie_query)
# apoIu_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_apoIu = []
# labels_apoIu = []
# for apoIu_label in apoIu_labels:
#     sizes_apoIu.append(apoIu_label[0])
#     labels_apoIu.append(str(apoIu_label[1]))
#
# # Figures and axes
# pie_fig_apoIu, axu = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#8a95aa',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# yu = sizes_apoIu
# yu = np.around(yu)
# yu = yu.astype(int)
# xu = labels_apoIu
# porcent = 100.* yu/yu.sum()
#
# # Colors & Labels
# # figure.figsize=[4, 5]
# patches, texts = plt.pie(yu, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xu, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, yu), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax.set_title("Top 25 Biological Processes Effected in ApoER2 Compared to WT", fontsize=7)
#
# # Store & Print Image
# apoIu_img_file = '/var/www/html/students_20/groupH/img/about_pie_Dfc_Apo.png'
# pie_fig_apoIu.savefig(apoIu_img_file, bbox_inches='tight', pad_inches=0)
apoIu_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Dfc_Apo.png"
print("<br><img id='plots' src=" + apoIu_img_loc + " /></br>")

# cursor.close()
# connection.close()

# #############################################################################################################
# ################ Reelin     UNKNOWN INCLUDED #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in Reln KO Compared to WT - including unknown</h1>""")

# Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()

# rlnIu_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN Reln USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 "+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(rlnIu_pie_query)
# rlnIu_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_rlnIu = []
# labels_rlnIu = []
# for rlnIu_label in rlnIu_labels:
#     sizes_rlnIu.append(rlnIu_label[0])
#     labels_rlnIu.append(str(rlnIu_label[1]))
#
# # Figures and axes
# pie_fig_rlnIu, ax2u = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#8a95aa',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# ybu = sizes_rlnIu
# ybu = np.around(ybu)
# ybu = ybu.astype(int)
# xbu = labels_rlnIu
# porcent = 100.* ybu/ybu.sum()
#
# # Colors & Labels
# patches, texts = plt.pie(ybu, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xbu, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, ybu), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax2.set_title("Top 10 Increased Genes in Reln Compared to WT", fontsize=7)
#
# # Store & Print Image
# rlnIu_img_file = '/var/www/html/students_20/groupH/img/about_pie_Dfc_Rln.png'
# pie_fig_rlnIu.savefig(rlnIu_img_file, bbox_inches='tight', pad_inches=0)
rlnIu_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Dfc_Rln.png"
print("<br><img id='plots' src=" + rlnIu_img_loc + " /></br>")
#
# cursor.close()
# connection.close()
#
# # #############################################################################################################
# # ################ Dab1     UNKNOWN INCLUDED #################################################################################
# # #############################################################################################################
#
# print("""<h1>Top 25 Biological Processes Effected in Dab1 KO Compared to WT - including unknown</h1>""")
#
# # Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()
#
# dabIu_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN Dabl USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 "+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(dabIu_pie_query)
# dabIu_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_dabIu = []
# labels_dabIu = []
# for dabIu_label in dabIu_labels:
#     sizes_dabIu.append(dabIu_label[0])
#     labels_dabIu.append(str(dabIu_label[1]))
#
# # Figures and axes
# pie_fig_dabIu, ax3u = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#8a95aa',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# ycu = sizes_dabIu
# ycu = np.around(ycu)
# ycu = ycu.astype(int)
# xcu = labels_dabIu
# porcent = 100.* ycu/ycu.sum()
#
# # Colors & Labels
# patches, texts = plt.pie(ycu, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xcu, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, ycu), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax2.set_title("Top 10 Increased Genes in Reln Compared to WT", fontsize=7)
#
# # Store & Print Image
# dabIu_img_file = '/var/www/html/students_20/groupH/img/about_pie_Dfc_Dab.png'
# pie_fig_dabIu.savefig(dabIu_img_file, bbox_inches='tight', pad_inches=0)
dabIu_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Dfc_Dab.png"
print("<br><img id='plots' src=" + dabIu_img_loc + " /></br>")

# cursor.close()
# connection.close()

# #############################################################################################################
# ################ DKO    UNKNOWN INCLUDED   #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in VLDLR/ApoER2 DKO Compared to WT - including unknown</h1>""")

# Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()

# dkoIu_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN ApoE_VLDLR USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5 "+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(dkoIu_pie_query)
# dkoIu_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_dkoIu = []
# labels_dkoIu = []
# for dkoIu_label in dkoIu_labels:
#     sizes_dkoIu.append(dkoIu_label[0])
#     labels_dkoIu.append(str(dkoIu_label[1]))
#
# # Figures and axes
# pie_fig_dkoIu, ax5u = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#8a95aa',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# yeu = sizes_dkoIu
# yeu = np.around(yeu)
# yeu = yeu.astype(int)
# xeu = labels_dkoIu
# porcent = 100.* yeu/yeu.sum()
#
# # Colors & Labels
# patches, texts = plt.pie(yeu, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xeu, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, yeu), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax2.set_title("Top 10 Increased Genes in Reln Compared to WT", fontsize=7)
#
# # Store & Print Image
# dkoIu_img_file = '/var/www/html/students_20/groupH/img/about_pie_Dfc_Dko.png'
# pie_fig_dkoIu.savefig(dkoIu_img_file, bbox_inches='tight', pad_inches=0)
dkoIu_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Dfc_Dko.png"
print("<br><img id='plots' src=" + dkoIu_img_loc + " /></br>")

# cursor.close()
# connection.close()

# #############################################################################################################
# ################ VLDLR     UNKNOWN INCLUDED #################################################################################
# #############################################################################################################

print("""<h1>Top 25 Biological Processes Effected in VLDLR KO Compared to WT - including unknown</h1>""")

# Retrieve data for chart
# connection = pymysql.connect(host="bioed.bu.edu", user='wyueh', password='wyueh', database='groupH', port=4253)
# cursor = connection.cursor()

# vldIu_pie_query = "SELECT count(Process_name), Process_name"+\
#     " FROM Biological_process JOIN VLDLR USING (Probe_Set_ID)"+\
# 	" WHERE Change_direction <> 'NC' AND Foldchange >1.5"+\
# 	" Group by Process_name"+\
# 	" Order by count(Process_name) desc"+\
# 	" LIMIT 25;"
#
# cursor.execute(vldIu_pie_query)
# vldIu_labels = cursor.fetchall()
#
# # Labels & Sizes for Pie Chart
# sizes_vldIu = []
# labels_vldIu = []
# for vldIu_label in vldIu_labels:
#     sizes_vldIu.append(vldIu_label[0])
#     labels_vldIu.append(str(vldIu_label[1]))
#
# # Figures and axes
# pie_fig_vldIu, ax4u = plt.subplots()
#
# #Colors as Hex
# colors = [
# '#8a95aa',
# '#2dadab',
# '#289a98',
# '#238785',
# '#1e7372',
# '#c54040',
# '#b13939',
# '#9d3333',
# '#892c2c',
# '#762626',
# '#c58d36',
# '#b17e30',
# '#9d702b',
# '#896225',
# '#765420',
# '#65c336',
# '#5aaf30',
# '#509c2b',
# '#468825',
# '#3c7520',
# '#918ad8',
# '#7e77d1',
# '#6c63cb',
# '#5a50c4',
# '#483dbe',
# ]
#
# # Format data for Legend
# ydu = sizes_vldIu
# ydu = np.around(ydu)
# ydu = ydu.astype(int)
# xdu = labels_vldIu
# porcent = 100.* ydu/ydu.sum()
#
# # Colors & Labels
# patches, texts = plt.pie(ydu, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(xdu, porcent)]
#
# # Sort Legend by percent
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, ydu), key=lambda x: x[2], reverse=True))
# # Legend
# plt.legend(patches, labels, loc='left top', bbox_to_anchor=(-0.1, 1.), fontsize=8)
#
# # Title
# # ax2.set_title("Top 10 Increased Genes in Reln Compared to WT", fontsize=7)
#
# # Store & Print Image
# vldIu_img_file = '/var/www/html/students_20/groupH/img/about_pie_Dfc_Vld.png'
# pie_fig_vldIu.savefig(vldIu_img_file, bbox_inches='tight', pad_inches=0)
vldIu_img_loc = "https://bioed.bu.edu/students_20/groupH/img/about_pie_Dfc_Vld.png"
print("<br><img id='plots' src=" + vldIu_img_loc + " /></br>")

cursor.close()
connection.close()


# End
print("""      
    </div>
  </div>

</body>
</html>
""")









