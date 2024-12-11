from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  
socketio = SocketIO(app, cors_allowed_origins="*")  

@app.route('/')
def index():
    return render_template('index.html')

messages = []  # Lista pentru stocarea mesajelor

@socketio.on('request_history')
def handle_history_request():
    emit('message_history', messages)

@socketio.on('message')
def handle_message(msg):
    messages.append(msg)  # Salvăm mesajul în listă
    emit('message', msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)