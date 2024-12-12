from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load data
routes = pd.read_csv('routes.txt', delimiter=',')
stops = pd.read_csv('stops.txt', delimiter=',')
trips = pd.read_csv('trips.txt', delimiter=',')
stop_times = pd.read_csv('stop_times.txt', delimiter=',')

# Merge dataframes to get the final dataset
stop_times_with_stops = pd.merge(stop_times, stops, on='stop_id', how='left')
stop_times_with_trips = pd.merge(stop_times_with_stops, trips, on='trip_id', how='left')
final_df = pd.merge(stop_times_with_trips, routes, on='route_id', how='left')

@app.route('/')
def home():
    return "Welcome to the API. Use /api/stops?route_id=<route_id> to get stops."

@app.route('/api/stops', methods=['GET'])
def get_stops():
    # Get route_id from query parameter
    route_id = request.args.get('route_id', type=int)
    
    # If route_id is not provided, return an error
    if route_id is None:
        return jsonify({"error": "route_id is required"}), 400
    
    # Filter stops based on route_id
    route_stops = final_df[final_df['route_id'] == route_id]
    
    # Get unique stop data
    unique_stops = route_stops[['stop_name', 'stop_id', 'stop_lat', 'stop_lon']].drop_duplicates()
    
    # Convert to list of dictionaries for JSON
    stops_data = unique_stops.to_dict(orient='records')
    
    return jsonify(stops_data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)
