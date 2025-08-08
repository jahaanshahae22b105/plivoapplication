# image_analysis.py
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load BLIP (a popular open-source image captioning model, lightweight, no external vendors needed)
# You only need to run this once; for performance, consider loading these outside the function (when your app starts)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def describe_image(image_file):
    # Read image with PIL
    image = Image.open(image_file).convert('RGB')
    # Prepare input
    inputs = processor(image, return_tensors="pt")
    # Generate description
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
