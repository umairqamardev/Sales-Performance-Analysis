from flask import Flask, request, jsonify
import pandas as pd
import openai
import os

app = Flask(__name__)

# Load data function
def load_data():
    # Yahan par CSV ya JSON file se data load karne ka logic daalenge
    return pd.read_csv('sales_performance_data.csv')

# OpenAI call example
def generate_insights(data):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure your OpenAI API key is set as an environment variable
    response = openai.ChatCompletion.create(  # Corrected line
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Analyze this sales data: {data.to_json()}"}
        ]
    )
    return response['choices'][0]['message']['content']  # Access response correctly

@app.route('/')
def home():
    return "Welcome to the Sales Performance Analysis API!"

# Endpoint for individual sales representative performance
@app.route('/api/rep_performance', methods=['GET'])
def rep_performance():
    rep_id = request.args.get('rep_id')
    data = load_data()  # Load the data
    # Yahan par aap apna logic daalenge to analyze the performance for the specific representative
    insights = generate_insights(data)  # Generate insights
    return jsonify({"rep_id": rep_id, "insights": insights})

# Endpoint for overall team performance
@app.route('/api/team_performance', methods=['GET'])
def team_performance():
    data = load_data()  # Load the data
    # Yahan par aap apna logic daalenge to analyze overall team performance
    insights = generate_insights(data)  # Generate insights
    return jsonify({"message": "Overall team performance data", "insights": insights})

# Endpoint for sales performance trends and forecasting
@app.route('/api/performance_trends', methods=['GET'])
def performance_trends():
    time_period = request.args.get('time_period')
    data = load_data()  # Load the data
    # Yahan par aap apna logic daalenge to analyze trends based on the time period
    insights = generate_insights(data)  # Generate insights
    return jsonify({"message": f"Sales performance trends for {time_period}", "insights": insights})

if __name__ == '__main__':
    app.run(debug=True)