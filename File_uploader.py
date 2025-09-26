import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv
import os
# Configuration       
load_dotenv()
cloudinary.config( 
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"), 
    api_key = os.getenv("CLOUDINARY_API_KEY"), 
    api_secret = os.getenv("CLOUDINARY_API_SECRET"), # Click 'View API Keys' above to copy your API secret
    secure=True
)


def upload_image(file):
# Upload an image
    upload_result = cloudinary.uploader.upload(file,
                                           public_id="shoes")
    return (upload_result["secure_url"])
