
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
        item = request.form.get("mood_input_" + str(i + 1))
        nums.append(str(item))
    return nums

@app.route('/', methods=['POST', 'GET'])
def index():
        if request.method == 'GET':
            return render_template('index.html')
        elif request.method == 'POST':
            factors = ["1","1","1","1","1","1","1"]
            nums = getNums()
            paragraph = "Give me a list of songs that meet the criteria on a scale of 0-5. Happy(" + nums[0] + "), Sad(" + nums[1] + "), calm(" + nums[2] + "), energetic(" + nums[3] + "), nostalgic(" + nums[4] + "), romantic(" + nums[5] + "), and inspirational(" + nums[6] + "). Return one string of 5 song titles separated by a semicolon without the artist"
            message = {"role": "user", "content": paragraph}
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages = [{"role": "user", "content": paragraph}]
            )
            item = completion.choices[0].message.content
            print(paragraph)
            print(completion.choices[0].message)
            song_names_str = item.strip('"')  # Remove leading and trailing quotes
            song_names_list = [song.strip() for song in song_names_str.split(';')]

            print(song_names_list)
            return redirect('/playlist')
        
@app.route('/playlist', methods=['GET'])
def playlist():
     if request.method == 'GET':
          return render_template('playlist.html')

if __name__ == '__main__':
    app.run(debug=True)
