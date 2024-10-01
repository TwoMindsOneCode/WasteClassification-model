# WasteClassification-model
# Waste Classification Using Deep Learning

## Overview
This project aims to build a web application that utilizes a deep learning model to classify types of waste (glass, metal, paper, plastic) based on uploaded images. The application is built using Flask, allowing users to upload waste images, which are then analyzed to provide the appropriate classification.

## Objectives
- **Waste Classification**: Identify the type of waste by analyzing uploaded images.
- **Increase Environmental Awareness**: Assist in more efficient waste management.
- **Utilize Machine Learning**: Apply artificial intelligence techniques to address real-world problems.

## How It Works
1. **User Interface**: A simple web interface created using Flask allows users to upload images.
2. **Image Upload**: Users can upload images to the application.
3. **Image Processing**: The uploaded images are processed using OpenCV, resized to fit the model's input (150 × 150 pixels).
4. **Prediction**: The trained model predicts the type of waste by analyzing the image.
5. **Return Classification**: The classification result is returned to the user in a JSON response, indicating the predicted type of waste.

## Outcome
Upon uploading an image, the model accurately classifies it using deep learning techniques, assisting individuals in properly sorting waste. The model supports several categories: "Trash," "Metal," "Glass," "Paper," and "Plastic."

## Technologies Used
- **Python**: The programming language used to build the application.
- **Flask**: A framework for developing web applications.
- **OpenCV**: A library for image processing.
- **TensorFlow and Keras**: For building and training the deep learning model.
- **NumPy**: For handling arrays.
- **HTML/CSS**: For designing the user interface.

##Usage
Anyone interested in machine learning or waste management can use this project as a starting point to understand how artificial intelligence can be applied to environmental issues. The project also provides an interactive experience for users, allowing them to upload images and receive instant results on waste classification

