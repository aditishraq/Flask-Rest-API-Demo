from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_temperature():
    if request.method == 'POST':
        data = request.get_json()

        if 'celsius' not in data:
            return jsonify({'error': 'Missing "celsius" parameter'}), 400

        try:
            celsius = float(data['celsius'])
        except ValueError:
            return jsonify({'error': 'Invalid input for "celsius", must be a number'}), 400

        fahrenheit = (celsius * 9/5) + 32

        return jsonify({'celsius': celsius, 'fahrenheit': fahrenheit})

    # Handle GET request, render the HTML page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
