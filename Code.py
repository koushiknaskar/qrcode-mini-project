#!/usr/bin/env python
# coding: utf-8

# In[2]:


import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
    
)
data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x&ab_channel=TechieCoder"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white")
img.save("test.png")


# In[ ]:




