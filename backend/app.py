from flask import Flask, request, jsonify
from flask_cors import CORS
from nutrition_rag import NutritionRAG
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the NutritionRAG system
try:
    nutrition_rag = NutritionRAG()
    print("NutritionRAG system initialized successfully")
except Exception as e:
    print(f"Error initializing NutritionRAG: {e}")
    nutrition_rag = None

@app.route('/')
def home():
    return jsonify({"message": "Nutrição Nordestina API - Chatbot especializado em nutrição com receitas nordestinas"})

@app.route('/chat', methods=['POST'])
def chat():
    if not nutrition_rag:
        return jsonify({"error": "System not initialized properly"}), 500
        
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        
        # Get response from the nutrition RAG system
        response = nutrition_rag.answer_nutrition_query(user_message)
        
        return jsonify({
            "response": response,
            "message": user_message
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)