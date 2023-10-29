import io
import requests
from PIL import Image, PngImagePlugin
import base64

url = "http://127.0.0.1:7860"

img_payload = {
    "prompt": "red hair",
    "init_images": ["https://images.unsplash.com/photo-1601979031925-424e53b6caaa?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cHVwcHl8ZW58MHx8MHx8fDA%3D"],
    "width": 512,
    "height": 512,
    "samples": 5,
    "num_inference_steps": 30,
    "model_id": "hf-model"
}

response = requests.post(url=f'{url}/sdapi/v1/img2img', json=img_payload)
if response.status_code == 200:
    r = response.json()
    image1 = r['images'][0]
    image2 = r['images'][1]
    image3 = r['images'][2]

    image1 = Image.open(io.BytesIO(base64.b64decode(image1)))
    image2 = Image.open(io.BytesIO(base64.b64decode(image2)))
    image3 = Image.open(io.BytesIO(base64.b64decode(image3)))
    image1.save('output1.png')
    image2.save('output2.png')
    image3.save('output3.png')
else:
    print("API isteği başarısız oldu. HTTP kodu:", response.status_code)
