Step 1: Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Step 2: Install Libraries

pip install -r requirements.txt

Step 3: Add Your API Key

Create file:
.env

Inside it:
OPENAI_API_KEY=your_api_key_here

Step 4: Run the Project
python summarizer.py

Example
Input:
Artificial intelligence is changing the world by helping machines think...


Output:
AI is helping machines think and solve problems like humans.

Why This Project
Learn LLM usage
Learn text summarization
Learn project structure
Useful for data science and GenAI roles

Technologies Used
Python
LLM API
Virtual Environment
Prompt Engineering
