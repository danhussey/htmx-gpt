from flask import Flask, render_template, request
import openai

openai.api_key = 'your-api-key-here'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    word = request.form.get('word')
    prompt = f"Generate a list of related words for '{word}'"
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
    words = response.choices[0].text.strip().split(', ')
    
    html = "<ul>"
    for word in words:
        html += f'<li hx-get="/generate" hx-params="word:\'{word}\'" hx-trigger="click" hx-swap="outerHTML" hx-indicator="#loadingIndicator" hx-include="#loadingIndicator">{word}</li>'
    html += "</ul>"
    
    return html

if __name__ == '__main__':
    app.run(debug=True)
