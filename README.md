AI Chatbot Project – Commands Used
1️⃣ Prerequisites Check
python --version
pip --version

2️⃣ Create Project Folder
mkdir AICHATBOT
cd AICHATBOT

3️⃣ Create Virtual Environment
python -m venv venv

Activate Virtual Environment (Windows – PowerShell / CMD)
venv\Scripts\activate

4️⃣ Install Required Python Packages
pip install fastapi uvicorn requests pydantic


(Optional – install all at once later)

pip freeze > requirements.txt

5️⃣ Install & Verify Ollama
Check Ollama Installation
ollama --version

Start Ollama Service
ollama serve

6️⃣ Pull LLaMA Model
ollama pull llama3


Verify model:

ollama list

7️⃣ Test Model in Terminal
ollama run llama3


Example message:

Hello! Who are you?


Exit:

/bye

8️⃣ Run FastAPI Backend Server
uvicorn main:app --reload


Backend URL:

http://127.0.0.1:8000

9️⃣ API Testing (Optional – Browser or Postman)
Open API Docs
http://127.0.0.1:8000/docs

🔟 Frontend Usage

Open index.html using:

Live Server (VS Code)

OR double-click file

Frontend sends POST request to:

http://127.0.0.1:8000/chat
