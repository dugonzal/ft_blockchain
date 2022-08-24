import time
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, session
from datetime import datetime
import hashlib, json


class blockchain:
	def __init__(self):
		self.chain = []
		self.transaction_pendientes = []
		self.transaction(0, 0, 0) # se crea la transaccion genesis
		self.create_block(proof = 1, previous_hash = '0') # se crea el bloque genesis

	def create_block(self, proof, previous_hash):
		block = {
			'index': len(self.chain) + 1,
			'tiempo': str(datetime.now()),
			'transacciones': self.transaction_pendientes,
			'proof': proof,
			'previous_hash': previous_hash
			} # despues de agregar las transacciones, se limpian las transacciones pendientes para que no se repitan en la proxima creacion de bloque
		self.transaction_pendientes = [] #limpiar las transacciones pendientes
		self.chain.append(block) #agregar el bloque a la blockchain
		return block #retornar el bloque creado

	def anterior_bloque(self): #retornar el bloque anterior
		return self.chain[-1]

	def proof_of_work(self, previous_proof):
		new_proof = 1
		check_proof = False
		while check_proof is False:
			hash_operation = hashlib.sha256(str(new_proof**2 + previous_proof**2).encode()).hexdigest()
			if hash_operation[:4] == '4242': #si el hash empieza con 4242, es correcto
				check_proof = True
			else:
				new_proof += 1
		if check_proof is True:
			blockchain.transaction('4c6e7e2a9f2f7f7ff8e7d3d6c8b7c6e8e23a7', '4c6e7e2a9f2f7f7ff8e7d3d6c8b7c6e8e23a7', 42) #transaccion para minar
			print('Se ha minado un bloque con un hash de: ' + hash_operation, 'y se han recompesado al minero: ')
		return new_proof

	def hash(self, block): #funcion para calcular el hash del bloque
		encoded_block = json.dumps(block, sort_keys = True).encode() #se codifica el bloque
		return hashlib.sha256(encoded_block).hexdigest() #se retorna el hash del bloque

	def transaction(self, sender, recipient, amount): #funcion para agregar transacciones a la blockchain
		transaccion = {
			'sender': sender,
			'recipient': recipient,
			'amount': amount
			}
		self.transaction_pendientes.append(transaccion) #se agrega la transacc
		return transaccion #se retorna la transaccion


blockchain = blockchain()

print('El bloque creado es: ')


############################## flask appp web ################################################


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return r'<h1>ft_blockchain is going on!</h1>'

@app.route('/chain', methods=['GET'])
def chain():
	chain = {
		'chain': blockchain.chain,
		'length': len(blockchain.chain)
	}
	return jsonify(chain)

@app.route('/mine', methods=['GET'])
def mine():
	previous_block = blockchain.anterior_bloque()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	block = blockchain.create_block(proof, previous_hash)
	print ('Se ha minado un bloque con un hash de: ' + blockchain.hash(block))
	return jsonify(block), 200

@app.route('/transactions/new', methods=['POST', 'GET'])
def new_transaction():
	if request.method == 'GET':
		a = blockchain.transaction('4c6e7e2a9f2f7f7ff8e7d3d6c8b7c6e8e23a7', '4c6e7e2a9f2f7f7ff8e7d3d6c8b7c6e8e23a7', 1000) #transaccion para mi
		return jsonify(a), 200
	elif request.method == 'POST':
		values = request.get_json()
		required = ['sender', 'recipient', 'amount']
		if not all(k in values for k in required):
			return 'Missing values', 400
		blockchain.transaction(values['sender'], values['recipient'], values['amount'])
		print('Se ha agregado una transaccion a la blockchain' + str(values))
	return 'Transaccion agregada', 201
def main():
	app.run(debug=True)

if __name__ == '__main__':
	main()
