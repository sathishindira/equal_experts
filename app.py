"""
importing requried modules to collect and build the gist api server with uvicorn
"""
from fastapi import FastAPI, HTTPException
import requests
import uvicorn

app = FastAPI()

@app.get('/')
"""
Gists api root module for the welecome message
"""
def root():
    return {'message': 'Welcome to GitHub Gists API', 'usage': 'GET /{username}'}

@app.get('/health')
"""
Gists api health status monitoring
"""
def health():
    return {'status': 'healthy'}

@app.get('/{username}')
"""
Gists api collection for the provided username
"""
def get_gists(username: str):
    response = requests.get(f'https://api.github.com/users/{username}/gists',timeout=5)

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail='User not found')

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail='GitHub API error')

    gists = response.json()
    return [{
        'id': gist['id'],
        'description': gist['description'],
        'url': gist['html_url'],
        'files': list(gist['files'].keys())
    } for gist in gists]

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)

