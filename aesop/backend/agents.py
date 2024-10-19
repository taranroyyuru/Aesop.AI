import os
import google.generativeai as genai
from dotenv import load_dotenv
from secret_key	import groq_api, lmnt_api
def audio_agent():
	pass

def text_agent(topic: string, character: str, level, model_to_use = 'llama', style='comic'):
	"""
	Generates a comic based converstation on a topic based on the character user choses.
	We also have options to choose different .
	llama is default.
	
	Params:
	topic: string, 
	character: str, 
	model_to_use = 'llama', 
	style='comic'
	"""
	model = 'llama-3.1-70b-versatile'
	prompt = f'Tell Me the concepts about {topic} in {character} style so that i can teach it to a children. Use a {style} conversational style.'

	response = client.chat.completions.create(
        model=model,
        messages=[
            {
                'role':'user', 'content': prompt
            }
        ]
    )
    # Extract the embedding from the response
    # Note: This is a simplified example. You'll need to parse the actual output.
    return response.choices[0].message.content
	

def image_agent(prompt_text):
	"""
	WIP
	"""
	load_dotenv()
	genai.configure(api_key=os.environ['GEMINI_KEY'])
	imagen = genai.ImageGenerationModel("imagen-3.0-generate-001")

	result = imagen.generate_images(
		prompt=prompt_text,
		number_of_images=1,
		safety_filter_level="block_only_high",
		person_generation="allow_adult",
		aspect_ratio="3:4",
		negative_prompt="Outside",
	)
	
	return result.images
  # Open and display the image using your local operating system.
  		


