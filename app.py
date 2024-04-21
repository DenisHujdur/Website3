from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os
load_dotenv

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')


# Define your API endpoint for rendering the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Define your API endpoint for handling user input and returning ChatGPT response
@app.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    # Get the user's input from the request
    user_input = request.json.get('user_input')

    # Send the input to ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_input}]
    )

    # Get the response from ChatGPT
    gpt_response = response['choices'][0]['message']['content']

    # Return the response to the frontend
    return jsonify({'gpt_response': gpt_response})

if __name__ == '__main__':
    app.run(debug=True)