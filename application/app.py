from flask import Flask
from flask import Flask
from flask import request
from flask import jsonify
from flask import send_from_directory
from flask import send_file
from flask_cors import CORS
import os
from flasgger import Swagger
import json
from flask import send_file
import os
app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

with open('listings.json' , 'rb') as file:
    listings = json.load(file)
    
RESULT_LIMIT = 5

def get_listings(city=None, bedrooms=None, bathrooms=None, amenities=None):
    # Filter listings based on the criteria
    def match_criteria(listing):
        city_match = listing['city'].lower() == city.lower() if city else True
        bedrooms_match = listing['bedrooms'] == bedrooms if bedrooms else True
        bathrooms_match = listing['bathrooms'] == bathrooms if bathrooms else True
        amenities_match = all(amenity in listing['amenities'] for amenity in amenities) if amenities else True

        return city_match and bedrooms_match and bathrooms_match and amenities_match

    # Return only the first 5 results that match the criteria
    return list(filter(match_criteria, listings))[:RESULT_LIMIT]

@app.route('/')
def hello():
    """
    Returns a simple hello message
    """
    return "app is running"


@app.route("/get-listings", methods=['GET'])
def get_listings_route():
    city = request.args.get('city')
    bedrooms = request.args.get('bedrooms', type=int)
    bathrooms = request.args.get('bathrooms', type=int)
    amenities = request.args.getlist('amenities')

    try:
        listings = get_listings(city, bedrooms, bathrooms, amenities)
        return jsonify(listings)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/openapi.yaml', methods=['GET'])
def get_openapi():
    return send_from_directory(os.path.dirname(__file__), 'openapi.yaml')

@app.route('/logo.png', methods=['GET'])
def logo():
    return send_from_directory(os.path.dirname(__file__), 'logo.png')

@app.route('/ai-plugin.json', methods=['GET'])
def ai_plugin():
    return send_from_directory(os.path.dirname(__file__), 'ai-plugin.json')

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)