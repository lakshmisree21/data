import urllib2
import urllib
import gspread
import Image
import ImageDraw
import ImageFont

w=420

#url = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Example"
#image = urllib2.urlopen(url).read()
#print image

#name = 'hello' + '.png'
#outfile = open(name,'wb')
#outfile.write(image)
#outfile.close()

gc = gspread.login('username@gmail.com','password')
wks = gc.open("Spreadsheet").sheet1  # "Spreadsheet" is the name of the Google Spreadsheet made in the account
val = wks.acell('B1').value
print val
#print len(wks.row_values(1))
list_of_lists = wks.get_all_values()
print list_of_lists

#url = "https://api.qrserver.com/v1/create-qr-code/?data=BEGIN%3AVCARD%0AVERSION%3A2.1%0AFN%3APraveen+Sridhar%0AN%3A%3BPraveen+Sridhar%0ATEL%3BHOME%3BVOICE%3A9544344104%0AEMAIL%3BHOME%3BINTERNET%3Aprvn431%40gmail.com%0AEND%3AVCARD%0A&amp;size=220x220&amp;margin=0"

for i in range(5):
    idi = list_of_lists[i][0]
    name = list_of_lists[i][1]
    name_url = urllib.quote_plus(list_of_lists[i][1]) #url encoded name for api call
    email = urllib.quote_plus(list_of_lists[i][2])
    number = urllib.quote_plus(list_of_lists[i][3])
    url = "https://api.qrserver.com/v1/create-qr-code/?data=BEGIN%3AVCARD%0AVERSION%3A2.1%0AFN%3A"+name_url+"%0AN%3A%3B"+name_url+"%0ATEL%3BHOME%3BVOICE%3A"+number+"%0AEMAIL%3BHOME%3BINTERNET%3A"+email+"%0AEND%3AVCARD%0A&amp;size=50x50"
    qr_image = urllib2.urlopen(url).read()
    name_qr = name + ".png"
    outfile = open(name_qr,'wb')
    outfile.write(qr_image)
    outfile.close()
    
    qr = Image.open(name_qr)
    qr.thumbnail((120,120))
    thid = Image.open("tinkerhub_card.png")  # Blank ID Card over which the QR code has to be placed
    thid_new = Image.new('RGB', (420,680))
    thid_new.paste(thid, (0,0))
    thid_new.paste(qr, (150,220))
    id_usr_font = ImageFont.truetype("resources/OpenSans-Regular.ttf", 25)
    id_usr = ImageDraw.Draw(thid_new)
    w1,h1 = id_usr_font.getsize(idi)
    id_usr = id_usr.text(((w-w1)/2,150), idi ,(0,0,0), font=id_usr_font)
    
    name_usr_font = ImageFont.truetype("resources/OpenSans-Regular.ttf", 30)
    name_usr = ImageDraw.Draw(thid_new)
    name_usr = name_usr.text((90,365), name ,(0,0,0), font=name_usr_font)


    thid_new.show()
    