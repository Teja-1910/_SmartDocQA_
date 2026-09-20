<<<<<<< HEAD
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
=======
# SmartDocQA

SmartDocQA is an end-to-end RAG-based document question-answering system designed to make internal company information easier and faster for HR admins and employees to access.

Instead of manually searching through large company PDF documents, employees can ask questions in natural language and receive concise, context-aware answers based on their company's documents.

## Features

- PDF document upload and text extraction
- Text chunking with overlap
- Embedding-based semantic retrieval
- Pinecone vector database
- LLM-powered contextual answers
- Centralized multi-company architecture
- Company-level data isolation using Pinecone namespaces
- Organization email-based company identification
- Automatic user name and company extraction
- Natural-language document querying
- Live RAG evaluation
- Offline RAG evaluation
- FastAPI backend
- React frontend

## System Architecture

SmartDocQA

Admin User / Employee
        |
        v
React Frontend
        |
        v
FastAPI Backend
        |
        +-----------------------+
        |                       |
        v                       v
Document Upload           User Query
        |                       |
        v                       v
PDF Text Extraction       Query Embedding
        |                       |
        v                       v
Text Chunking             Pinecone Search
        |                       |
        v                       v
Embedding Generation      Top-K Relevant Chunks
        |                       |
        v                       v
Pinecone Storage          Retrieved Context
        |                       |
        +-----------+-----------+
                    |
                    v
                   LLM
                    |
                    v
              Final Answer

## RAG Pipeline

### 1. Document Upload

An admin uploads a company PDF.

Example:

amazon_policies.pdf

The system extracts the company name from the filename:

amazon

### 2. Text Extraction

The uploaded PDF is processed and text is extracted page by page.

PDF
 |
 +-- Page 1 -> Text
 +-- Page 2 -> Text
 +-- Page 3 -> Text
 +-- ...

### 3. Text Chunking

The extracted text is divided into smaller overlapping chunks.

Document
   |
   +-- Chunk 1
   +-- Chunk 2
   +-- Chunk 3
   +-- ...

Each chunk contains metadata such as:

- text
- page

### 4. Embedding Generation

Each text chunk is converted into a numerical vector representation using an embedding model.

Text Chunk
    |
    v
Embedding Model
    |
    v
Vector

### 5. Pinecone Storage

The generated vectors are stored in Pinecone.

Each company uses a separate namespace.

Pinecone
 |
 +-- amazon
 |
 +-- infosys
 |
 +-- tcs
 |
 +-- hyniva

This provides logical company-level data isolation.

### 6. User Query

An employee asks a question in natural language.

Example:

What dress code should I maintain?

The question is converted into an embedding.

Question
   |
   v
Embedding
   |
   v
Pinecone Search

### 7. Semantic Retrieval

Pinecone searches the company's namespace and retrieves the top-K most semantically relevant chunks.

Question
   |
   v
Pinecone
   |
   v
Top 5 Relevant Chunks

The retrieved chunks are provided to the LLM as context.

### 8. LLM Generation

The LLM receives the retrieved context and user question and generates a concise answer based on the retrieved information.

## Multi-Company Architecture

SmartDocQA follows a centralized multi-company architecture.

Company identity can be extracted from the user's organization email.

Example:

teja@amazon.com

The system extracts:

Name: teja
Company: amazon

The company name is then used to identify the appropriate Pinecone namespace.

teja@amazon.com
        |
        v
     amazon
        |
        v
Pinecone namespace: amazon

Similarly:

teja@tcs.com
        |
        v
      tcs
        |
        v
Pinecone namespace: tcs

This allows multiple companies to use the same centralized application while keeping their document data logically isolated.

## User Identity

The system extracts user information directly from the organization email.

Example:

brahmateja@amazon.com

Extracted information:

Name: brahmateja
Company: amazon
Email: brahmateja@amazon.com

The extracted information can be displayed in the user's profile.

## Admin Workflow

Admin Login
     |
     v
Organization Email
     |
     v
Company Identification
     |
     v
Admin Dashboard
     |
     v
Upload Company PDF
     |
     v
Extract Company Name
     |
     v
Extract PDF Text
     |
     v
Chunk Text
     |
     v
Generate Embeddings
     |
     v
Store in Company Pinecone Namespace

## Employee Workflow

Employee Login
      |
      v
Organization Email
      |
      v
Extract Name + Company
      |
      v
Employee Dashboard
      |
      v
Ask Question
      |
      v
Generate Query Embedding
      |
      v
Search Company Namespace
      |
      v
Retrieve Top-K Chunks
      |
      v
Send Context to LLM
      |
      v
Generate Concise Answer

## RAG Evaluation

SmartDocQA includes evaluation of the RAG pipeline to measure retrieval and answer-generation quality.

The evaluation is divided into:

1. Live Evaluation
2. Offline Evaluation

## Live Evaluation

Every real question asked through the SmartDocQA application can be evaluated after the RAG pipeline generates an answer.

User Question
      |
      v
Query Embedding
      |
      v
Pinecone Retrieval
      |
      v
Retrieved Chunks
      |
      v
LLM
      |
      v
Generated Answer
      |
      v
Live Evaluation
      |
      v
Console Metrics

The current live evaluation tracks:

- Retrieval Relevance
- Answer Relevance
- Faithfulness
- Overall Evaluation Score
- Number of Retrieved Chunks

Example console output:

============================================================
SMARTDOCQA LIVE EVALUATION
============================================================

Question:
What is the dress code?

Generated Answer:
Business casual attire is recommended unless otherwise specified.

