import os
from flask import jsonify, request
from uuid import uuid4
from app import app
from .blockchain import Blockchain

blockchain = Blockchain()
node_address = str(uuid4()).replace('-', '')

@app.route('/mine-block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    
    blockchain.add_transaction(sender=node_address, receiver=os.environ.get('BLOCKCHAIN_RECEIVER'), amount=1)
    
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        'message': 'Congratulations! You mined a block.',
        'data': block
    }
    
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def chain():
    response = {
        'data': blockchain.chain
    }
    
    return jsonify(response), 200

@app.route('/chain/valid', methods=['GET'])
def chain_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    response = {
        'data': is_valid
    }
    
    return jsonify(response), 200

@app.route('/transaction', methods=['POST'])
def add_transaction():
    json_data = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    
    if not all(key in json_data for key in transaction_keys):
        return 'Some parameters are missing.', 400
    
    index = blockchain.add_transaction(sender=json_data['sender'], receiver=json_data['receiver'], amount=json_data['amount'])
    
    response = {
        'message': f'This transaction will be added to block {index}'
    }
    
    return jsonify(response), 201

@app.route('/node', methods=['POST'])
def connect_node():
    json_data = request.get_json()
    nodes = json_data.get('nodes', [])
    
    if not nodes:
        return 'Empty nodes list.', 400
    
    for node_url in nodes:
        blockchain.add_node(node_url)
        
    response = {
        'message': 'All nodes added to the blockchain',
        'data': list(blockchain.nodes)
    }
    
    return jsonify(response), 201

@app.route('/chain/replace', methods=['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    
    if is_chain_replaced:
        response = {
            'message': 'Chain replaced',
            'data': blockchain.chain
        }
    else:
        response = {
            'message': 'Chain not replaced',
            'data': blockchain.chain
        }
    
    return jsonify(response), 200