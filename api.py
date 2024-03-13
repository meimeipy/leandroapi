from flask import Flask, request
import requests  

app = Flask(__name__)

@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp():
    customer_number = request.json.get('number')
    
    url="https://appapi.watchat.com.br/api/messages/send"
    headers = { 
               "Authorization": "Bearer 1937DJ@ASS",
               "Content-Type": "application/json" 
              }
    Body= {
            "number": customer_number,
            "body":'Olá! Seja bem-vindo ao canal de atendimento da Asseguro Benefícios! Digite seu nome, em instantes iremos prosseguir com seu atendimento.'

          }
    response = requests.post(url, headers=headers, json=Body)
    print(response.text)
    print(response.status_code)
    if response.status_code == 200:
        return "true"
    else:
        return "false"
if __name__ == '__main__':
    app.run(debug=True)