#  Playlist API (FastAPI)

##  Overview

A RESTful API built with FastAPI that allows users to create accounts, manage playlists, and add tracks. The system includes JWT-based authentication and relational database design with many-to-many relationships.

---

##  Features

* User registration and login
* JWT authentication
* Create and manage playlists
* Add/remove tracks from playlists
* Many-to-many relationship between playlists and tracks
* Secure, modular backend architecture

---

##  Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT (python-jose)

---

##  Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/playlist-api.git
cd playlist-api
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

### 5. Open API docs

Go to:
http://127.0.0.1:8000/docs

---

##  Authentication

* Login to receive JWT token
* Use token in Authorization header:

```
Authorization: Bearer <your_token>
```

---

##  Example Endpoints

### Create User

POST /users/

### Login

POST /users/login

### Create Playlist

POST /playlists/

### Add Track to Playlist

POST /playlists/{playlist_id}/add-track/{track_id}

---

##  What I Learned

* Designing RESTful APIs using FastAPI
* Implementing JWT authentication
* Working with relational databases and many-to-many relationships
* Structuring scalable backend applications

---

##  Future Improvements

* Pagination for large datasets
* Search functionality
* Deployment (Docker / cloud)
* Frontend integration

---
