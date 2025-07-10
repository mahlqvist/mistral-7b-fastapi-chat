from langchain_community.chat_models import ChatLlamaCpp
from app.config import MODEL_PATH, GPU_LAYERS, CONTEXT_SIZE, BATCH_SIZE, MAX_TOKENS
import multiprocessing

class MistralChat:
	def __init__(self):
		self.llm = None
	
	def load(self):
		"""Initialize model (call once at startup)."""
		self.llm = ChatLlamaCpp(
			model_path=str(MODEL_PATH),
			n_gpu_layers=GPU_LAYERS,
			n_ctx=CONTEXT_SIZE,
			n_batch=BATCH_SIZE,
			max_tokens=MAX_TOKENS,
			temperature=0.3,
			top_p=0.9,
			n_threads=max(1, multiprocessing.cpu_count() - 1),
			repeat_penalty=1.5,
			stop=["[/INST]", "<|endoftext|>"],
			verbose=False,
		)
	
	def generate(self, prompt: str) -> str:
		"""Simple Q&A with Mistral."""
		if not self.llm:
			raise ValueError("Model not loaded! Call load() first.")
		
		# Mistral's instruction template
		formatted_prompt = f"[INST] {prompt} [/INST]"
		return self.llm.invoke(formatted_prompt)