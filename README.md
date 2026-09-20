
🤖 SmartDocQA – Intelligent RAG-Based Document Question Answering System
------------------------------------------------------------------------------

SmartDocQA is an end-to-end Retrieval-Augmented Generation (RAG) application that allows employees to ask natural-language questions about company documents and receive concise, context-aware answers.

The system supports a multi-company architecture, where each company's documents are logically isolated using Pinecone namespaces.

==============================================================================


🚀 Project Overview
------------------------------------------------------------

Instead of manually searching through large company PDF documents, employees can ask questions in natural language and receive answers generated from the relevant company documents.

SmartDocQA combines:

- 📄 PDF document processing

- 🧠 Text embeddings

- 🔎 Semantic search

- 🗃️ Pinecone vector database

- 🤖 Groq-powered LLM inference

- ⚡ FastAPI backend

- ⚛️ React frontend

- 📊 RAG evaluation

- ☁️ Cloud deployment

==============================================================================


🏗️ System Architecture
------------------------------------------------------------------------------


                         ┌─────────────────┐

                         │      User       │

                         └────────┬────────┘

                                  │

                                  ▼

                         ┌─────────────────┐

                         │ React Frontend │

                         │     Vercel      │

                         └────────┬────────┘

                                  │

                                HTTPS

                                  │

                                  ▼

                         ┌─────────────────┐

                         │ FastAPI Backend │

                         │     Railway     │

                         └────────┬────────┘

                                  │

                    ┌─────────────┴─────────────┐

                    │                           │

                    ▼                           ▼

           ┌─────────────────┐         ┌─────────────────┐

           │    Pinecone     │         │    Groq API     │

           │  Vector Store   │         │       LLM       │

           └─────────────────┘         └─────────────────┘


✨ Features

📂 PDF document upload

📑 Page-wise PDF text extraction

✂️ Text chunking with overlap

🧠 SentenceTransformer embeddings

🔎 Semantic vector search

📚 Top-K relevant document retrieval

🤖 LLM-powered contextual answers

⚡ Groq API for fast inference

🏢 Multi-company architecture

🔐 Company-level document isolation using Pinecone namespaces

📧 Organization email-based company identification

👤 Automatic user name and company extraction

👨‍💼 Admin document upload workflow

👨‍💻 Employee question-answering workflow

💬 Chat-based interface

🌙 Dark mode

📊 RAG answer evaluation

☁️ Cloud deployment


🧠 How It Works

SmartDocQA follows a complete Retrieval-Augmented Generation pipeline.

PDF Document

     │

     ▼

Text Extraction

     │

     ▼

Text Chunking

     │

     ▼

Embedding Generation

     │

     ▼

Pinecone Vector Storage

     │

     │

     │ User Question

     ▼

Query Embedding

     │

     ▼

Semantic Search

     │

     ▼

Top-K Relevant Chunks

     │

     ▼

Groq LLM

     │

     ▼

Context-Aware Answer


🔄 RAG Pipeline

1. 📂 Document Upload

An administrator uploads a company PDF document.

Example:

amazon_policies.pdf

The document is processed and associated with the appropriate company.

2. 📑 Text Extraction

The uploaded PDF is processed and text is extracted page by page.

PDF

 ├── Page 1 → Text

 ├── Page 2 → Text

 ├── Page 3 → Text

 └── ...

3. ✂️ Text Chunking

The extracted text is divided into smaller overlapping chunks.

Document

 ├── Chunk 1

 ├── Chunk 2

 ├── Chunk 3

 └── ...

Each chunk can contain metadata such as:

Text

Page number

Company information

4. 🧠 Embedding Generation

Each text chunk is converted into a numerical vector representation using a SentenceTransformer embedding model.

Text Chunk

     │

     ▼

SentenceTransformer

     │

     ▼

Vector Representation

5. 🔎 Pinecone Vector Storage

Generated embeddings are stored in Pinecone.

Each company uses a separate namespace.

Pinecone

 ├── amazon

 ├── infosys

 ├── tcs

 └── hyniva

This provides logical company-level separation of document data.

6. 💬 User Query

An employee asks a question in natural language.

Example:

