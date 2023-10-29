from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for the session

spell_checker_module = SpellCheckerModule()

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST', 'GET'])
def spell():
    corrected_text = ""
    corrected_grammar = []
    
    if request.method == 'POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        _, corrected_grammar = spell_checker_module.correct_grammar(text)
        
    return render_template('index.html', corrected_text=corrected_text, corrected_grammar=corrected_grammar)

@app.route('/grammar', methods=['POST', 'GET'])
def grammar():
    corrected_file_text = ""
    corrected_file_grammar = []
    
    if request.method == 'POST':
        file = request.files['file']
        try:
            readable_file = file.read().decode('utf-8', errors='ignore')
            corrected_file_text = spell_checker_module.correct_spell(readable_file)
            _, corrected_file_grammar = spell_checker_module.correct_grammar(readable_file)
        except Exception as e:
            # Handle the error, for example, print it for debugging purposes
            print("Error occurred:", e)
    
    return render_template('index.html', corrected_file_text=corrected_file_text, corrected_file_grammar=corrected_file_grammar)

# python main
if __name__ == "__main__":
    app.run(debug=True)
