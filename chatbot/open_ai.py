import os
from openai import OpenAI



client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def chat_with_gtp(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}]

    )

    # return response.choices[0].message.content.split()
    return response.choices[0].message.content



if __name__ == "__main__":
     while True:
         user_input= input("User: ")
         if user_input.lower() in ["quit", "exit", "bye"]:
             break

         response = chat_with_gtp(user_input)
         print("Chatbot: ", response)

