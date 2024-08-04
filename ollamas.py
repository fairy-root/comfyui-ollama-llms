import subprocess
import sys

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Package {package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

# Install packages if not already installed
install_and_import("ollama")

# Import the installed packages
import ollama

class OllamaService:
    @classmethod
    def INPUT_TYPES(cls):
        # Load available models and API keys
        ollama_models = ollama.list()["models"]
        ollama_model_names = [model['name'] for model in ollama_models]

        return {
            "required": {
                "prompt": ("STRING", {"default": "Enter your prompt here..."}),
            },
            "optional": {
                "ollama_model": (ollama_model_names, {"default": ollama_model_names[0] if ollama_model_names else ""}),
                "Console_log": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "advanced/loaders"

    def execute(self, prompt, ollama_model=None, stream=True, Console_log=False):
        return self._ollama_interaction(ollama_model, prompt, stream, Console_log)

    def _ollama_interaction(self, model, prompt, stream, Console_log):
        try:
            response_stream = ollama.chat(
                model=model,
                messages=[{'role': 'user', 'content': prompt}],
                stream=stream,
            )

            output_text = ""
            if stream:
                for chunk in response_stream:
                    output_text += chunk['message']['content']
                    if Console_log:
                        print(chunk['message']['content'], end='', flush=True)
            else:
                for chunk in response_stream:
                    output_text += chunk['message']['content']
            output_text = str(output_text)
            return (output_text,)

        except Exception as e:
            print('Error:', e)

    @classmethod
    def IS_CHANGED(cls, *args):
        return True

# Node export details
NODE_CLASS_MAPPINGS = {
    "ollama": OllamaService
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ollama": "Load Ollama LLms"
}