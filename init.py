# Import
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

# Init
app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/chains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Before first request
@app.before_first_request
def create_tables():
    db.create_all()

# Class DataModel
# @arg Object
class Chain(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	string = db.Column(db.String(200))
	hash = db.Column(db.String(200))
	algorithm = db.Column(db.String(200))

# Index route...
# [GET]
# @return response
@app.route('/')
def index():
	return render_template('index.html')

# Chain route...
# [GET|POST]
# @return response
@app.route('/chain', methods = ['GET', 'POST'])
def chain():
	# POST
	if request.method == 'POST':
		chain = Chain(string = request.form['string'], hash = request.form['hash'],	algorithm = request.form['algorithm'])
		db.session.add(chain)
		db.session.commit()
		return render_template('last.html', chain = last_chain(), message = 'Hash stored successfully')

	# GET
	return redirect(url_for('list'))

# List route...
# [GET]
# @return response
@app.route('/chain/list')
def list():
	chains = Chain.query.all()
	return render_template('list.html', chains = chains)

# Last chain support function
# @arg None
# @return Object
def last_chain():
	return Chain.query.order_by(desc(Chain.id)).first()

# Last route...
# [GET]
# @return response
@app.route('/chain/last')
def last():
	return render_template('last.html', chain = last_chain())

# Last json route...
# [GET]
# @return response
@app.route('/api/v1/chain/last')
def last_json():
	last = last_chain()
	if last:
		return jsonify(
			id = last.id,
			string = last.string,
			hash = last.hash,
			algorithm = last.algorithm)

	return jsonify(error = 'Database is empty... Please fill it')

# List json route...
# [GET]
# @return response
@app.route('/api/v1/chain/list', methods = ['GET'])
def list_json():
	chains = Chain.query.all()
	chain_json = {}

	for chain in range(0,len(chains)):
		chain_json[chain + 1] = chains[chain].hash	# TODO: Show all data from chains

	if chain_json:
		return jsonify(chain_json)

	return jsonify(error = 'Database is empty... Please fill it')

# Main
if __name__ == "__main__":
	app.run(debug = True)
