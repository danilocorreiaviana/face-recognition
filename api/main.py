from flask import Flask, request, jsonify
import face_recognition

app = Flask(__name__)

def compare_faces(image_path1, image_path2):
    # Carrega as imagens e codifica os rostos
    image1 = face_recognition.load_image_file(image_path1)
    face_encoding1 = face_recognition.face_encodings(image1)[0]

    image2 = face_recognition.load_image_file(image_path2)
    face_encoding2 = face_recognition.face_encodings(image2)[0]

    # Compara as codificações dos rostos
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)
    
    return results[0]

@app.route('/', methods=['GET'])
def home():
    return """
        <center>
            <br>
            <h1><b>Bem-vindo(a) à API de Reconhecimento Facial</h1></b>
            <br>
            <br>
            <br>
            <br>
            <br>
            Acesse a rota POST 'https://face-recognition.vercel.app/compare_faces' para realizar o reconhecimento facial
            <br>
            <br>
            <br>
            <br>
            <br>
            <h2>Criado por <b>Danilo Correia</b></h2>
        </center>
    """

@app.route('/compare_faces', methods=['POST'])
def compare_faces_api():
    # Recebe as imagens no corpo da requisição
    data = request.json
    image_path1 = data['image_path1']
    image_path2 = data['image_path2']

    # Compara os rostos
    result = compare_faces(image_path1, image_path2)

    # Retorna o resultado em JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
