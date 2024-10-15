# Sales-Performance-Analysis

## Overview
This project implements a backend system that uses a Large Language Model (LLM) to analyze sales data and provide feedback on both individual sales representatives and overall team performance.

### Architecture
The system is built using Flask as the backend framework, utilizing Python for implementation. It integrates OpenAI's GPT-3.5-turbo for data analysis, supporting both CSV and JSON data formats.

## Technology Stack
- **Backend Framework**: Flask
- **Programming Language**: Python
- **Large Language Model**: OpenAI's GPT-3.5-turbo
- **Data Formats Supported**: CSV and JSON
- **Development Environment**: Replit

## API Endpoints
### 1. Individual Sales Representative Performance Analysis
- **Endpoint**: /api/rep_performance
- **Method**: GET
- **Parameters**: 
  - rep_id (unique identifier for the sales representative)
- **Function**: Returns detailed performance analysis and feedback for the specified sales representative.

### 2. Overall Sales Team Performance Summary
- **Endpoint**: /api/team_performance
- **Method**: GET
- **Function**: Provides a summary of the sales team’s overall performance.

### 3. Sales Performance Trends and Forecasting
- **Endpoint**: /api/performance_trends
- **Method**: GET
- **Parameters**: 
  - `time_period (e.g., monthly, quarterly)
- **Function**: Analyzes sales data over the specified time period to identify trends and forecast future performance.

## Setup and Run Instructions
1. Clone this repository.
2. Navigate to the project directory.
3. Install the required dependencies:
   
   pip install -r requirements.txt

4.Set your OpenAI API key in the environment variables:
      
  export OPENAI_API_KEY='your_openai_api_key'

5.Run the application:
  
  python app.py

6.Access the API endpoints via the browser or API testing tools like Postman or Insomnia.
