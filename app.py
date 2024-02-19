from flask import Flask, request, jsonify, render_template, abort  
from temperature import celsius_to_fahrenheit
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/convert', methods=['GET'])
def convert_temperature():
    """Convert temperature from Celsius to Fahrenheit and return JSON."""
    celsius_input = request.args.get('celsius', default=None)
    
    if celsius_input is not None:
        try:
            celsius = float(celsius_input)
        except ValueError:
            abort(400)
    else:
        celsius = 0

    fahrenheit = celsius_to_fahrenheit(celsius)
    return jsonify({'celsius': celsius, 'fahrenheit': fahrenheit})

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
