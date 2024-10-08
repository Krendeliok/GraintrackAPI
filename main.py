from fastapi import FastAPI

from routes import route

app = FastAPI(debug=True, root_path="/api/v1")
route(app)


