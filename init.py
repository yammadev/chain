# Import
from flask import Flask, render_template, request, jsonify

# Init
app = Flask(__name__)

# Index route
# [GET]
@app.route('/')
def index():
	return render_template('index.html')

# Chain route
# [GET|POST]
@app.route('/chain', methods=['GET', 'POST'])
def chain():
	# POST
	if request.method == 'POST':
		return post(request.form['string'], request.form['hash'], request.form['algorithm'])

	# GET
	return list()

# Post function
# @arg string, string, string
# @return json
def post(string, hash, algorithm):
	return jsonify(string = string, hash = hash, algorithm = algorithm)

# List function
# @return string
def list():
	return 'return list template'	## TODO
