import google.generativeai as genai

genai.configure(api_key="AIzaSyDOXBMS4S_x3rrVsrq66QfZ7zDKAiHStLE")

# for i in genai.list_models():
#     print(i.name)

def read(message):
    for chunk in message:
        chunk.text.replace('*',"")
        print(chunk.text)

model=genai.GenerativeModel("gemini-pro")

history=[]
chat=model.start_chat(history=history)

chat.send_message("your name is kate.")

def chatting(text):
    res=chat.send_message(text)
    read(res)


# print(chat.history)

# message=model.generate_content("who i am?")



# print(message)

if __name__=="__main__":
    text="true"
    while(text!="exit"):
        text=input("User: ")
        chatting(text)
        
    




















