#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install Pillow


# In[15]:


from PIL import Image, ImageFilter

# Open an image file
image = Image.open("C:\\Users\\MONICA P\\Downloads\\project images\\tired dog hd wallpaper.jpg")


# Display the original image
image.show()

# Convert the image to grayscale
grayscale_image = image.convert("L")
grayscale_image.show()

# Rotate the image by 90 degrees
rotated_image = image.rotate(90)
rotated_image.show()

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()

# Resize the image
resized_image = image.resize((300, 300))
resized_image.show()

# Crop a region of interest from the image
cropped_image = image.crop((100, 100, 400, 400))
cropped_image.show()

# Save manipulated images
grayscale_image.save("grayscale_image.jpg")
rotated_image.save("rotated_image.jpg")
blurred_image.save("blurred_image.jpg")
resized_image.save("resized_image.jpg")
cropped_image.save("cropped_image.jpg")


# In[ ]:




