from flask import Flask, request, jsonify, render_template, send_from_directory
import util

app = Flask(__name__, static_folder='../UI', template_folder='../UI')

# Serve the HTML file
@app.route('/')
def index():
   return render_template('app.html')

# Serve static files (CSS, JS, etc.)
@app.route('/<path:path>')
def serve_static(path):
   return send_from_directory(app.static_folder, path)

@app.route('/predict_price', methods=['POST'])
def predict_price():
   data = request.get_json()
   bed = data['bed']
   bath = data['bath']
   acre_lot = data['acre_lot']
   house_size = data['house_size']

   # Use the function from util.py
   estimated_price = util.price_predict(bed, bath, acre_lot, house_size)

   response = jsonify({
       'estimated_price': estimated_price  # No need to round here
   })
   return response

if __name__ == "__main__":
   print("Starting Python Flask Server for Philadelphia Home Price Prediction...")
   util.load_saved_artifacts()  # Load model and columns at startup
   app.run(debug=True)






