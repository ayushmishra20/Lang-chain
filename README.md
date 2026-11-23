# LangChain Learning Demos

Small, standalone Python examples for learning LangChain concepts and integrations. The examples cover language models, chat models, embeddings, prompts, structured output, parsers, chains, runnables, and document loading. Some examples call hosted model APIs; others download or run models locally.

## Project layout

| Folder | Topics |
| --- | --- |
| `1.LLMs/` | Text completion with an LLM |
| `2.chatModel/` | OpenAI, Anthropic, Google, and Hugging Face chat models |
| `3.EmbeddingModel/` | Text embeddings and document similarity |
| `4.Langchain_prompts/` | Messages, prompt templates, chat history, and Streamlit prompt apps |
| `5.Output/` | TypedDict, JSON, Pydantic, and model-backed structured output |
| `6.Parser/` | String, JSON, Pydantic, and structured output parsers |
| `7.Chains/` | Simple, sequential, parallel, and conditional chains |
| `8.Runnables/` | Runnable sequences, parallel branches, lambdas, and passthrough |
| `9.langchain-document-loaders/` | Loading CSV and other document examples |

Each numbered Python file is an independent example. Run commands from the project directory so relative paths to files such as `template.json` and `Social_Network_Ads.csv` resolve correctly.

## Requirements

- Python 3.10 or later
- Packages listed in `requirements.txt`
- API credentials for the hosted model providers used by the examples

Create and activate a virtual environment, then install the listed packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The CSV loader example also uses `langchain-community`, which is not currently listed in `requirements.txt`. Install it to run that example:

```powershell
pip install langchain-community
```

The local Hugging Face examples may require PyTorch. Install a PyTorch build suitable for your operating system and hardware before running them.

## Configure API keys

Many examples call `load_dotenv()`, which reads environment variables from a `.env` file in the project directory. Add only the credentials needed for the examples you intend to run:

```dotenv
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
GOOGLE_API_KEY=your-google-api-key
HUGGINGFACEHUB_API_TOKEN=your-hugging-face-token
```

The `.env` file is ignored by Git. Keep real credentials private and do not commit them. Hugging Face local-model examples may not require a token, while hosted endpoints typically do.

## Run examples

Run a Python example from the project directory:

```powershell
python "1.LLMs\1_llm_demo.py"
python "2.chatModel\3chatmodel_google.py"
```

Run the Streamlit chatbot or research prompt app with:

```powershell
streamlit run "4.Langchain_prompts\1chatbot.py"
streamlit run "4.Langchain_prompts\6prompt_ui.py"
```

Choose a script that matches the provider credentials and installed integrations available in your environment. Some examples use particular model names that may need to be updated if a provider has changed or retired them.
