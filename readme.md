# Authors
- Yefferson Marín
- Jesus Caraballo
- Edgar Ropero

# Requirements
- Python
- Flask
- Sqlite3
- SQLAlchemy
- Docker

# Simple Development Guide
## Before to start
```sh
  # Clone
  $ git clone https://github.com/yammadev/chain.git
  $ cd chain
```

## Docker instructions
### 1. Run and update
```sh
  # Create an image
  $ docker build -t "image-name" .

  # Create a container from image
  $ docker run -p 5000:5000 "image-name"
```

### 2. Restart
```sh
  # Stop all containers
  $ docker stop $(docker ps -q)

  # Remove all containers
  $ docker rm $(docker ps -aq)
```

## Direct console instructions
### 1. Prepare
```sh
  # Install virtual environment
  $ python3 -m venv venv

  # (On Windows)
  $ py -3 -m venv venv

  # Activate virtual environment
  $ . venv/bin/activate

  # (On Windows)
  $ venv\Scripts\activate

  # Install flask
  $ pip install Flask

  # Install SQLAlchemy
  $ pip install SQLAlchemy

  # Install Flask-SQLAlchemy
  $ pip install Flask-SQLAlchemy
```

### 2. Run
```sh
  # Setting
  $ export FLASK_APP=init.py

  # (On Windows)
  $ set FLASK_APP=init.py

  # Debug mode
  $ export FLASK_ENV=development

  # (On Windows)
  $ set FLASK_ENV=development

  # Run
  $ flask run

  # Go to http://127.0.0.1:5000
```

### 3. Restart
```sh
  (venv) sqlite3 database/chains.db
  sqlite3> $ DELETE FRON chain ;

  # Close using ^Z (CTRL + Z)
```

# Simple Change log
## [1.3.4]
- `Docker` instructions updated.

## [1.3.3]
- Minimal changes.

## [1.3.2]
- `Readme` minimal change.

## [1.3.1]
- `Readme` minimal change.

## [1.3.0]
- `Docker` instructions added to `Dockerfile`.
- `Readme` updated for more detailed instructions.

## [1.2.0]
- `SQLAlchemy` integrated.
- `MD5 hash` now is stored in `SQL` database.
- All data is return in `JSON` and in `Views`

## [1.1.0]
- `MD5 hash` is generated based on a string in `index` template.
- `Form` data (string, hash, algorithm) is received via `POST` method and returned as `JSON`.
- Readability in code improved.
- Some `CSS` and `JS` libraries added.
- Front-end and scalability improved by using layouts.
- `Windows` instruction added to readme.

## [1.0.0]
- Simple and minimal application.
- Detailed `readme`.
- Common `.gitignore` flask file.
- Initial `Dockerfile`.
