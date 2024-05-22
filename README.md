# Application Name
/application

## Description

This is a Flask application that provides several endpoints for different purposes. It includes a hello endpoint, an endpoint to get listings, and endpoints to serve static files like `openapi.yaml`, `logo.png`, and `ai-plugin.json`.

## Installation

1. Clone the repository.
2. Install the required Python packages by running `pip install -r requirements.txt` in the `application` directory.

## Running the Application

1. Navigate to the `application` directory.
2. Run the application with the command `flask run --host 0.0.0.0`.

## Endpoints

- `GET /`: Returns a simple hello message.
- `GET /get-listings`: Returns a list of listings based on the provided criteria.
- `GET /openapi.yaml`: Returns the OpenAPI specification file.
- `GET /logo.png`: Returns the logo image.
- `GET /ai-plugin.json`: Returns the AI plugin configuration file.

## Hosting The API on Azure
- Create a Docker Image and push it to Azure Container Registry
- Publish a webapp based on the image contained in the Azure Container Registry