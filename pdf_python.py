#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from datetime import date
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
today = date.today()

report = SimpleDocTemplate("processed.pdf")

a="Processed Update on {} {},{}".format(today.strftime("%B"),today.strftime("%d"),today.strftime("%Y"))
report_title = Paragraph(a, styles["h1"])
b="name: Apple\nweight: 500 lbs\n\nname: Avocado\nweight: 200 lbs\n\nname: Blackberry\nweight: 150 lbs\n\nname: Grape\nweight: 200 lbs\n\nname: Kiwifruit\nweight: 250 lbs\n\nname: Lemon\nweight: 300 lbs\n\nname: Mango\nweight: 300 lbs\n\nname: Plum\nweight: 150 lbs\n\nname: Strawberry\nweight: 240 lbs\n\nname: Watermelon\nweight: 500 lbs\n\n"
b=b.replace('\n','<br />\n')
report_content=Paragraph(b)

report.build([report_title,report_content])