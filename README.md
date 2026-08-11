# 🚀 How to Run

## Clone the Repository

```bash
git clone https://github.com/Arun-cmd-22/novacopilot-ai.git
cd novacopilot-ai
```

---

## Backend Setup

Go to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the `backend` folder.

Run the backend server:

```bash
uvicorn app.main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Go to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Create a `.env.local` file inside the `frontend` folder.

Run the frontend development server:

```bash
npm run dev
```

Frontend URL:

```
http://localhost:3000
```

---

## Database

Import the database:

```
database/novacopilot.sql
```

---

## Ollama

Start the Ollama service:

```bash
ollama serve
```

Download the model (first time only):

```bash
ollama pull llama3
```

Run the model:

```bash
ollama run llama3
```

Check installed models:

```bash
ollama list
```

---

## Build for Production

### Frontend

```bash
npm run build
npm start
```

### Backend

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```