import google.generativeai as genai

genai.configure(api_key="AIzaSyBzIZFqiM75Jx3bKNDM_eK4WL6XVlt9XeY")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)