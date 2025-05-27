# QnA Chatbot with Streamlit, LangChain & Groq LLMs.

An interactive Question & Answer chatbot built using **Streamlit**, **LangChain**, and **Groq's blazing-fast LLMs**. This project allows users to query using a web interface and get AI-generated responses from large language models like LLaMA-3, LLaMA-Guard, and Gemma.

---

## Features

- Uses Groq's LLMs (LLaMA-3, Gemma, etc.) for generating high-quality answers.
- Simple and clean UI built using Streamlit.
- Customizable temperature and max tokens via sidebar sliders.
- Modular LangChain pipeline with prompt templating and output parsing.

---

## Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [LangChain](https://www.langchain.com/) – LLM orchestration
- [Groq](https://groq.com/) – High-performance language model inference
- [Python-dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management

---

## Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/qna-chatbot.git
cd qna-chatbot
```

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

5. **Running the App**

```bash
streamlit run app.py
```
This will launch a local web server where you can interact with your QnA chatbot.

---

## Preview

![image](https://github.com/user-attachments/assets/fcddb627-e273-4e0a-9cee-cffa1922a39f)
![image](https://github.com/user-attachments/assets/2f35e966-733e-48ff-b7a4-17096ee323c6)


---

## Model Options

Choose from the following models via the sidebar:

- gemma2-9b-it
- meta-llama/Llama-Guard-4-12B
- llama-3.3-70b-versatile
- llama-3.1-8b-instant

## Project Structure

qna-chatbot/       
├── app.py               # Main Streamlit app      
├── .env                 # Environment variables      
├── requirements.txt     # Python dependencies      
└── README.md            # Project documentation      

## Contact

For feedback or contributions, feel free to open an issue or reach out!      
Let me know if you'd like to include deployment instructions (e.g., using Streamlit Cloud or Vercel) or integrate additional features like chat history or PDF/QnA ingestion.
