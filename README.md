# Pictor_Craft

## Overview
PictorCraft is an AI-powered image generation tool that leverages the **Stable Diffusion** model to create high-quality AI-generated images. It utilizes **Hugging Face** to connect with Stable Diffusion servers and can run on either a **CPU or GPU**, depending on available hardware resources.

The project is built as a **client-server architecture**, where the server hosts the Stable Diffusion model and processes image generation requests from the client. The client sends text-based prompts to the server and receives generated images in return.

## Features
- AI-driven image generation using Stable Diffusion.
- Supports **both CPU and GPU acceleration** (depending on hardware availability).
- Flask-based **REST API server** for image generation.
- Command-line client for interacting with the server.
- Image output in **PNG format**.

## System Requirements
### Hardware
- **CPU:** AMD Ryzen 7 6800H or equivalent (for CPU-based inference)
- **GPU:** NVIDIA RTX 3050 (4GB VRAM) or higher (recommended for GPU acceleration)
- **RAM:** Minimum 8GB (16GB recommended for better performance)
- **Storage:** At least 10GB of free space for model storage and image generation

### Software
- **Operating System:** Windows 10/11, Linux, or macOS
- **Python:** Version 3.8 or higher
- **Dependencies:**
  - Flask (`pip install flask`)
  - Diffusers (`pip install diffusers`)
  - Torch (`pip install torch`)
  - PIL (Python Imaging Library, included in `Pillow` package)
  - Requests (`pip install requests`)

## Installation and Setup
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/PictorCraft.git
cd PictorCraft
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Running the Server
```bash
python server.py
```
The server will start on `http://0.0.0.0:5000/` and listen for image generation requests.

### 4. Running the Client
```bash
python client.py
```
The client will prompt for a text input and send the request to the server.

## API Endpoint
### `POST /generate`
- **Request Body:**
```json
{
    "prompt": "A futuristic cyberpunk city at night"
}
```
- **Response:**
```json
{
    "image": "<base64-encoded-image>"
}
```

## Future Enhancements
- **Web-based UI** for an interactive user experience.
- **Multi-threading support** for handling multiple requests efficiently.
- **Integration with cloud services** for high-performance GPU-based processing.
- **Fine-tuning Stable Diffusion models** to customize AI-generated results.

## License
This project is open-source under the MIT License.

## Author
**Raghavendra KM**  
[GitHub]([https://github.com/yourusername](https://github.com/Raghavendra-KM))  
[LinkedIn](linkedin.com/in/raghavendrakm08/)

