import os
from flask import Flask, redirect, render_template, request, url_for
from gpt_index import GPTSimpleVectorIndex
os.environ["OPENAI_API_KEY"] = "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"

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        query = request.form["question"]
        print("question:"+query)
        result = ask_ai(query)
        return redirect(url_for("index", result=result))
    result = request.args.get("result")
    return render_template("index.html",result=result)

def ask_ai(query):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True:
        response = index.query(query, response_mode="compact")
        print(f"Response: {response}")
        return response

if __name__ == '__main__':
    app.run()
