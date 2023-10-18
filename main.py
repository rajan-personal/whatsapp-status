from PIL import Image, ImageDraw

image = Image.open('templates/1.jpg')
logo = Image.open('logo/company.jpeg')

logo = logo.resize((80, 80))  # Resize to 80x80 pixels

image.paste(logo, (50, 50))  # Paste the logo at the top left corner

I1 = ImageDraw.Draw(image)
I1.text((58, 136), "Nice Company", fill=(0, 0, 0))

image.save('results/image_with_logo.jpg')



