from re import L
from fastapi import (
    APIRouter
)
from app.v1.schemas.blockchain import *

blockchain = APIRouter(prefix="/blockchain")

node_identifier = str(uuid4()).replace('-', '')
 
blockchain_obj = Blockchain()

@blockchain.get("/mine")
async def mine_event():
    return "Coming soon....."

@blockchain.post("/transaction/new")
async def new_transaction_event(transaction: Transaction):
    index = blockchain_obj.new_transaction(transaction.sender, transaction.recipient, transaction.amount)
 
    response = {'message': f'Transaction will be added to Block {index}'}

    return response

@blockchain.get("/chain")
async def full_chain():
    response = {
        'chain': blockchain_obj.chain,
        'length': len(blockchain_obj.chain),
    }
    return response

@blockchain.post("/nodes/register")
async def register_node(nodes: Nodes):
    for node in nodes.nodes:
        blockchain_obj.register_node(node)
    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain_obj.nodes),
    }
    return response

@blockchain.get("/nodes/resolve")
async def consensus():
    replaced = blockchain_obj.resolve_conflicts()
    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain_obj.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain_obj.chain
        }
    return response

@blockchain.get("/nodes/active")
async def nodes_list():
    return {"nodes":list(blockchain_obj.nodes)}
