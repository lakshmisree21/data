##import qrtools 
##from qrtools import QR 
import xlwt
import qrcode,sys
d = qrcode.Decoder()
#img = QR()
#print myCode.webcam()
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("info")
worksheet.write(0,0,d.Name)
worksheet.write(0,1,d.Email)
worksheet.write(0,3,d.Contact)
print d.Name
print d.Email
print d.Contact