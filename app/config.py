from pathlib import Path


MODEL_DIR = Path("models")
MODEL_NAME = "Mistral-7B-Instruct-v0.3-Q4_K_M.gguf"
MODEL_PATH = MODEL_DIR / MODEL_NAME

GPU_LAYERS = 33 
CONTEXT_SIZE = 32768 
BATCH_SIZE = 256 
MAX_TOKENS = 512