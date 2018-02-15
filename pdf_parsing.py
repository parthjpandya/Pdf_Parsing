# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:13:54 2018

@author: parth pandya
"""

import pdfquery
from pandas import json
pdf_list = ["U16571275.pdf","U16572745.pdf","U16573131.pdf"]
for i in pdf_list:
    
    pdf = pdfquery.PDFQuery(i)
    a=pdf.extract( [
        ('with_parent','LTPage[pageid=\'1\']'),
        ('with_formatter', 'text'),
        ('SRN', 'LTTextLineHorizontal:in_bbox("19.417,723.128,106.597,734.158")'),
        ('ServiceDate', 'LTTextLineHorizontal:contains("Service Request Date :")'),
        ('PaymentMade', 'LTTextLineHorizontal:in_bbox("20.364,707.73,134.364,718.33")'),
        ('Total', 'LTTextLineHorizontal:in_bbox("502.339, 542.578, 544.339, 553.098")'),
        ('Type of Fee', 'LTTextLineHorizontal:in_bbox("356.544, 542.801, 392.544, 553.321")'),
        ('Received Payment Rupees', 'LTTextLineHorizontal:in_bbox("19.417, 476.185, 266.687, 487.435")'),
        ('Mode of Payment', 'LTTextLineHorizontal:in_bbox("116.393, 491.292, 338.393, 501.812")'),
        ('Amount', 'LTTextLineHorizontal:in_bbox("502.339, 542.578, 544.339, 553.098")'),
        ('Name', 'LTTextLineHorizontal:in_bbox("88.997, 677.663, 346.997, 688.183")'),
        ('Address', 'LTTextLineHorizontal:in_bbox("88.997,622.36,287.51,674.495")'),
        ('Service Description', 'LTTextLineHorizontal:in_bbox("32.66,532.478,290.666,563.018")'),
        ('Service Type', 'LTTextLineHorizontal:in_bbox("19.417, 595.417, 327.487, 606.457")')
        ] )
    
    value=[(a['SRN']),(a['ServiceDate']),(a['PaymentMade']),(a['Total']),(a['Type of Fee']),(a['Received Payment Rupees']),(a['Mode of Payment']),(a['Amount']),(a['Name']),(a['Address']),(a['Service Description']),(a['Service Type'])]

     
 
