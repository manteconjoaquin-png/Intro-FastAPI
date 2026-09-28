from fastapi import FastAPI, Query, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI()

class ModelMovies(BaseModel):
        id:int
        title:str
        overview:str
        rating:float
        category:str
movies = [
    {
     "id": 1,
     "title": "Inception",
     "overview": "A thief who steals corporate",
     "rating": 8.8,
     "category": "Action"
     },
     {
     "id": 2,
     "title": "Titanic",
     "overview": "The story of the ill-fated ship",
     "rating": 7.5,
     "category": "Romance"
}
]

@app.get("/hola", tags=["Home"])
def index():
    return"Hello, World FastApi!"


@app.get("/movies",tags=["Movies"])
def movie():
    #return HTMLResponse("<h1>Movies</h1><p>Welcome to the Movies page!</p>")
    return movies


#@app.get("/movies/{id}", tags=["Movies"])
#def get_movie_by(id: int):
#    return id

@app.get("/movies/{id}", tags=["Movies"])
def get_movie_by_id(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return []


#@app.get("/movies/query/", tags=["Movies"])
#def get_movies_by_query(year:int, category:str):
#    return f"{year}-{category}"

@app.get("/movies/search/", tags=["Movies"])
def get_movies_by_categoryy(category: str):
    for movie in movies:
        if movie["category"].lower() == category.lower():
            return movie
    return []


@app.post("/movies", tags=["Movies"])
#def create_movie(id: int=Body(), title: str=Body(), overview: str=Body(), rating: float=Body(), category: str=Body()):
def create_movie(body: ModelMovies):
    movies.append(
        body
        )
    return movies

@app.put("/movies/{id}", tags=["Movies"])
def update_movie():
    pass