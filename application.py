from flask import Flask, request, render_template, jsonify
import os
from src.logger import logging
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CustomData(
            levy=float(request.form.get('levy'))
            manufacturer=request.form.get('manufacturer'),
            year=int(request.form.get('year')),
            category=request.form.get('category'),
            leather_interior=int(request.form.get('leather_interior')),
            fuel_type=request.form.get('fuel_type'),
            engine_volume=float(request.form.get('engine_volume')),
            mileage=int(request.form.get('mileage')),
            cylinders=float(request.form.get('cylinders')),
            gear_box_type=request.form.get('gear_box_type'),
            drive_wheels=request.form.get('drive_wheels'),
            doors=request.form.get('doors'),
            wheel=request.form.get('wheel'),
            color=request.form.get('color'),
            airbags=int(request.form.get('airbags')),
            turbo=int(request.form.get('turbo'))
        )
        
        pred_df = data.get_data_as_dataframe()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)
        results = round(pred[0], 2)
        return render_template('index.html', results=results, pred_df=pred_df)

@app.route('/predictAPI', methods=['POST'])
def predict_api():
    if request.method == 'POST':
        data = CustomData(
            levy=float(request.json['levy']),
            manufacturer=request.json['manufacturer'],
            year=int(request.json['year']),
            category=request.json['category'],
            leather_interior=int(request.json['leather_interior']),
            fuel_type=request.json['fuel_type'],
            engine_volume=float(request.json['engine_volume']),
            mileage=int(request.json['mileage']),
            cylinders=float(request.json['cylinders']),
            gear_box_type=request.json['gear_box_type'],
            drive_wheels=request.json['drive_wheels'],
            doors=int(request.json['doors']),
            wheel=request.json['wheel'],
            color=request.json['color'],
            airbags=int(request.json['airbags']),
            turbo=int(request.json['turbo'])
        )
        
        pred_df = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)

        dct = {'price': round(pred[0], 2)}
        return jsonify(dct)

if __name__ == '__main__':
    handler = logging.FileHandler('flask.log')  # Create a file handler
    handler.setLevel(logging.ERROR)  # Set the logging level to ERROR
    application.logger.addHandler(handler)  # Add the handler to your app's logger
    application.run(host='0.0.0.0', port = 8000)