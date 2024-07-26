import tkinter as tk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.text_input = tk.Text(self.root, wrap=tk.WORD, width=70, height=30)
        self.text_input.pack(fill=tk.BOTH, expand=True)

        translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        translate_button.pack(pady=10)

        # Text widget to display translated text
        self.translated_text_widget = tk.Text(self.root, wrap=tk.WORD, width=70, height=10)
        self.translated_text_widget.pack(fill=tk.BOTH, expand=True)
        self.translated_text_widget.config(state=tk.DISABLED)

        # Google Translator instance
        self.translator = Translator()

        # Custom translation dictionary (English to Gujarati)
        self.translation_dict = {
            "hello": "નમસ્તે",
            "how are you": "કેમ છો",
            "good morning": "શુભ સવાર",
            "good afternoon": "શુભ અપરાહ્ન",
            "good evening": "શુભ સાંજ",
            "thank you": "ધન્યવાદ",
            "please": "કૃપા કરીને",
            "sorry": "ક્ષમા કરો",
            "how is it going": "તમારે કેવી રીતે જઈતું છે",
            "see you later": "ફરી મુલાકાત",
        }

    def translate_text(self):
        # Get the content from the input text box
        input_text = self.text_input.get("1.0", tk.END)

        # Translate the text from English to Gujarati
        translated_text, translation_source = self.translate_to_gujarati(input_text)

        # Enable the text widget and set the translated text
        self.translated_text_widget.config(state=tk.NORMAL)
        self.translated_text_widget.delete("1.0", tk.END)
        self.translated_text_widget.insert(tk.END, f"{translation_source}: {translated_text}")
        self.translated_text_widget.config(state=tk.DISABLED)

    def translate_to_gujarati(self, text):
        # Check if the phrase is found in the dictionary
        if any(phrase.lower() in text.lower() for phrase in self.translation_dict):
            # Simple translation logic using the custom dictionary
            for key, value in self.translation_dict.items():
                text = text.replace(key, value)
            return text.strip(), "Dictionary Translated"
        else:
            # Use Google Translate for phrases not found in the dictionary
            try:
                google_translation = self.translator.translate(text, dest='gu').text
                return google_translation.strip(), "Google Translated"
            except Exception as e:
                return f"Error in translation: {str(e)}", "Translation Error"

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
