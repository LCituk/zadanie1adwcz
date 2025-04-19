from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1.0/predict")
def predict():
    try:
        num1 = float(request.args.get("num1", 0))
        num2 = float(request.args.get("num2", 0))
    except ValueError:
        return jsonify({"error": "Nieprawidłowe dane wejściowe. Upewnij się, że num1 i num2 to liczby."}), 400

    suma = num1 + num2
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

