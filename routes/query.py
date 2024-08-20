from flask import Blueprint, request, jsonify,Response
from pandasai import SmartDataframe
import logging
from config import llm
from file_manager import FileManager
import pandas as pd

# Disable pandasai logging
logging.getLogger('pandasai').setLevel(logging.CRITICAL)

query_bp = Blueprint('query', __name__)
file_manager = FileManager()

@query_bp.route('/', methods=['POST'])
def query_data():
    data = request.json
    query = data.get('query')

    if not query:
        return jsonify({'error': 'Please provide a query to analyze your data.'}), 400
    
    df = pd.read_excel("uploaded_file.xlsx")  # Load the dataframe using pandas
    smart_df = SmartDataframe(df, config={"llm": llm})
    smart_df.save_logs = False
    smart_df.save_charts = False
    response = smart_df.chat(query)
    # Check if the response is a string and contains an error message
    if isinstance(response, pd.DataFrame):
        response = response.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries

    if isinstance(response, str) and "Unfortunately, I was not able to answer your question" in response:
        return jsonify({'error': 'There was an issue processing your query. Please check your data and query syntax.'}), 500

    try:
        # Attempt to jsonify the response
        return jsonify({'response': response}), 200
    except TypeError as e:
        # If the response is not JSON serializable, return it as a plain text response
        return Response(str(response), content_type="text/plain")

    # Check if the response is a string and contains an error message
