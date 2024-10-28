# Inventory Tracking Service

This is a simple Flask application that serves inventory data.

## Getting Started

### Prerequisites

- Docker
- Python 3.x (for local testing)

### Running the Application Locally

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:
    ```bash
    python app.py
    ```

3. Access the application at `http://localhost:8080/inventory`.

### Building and Running with Docker

1. Build the Docker image:
    ```bash
    docker build -t inventory-tracking .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8080:8080 inventory-tracking
    ```

3. Access the application at `http://localhost:8080/inventory`.

