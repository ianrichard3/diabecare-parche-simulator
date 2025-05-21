from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Variables globales
glucose_level = 100
trend_level = "steady"

trend_factors = {
    "rapidly_falling": (-16, -8),
    "falling": (-8, -3),
    "steady": (-3, 3),
    "rising": (3, 8),
    "rapidly_rising": (8, 16)
}

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    global glucose_level, trend_level

    trend_options = list(trend_factors.keys())

    if request.method == 'POST':
        trend = request.form.get('trend')
        number = request.form.get('number_value')

        if trend in trend_factors:
            trend_level = trend
        
        try:
            glucose_level = float(number)
        except (TypeError, ValueError):
            pass

    return render_template(
        'dashboard.html',
        trend_options=trend_options,
        selected_trend=trend_level,
        number_value=glucose_level
    )


@app.route('/glucose', methods=['GET'])
def get_glucose():
    global glucose_level, trend_level

    factor = trend_factors.get(trend_level, 1.0)
    random_variation = random.uniform(factor[0], factor[1])
    glucose_level += random_variation
    glucose_level = round(glucose_level, 2)

    return jsonify({
        "glucose_level": glucose_level,
        "trend": trend_level,
        "variation": random_variation
    })

if __name__ == '__main__':
    app.run(debug=True)
