
from project import create_app
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import openai
from openai import OpenAI
client = OpenAI(api_key='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')

app = create_app()

def getNums():
    nums = []
    for i in range(7):
        item = request.form.get("SOMETHING" + str(i + 1))
        nums.append(item)
    return nums

@app.route('/', methods=['POST', 'GET'])
def index():
        if request.method == 'GET':
            return render_template('index.html')
        elif request.method == 'POST':
            factors = ["1","1","1","1","1","1","1"]
            paragraph = "I am going to give you a list of critera for songs. Here are the criteria:"
            nums = getNums()
            for i in range(7):
                paragraph += (" " + factors[i] + ": " + str(nums[i]) + "\n")
            message = {"role": "user", "content": paragraph}
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages = [{"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}]
            )
            print(completion.choices[0].message)
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