Retrieved Chunks: 5

Retrieval Relevance: 39.29%
Answer Relevance:    57.03%
Faithfulness:        68.52%
Overall Score:       54.95%

============================================================

The live metrics are used as evaluation signals for monitoring and debugging the RAG pipeline.

## Offline Evaluation

SmartDocQA also supports controlled evaluation using a fixed evaluation dataset.

The evaluation dataset contains:

- Question
- Reference Answer
- Relevant Page

Example:

{
  "question": "What dress code should employees follow?",
  "reference_answer": "Business casual attire is recommended unless otherwise specified.",
  "relevant_pages": [4]
}

The offline evaluation can be used to measure:

### Retrieval Metrics

- Hit@5
- Mean Reciprocal Rank (MRR)
- Context Relevance

### Generation Metrics

- Faithfulness
- Answer Relevance
- Answer Correctness

This makes it possible to systematically compare different RAG configurations.

## Evaluation Architecture

Evaluation Dataset
        |
        v
    Question
        |
        v
    Embedding
        |
        v
    Pinecone
        |
        v
   Top-K Chunks
        |
        +----------------+
        |                |
        v                v
Retrieval Metrics       LLM
        |                |
        |                v
        |         Generated Answer
        |                |
        |       +--------+--------+
        |       |        |        |
        v       v        v        v
      Hit@5  Faithfulness
      MRR    Relevance
             Correctness

## Evaluation Metrics

### Hit@5

Measures whether at least one relevant chunk appears within the top 5 retrieved chunks.

Relevant chunk in Top 5 -> Hit
Relevant chunk not in Top 5 -> Miss

### Mean Reciprocal Rank (MRR)

Measures how highly the first relevant chunk is ranked.

A higher MRR means relevant information is generally appearing closer to the top of the retrieval results.

### Retrieval Relevance

Measures how semantically relevant the retrieved chunks are to the user's question.

### Answer Relevance

Measures whether the generated answer is relevant to the user's question.

### Faithfulness

Measures whether the generated answer is supported by the retrieved context.

### Answer Correctness

Measures whether the generated answer agrees with the reference answer in the controlled evaluation dataset.

## Technology Stack
>>>>>>> 69a6289 (Updated with project screenshots)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<<<<<<< HEAD
5️⃣ 🔎 PINECONE STORAGE
=======
- Python
- FastAPI
- Uvicorn

### AI / ML

- Retrieval-Augmented Generation (RAG)
- Text Embeddings
- Semantic Search
- Large Language Models

### Vector Database

- Pinecone

### LLM

- Groq API
- Llama 3.1
>>>>>>> 69a6289 (Updated with project screenshots)

The generated embeddings are stored in Pinecone.

<<<<<<< HEAD
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
=======
- React
- JavaScript
- HTML
- CSS

### Evaluation

- Embedding-based similarity
- Retrieval evaluation
- RAG evaluation
- NumPy
- Matplotlib
- CSV-based evaluation results

## Project Structure

SmartDocQA/
|
+-- backend/
|   |
|   +-- main.py
|   |
|   +-- routers/
|   |   +-- upload.py
|   |   +-- query.py
|   |
|   +-- utils/
|   |   +-- pdf_loader.py
|   |   +-- chunking.py
|   |   +-- embeddings.py
|   |   +-- vector_store.py
|   |   +-- llm.py
|   |   +-- helpers.py
|   |
|   +-- evaluation/
|   |   +-- evaluation.py
|   |   +-- dataset.json
|   |
|   +-- requirements.txt
|   +-- .env
|
+-- frontend/
    |
    +-- src/
    +-- public/
    +-- package.json

## Environment Variables

Create a .env file in the backend:

PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key

Never commit API keys or .env files to GitHub.

## Running the Backend

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

## Running the Frontend

Install dependencies:

npm install

Start the development server:

npm start

## API Endpoints

### Upload Document

POST /upload

Uploads a company PDF, extracts its text, generates embeddings, and stores the vectors in the company's Pinecone namespace.

### Ask Question

POST /query

Accepts a user question and company identity, retrieves relevant company information, generates an answer using the LLM, and performs live evaluation.

## Data Isolation

Company data is isolated using Pinecone namespaces.

Company A
    |
    v
Namespace A

Company B
    |
    v
Namespace B

Company C
    |
    v
Namespace C

During retrieval, the user's company identity determines which namespace is searched.

## Deployment Architecture

User
 |
 v
Vercel Frontend
 |
 | HTTPS
 v
FastAPI Backend
 |
 +----------------+
 |                |
 v                v
Pinecone         Groq
Vector DB         LLM

The frontend and backend are deployed separately, while Pinecone and Groq are accessed securely through the backend.

## Project Goal

The goal of SmartDocQA is to transform static company documents into an intelligent, searchable knowledge system where employees can obtain concise answers through natural-language queries instead of manually searching through large PDF documents.

## Future Enhancements

- Complete authentication and authorization
- Role-based access control
- Admin and employee permission management
- Improved retrieval strategies
- Reranking of retrieved chunks
- Advanced RAG evaluation
- Evaluation dashboard
- Conversation history
- Document management
- Multi-document support
- Production monitoring and logging

## Author

Brahma Teja Reddy Polu

B.Tech - Computer Science and Engineering (Artificial Intelligence & Machine Learning)

Chaitanya Bharathi Institute of Technology

## SmartDocQA

An intelligent RAG-based document question-answering system for centralized, multi-company knowledge access.
>>>>>>> 69a6289 (Updated with project screenshots)
