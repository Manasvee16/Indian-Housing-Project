from flask import Flask, request, app, jsonify, render_template
from src.pipelines.Prediction_Pipleline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def predict_datapoints():
    if request.method == 'GET':
        # Just show the form on a GET request
        return render_template('index.html')
    else:
        # This is the correct way to initialize CustomData
        data = CustomData(
            lcr=float(request.form.get('lcr')),
            lpz=float(request.form.get('lpz')),
            ia=float(request.form.get('ia')),
            wp=float(request.form.get('wp')),
            pl=float(request.form.get('pl')),
            rph=float(request.form.get('rph')),
            age=float(request.form.get('age')),
            dis=float(request.form.get('dis')),
            ha=float(request.form.get('ha')),
            tax=float(request.form.get('tax')),
            ptratio=float(request.form.get('ptratio')),
            ld=float(request.form.get('ld')),
            lip=float(request.form.get('lip'))
        )

        pred_df = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        # Format the result to look nice (e.g., "25.40")
        formatted_result = f"{result[0]:.2f}"

        # Pass the formatted result back to index.html
        return render_template('index.html', results=formatted_result)

## execution begin 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)