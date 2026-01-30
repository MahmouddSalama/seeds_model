from flask import Flask, request, jsonify
from load_model import pip_line
from load_model import soil_comparison


app = Flask(__name__)


@app.route('/')
def home():
	return "Hello world"

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    
    if request.method == 'POST':
        f = request.files['file']
        f.save('api\images\\'+f.filename)
      
        print('api\images\\'+f.filename)
        results = pip_line('api\images\\'+f.filename) 
        return jsonify(
            {
                'name':results,
                'info':soil_comparison[results]
            }
            )

if __name__ == "__main__":
    app.run(debug=True)