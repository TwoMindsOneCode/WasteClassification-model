from flask import Flask, render_template, request, jsonify, send_from_directory
import cv2
import numpy as np
import os
import tensorflow as tf

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('metal_glass_paper_plastic_model_with_augmentation.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    file = request.files['image']
    if file:
        img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (150, 150))
        img = np.expand_dims(img, axis=0)
        class_probabilities = model.predict(img)[0]
        class_labels = {0: 'Trash', 1: 'Metal', 2: 'Glass', 3: 'Paper', 4: 'Plastic'}
        predicted_class = class_labels[np.argmax(class_probabilities)]
        return jsonify({'predicted_class': predicted_class})
    return jsonify({'error': 'No file provided'})

# Serve static files from the templates directory
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'templates'), filename)

if __name__ == '__main__':
    app.run(debug=True)

    
