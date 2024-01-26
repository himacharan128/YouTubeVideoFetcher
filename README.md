# FamPay YouTube Video Fetcher

## Overview

This Flask application fetches YouTube videos based on a search query, stores them in a MySQL database, and provides an API to retrieve the latest videos.

## Table of Contents

- [Running the Server](#running-the-server)
- [Testing the API](#testing-the-api)
- [How to Use](#how-to-use)
- [Dependencies](#dependencies)
- [Features](#features)

## Running the Server

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/FamPay-YouTube-Video-Fetcher.git
2. **Navigate to the project folder:**
   ```bash
   cd FamPay-YouTube-Video-Fetcher
3. **Install dependencies:**
   ```bash
   pip install Flask Flask-SQLAlchemy APScheduler gevent requests mysql-connector-python
4. **Set up your database URI and YouTube API keys:**
   
    - Open `config.py`.
    - Replace `'your_database_uri_here'` in `SQLALCHEMY_DATABASE_URI` with your actual database URI.
    - Replace `'your_api_key_1_here'` and `'your_api_key_2_here'` in `API_KEYS` with your actual YouTube API keys.
5. **Initialize the database:**
   ```bash
   python manage.py
5. **Run the server:**
   ```bash
   python app.py

 ## Testing the API
 After running the server, you can test the API by making a GET request to http://localhost:5000/videos. You can also specify optional parameters such as page and per_page.
 ## How to Use
1. **Fetch Videos:**
        The server fetches YouTube videos with the search query 'latest news' at regular intervals.
2. **API Endpoint:**
        Use the /videos endpoint to get a paginated list of videos.
3. **Scheduled Job:**
        Videos are fetched and stored every 10 seconds (configurable).
## Dependencies
- Flask: Micro web framework for Python.
- Flask-SQLAlchemy: Flask extension for SQLAlchemy, the Python SQL toolkit.
- APScheduler: Advanced Python Scheduler for scheduling jobs.
- gevent: Coroutine-based Python networking library.
- requests: HTTP library for making API requests.
## Features
- Scheduled Video Fetching: Periodic fetching of YouTube videos based on a search query.
- RESTful API: Provides a clean API endpoint to retrieve the latest videos.
- Pagination: Supports paginated responses for video retrieval.



**Note:** Replace sensitive information in `config.py` with your actual credentials.

