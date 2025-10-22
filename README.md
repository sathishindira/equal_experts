GitHub Gists API:

A simple HTTP web server that fetches and displays a GitHub user's public Gists.

Setup and Run:

Using Docker (Recommended)

1. Build the container:
```bash
docker build -t gists-api .
```

2. Run the container:
```bash
docker run -p 8080:8080 gists-api
```

3. Test the API:
```bash
curl http://localhost:8080/octocat
```

Local Development:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python app.py
```

3. Run tests:
```bash
pytest test_app.py
```

API Usage:

Endpoint: 

GET /<username>
GET / - Returns API info and usage instructions
GET /health - Returns health status (useful for container health checks)

Example:
```bash
curl http://localhost:8080/octocat
```

Response for GET /<username> endpoint: JSON array of gists with id, description, url, and files.
