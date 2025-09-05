from flask import Flask, request, jsonify
from services.firebase_service import db, bucket
from services.embeddings import get_embedding
from utils.similarity import cosine_similarity
import os

app = Flask(__name__)

# Add memory (text + optional image)
@app.route('/memories', methods=['POST'])
def add_memory():
    data = request.json
    user_id = data['user_id']
    text = data['text']
    tags = data.get('tags', [])
    memory_ref = db.collection('users').document(user_id).collection('memories').document()
    
    # Store in Firestore
    memory_ref.set({
        'text': text,
        'tags': tags,
        'created_at': firestore.SERVER_TIMESTAMP
    })
    
    # Create embedding
    embedding = get_embedding(text)
    memory_ref.update({'embedding': embedding})
    
    return jsonify({'memory_id': memory_ref.id}), 200

# Search memories using embedding similarity
@app.route('/search', methods=['POST'])
def search():
    data = request.json
    user_id = data['user_id']
    query = data['q']
    query_emb = get_embedding(query)
    
    docs = db.collection('users').document(user_id).collection('memories').stream()
    results = []
    for d in docs:
        mem = d.to_dict()
        if 'embedding' in mem:
            score = cosine_similarity(query_emb, mem['embedding'])
            results.append((score, d.id, mem))
    
    results.sort(key=lambda x: x[0], reverse=True)
    top5 = results[:5]
    
    return jsonify({'hits':[{'id':r[1], 'score':r[0], 'text':r[2]['text']} for r in top5]}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
