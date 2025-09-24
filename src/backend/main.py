import ollama   #llm model
import PyPDF2
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask("main") 
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/uploadtext")
def upload_text():
    return render_template('uploadtext.html')

@app.route("/uploadtext")
def uploadtext():
    return render_template('uploadtext.html')
@app.route("/uploadpdf")
def uploadPdf():
    return render_template("uploadpdf.html")



@app.route("/short", methods=['POST'])
def short_summarise():                   #eta holo short summary
    text = request.data.decode('utf-8')
    print(text)
    prompt = f"Summarise the text into a short version \n\n {text}"

    response = ollama.generate(
            model="mistral",
            prompt=prompt
            )
    print(response["response"])
    return response["response"]
       
@app.route("/medium", methods=['POST'])
def medium_summarise():                   #eta holo medium summary
    text = request.data.decode('utf-8')
    print(text)
    prompt = f"Summarise the text into a medium version \n\n {text}"

    response = ollama.generate(
            model="mistral",
            prompt=prompt
            )
    print(response["response"])
    return response["response"]

@app.route("/long", methods=['POST'])
def long_summarise():                   #eta holo short summary
    text = request.data.decode('utf-8')
    print(text)
    prompt = f"Summarise the text into a long version \n\n {text}"

    response = ollama.generate(
            model="mistral",
            prompt=prompt
            )
    print(response["response"])
    return response["response"]


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/summarizepdfshort", methods=['POST'])
def summarize_pdf():
    # Check if the post request has the file part
    if 'pdf' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['pdf']
    
    # If user does not select file, browser might submit an empty part without filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Get summary length from form data
    summary_length = request.form.get('length', 'short')
    
    if file and allowed_file(file.filename):
        try:
            # Save the file temporarily
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Extract text from PDF
            text = ""
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
            
            # Clean up - remove the temporary file
            os.remove(filepath)
            
            if not text.strip():
                return jsonify({"error": "No text was found in the PDF file."}), 400
            
            # Generate summary using Ollama
            prompt = f"Summarize the following text into a {summary_length} version:\n\n{text}"
            
            response = ollama.generate(
                model="mistral",
                prompt=prompt
            )
            
            return jsonify(response["response"])
            
        except PyPDF2.errors.PdfReadError:
            return jsonify({"error": "Invalid PDF file"}), 400
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
    return jsonify({"error": "Invalid file type"}), 400

@app.route("/summarizepdfmedium", methods=['POST'])
def summarize_pdf_medium():
    # Check if the post request has the file part
    if 'pdf' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['pdf']
    
    # If user does not select file, browser might submit an empty part without filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Get summary length from form data
    summary_length = request.form.get('length', 'short')
    
    if file and allowed_file(file.filename):
        try:
            # Save the file temporarily
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Extract text from PDF
            text = ""
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
            
            # Clean up - remove the temporary file
            os.remove(filepath)
            
            if not text.strip():
                return jsonify({"error": "No text was found in the PDF file."}), 400
            
            # Generate summary using Ollama
            prompt = f"Summarize the following text into a {summary_length} version:\n\n{text}"
            
            response = ollama.generate(
                model="mistral",
                prompt=prompt
            )
            
            return jsonify(response["response"])
            
        except PyPDF2.errors.PdfReadError:
            return jsonify({"error": "Invalid PDF file"}), 400
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
    return jsonify({"error": "Invalid file type"}), 400

@app.route("/summarizepdflong", methods=['POST'])
def summarize_pdf_long():
    # Check if the post request has the file part
    if 'pdf' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['pdf']
    
    # If user does not select file, browser might submit an empty part without filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Get summary length from form data
    summary_length = request.form.get('length', 'short')
    
    if file and allowed_file(file.filename):
        try:
            # Save the file temporarily
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Extract text from PDF
            text = ""
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
            
            # Clean up - remove the temporary file
            os.remove(filepath)
            
            if not text.strip():
                return jsonify({"error": "No text was found in the PDF file."}), 400
            
            # Generate summary using Ollama
            prompt = f"Summarize the following text into a {summary_length} version:\n\n{text}"
            
            response = ollama.generate(
                model="mistral",
                prompt=prompt
            )
            
            return jsonify(response["response"])
            
        except PyPDF2.errors.PdfReadError:
            return jsonify({"error": "Invalid PDF file"}), 400
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
    return jsonify({"error": "Invalid file type"}), 400
