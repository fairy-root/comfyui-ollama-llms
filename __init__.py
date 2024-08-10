from .ollamas import OllamaService
from .concatenate import ConcatenateText
from .llava import LlavaVision

NODE_CLASS_MAPPINGS = {
    "ollama": OllamaService,
    "ConcatenateText": ConcatenateText,
    "llava": LlavaVision
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ollama": "Load Ollama LLMs",
    "ConcatenateText": "Concatenate Text Prompts LLMs",
    "llava": "Load Llava Vision LLMs"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]