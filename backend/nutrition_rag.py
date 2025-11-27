import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NutritionRAG:
    def __init__(self):
        # Initialize the Gemini model
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        # Initialize embeddings
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        # Load and process the recipes dataset
        self.recipe_docs = self.load_recipes()
        
        # Create vector store
        self.vectorstore = self.create_vectorstore()
        
    def load_recipes(self):
        """Load and split the recipes dataset"""
        loader = TextLoader("recipes_nordestinas.txt", encoding='utf-8')
        documents = loader.load()
        
        # Split documents into chunks
        text_splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        docs = text_splitter.split_documents(documents)
        
        logger.info(f"Loaded {len(docs)} document chunks from recipes dataset")
        return docs
    
    def create_vectorstore(self):
        """Create the vector store from recipe documents"""
        vectorstore = Chroma.from_documents(
            documents=self.recipe_docs,
            embedding=self.embeddings,
            persist_directory="./chroma_db"
        )
        return vectorstore
    
    def get_relevant_recipes(self, query, k=4):
        """Retrieve relevant recipes based on the query"""
        retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": k}
        )
        relevant_docs = retriever.get_relevant_documents(query)
        return relevant_docs
    
    def answer_nutrition_query(self, query):
        """Answer nutrition-related queries using RAG"""
        # Check if the query is related to nutrition
        nutrition_related = self.is_nutrition_related(query)
        
        if not nutrition_related:
            return "Desculpe, só posso responder perguntas relacionadas à nutrição, nutrição esportiva, dietas, alimentos e receitas nordestinas."
        
        # Get relevant recipes
        relevant_docs = self.get_relevant_recipes(query)
        context = "\n".join([doc.page_content for doc in relevant_docs])
        
        # Format the response using the nutrition prompt
        from prompt_template import nutrition_prompt
        
        formatted_prompt = nutrition_prompt.format(
            context=context,
            question=query
        )
        
        # Generate response
        response = self.llm.invoke(formatted_prompt)
        
        return response.content
    
    def is_nutrition_related(self, query):
        """Check if a query is related to nutrition"""
        nutrition_keywords = [
            'nutrição', 'nutricional', 'dieta', 'proteína', 'carboidrato', 'gordura', 
            'calorias', 'vitamina', 'mineral', 'alimento', 'refeição', 'emagrecer', 
            'ganhar massa', 'ganho de massa', 'perda de peso', 'nutricionista', 
            'caloria', 'macro', 'micro', 'suplemento', 'reeducação', 'jejum',
            'proteina', 'carboidratos', 'gorduras', 'alimentos', 'receitas',
            'nordestina', 'nordestino', 'culinária', 'comida', 'feijão', 'arroz',
            'musculação', 'treino', 'ganho muscular', 'definição', 'hipertrofia'
        ]
        
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in nutrition_keywords)

# Example usage
if __name__ == "__main__":
    rag = NutritionRAG()
    response = rag.answer_nutrition_query("Quero ganhar massa magra, me sugira uma receita nordestina rica em proteínas")
    print(response)