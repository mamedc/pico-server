from flask import Flask, request, jsonify

app = Flask(__name__)

# estado do LED guardado no servidor
estado_led = {"led": "off"}

@app.route("/")
def home():
    return "Servidor do Pico W ativo!"

@app.route("/update", methods=["POST"])
def update():
    """
    Pico envia dados (ex: sensores)
    """
    data = request.json
    print("Dados recebidos:", data)
    return "ok"

@app.route("/command", methods=["GET"])
def command():
    """
    Pico consulta se tem comandos (ex: ligar LED)
    """
    return jsonify(estado_led)

@app.route("/set_led/<state>", methods=["POST"])
def set_led(state):
    """
    Usuário (via navegador/app) define comando para o Pico
    """
    if state in ["on", "off"]:
        estado_led["led"] = state
        return f"LED definido como {state}"
    return "Comando inválido", 400
