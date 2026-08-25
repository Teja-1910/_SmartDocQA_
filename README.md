📄 SMARTDOCQA – INTELLIGENT RAG-BASED DOCUMENT QUESTION ANSWERING SYSTEM

🤖 SmartDocQA is an end-to-end RAG-based document question-answering system designed to make internal company information easier and faster for HR admins and employees to access.

Instead of manually searching through large company PDF documents, users can ask questions in natural language and receive concise, context-aware answers based on their company’s documents.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 FEATURES

📂 PDF document upload
📑 Automatic page-wise text extraction
✂️ Text chunking with overlap
🧠 Embedding generation
🔎 Semantic search using Pinecone
📚 Top-K relevant document retrieval
🤖 LLM-based contextual answer generation
⚡ Fast responses using Groq API
🏢 Centralized multi-company architecture
🔐 Company-level document isolation using Pinecone namespaces
📧 Organization email-based company identification
👤 Automatic user name and company extraction
👨‍💼 Admin document upload workflow
👨‍💻 Employee question-answering workflow
💬 Modern chat-based UI
✨ Animated chat experience
🌙 Dark mode support
📊 Live answer evaluation
☁️ Cloud deployment support

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 HOW IT WORKS

SmartDocQA follows a complete Retrieval-Augmented Generation (RAG) pipeline.

📄 PDF Document
↓
📑 Text Extraction
↓
✂️ Text Chunking
↓
🧠 Embedding Generation
↓
🔎 Pinecone Vector Storage
↓
💬 User Question
↓
🧠 Query Embedding
↓
🔎 Semantic Retrieval
↓
📚 Top-K Relevant Chunks
↓
🤖 Groq LLM
↓
💡 Context-Aware Answer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 RAG PIPELINE

1️⃣ 📂 DOCUMENT UPLOAD

An administrator uploads a company PDF document.

Example:

amazon_policies.pdf

The system extracts the company name from the filename:

amazon

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ 📑 TEXT EXTRACTION

The uploaded PDF is processed and the text is extracted page by page.

📄 PDF
├── 📄 Page 1 → Text
├── 📄 Page 2 → Text
├── 📄 Page 3 → Text
└── …

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ ✂️ TEXT CHUNKING

The extracted text is divided into smaller overlapping chunks.

📄 Document
├── 🧩 Chunk 1
├── 🧩 Chunk 2
├── 🧩 Chunk 3
└── …

Each chunk stores metadata such as:

📝 Text
📄 Page number

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ 🧠 EMBEDDING GENERATION

Each text chunk is converted into a numerical vector representation using an embedding model.

📝 Text Chunk
↓
🧠 Embedding Model
↓
🔢 Vector Representation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ 🔎 PINECONE STORAGE

The generated embeddings are stored in Pinecone.

SmartDocQA uses company-specific namespaces for logical data isolation.

🔎 Pinecone

├── 🏢 amazon
├── 🏢 infosys
├── 🏢 tcs
└── 🏢 hyniva

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ 💬 USER QUERY

An employee asks a question in natural language.

Example:

“What dress code should I maintain?”

The query is converted into an embedding.

💬 Question
↓
🧠 Query Embedding
↓
🔎 Pinecone Search

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ 🎯 SEMANTIC RETRIEVAL

Pinecone searches the appropriate company namespace and retrieves the Top-K most relevant chunks.

💬 User Question
↓
🧠 Query Embedding
↓
🔎 Pinecone
↓
📚 Top 5 Relevant Chunks

The retrieved chunks are passed to the LLM as context.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ 🤖 LLM ANSWER GENERATION

The LLM receives the retrieved context and user question and generates a concise answer based on the retrieved information.

📚 Context
+
💬 Question
↓
🤖 Groq LLM
↓
💡 Concise Answer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏢 MULTI-COMPANY ARCHITECTURE

SmartDocQA is designed as a centralized multi-company system.

Each company has its own Pinecone namespace.

🏢 Amazon
↓
🔎 Pinecone Namespace: amazon

🏢 TCS
↓
🔎 Pinecone Namespace: tcs

🏢 Hyniva
↓
🔎 Pinecone Namespace: hyniva

During retrieval, the user’s company identity is used to determine which namespace should be searched.

This prevents the retrieval process from mixing documents belonging to different companies.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📧 ORGANIZATION EMAIL IDENTIFICATION

The system can identify the user’s company from their organization email.

Example:

teja@amazon.com

Extracted information:

👤 Name    : Teja
🏢 Company : amazon
📧 Email   : teja@amazon.com

The company name can then be used during document retrieval.

📧 teja@amazon.com
↓
🏢 amazon
↓
🔎 Pinecone Namespace: amazon

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👨‍💼 ADMIN WORKFLOW

👨‍💼 Admin Login
↓
📧 Organization Email
↓
🏢 Company Identification
↓
📊 Admin Dashboard
↓
📂 Upload PDF
↓
🏢 Extract Company Name
↓
📑 Extract PDF Text
↓
✂️ Chunk Text
↓
🧠 Generate Embeddings
↓
🔎 Store in Company Pinecone Namespace

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👨‍💻 EMPLOYEE WORKFLOW

👨‍💻 Employee Login
↓
📧 Organization Email
↓
👤 Extract Name + Company
↓
💻 Employee Dashboard
↓
💬 Ask Question
↓
🧠 Generate Query Embedding
↓
🔎 Search Company Namespace
↓
📚 Retrieve Top-K Chunks
↓
🤖 Send Context to LLM
↓
💡 Generate Concise Answer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 LIVE ANSWER EVALUATION

SmartDocQA performs evaluation on real user questions after the RAG pipeline generates an answer.

