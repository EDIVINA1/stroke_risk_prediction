import google.generativeai as genai

genai.configure(api_key="AIzaSyDrGt_CZsE3wI9CZgXOJi0bPm84ntQFrCY")

# Example: send a prompt
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hello! What can you do?")
print(response.text)