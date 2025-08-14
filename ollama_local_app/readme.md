# Your personal, secret & private chatbot who don't judge you
> Running local Open source LLM module and chat with it. 

## Installing Ollama
Ollama is a set of open LLM models provided by Meta. an open-source application that simplifies the process of running large language models (LLMs) locally on your computer. 
It allows users to download, manage, and interact with various open-source LLMs without needing cloud-based services, ensuring data privacy and control.

1) Download and install Ollama from https://ollama.com
2) On a PC you might need to have administrator permissions for the install to work properly.
3) On a Windows OS PC, start a Command prompt / Powershell (Press Win + R, type cmd, and press Enter).
4) On a Mac, start a Terminal (Applications > Utilities > Terminal).
5) Run `ollama run llama3.2` or for smaller machines try `ollama run llama3.2:1b`
6) Please stay away of Meta's latest model llama3.3 because at 70 Billion parameters that's way too large for most home computers!
7) If this doesn't work; you may need to run `ollama serve` in another Powershell (Windows) or Terminal (Mac), and try step 3 again.

## Install Python OpenAI library
The OpenAI Python library provides a convenient and official interface for interacting with the OpenAI REST API from Python applications. 
We will use this API to communicate with ollama server we just setup.

1) Check python version. This project is tested on python 3.11, 3.12 and 3.13.
   > `python --version`
2) Install OpenAI library
   > `pip3 install openai`

## Testing the installation

1) Make sure that the ollama server is running in a separate terminal window.
2) Clone this git repository in a `project` folder.
3) Navigate to the project folder `project\llm_ai_chatbot_apps\ollama_local_app`
4) Execute the python script `test_local_ollama.py`
   > `python3 test_local_ollama.py`
5) It should execute and respond to the prompt. Try changing the prompt and ask question.

# Start talking to your virtual AI friend

1) Make sure that the ollama server is running in a separate terminal window.
2) Clone this git repository in a `project` folder.
3) Navigate to the project folder `project\llm_ai_chatbot_apps\ollama_local_app`
4) Execute the python script `test_local_ollama.py`
   > `python3 my_chatbot.py`
5) It should start shortly. Please be patient with it, because LLM model on PC is really slow.

** Please note taht this server is running at your local computer. So, depending on how powerful is the computer, prompt can take several minute before responding. **
