# Este é um exemplo de como o backend poderia ser em Python usando Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-apps')
def get_apps():
    # Aqui você pode buscar a lista de apps do banco de dados
    apps = [
        {'name': 'App 1', 'description': 'Esta é a descrição do App 1'},
        {'name': 'App 2', 'description': 'Esta é a descrição do App 2'},
        # ...
    ]
    return jsonify(apps)

if __name__ == '__main__':
    app.run()