What dress code should I maintain?

The question is converted into an embedding.

Question

    │

    ▼

Query Embedding

    │

    ▼

Pinecone Search

7. 🎯 Semantic Retrieval

Pinecone searches the appropriate company namespace and retrieves the most relevant document chunks.

User Question

      │

      ▼

Query Embedding

      │

      ▼

Pinecone

      │

      ▼

Top-K Relevant Chunks

The retrieved chunks are passed to the LLM as context.

8. 🤖 LLM Answer Generation

The Groq-powered LLM receives the retrieved context and user question.

Retrieved Context

       +

User Question

       │

       ▼

   Groq LLM

       │

       ▼

Generated Answer

The system generates a concise, context-aware response.

🏢 Multi-Company Architecture

SmartDocQA is designed as a centralized multi-company system.

Each company has its own Pinecone namespace.

Amazon

   │

   └── Pinecone Namespace: amazon

TCS

   │

   └── Pinecone Namespace: tcs

Hyniva

   │

   └── Pinecone Namespace: hyniva

During retrieval, the user's company identity determines which namespace is searched.

This prevents documents from different companies from being mixed during retrieval.

📧 Organization Email Identification

The system can identify the user's company from their organization email.

Example:

teja@amazon.com

Extracted information:

Name    : Teja

Company : amazon

Email   : teja@amazon.com

The company information can then be used to determine the appropriate Pinecone namespace.

👨‍💼 Admin Workflow

Admin Login

     │

     ▼

Organization Email

     │

     ▼

Company Identification

     │

     ▼

Admin Dashboard

     │

     ▼

Upload Company PDF

     │

     ▼

PDF Text Extraction

     │

     ▼

Text Chunking

     │

     ▼

Embedding Generation

     │

     ▼

Pinecone Company Namespace

👨‍💻 Employee Workflow

Employee Login

     │

     ▼

Organization Email

     │

     ▼

Company Identification

     │

     ▼

Employee Dashboard

     │

     ▼

Ask Question

     │

     ▼

Query Embedding

     │

     ▼

Search Company Namespace

     │

     ▼

Retrieve Relevant Chunks

     │

     ▼

Groq LLM

     │

     ▼

Generated Answer

📊 RAG Evaluation

SmartDocQA includes evaluation mechanisms to monitor the quality of the RAG pipeline.

The evaluation tracks:

Retrieval Relevance

Answer Relevance

Faithfulness

Overall Evaluation Score

Number of Retrieved Chunks

Example:

============================================================

SMARTDOCQA LIVE EVALUATION

============================================================

Question: What is the dress code?

Retrieved Chunks: 5

Retrieval Relevance: 39.29%

Answer Relevance: 57.03%

Faithfulness: 68.52%

Overall Score: 54.95%

============================================================

These metrics can be used as signals for monitoring and debugging the RAG pipeline.

🛠️ Technology Stack

🎨 Frontend

React.js

JavaScript

HTML

CSS

Fetch API

Responsive UI

Chat Interface

⚡ Backend

Python

FastAPI

Uvicorn

REST APIs

🧠 AI / ML

Retrieval-Augmented Generation (RAG)

SentenceTransformers

Text Embeddings

Semantic Search

Large Language Models

🔎 Vector Database

Pinecone

🤖 LLM

Groq API

LLaMA-based model

📊 Evaluation

Retrieval Evaluation

Answer Relevance

Faithfulness

Context Evaluation

NumPy

Matplotlib

CSV-based Evaluation

☁️ Deployment

GitHub

Vercel

Railway

Pinecone Cloud

Groq API

📁 Project Structure

SmartDocQA-Project/

│

├── frontend/

│   ├── src/

│   ├── public/

│   └── package.json

│

├── routes/

│   ├── upload.py

│   └── query.py

│

├── utils/

│   ├── embeddings.py

│   ├── vector_store.py

│   └── ...

│

├── main.py

├── requirements.txt

├── .gitignore

└── README.md

🔐 Environment Variables

For local development, create a .env file in the project root.

PINECONE_API_KEY=your_pinecone_api_key

GROQ_API_KEY=your_groq_api_key

