
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Nyx Programadora está activa y lista para trabajar"}), 200

@app.route('/generar_codigo', methods=['POST'])
def generar_codigo():
    data = request.json
    lenguaje = data.get('lenguaje', 'python')
    funcionalidad = data.get('funcionalidad', 'default')

    if lenguaje.lower() == 'python':
        codigo = f"""def {funcionalidad}():
    print("Este es un código generado automáticamente")"""
    elif lenguaje.lower() == 'javascript':
        codigo = f"""function {funcionalidad}() {{
    console.log("Este es un código generado automáticamente");
}}"""
    else:
        return jsonify({"error": "Lenguaje no soportado"}), 400

    return jsonify({"codigo_generado": codigo}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
