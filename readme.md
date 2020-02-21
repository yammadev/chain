# Authors
- Yefferson MarÃ­n

# Simple Guide
## Development
### 1. Prepare
```sh
  # Clone
  $ git clone https://github.com/yammadev/chain.git
  $ cd chain

  # Install virtual environment
  $ python3 -m venv venv

  # Activate virtual environment
  $ . venv/bin/activate

  # Install flask
  $ pip install Flask

```

### 2. Run
```sh
  # Debug mode
  $ export FLASK_ENV="development"

  # Start
  $ export FLASK_APP=init.py
  $ flask run
  
  # Go to http://127.0.0.1:5000
```

# Simple Change log
## [1.0.0]
- Simple and minimal application
- Detailed readme
- Common `.gitignore` flask file
- Initial `Dockerfile`