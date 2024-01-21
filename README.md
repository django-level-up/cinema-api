# Cinema API

The Cinema API project provides an interface to interact with the Cinema application, allowing users to retrieve data from the Django server.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/django-level-up/cinema-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd cinema-api
    ```

3. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    # or
    .\venv\Scripts\activate  # For Windows

    pip install -r requirements.txt
    ```

4. Run the API:

    ```bash
    uvicorn main:app --reload --port 8080
    ```

5. Access the Swagger documentation:

    Open [http://localhost:8080/docs](http://localhost:8080/docs) in your browser to interact with the API and explore available endpoints.

## Project Dependencies

- FastAPI
- httpx

## Note

Ensure that the Django server of the Cinema application is running and accessible at the URL specified in the `main.py` file. Update the URL if necessary.
