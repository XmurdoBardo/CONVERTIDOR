from flask import Flask, request, jsonify

app = Flask(__name__)

# Supongamos que tienes una tasa de conversión estática
conversion_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'GBP': 0.88},
    'GBP': {'USD': 1.33, 'EUR': 1.14},
}

@app.route('/convert')
def convert_currency():
    amount = float(request.args.get('amount'))
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    
    if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
        converted_amount = amount * conversion_rates[from_currency][to_currency]
        return jsonify({'convertedAmount': converted_amount})
    
    return jsonify({'error': 'Conversión no soportada'}), 400

if __name__ == '__main__':
    app.run(debug=True)
