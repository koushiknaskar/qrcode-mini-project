#First step go to cmd and type "pip install qrcode" it will install the most of the necessary files.
#Scond step again go to cmd and type "pip install image" it will install the rest of of the files.

import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 10, #size of the box where qr code will be displayed
    border = 5 #it is the white part of the image -- border in all 4 side with white color
       
)
data = "https://www.youtube.com"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white")
img.save("test.png")