⚠️ Never commit API keys or .env files to GitHub.

For cloud deployment, configure environment variables through the hosting platform.

▶️ Local Setup

Backend

From the project root:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

Frontend

Navigate to the frontend directory:

cd frontend

Install dependencies:

npm install

Start the React application:

npm start

🔌 API Endpoints

📄 Upload Document

POST /upload

Uploads a company PDF, extracts its text, generates embeddings, and stores the vectors in the appropriate Pinecone namespace.

💬 Ask Question

POST /query

Accepts a user question and company identity, retrieves relevant company information, sends the context to the LLM, and returns the generated answer.

🗑️ Delete Company Documents

POST /delete

Deletes the corresponding company document data from the configured vector-store namespace.

🔒 Data Isolation

Company data is logically isolated using Pinecone namespaces.

Company A

    │

    ▼

Namespace A

Company B

    │

    ▼

Namespace B

Company C

    │

    ▼

Namespace C

The user's company identity determines which namespace is searched during retrieval.

☁️ Deployment Architecture

SmartDocQA uses a separated frontend and backend deployment architecture.

                         GitHub

                           │

              ┌────────────┴────────────┐

              │                         │

              ▼                         ▼

         frontend/                   Backend

              │                         │

              ▼                         ▼

           Vercel                    Railway

              │                         │

              │         HTTPS           │

              └────────────┬────────────┘

                           │

                  ┌────────┴────────┐

                  │                 │

                  ▼                 ▼

             Pinecone             Groq

           Vector Database          LLM

🎨 Frontend Deployment

The React frontend is deployed on:

Vercel

The frontend communicates with the FastAPI backend through HTTPS API requests.

⚡ Backend Deployment

The FastAPI backend is deployed on:

Railway

Railway runs the backend using:

uvicorn main:app --host 0.0.0.0 --port $PORT

The backend uses the following environment variables:

PINECONE_API_KEY

GROQ_API_KEY

🔎 Vector Database

Pinecone Cloud is used for:

Vector storage

Semantic search

Top-K retrieval

Company namespace isolation

🤖 LLM

Groq API is used for LLM inference and contextual answer generation.

🔄 Deployment Flow

Developer

    │

    ▼

Git

    │

    ▼

GitHub

    │

    ├──────────────► Vercel

    │                  │

    │                  ▼

    │             React Frontend

    │

    └──────────────► Railway

                       │

                       ▼

                  FastAPI Backend

                       │

                 ┌─────┴─────┐

                 ▼           ▼

             Pinecone      Groq

🚧 Current Limitations

Full production authentication and authorization can be further enhanced.

Complete role-based access control is a future enhancement.

Advanced retrieval reranking is not currently implemented.

Conversation history can be expanded.

Advanced document version management is not currently implemented.

RAG evaluation can be extended with more advanced techniques.


🔮 Future Enhancements


🔐 Authentication & Authorization

JWT authentication

Role-based access control

Admin and Employee permissions

Secure authorization workflow

🏢 Multi-Tenant Security

Enhanced company-level access control

Stronger tenant isolation

Organization-level authorization

📊 Advanced RAG Evaluation

Ground-truth evaluation

Advanced retrieval metrics

LLM-as-a-judge

Evaluation dashboard

📁 Document Management

Document update

Document deletion

Document version control

Multiple document management

💬 Chat Improvements

Conversation history

Persistent conversations

Follow-up questions

Streaming responses

🎨 UI Improvements

Improved accessibility

Mobile responsiveness

Enhanced chat experience

Additional UI animations

💡 Use Cases

🏢 Company Policy Assistant

👥 HR Knowledge Assistant

📚 Internal Documentation Search

🧑‍💼 Employee Self-Service Assistant

💬 Internal Knowledge Base

🤖 Organization-Specific AI Assistant

🎯 Project Goal

The goal of SmartDocQA is to transform static company documents into an intelligent, searchable knowledge system where employees can obtain concise answers through natural-language queries instead of manually searching through large PDF documents.

👨‍💻 Author

Brahma Teja Reddy Polu

B.Tech – Artificial Intelligence & Machine Learning

Chaitanya Bharathi Institute of Technology
