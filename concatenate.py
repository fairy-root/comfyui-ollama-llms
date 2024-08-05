class ConcatenateText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "instruction": ("STRING", {"multiline": True, "default": "Act as a creative problem solver that answers in prompts. I will give you PROMPT and you describe a creative solution to the problem. Use terse concise terms to describe the answer. Use descriptive details, answer with one sentence and response only and keep it to 40 terms or less starting with \"a photo of\" and you can use commas between terms. Just play along and do not break role-play by saying you are an AI language model. Just guess at the answer."}),
                "prompt": ("STRING", {"multiline": True, "default": "beautiful woman. close-up, depth of field, ray tracing"}),
                "separator": ("STRING", {"default": "PROMPT="})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate"
    CATEGORY = "Ollama"

    def concatenate(self, instruction, prompt, separator):
        concatenated_text = instruction + separator + prompt
        return (concatenated_text,)

# Node export details
NODE_CLASS_MAPPINGS = {
    "ConcatenateText": ConcatenateText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ConcatenateText": "Concatenate Text"
}