from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Configuration for file uploads
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Isochrone Fitting Page
@app.route('/isochrone-fitting', methods=['GET', 'POST'])
def isochrone_fitting():
    if request.method == 'POST':
        # Process form data
        model = request.form.get('model')
        temperature = float(request.form.get('temperature'))
        luminosity = float(request.form.get('luminosity'))

        # Call your Python backend function for isochrone fitting
        # Example: result = isochrone_fit(model, temperature, luminosity)
        result = {
            'mass': 1.2,  # Example result
            'age': 100,   # Example result
        }

        # Render the results
        return render_template('isochrone_fitting.html', result=result)

    return render_template('isochrone_fitting.html')

# Mass-Magnitude Modeling Page
@app.route('/mass-magnitude-modeling', methods=['GET', 'POST'])
def mass_magnitude_modeling():
    if request.method == 'POST':
        # Process form data
        model = request.form.get('model')
        mass_range = request.form.get('massRange')
        age = float(request.form.get('age'))
        mag_filter = request.form.get('filter')

        # Call your Python backend function for mass-magnitude modeling
        # Example: result = mass_magnitude_model(model, mass_range, age, mag_filter)
        result = {
            'regression_plot': 'regression_plot.png',  # Example result
            'model_report': 'Model built successfully.',  # Example result
        }

        # Render the results
        return render_template('mass_magnitude_modeling.html', result=result)

    return render_template('mass_magnitude_modeling.html')

# Mathematical Modeling Page
@app.route('/mathematical-modeling', methods=['GET', 'POST'])
def mathematical_modeling():
    if request.method == 'POST':
        # Process form data
        target = request.form.get('target')
        features = request.form.getlist('features')  # Get multiple selected features

        # Call your Python backend function for mathematical modeling
        # Example: result = mathematical_model(target, features)
        result = {
            'pca_plot': 'pca_plot.png',  # Example result
            'regression_report': 'Regression model built successfully.',  # Example result
        }

        # Render the results
        return render_template('mathematical_modeling.html', result=result)

    return render_template('mathematical_modeling.html')

# File Upload Route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Process the uploaded file (e.g., load it into a DataFrame)
        data = pd.read_csv(file_path)
        flash('File uploaded successfully')
        return redirect(url_for('home'))

    flash('Invalid file type')
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)