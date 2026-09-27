from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Risk Predictor vulnerability test"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/users")
def get_user(username: str):
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE users (id INTEGER, username TEXT)"
    )

    cursor.execute(
        "INSERT INTO users VALUES (1, 'admin')"
    )

    # INTENTIONALLY VULNERABLE - SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    result = cursor.fetchall()
    connection.close()

    return {"users": result}