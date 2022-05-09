# Pokemon to Shakespeare 

 Small Flask app for handling GET requests 

# Requirements

- Docker  
- Python 3.7+ 

## How to run

1. Make sure Docker is installed and running
2. Navigate to project root in terminal window
3. Run the following: `docker image build -t docker-flask-api . ` to create docker image
4. `docker run -p 5000:5000 -d docker-flask-api`
5. Access the frontend via localhost:5000/
6. Although instructions are provided on the index page, to call query the API for a specific Pokemon use the following:
7. `http://localhost:5000/api/v1/shakespearify/pokemon?name=charizard` 

## Known issues

Due to rate limit imposed by Shakespeare API, the Poke2Shakespeare API can only make up to five requests each hour. After 5 attempts, the API will return a key error.
