import subprocess
import sys
import numpy as np
import base64
from PIL import Image
from io import BytesIO

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

class LlavaVision:
    @classmethod
    def INPUT_TYPES(cls):
        # Load available models and API keys
        ollama_models = ollama.list()["models"]
        ollama_model_names = [model['name'] for model in ollama_models if "llava" in model['name'].lower()]
        

        return {
            "required": {
                "prompt": ("STRING", {"default": "Describe this image."}),
                "images": ("IMAGE",),
            },
            "optional": {
                "ollama_model": (ollama_model_names, {"default": ollama_model_names[0] if ollama_model_names else ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Ollama"

    def execute(self, prompt, images=None, ollama_model=None):

        images_encoded = []

        if images is not None:
            for (batch_number, image) in enumerate(images):
                i = 255. * image.cpu().numpy()
                img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
                buffered = BytesIO()
                img.save(buffered, format="PNG")
                img_bytes = base64.b64encode(buffered.getvalue())
                images_encoded.append(str(img_bytes, 'utf-8'))
        else:
            return ("Error: No image provided", "Error: No image provided")

        return self._ollama_interaction(ollama_model, prompt, images_encoded)

    def _ollama_interaction(self, model, prompt, images):
        try:
            res = ollama.chat(
                model=model,
                messages=[
                    {'role': 'user',
                     'content': prompt,
                     "images": images}
                ]
            )

            output_text = ""
            output_text += res['message']['content']
            output_text = str(output_text)
            return (output_text,)

        except Exception as e:
            print(f"Error during Ollama interaction: {e}")
            return (f"Error during Ollama interaction: {e}", f"Error during Ollama interaction: {e}")

    @classmethod
    def IS_CHANGED(cls, *args):
        return True

# Node export details
NODE_CLASS_MAPPINGS = {
    "llava": LlavaVision
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "llava": "Load LLava LLms"
}
