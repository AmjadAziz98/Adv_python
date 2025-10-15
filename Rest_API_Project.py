# THis project must run in the Google's Colab
from google import genai
from google.colab import userdata
from google. genai import types
import requests
from IPython.display import display, Image

image_path = "https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fit,w_730,h_521/k%2FPhoto%2FSeries%2F2019-10--power-hour-instant-pot%2FPower-Hour-Instant-Pot_001-rotated"

image = requests.get(image_path)

# client = genai.Client(api_key="Your API Key here")
client = genai.Client(api_key= userdata.get('api_key'))
response = client.models.generate_content(model ="gemini-2.0-flash-exp",
        contents =["Provide the list of food items in the picutres in bullet points.",
        types.Part.from_bytes(data=image.content,mime_type="image/jpeg")])

res = response.text

# Extract only lines that start with '*', then clean them
food_items = [line.lstrip('*').strip() for line in res.splitlines() if line.strip().startswith('*')]

print(response.text)
print(food_items)
display(Image(url=image_path))
