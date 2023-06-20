from flask import Flask, request, render_template
import openai
import re

app = Flask(__name__)
openai.api_key = 'your-api-key-here'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        word = request.form.get('word')
        related_words = get_related_words(word)
        return render_template('word_list.html', word=word, words=related_words)
    return render_template('index.html')

@app.route('/explore', methods=['POST'])
def explore():
    word = request.form.get('word')
    related_words = get_related_words(word)
    return render_template('word_list.html', word=word, words=related_words)

def get_related_words(word):
    if request.method == 'POST':
        word = request.form.get('word')
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"Generate a comma separated list of 5 words related to the word {word}",
      temperature=0.5,
      max_tokens=60
    )
    words = response.choices[0].text.strip().split(", ")
    return words

if __name__ == '__main__':
    app.run(port=5000, debug=True)
