import ollama   #llm model

from flask import Flask, request, render_template
app = Flask("short") 
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/uploadtext")
def upload_text():
    return render_template('uploadtext.html')

@app.route("/uploadtext")
def uploadtext():
    return render_template('uploadtext.html')



@app.route("/short", methods=['POST'])
def short_summarise():                   #eta holo short summary
    text = request.data.decode('utf-8')
    print(text)
    prompt = f"Summarise the text into a short version \n\n {text}"

    response = ollama.generate(
            model="mistral",
            prompt=prompt
            )
    print(response["response"])
    return response["response"]
       
@app.route("/medium", methods=['POST'])
def medium_summarise():                   #eta holo medium summary
    text = request.data.decode('utf-8')
    print(text)
    prompt = f"Summarise the text into a medium version \n\n {text}"

    response = ollama.generate(
            model="mistral",
            prompt=prompt
            )
    print(response["response"])
    return response["response"]

@app.route("/long", methods=['POST'])
def long_summarise():                   #eta holo short summary
    text = request.data.decode('utf-8')
    print(text)
    prompt = f"Summarise the text into a long version \n\n {text}"

    response = ollama.generate(
            model="mistral",
            prompt=prompt
            )
    print(response["response"])
    return response["response"]
