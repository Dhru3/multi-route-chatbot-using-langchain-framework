# MultiRouteChatbot

A Streamlit-powered chatbot using [LangChain](https://www.langchain.com/) and [Groq](https://console.groq.com/) LLMs, capable of routing user questions to different expert personas (Math Professor, Philosopher, Medical Doctor, or General Assistant) based on the question's content.

---

## Features

- **Expert Routing:** Directs user questions to the most relevant expert.
- **Two Routing Modes:**
  - **Keyword-based routing** (`app.py`): Fast, transparent, and simple.
  - **LLM-based smart routing** (`app2.py`): Uses the LLM to classify questions for more flexible and robust routing.
- **Streamlit UI:** Simple web interface for chatting with the routed experts.
- **LangSmith Tracing:** Integrated tracing for debugging and monitoring via LangSmith.

---

## Files

### `app.py` (Keyword-based Routing)

- **How it works:**  
  Uses a Python function to check for keywords in the user's question and selects the appropriate expert chain.
- **Pros:**  
  - Fast and cost-effective (only one LLM call per question).
  - Easy to understand and modify routing logic.
- **Cons:**  
  - Limited to the keywords defined in the code.
  - May misclassify questions that use unexpected wording.

### `app2.py` (LLM-based Smart Routing)

- **How it works:**  
  Uses the LLM itself to classify the user's question into one of four categories: `math`, `philosophy`, `doctor`, or `default`. The selected expert then answers the question.
- **Pros:**  
  - More flexible and robust to varied question phrasing.
  - Can handle ambiguous or complex queries better.
- **Cons:**  
  - Slightly slower (two LLM calls per question: one for routing, one for answering).
  - Higher API usage/cost.

---

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Dhru3/multi-route-chatbot-using-langchain-framework.git
    cd MultiRouteChatbot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file in the root directory with the following:
      ```
      GROQ_API_KEY=your_groq_api_key
      LANGCHAIN_API_KEY=your_langchain_api_key
      ```

4. **Run the app:**
    - For keyword-based routing:
      ```bash
      streamlit run app.py
      ```
    - For LLM-based smart routing:
      ```bash
      streamlit run app2.py
      ```

---

## Usage

- Enter your question in the input box.
- The chatbot will route your question to the most relevant expert and display the answer, indicating which expert responded.

---

## Example Questions

- **Math:**  
  "How do I solve this integral?"  
- **Philosophy:**  
  "What is the meaning of life?"  
- **Doctor:**  
  "What should I do if I have a fever?"  
- **Default:**  
  "How are potatoes grown?"# MultiRouteChatbot

A Streamlit-powered chatbot using [LangChain](https://www.langchain.com/) and [Groq](https://console.groq.com/) LLMs, capable of routing user questions to different expert personas (Math Professor, Philosopher, Medical Doctor, or General Assistant) based on the question's content.

---

## Features

- **Expert Routing:** Directs user questions to the most relevant expert.
- **Two Routing Modes:**
  - **Keyword-based routing** (`app.py`): Fast, transparent, and simple.
  - **LLM-based smart routing** (`app2.py`): Uses the LLM to classify questions for more flexible and robust routing.
- **Streamlit UI:** Simple web interface for chatting with the routed experts.
- **LangSmith Tracing:** Integrated tracing for debugging and monitoring via LangSmith.

---

## Files

### `app.py` (Keyword-based Routing)

- **How it works:**  
  Uses a Python function to check for keywords in the user's question and selects the appropriate expert chain.
- **Pros:**  
  - Fast and cost-effective (only one LLM call per question).
  - Easy to understand and modify routing logic.
- **Cons:**  
  - Limited to the keywords defined in the code.
  - May misclassify questions that use unexpected wording.

### `app2.py` (LLM-based Smart Routing)

- **How it works:**  
  Uses the LLM itself to classify the user's question into one of four categories: `math`, `philosophy`, `doctor`, or `default`. The selected expert then answers the question.
- **Pros:**  
  - More flexible and robust to varied question phrasing.
  - Can handle ambiguous or complex queries better.
- **Cons:**  
  - Slightly slower (two LLM calls per question: one for routing, one for answering).
  - Higher API usage/cost.

---

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Dhru3/MultiRouteChatbot.git
    cd MultiRouteChatbot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file in the root directory with the following:
      ```
      GROQ_API_KEY=your_groq_api_key
      LANGCHAIN_API_KEY=your_langchain_api_key
      ```

4. **Run the app:**
    - For keyword-based routing:
      ```bash
      streamlit run app.py
      ```
    - For LLM-based smart routing:
      ```bash
      streamlit run app2.py
      ```

---

## Usage

- Enter your question in the input box.
- The chatbot will route your question to the most relevant expert and display the answer, indicating which expert responded.

---

## Example Questions

- **Math:**  
  "How do I solve this integral?"  
- **Philosophy:**  
  "What is the meaning of life?"  
- **Doctor:**  
  "What should I do if I have a fever?"  
- **Default:**  
  "How are potatoes grown?"
