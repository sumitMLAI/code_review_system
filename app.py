from flask import Flask, request, jsonify, render_template
from services.review import review_code
import os




# Initialize Flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_code():
    data = request.get_json()
    code = data.get('code')
    language = data.get('language')
    if not code or not language:
        return jsonify({'error': 'Code and language are required.'})

    try:
        review = review_code(code, language)
        return jsonify({'review': review})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9000)
