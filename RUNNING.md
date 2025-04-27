# Running the Project

This guide explains how to set up and run the project locally.

## Prerequisites

1. **Python**: Ensure you have Python 3.8 or higher installed.
2. **Dependencies**: Install the required dependencies listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

3. **Docker (Optional)**: If you prefer to run the project in a container, ensure Docker is installed.

## Running Locally

1. Navigate to the `webapp` directory:

   ```bash
   cd webapp
   ```

2. Start the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000` to access the API.

4. To explore the API documentation, visit:

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Running with Docker

1. Build the Docker image:

   ```bash
   docker build -t webapp .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 webapp
   ```

3. Access the API at `http://127.0.0.1:8000`.

## Running Tests

To run the tests, use the following command:

```bash
pytest webapp/test_main.py
```

This will execute the test cases defined in `test_main.py`.

## Additional Notes

- The static files are served at `/ui`.
- The API includes endpoints for generating tokens and retrieving city data.

For any issues, refer to the [SECURITY.md](SECURITY.md) file for reporting vulnerabilities.