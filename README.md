# Language Translator

The Language Translator facilitates seamless translation between English and Kannada, and English and Gujarati. It supports bidirectional translations, enabling users to translate both to and from these languages. Features include a user-friendly interface, real-time translation, and high accuracy, making communication easier and more accessible.

## Features

- **Bidirectional Translation**: Translate text between English and Kannada, and English and Gujarati.
- **User-Friendly Interface**: Simple and intuitive UI built using Tkinter.
- **Real-Time Translation**: Provides instant translations as you type.
- **Custom Dictionary**: Uses a custom dictionary for common phrases to improve translation accuracy.
- **Google Translate Integration**: Utilizes Google Translate for phrases not found in the custom dictionary.

## Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/language-translator.git
    cd language-translator
    ```

2. **Install Dependencies**
    ```sh
    pip install googletrans==4.0.0-rc1
    ```

## Usage

1. **Run the Application**
    ```sh
    python translator_app.py
    ```

2. **Using the Translator**
    - Enter the text you want to translate in the input text box.
    - Click the "Translate" button to get the translation in the output text box.

## Example

Here's an example of translating "hello" from English to Gujarati:
- **Input**: hello
- **Output**: Dictionary Translated: નમસ્તે

## Project Structure

language-translator/
├── translator_app.py
├── README.md
└── requirements.txt


## Dependencies

1. **tkinter** - Standard Python interface to the Tk GUI toolkit.
2. **googletrans** - Free and unlimited Python library that implements Google Translate API.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
