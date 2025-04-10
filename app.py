from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def prediction_model():
    number1 = float(request.args.get("number1", 0))
    number2 = float(request.args.get("number2", 0))
    prediction = int(number1 + number2 > 5.8)
    
    return jsonify({
        'prediction': prediction,
        'features': {
            'number1': number1,
            'number2': number2
        }
    })

if __name__ == "__main__":
    app.run()