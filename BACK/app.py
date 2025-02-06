from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz # PyMuPDF
import json
import os
from nltk.corpus import stopwords
import nltk
import string


app = Flask(__name__)
CORS(app) #habilitar el cors porque el front viene desde otra ruta


UPLOAD_FOLDER = 'uploads' # Carpeta en la que se guardan los archivos subidos en este caso se encuentra sobre el mismo directorio
JSON_FOLDER = 'jsons' # Carpeta en la que se guardan los archivos jsons ya procesados
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_FOLDER'] = JSON_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'pdf'} #extensiones que se van a permitir subir a la carpeta

# Función para verificar que el archivo tenga la extensión correcta dentro de ALLOWED_EXTENSIONS
#FILTRO para PDF
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def PDF_procesor(PDF):
    # Abre el archivo PDF usando la ruta proporcionada
    pdf_document = fitz.open(PDF)
    words = []

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = clean_spanish_text(page.get_text("text"))
        words_list = text.split()
        words.extend(words_list)
    
    # Cierra el documento PDF después de extraer el texto
    pdf_document.close()
    
    return {"palabras": words}
    
def clean_spanish_text(text):
    """Funcion para eliminar StopWords con la librería nltk, ya que estamos en español tambien se reemplaza la letra ñ por una n """
    nltk.download('stopwords')
    stop_words = set(stopwords.words('spanish')) # incluye Artículos, Preposiciones, Pronombres, Conjunciones y Auxiliares.
    text = text.lower() #Paso el texto a minúsculas
    clean_words = []
    for char in text:
        if char == 'ñ' or char == 'Ñ':
            clean_words.append('n')  # Reemplaza la 'ñ' y 'Ñ' por 'n'
        elif char.isalnum() or char.isspace():  # Filtro alfanumérico y espacios
            clean_words.append(char)
    clean_text = "".join(clean_words)
    words = clean_text.split()

    clean_words = [word for word in words if word not in stop_words]

    return " ".join(clean_words)  



@app.route('/upload', methods=['POST']) # Ruta en la que se van a enviar los pdf
def upload_file():
    #Manejo de archivos si no hay 
    if 'file' not in request.files:
        return jsonify({'message': 'No hay archivo'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No se seleccionaron archivos'}), 400

    # Si el archivo es válido pasando por el filtro 
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)# guarda el archivo en la carpeta espesíficada en UPLOAD_FOLDER
        
        processed_data = PDF_procesor(filename)

        # Crea el archivo JSON
        json_filename = f"{os.path.splitext(filename)[0]}.json"
        json_path = os.path.join(app.config['JSON_FOLDER'], json_filename)

        os.makedirs(os.path.dirname(json_path), exist_ok=True)

        # Guarda el JSON
        with open(json_path, 'w') as json_file:
            json.dump(processed_data, json_file)
        
        return jsonify({
            'message': 'Archivo subido y procesado correctamente',
            'json_data': processed_data  # acá esta el json ya filtrado
        }), 200
        
    #si no pasa el filtro allowed files es porque no es PDF se enviará el siguiente mensaje
    return jsonify({'message': 'Archivo inválido solo se permiten PDF.'}), 400 

if __name__ == '__main__':    
    app.run(debug=True) # va a correr en el puerto 5000 sobre http://127.0.0.1:5000
