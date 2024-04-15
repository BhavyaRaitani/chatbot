from bardapi import Bard, BardCookies
import os
import time
import gradio as gr

prompt = "The following is a conversation with a financial management assistant named FineBot. The assistant is very friendly, knowledgeable, resourceful, and dedicated to achieve all your financial goals and helping you understand the technical words or jargon in personal finance management.\n\nHuman: Hello, what services do you provide?\nAssistant: Hello I am FineBot and I'm here to assist you with all aspects of personal financial management along with helping you understand the vocabulary of the Finance world. How can I assist you today?\nHuman: "

def chat_create(input_text):
    os.environ['_BARD_API_KEY']="g.a000igisCZMjGQcgIjxuhoqwnIngMrkzq99_a6U837NsWafmUVap8ArwHODd8LsnWEDtPBekXAACgYKAUMSAQASFQHGX2MijaaFe0HkYOTn5S93bLGaVBoVAUF8yKrrO2sqO52vPmBkvKSdqVDH0076"
    #input_text="why is the sky blue?"
    cookie_dict = {
        "__Secure-1PSID": "g.a000igiRPfm4ALkWa99FoKhVzFBPcQYYfKj47x4imHDo0d-4airs9BDvdBmYQGet3OxlYLF5bQACgYKAYUSAQASFQHGX2MiyE9Q96l8-F-cgXZC_gPsIxoVAUF8yKpl-5ty01ZXrOJdyIJpyifx0076",
        
    }

    bard = BardCookies(cookie_dict=cookie_dict)
    return bard.get_answer(input_text)['content']

def chatbot_finebot(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = chat_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>FineBot</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatbot_finebot, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
