from flask import Flask, request, jsonify
from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import base64
from PIL import Image

# Flask app initialization
app = Flask(__name__)

# Model configuration
model_id = "runwayml/stable-diffusion-v1-5"  # Use a known compatible model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the Stable Diffusion pipeline
try:
    pipeline = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device.type == "cuda" else torch.float32,
        revision="fp16" if device.type == "cuda" else None,
        safety_checker=None  # Optional: Disable safety checker
    )
    pipeline.to(device)
    print("Pipeline loaded successfully!")
except ValueError as e:
    print(f"Error loading pipeline: {e}")
    exit()

# Route to generate images
@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        # Extract prompt from request
        data = request.json
        prompt = data.get("prompt", "A beautiful landscape")
        
        # Generate the image
        with torch.no_grad():
            result = pipeline(prompt)
            image = result.images[0]

        # Convert image to base64
        img_io = BytesIO()
        image.save(img_io, format="PNG")
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode("utf-8")

        return jsonify({"image": img_base64})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
