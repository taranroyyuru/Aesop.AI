import os
import google.generativeai as genai

def audio_agent():
	pass

def text_agent():
	pass

def image_agent(prompt_text):
	genai.configure(api_key=os.environ['API_KEY'])
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
  		


