pip install google-generativeai
import google.generativeai as genai
api_key='AIzaSyCcz5ZBpMBhX6fMFne7N1mDbB1ehKtqfV8'
genai.configure(api_key=api_key)
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
model=genai.GenerativeModel("gemini-pro")
model
response=model.generate_content("who is pm of india")
print(response.text)
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])
while True:
  Question=input("Enter a Question:")
  if Question=="Done":
    print("Thank you !!")
    break
  elif Question=='I will kill u':
    print("That was a nice joke!! HA HA HA")
  elif Question=='what is your name':
    print("Iam chitti")
  elif Question=='Who is the cm of telangana':
    print("Revanth Reddy")
  else:
    response=chat.send_message(Question)
    print(response.text)
