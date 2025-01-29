import requests
import base64
from PIL import Image
from io import BytesIO

# Server URL (replace with network IP address or domain)
server_url = "http://ipaddress:5000/generate"

def main():
    # Prompt for the image
    prompt = input("Enter a prompt for the image: ").strip()

    # Send the prompt to the server
    try:
        print("Sending request to the server...")
        response = requests.post(server_url, json={'prompt': prompt})

        # Handle the server response
        if response.status_code == 200:
            response_json = response.json()
            if 'image' in response_json:
                # Decode the base64 image string returned by the server
                print("Decoding the image...")
                img_data = base64.b64decode(response_json['image'])
                img = Image.open(BytesIO(img_data))

                # Save the image to a file
                output_file = "generated_image.png"
                img.save(output_file)
                print(f"Image successfully saved as {output_file}")
                
                # Display the image
                img.show()
            else:
                print("Server response did not include an image.")
        else:
            print("Server error:", response.json().get('error', 'Unknown error'))
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
