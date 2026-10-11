import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import create_retrieval_chain  
from langchain_classic.chains.combine_documents import create_stuff_documents_chain  
from langchain_core.prompts import ChatPromptTemplate

# Page Configuration
st.set_page_config(page_title="Enterprise AI Document Agent", page_icon="🤖", layout="wide")

st.title("🤖 Enterprise AI Document Analytics Agent")
st.caption("Locally Parsed Retrieval-Augmented Generation (RAG) Pipeline")

# Sidebar for Configurations
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Enter Gemini API Key (For Chat Only):", type="password")
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    st.markdown("---")
    st.markdown("### Tech Stack Used:")
    st.code("• Python\n• Streamlit\n• LangChain v1.0+\n• ChromaDB\n• HuggingFace Embeddings\n• Gemini Flash LLM")

# File Upload Utility
uploaded_file = st.file_uploader("Upload a Corporate PDF / Invoice / Report", type=["pdf"])

if uploaded_file and api_key:
    # Save file temporarily to disk
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    with st.spinner("Processing document... Extraction, Chunking & Vectorization in progress."):
        try:
            # 1. Load Document
            loader = PyPDFLoader(temp_file_path)
            docs = loader.load()
            
            # 2. Chunk Text (Optimized for context windowing)
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.split_documents(docs)
            
            # 3. Initialize Embeddings & Vector Store (Running locally, no API limits)
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
            retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
            
            # 4. Set up LLM & Prompts (Perfectly aligned alignment)
            llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.3)
            
            system_prompt = (
                "You are an expert corporate AI assistant. Answer the user's question accurately using only the "
                "provided context below. If you do not know the answer, state that it is not available in the text.\n\n"
                "Context:\n{context}"
            )
            prompt = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                ("human", "{input}"),
            ])
            
            # 5. Create RAG Chain
            question_answer_chain = create_stuff_documents_chain(llm, prompt)
            rag_chain = create_retrieval_chain(retriever, question_answer_chain)
            
            st.success("Document analyzed successfully! Your AI agent is live.")
            
            # Chat User Interface Block
            user_query = st.text_input("Ask anything about the uploaded document:")
            if user_query:
                with st.spinner("Analyzing context vector matrices..."):
                    response = rag_chain.invoke({"input": user_query})
                    
                    st.markdown("### 🎯 AI Agent Response:")
                    st.write(response["answer"])
                    
                    # Show Source Context to prove it's a real RAG pipeline
                    with st.expander("🔍 View Context Blocks Retrieved from ChromaDB"):
                        for i, doc in enumerate(response["context"]):
                            st.markdown(f"**Chunk {i+1} (Page {doc.metadata.get('page', 'Unknown') + 1}):**")
                            st.caption(doc.page_content)
                            
        except Exception as e:
            st.error(f"An error occurred during processing: {str(e)}")
            
        finally:
            # Clean up local file storage safely
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

elif uploaded_file and not api_key:
    st.warning("Please enter your Gemini API Key in the sidebar to run the application pipelines.")
