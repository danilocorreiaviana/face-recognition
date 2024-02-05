from flask import Flask, request, jsonify
import face_recognition

app = Flask(__name__)

def compare_faces(image1, image2):
    try:
        # Carregue as imagens
        img1 = face_recognition.load_image_file(image1)
        img2 = face_recognition.load_image_file(image2)

        # Obtenha os descritores faciais
        face_encoding1 = face_recognition.face_encodings(img1)[0]
        face_encoding2 = face_recognition.face_encodings(img2)[0]

        # Compare os descritores faciais
        result = face_recognition.compare_faces([face_encoding1], face_encoding2)

        return True if result[0] else False

    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return "<center><b><h1>Bem-vindo à api de Reconhecimento Facial</h1></b></center>"

@app.route('/compare_faces', methods=['POST'])
def compare_faces_api():
    try:
        # Obtenha as imagens do corpo da solicitação
        image1 = request.files['image1']
        image2 = request.files['image2']

        # Verifique se as imagens têm o rosto da mesma pessoa
        result = compare_faces(image1, image2)

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
