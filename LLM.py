
from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()
apikey=os.getenv("OPENROUTER_API_KEY")
def analyze_image(image_url):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {apikey}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "qwen/qwen2.5-vl-72b-instruct:free",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "Solve the Question in the image and write the solution int <Solution> </Solution> tags"
            },
            {
                "type": "image_url",
                "image_url": {
                "url": f"{image_url}"
                }
            }
            ]
        }
        ],
        
    })
    )
    result = response.json()
# Print full response if you want to debug
# print(json.dumps(result, indent=2))

# Extract the model output
    output = result["choices"][0]["message"]["content"]
    return output