FROM python:3.7-buster

# Install all extensions
RUN pip install Flask
RUN pip install SQLAlchemy
RUN pip install FlasK-SQLAlchemy
RUN apt-get update
RUN apt-get install sqlite3

# Create folders 
RUN mkdir static
RUN mkdir static/css
RUN mkdir static/js
RUN mkdir templates
RUN mkdir database

# Export (copy option) from Project to Docker container
COPY static/css/main.css  static/css
COPY static/js/md5.min.js static/js
COPY templates/* templates/
COPY init.py / 

# Flask option for run app
ENV FLASK_ENV="development"
ENV FLASK_APP="init.py"

CMD flask run --host 0.0.0.0