💬 User Question
↓
🔎 Retrieved Chunks
↓
🤖 Generated Answer
↓
📊 Evaluation
↓
🖥️ Console / API Result

The current evaluation checks:

🔤 Keyword Overlap
📚 Context Coverage
📏 Answer Length
📊 Overall Answer Status

The system categorizes the generated answer as:

🟢 GOOD
🟡 AVERAGE
🔴 POOR

Example:

============================================================

📊 SMARTDOCQA ANSWER EVALUATION

💬 Question:
What is the dress code?

💡 Generated Answer:
Employees should follow the formal dress code.

🔤 Keyword Overlap: 3
📚 Context Score: 0.67
📏 Answer Length: 51
📊 Status: GOOD

============================================================

This evaluation provides a simple quality signal for monitoring answers generated by the RAG pipeline.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🛠️ TECHNOLOGY STACK

🎨 FRONTEND

React.js
JavaScript
CSS
Fetch API
Modern responsive UI
Chat interface
Dark mode

⚡ BACKEND

Python
FastAPI
Uvicorn
REST APIs

🧠 AI / ML

Retrieval-Augmented Generation (RAG)
Text Embeddings
Semantic Search
Large Language Models

🔎 VECTOR DATABASE

Pinecone

🤖 LLM

Groq API
LLaMA 3.1

📊 EVALUATION

Keyword overlap
Context coverage
Answer length validation
Overall answer status

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 PROJECT STRUCTURE

🚀 SmartDocQA-Project/

├── 🐍 backend/
│   ├── main.py
│   │
│   ├── 📂 routers/
│   │   ├── upload.py
│   │   └── query.py
│   │
│   ├── 📂 utils/
│   │   ├── pdf_loader.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── llm.py
│   │   └── helpers.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── 🎨 frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── .gitignore
└── README.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️ ENVIRONMENT VARIABLES

Create a .env file inside the backend directory:

PINECONE_API_KEY=your_pinecone_api_key

GROQ_API_KEY=your_groq_api_key

⚠️ Never commit .env or API keys to GitHub.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

▶️ LOCAL SETUP

🐍 BACKEND SETUP

Navigate to the backend:

cd backend

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn main:app –reload

FastAPI Swagger UI:

http://127.0.0.1:8000/docs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎨 FRONTEND SETUP

Navigate to the frontend:

cd frontend

Install dependencies:

npm install

Start the frontend:

npm start

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔌 API ENDPOINTS

📄 UPLOAD DOCUMENT

POST /upload

Uploads a company PDF, extracts the text, generates embeddings, and stores the vectors in the appropriate Pinecone company namespace.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 ASK QUESTION

POST /query

Accepts a user question and company identity, retrieves relevant company information, sends the context to the LLM, and returns the generated answer along with the live evaluation result.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔐 DATA ISOLATION

Company data is logically isolated using Pinecone namespaces.

🏢 Company A
↓
🔎 Namespace A

🏢 Company B
↓
🔎 Namespace B

🏢 Company C
↓
🔎 Namespace C

The company identity is used during retrieval so that the system searches only the corresponding company’s namespace.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

☁️ DEPLOYMENT ARCHITECTURE

SmartDocQA uses a separated frontend and backend deployment architecture.

👤 User
↓
🎨 Vercel Frontend
↓
🔒 HTTPS
↓
⚡ FastAPI Backend
↓
┌─────────────────┬─────────────────┐
↓                                 ↓
🔎 Pinecone                     🤖 Groq
Vector Database                   LLM

DEPLOYMENT STACK

🎨 Frontend → Vercel
⚡ Backend → Render
🔎 Vector Database → Pinecone Cloud
🤖 LLM → Groq API

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚧 CURRENT LIMITATIONS

🔐 Full production authentication and authorization is still a future enhancement.

👥 Complete role-based access control is planned.

📁 Advanced document management is limited.

📊 Current evaluation is a basic quality evaluation system.

💬 Conversation history is not yet fully implemented.

📚 Advanced retrieval reranking is not yet implemented.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔮 FUTURE ENHANCEMENTS

🔐 AUTHENTICATION & AUTHORIZATION

• Secure user authentication
• JWT-based authentication
• Role-based access control
• Admin / Employee permissions
• Complete authorization workflow

🏢 MULTI-COMPANY SECURITY

• Enhanced company-level access control
• Secure tenant isolation
• Organization-level authorization

📊 ADVANCED EVALUATION

• Ground-truth based evaluation
• Advanced retrieval metrics
• LLM-as-a-judge evaluation
• Evaluation dashboard

📁 DOCUMENT MANAGEMENT

• Document update
• Document deletion
• Document version control
• Multiple document management

💬 CHAT IMPROVEMENTS

• Conversation history
• Persistent conversations
• Follow-up questions
• Improved streaming responses

🎨 UI ENHANCEMENTS

• Responsive mobile interface
• Advanced animations
• Improved accessibility
• Enhanced chat experience

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 USE CASES

🏢 Company policy assistant
👥 HR knowledge assistant
📚 Internal documentation search
🧑‍💼 Employee self-service assistant
💬 Internal knowledge base
🤖 Organization-specific AI assistant

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 PROJECT GOAL

The goal of SmartDocQA is to transform static company documents into an intelligent, searchable knowledge system where employees can obtain concise answers through natural-language queries instead of manually searching through large PDF documents.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👨‍💻 AUTHOR

Brahma Teja Reddy Polu

🎓 B.Tech - Computer Science and Engineering
🧠 Artificial Intelligence & Machine Learning
🏫 Chaitanya Bharathi Institute of Technology

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⭐ SMARTDOCQA

🤖 An intelligent RAG-based document question-answering system for centralized, multi-company knowledge access.
