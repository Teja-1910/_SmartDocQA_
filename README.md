# SmartDocQA 🚀

## 📌 About Project
SmartDocQA is an AI-based system where companies can upload their documents (PDFs) and users can ask questions from those documents.

The main idea of this project is to build a centralized system where company data is stored and can be accessed easily using simple questions.



## ⚙️ What this project does
- Admin uploads PDF files  
- System processes and stores the document data  
- User asks questions  
- System gives answers only from the uploaded document  



## 🧠 How it works
1. Admin uploads a PDF  
2. Text is extracted from the PDF  
3. Text is divided into small chunks  
4. Chunks are converted into embeddings  
5. Stored in ChromaDB  
6. User asks a question with company name  
7. System finds the most relevant data  
8. LLM generates the answer  



## 🛠 Technologies Used
- FastAPI (Backend)  
- Python  
- ChromaDB (Vector Database)  
- Sentence Transformers (Embeddings)  
- Groq API (LLM)  
- PyPDF2 (PDF Processing)  



## 🚀 How to Run
pip install -r requirements.txt  
uvicorn main:app --reload  

Open in browser:  
http://127.0.0.1:8000/docs  



## 🔐 API Key Setup
Set your Groq API key using:  

setx GROQ_API_KEY "your_api_key_here"  

Restart terminal after setting the key.



## 📌 Features
- Supports multiple companies  
- Data stored separately for each company  
- Fast semantic search using embeddings  
- Clean API using FastAPI  
- Accurate answers based only on document  



## 📈 Future Improvements
- Login system using company email  
- Role-based access (Admin/User)  
- React frontend UI  
- Cloud deployment  
- Better UI/UX  



## 👨‍💻 Author
Brahma Teja Reddy Polu
