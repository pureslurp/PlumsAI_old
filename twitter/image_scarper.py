import os
import base64
from openai import OpenAI

def send_image_to_chatgpt(image_path, prompt):
    """
    Send an image to ChatGPT with a specific prompt.

    Args:
        image_path (str): Path to the image file
        prompt (str): Prompt to send with the image

    Returns:
        str: ChatGPT's response to the image and prompt
    """
    # Initialize the OpenAI client
    # Make sure to set your OPENAI_API_KEY environment variable
    # client = OpenAI()

    # Encode the image to base64
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Prepare the message with the image
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encode_image(image_path)}"
                    }
                }
            ]
        }
    ]

    # Send the request to ChatGPT
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Vision-capable model
            messages=messages,
            max_tokens=300  # Adjust as needed
        )

        # Return the response text
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
def main():
    # Set your OpenAI API key as an environment variable
    # You can also directly set it here, but it's not recommended for security reasons
    # os.environ['OPENAI_API_KEY'] = 'your-api-key-here'

    # Path to the image you want to analyze
    image_path = "twitter/bet.jpeg"

    # Prompt to send with the image
    prompt = 'From the image, return a string in this format: "{Team Name of bet}, {Type of Bet}, {Line), {Odds}, {Unit}" If no odds are specified, assume -110. If no unit is specified, assume 1'

    # Send image and get response
    response = send_image_to_chatgpt(image_path, prompt)
    print(response)

if __name__ == "__main__":
    main()

# Prerequisites:
# 1. Install required libraries:
#    pip install openai
# 2. Set up your OpenAI API key as an environment variable
#    export OPENAI_API_KEY='your-api-key-here'
# 3. Ensure you have a valid OpenAI account with API access
# 4. Make sure to use a vision-capable model like gpt-4-vision-preview
# Example usage

