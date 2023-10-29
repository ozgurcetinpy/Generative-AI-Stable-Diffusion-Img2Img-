import io
import requests
from PIL import Image,ImageDraw, ImageFont
import base64

url = "http://127.0.0.1:7860"

img_payload = {
    "prompt": "kraft coffee cup, sunny day background, black cover ",
    "init_images": ["https://img.fruugo.com/product/6/99/659457996_max.jpg"],
    "width": 512,
    "height": 512,
    "samples": 1,
    "num_inference_steps": 30,
    "model_id": "hf-model"
}

response = requests.post(url=f'{url}/sdapi/v1/img2img', json=img_payload)
if response.status_code == 200:
    r = response.json()
    image = r['images'][0]
    image = Image.open(io.BytesIO(base64.b64decode(image)))
    image.save('output.png')
else:
    print("API isteği başarısız oldu. HTTP kodu:", response.status_code)

generated_image_url = r"C:\Users\ozgur\stable-diffusion-webui-master\output.png"
generated_image = Image.open(generated_image_url)

logo_path = r"C:\Users\ozgur\stable-diffusion-webui-master\backtonature.jpeg"
logo = Image.open(logo_path)
logo = logo.resize((250, 150))


punchline_text = "AI ad banners lead to higher \n conversions ratesxxxx"
button_text = "Call to action test here!  >"
button_color = "#FF5733"

ad_template = Image.new('RGB', (generated_image.width, generated_image.height + 200), color='white')
ad_template.paste(logo, (generated_image.width // 2 - logo.width // 2, 20))
ad_template.paste(generated_image, (0, 120))

draw = ImageDraw.Draw(ad_template)

font_size_punchline = 25
font_punchline = ImageFont.truetype("arial.ttf", font_size_punchline)
text_width, text_height = 300,20
text_position = ((generated_image.width - text_width) / 2, generated_image.height + 10)
draw.text(text_position, punchline_text, fill='black', font=font_punchline)

button_font = ImageFont.truetype("arial.ttf", 30)
button_size = (350, 30)
button_width, button_height = button_size
button_x = (generated_image.width - button_width) // 2
button_y = generated_image.height + 100 
draw.rectangle([button_x - 10, button_y - 10, button_x + button_width + 10, button_y + button_height + 10],
               fill=button_color)
draw.text((button_x, button_y), button_text, fill='white', font=button_font)


ad_template.save('advertisement.png')