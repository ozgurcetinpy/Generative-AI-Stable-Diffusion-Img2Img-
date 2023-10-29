from PIL import Image, ImageDraw, ImageFont

# Image
generated_image_url = r"C:\Users\ozgur\stable-diffusion-webui-master\output.png"
generated_image = Image.open(generated_image_url)

# Logo
logo_path = r"C:\Users\ozgur\stable-diffusion-webui-master\images\backtonature.jpeg"
logo = Image.open(logo_path)
logo = logo.resize((250, 150))

# Text and Colors
punchline_text = "AI ad banners lead to higher \n conversions ratesxxxx"
button_text = "Call to action test here!  >"
button_color = "#FF5733"

ad_template = Image.new('RGB', (generated_image.width, generated_image.height + 200), color='white')
ad_template.paste(logo, (generated_image.width // 2 - logo.width // 2, 20))  # Orta üste hizala
ad_template.paste(generated_image, (0, 120))

draw = ImageDraw.Draw(ad_template)

# Punchline Text
font_size_punchline = 25
font_punchline = ImageFont.truetype("arial.ttf", font_size_punchline)
text_width, text_height = 300,20
text_position = ((generated_image.width - text_width) / 2, generated_image.height + 10)
draw.text(text_position, punchline_text, fill='black', font=font_punchline)

# Call-to-Action Button
button_font = ImageFont.truetype("arial.ttf", 30)
button_size = (350, 30)
button_width, button_height = button_size
button_x = (generated_image.width - button_width) // 2
button_y = generated_image.height + 100  # Buton ile metin arasındaki boşluğu artırmak için değeri 100 artırın
draw.rectangle([button_x - 10, button_y - 10, button_x + button_width + 10, button_y + button_height + 10],
               fill=button_color)
draw.text((button_x, button_y), button_text, fill='white', font=button_font)

# Save the final ad template
ad_template.save('advertisement_template.png')
