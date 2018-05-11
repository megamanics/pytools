# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import PyPDF2
import fire


pdf = open("C:\\Users\\vinayaks\\Documents\\TheKSMTrustCetrtificate.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
    
pdfWriter.encrypt('ksmtrust123','')
resultPdf = open("C:\\Users\\vinayaks\\Documents\\ksmtrustcert.pdf", 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
