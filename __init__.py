from .ollamas import OllamaService
from .concatenate import ConcatenateText

NODE_CLASS_MAPPINGS = {
    "ollama": OllamaService,
    "ConcatenateText": ConcatenateText,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ollama": "Load Ollama LLMs",
    "ConcatenateText": "Concatenate Text LLMs",
}

__all__ = ["ollama", "ConcatenateText", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]