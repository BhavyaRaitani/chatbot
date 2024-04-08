import os
import openai
import gradio as gr
"""
#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
#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
openai.api_key = "" #enter the key

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with a financial management assistant named Jerry. The assistant is very friendly, knowledgeable, resourceful, and dedicated to achieve all your financial goals and helping you understand the technical words or jargon in personal finance management.\n\nHuman: Hello, what services do you provide?\nAssistant: Hello I am Jerry and I'm here to assist you with all aspects of personal financial management. How can I assist you today?\nHuman: "
def openai_create(prompt):

    response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text"""

""" after this is the latest version code"""
from openai import OpenAI
api_key = "" #enter the key
prompt = "The following is a conversation with a financial management assistant named FineBot. The assistant is very friendly, knowledgeable, resourceful, and dedicated to achieve all your financial goals and helping you understand the technical words or jargon in personal finance management.\n\nHuman: Hello, what services do you provide?\nAssistant: Hello I am FineBot and I'm here to assist you with all aspects of personal financial management along with helping you understand the vocabulary of the Finance world. How can I assist you today?\nHuman: "

def openai_create(prompt):
    client = OpenAI(api_key=api_key)


    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].message['content']

def chatbot_Jerry(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>FineBot</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatbot_Jerry, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
