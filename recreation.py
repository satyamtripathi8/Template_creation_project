from PIL import Image, ImageDraw, ImageFont

template_path = 'template.jpg'
template = Image.open(template_path)
draw = ImageDraw.Draw(template)

text = "Hairstyling In Houstan"
font_path = 'Madina.ttf'  
font_size = 150
font = ImageFont.truetype(font_path, font_size)
text_color = (0, 0, 0) 
# text_width, text_height = draw.textsize(text, font=font)
# image_width, image_height = template.size
# x = (image_width - text_width) / 2
# y = (image_height - text_height) / 2


# Pointer
# point_to_find = (150, 130)  

# marker_radius = 5  
# marker_color = (255, 0, 0)  
# draw.ellipse((point_to_find[0] - marker_radius, point_to_find[1] - marker_radius,
#               point_to_find[0] + marker_radius, point_to_find[1] + marker_radius), fill=marker_color)

x1, y1 = 0, 850  
x2, y2 = 1100, 1100
background_color = (255, 255, 255)
draw.rectangle([x1, y1, x2, y2], fill=background_color)

draw.text((60, 900), text, font=font, fill=text_color)


ellip_color = (255,204,204)
# draw.ellipse((0,0,220,200),fill= ellip_color)

draw.rectangle([0,50,100,785],fill= ellip_color)
lavender = (230,230,250)
draw.rectangle([0,0,1100,50],fill=lavender)
turquoise =(64,224,208)
light_t =(173,216,230)
draw.rectangle([0,782,450,853],fill=light_t)
txt = "Oops Upside Yo Head"
font_path = 'Badoni.ttf'  
font_size = 50
fon = ImageFont.truetype(font_path, font_size)
text_color = (255, 255, 255)

draw.text((10,785),txt,font=fon,fill=text_color)
#draw.text((10,60), text, font=font, fill=text_color)
output_path = 'output_template.png'
template.save(output_path)