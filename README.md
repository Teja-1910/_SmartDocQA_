# 📄 SmartDocQA – Intelligent Document-Based Question Answering System

SmartDocQA is an AI-powered document question answering system designed for organizations. It enables users to upload documents and ask questions, receiving accurate answers based on document content using advanced AI techniques.

---

## 🚀 Features

- 📂 Upload PDF documents  
- ✂️ Automatic text extraction and chunking  
- 🧠 Semantic search using embeddings  
- 🔍 Context-based intelligent answers  
- ⚡ Fast response using Groq API (LLaMA 3)  
- 🗂️ Company-specific document filtering  
- 💬 Chat-based UI with typing animation  
- 🌙 Dark mode support  
- 📊 Basic answer evaluation system  

---

## 🧠 How It Works

1. User uploads PDF documents  
2. Text is extracted and split into chunks  
3. Each chunk is converted into embeddings  
4. Embeddings are stored in a vector database (Pinecone)  
5. User asks a question  
6. Query is converted into embedding  
7. Similar chunks are retrieved using cosine similarity  
8. Retrieved context is sent to LLM  
9. LLM generates answer based on context  

---

## 🏗️ Tech Stack

### 🔹 Frontend
- React.js  
- CSS (Custom UI)  
- Fetch API  

### 🔹 Backend
- FastAPI  
- Python  

### 🔹 AI & ML
- Sentence Transformers (Embeddings)  
- Groq API (LLaMA 3 Model)  

### 🔹 Database
- Pinecone (Vector Database)  

---

## 📊 Evaluation System

The system includes a basic evaluation mechanism to check answer quality:

- Context relevance check  
- Keyword overlap  
- Answer length validation  

This helps ensure that responses are meaningful and aligned with document content.

---

## 🌐 Deployment

The application is deployed using modern cloud platforms:

- Frontend → Vercel  
- Backend → Render  
- Vector Database → Pinecone (Cloud)  
- LLM → Groq API  

This architecture ensures scalability, accessibility, and real-time performance.

---

## 📁 Project Structure

SmartDocQA-Project/

├── backend/  
│   ├── main.py  
│   ├── query.py  
│   ├── helpers.py  
│   ├── embeddings.py  
│   └── requirements.txt  

├── frontend/  
│   ├── src/  
│   └── package.json  

├── .gitignore  
└── README.md  

---

## ⚙️ Setup Instructions

### Backend

pip install -r requirements.txt  
uvicorn main:app --reload  

### Frontend

npm install  
npm start  

---

## 🚧 Current Limitations

- Basic evaluation (not fully accurate)  
- No user authentication system  
- No multi-user data separation  
- Limited document management features  

---

## 🚀 Future Enhancements

### 🔐 User Authentication
- User registration and login system  
- JWT-based authentication  
- Role-based access (Admin / User)  

### 🏢 Multi-Company Support
- Separate document storage per company  
- Secure company-based access  

### 📊 Advanced Evaluation
- Embedding-based similarity scoring  
- Confidence score for answers  

### 📁 Document Management
- Update / delete documents  
- Version control  

### 💬 Chat Improvements
- Conversation history  
- Save previous queries  

### 📱 UI Enhancements
- Mobile responsiveness  
- Improved dark mode  
- Better chat experience  

---

## 💡 Use Cases

- Company policy assistant  
- HR knowledge system  
- Internal documentation search  
- Customer support automation  

---

## 👨‍💻 Author

Brahma Teja Reddy Polu  
Final Year B.Tech (AI & ML)  

---

## 📌 Conclusion

SmartDocQA demonstrates how modern AI technologies like embeddings, vector databases, and LLMs can be integrated to build intelligent and practical real-world applications for organization.