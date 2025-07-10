# Mistral-7B FastAPI Chat

A minimal FastAPI server for running **Mistral-7B-Instruct-v0.3** locally with GPU acceleration. A playground for testing LLM interactions.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Mistral](https://img.shields.io/badge/Mistral-7B-informational?style=for-the-badge)

## Features

- **FastAPI backend** with async support
- **Mistral-7B-Instruct-v0.3** with 4-bit quantization
- **GPU acceleration** (Full offload for NVIDIA GPUs)
- Single `/ask` endpoint for Q&A
- Health check endpoint


## Setup

- NVIDIA GPU (Tested on RTX 4070 8GB VRAM)
- Python 3.13+
- `pip` and `venv`

**Clone the repo**

```bash
git clone https://github.com/mahlqvist/mistral-7b-fastapi-chat.git
cd mistral-7b-fastapi-chat
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Download the model**

Place your GGUF model in `models/`:

```bash
mkdir models
cd models
wget https://huggingface.co/second-state/Mistral-7B-Instruct-v0.3-GGUF/resolve/main/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf
   ```

## Usage

**Start the server**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Test with CURL**
```bash
curl -X POST -d '{"text":"Explain quantum computing in 3 sentences"}' -H "Content-Type: application/json" http://localhost:8000/ask
```

## API Reference

### `POST /ask`

**Request:**
```json
{"text": "Your question here"}
```

**Response:**
```json
{"response": "Mistral's answer goes here..."}
```

### `GET /health`

```json
{"status": "alive"}
```

## Project Structure

```
mistral-7b-fastapi-chat/
├── app/
│   ├── main.py          # FastAPI routes
│   ├── model.py         # Mistral-7B wrapper
│   └── config.py        # Settings
├── models/              # GGUF model goes here
├── requirements.txt
└── README.md
```