import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={
    'Content-Type':'application/json',
}

h:list[str]=[]

def generate_response(prompt):
    h.append(prompt)
    p="\n".join(h)
    data={
        "model":"mdl",
        "prompt": p,
        "stream":False
    }

    res=requests.post(url,headers=headers,data=json.dumps(data))

    if res.status_code==200:
        res=res.text
        data=json.loads(res)
        res1=data['response']
        return res1
    else:
        print("Error:", res.status_code, res.text)
        return "Error occurred while generating response."
    

interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=5,placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Assistant"),
    title="Code Assistant",
)

interface.launch()