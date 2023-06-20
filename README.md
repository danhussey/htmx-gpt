# Interactive Word Explorer

Interactive Word Explorer is a web application that lets users explore related words with the help of OpenAI's GPT-3 and HTMX.

## Features

- Submit a word to generate a list of related words.
- Click on any word in the list to generate a new list.
- View a loading indicator while the list is being generated.

## Installation

Before you start, make sure you have Python 3.7 or later installed on your system. You can download Python from the official website.

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/interactive-word-explorer.git
    cd interactive-word-explorer
    ```

2. Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

4. Open your web browser and navigate to `http://localhost:5000` to use the application.

## Usage

Enter a word into the form on the main page and submit the form. The application will generate a list of related words. Click on any word in the list to generate a new list of words related to the clicked word.

## Notes

The OpenAI API is a paid service, and it is rate limited. Be sure to read and understand OpenAI's pricing and usage rules before using this application. This application should be used responsibly.

This is a demo application, and is not suitable for production use without further modifications. It does not handle errors from the OpenAI API, and does not secure the OpenAI API key.

## License

This project is licensed under the GNU GENERAL PUBLIC License. See the LICENSE file for details.
