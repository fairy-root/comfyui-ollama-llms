# ComfyUI Ollama Integration

This repository, maintained by [fairy-root](https://github.com/fairy-root), provides custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), integrating with the Ollama API for language model interactions and offering text manipulation capabilities.

![Ollama](https://i.imgur.com/JRlQQXr.png "Displaying help")

## Features

- **Load Ollama LLms** (`ollamas.py`): Interact with Ollama's language models, including streaming and logging capabilities.
- **Concatenate Text LLms** (`concatenate.py`): Concatenate instructional text with prompts, offering customizable text formatting.

## Installation

### Requirements

- Python 3.x
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

### Steps

1. Installing the node:
- Goto `ComfyUI/custom_nodes` dir in **terminal(cmd)**
- Clone the repository
   ```bash
   git clone https://github.com/fairy-root/comfyui-ollama.git
   ```
- Restart ComfyUI

2. Install required Python packages:
   ```bash
   pip install ollama
   ```

## Getting Started

### Obtaining Ollama Model

- To use the **Load Ollama LLms** node, you'll need to install **Ollama**. Visit [Ollama](https://ollama.com) and install the Ollama App for your OS, then in the terminal use the command:
   ```bash
   ollama pull phi3
   ```
   **or**
   ```bash
   ollama run phi3
   ```

### Example: Using the `phi3` Model

#### OllamaService Node

1. **Node Inputs:**
   - **Prompt:** Your text prompt.
   - **ollama_model:** Select the `phi3` model from the available options.
   - **Console_log:** Set to `True` to enable real-time logging.

2. **Sample Usage:**

   In ComfyUI, configure the OllamaService node with the following inputs:

   - **Prompt:** "What is the meaning of life?"
   - **ollama_model:** `phi3`
   - **Console_log:** `True`

3. **Expected Output:** The response from the `phi3` model based on the provided prompt.

#### ConcatenateText Node

![Ollama](https://i.imgur.com/2BbdNwq.png "Ollama")

1. **Node Inputs:**
   - **Instruction:** "Act as a creative problem solver that answers in prompts..."
   - **Prompt:** "beautiful woman. close-up, depth of field, ray tracing"
   - **Separator:** "PROMPT="

2. **Sample Usage:**

   In ComfyUI, configure the ConcatenateText node with the above inputs. The output will be a concatenated string with the instruction and prompt.

3. **Expected Output:** A single string combining the instruction and prompt with the separator.

4. **ConcatenateText and Loader**
   You can use the concatenate text node to concatenate the instruction and your prompt, then pass it to the loader node for processing by **converting the Prompt in the loader into an input**. then linking the two nodes together, you can generate a response based on your concatenated text.

## Node Details

### OllamaService (`ollama.py`)

- **Inputs:** 
  - `prompt`: Text prompt (STRING)
  - `ollama_model`: Selected model from Ollama (LIST)
  - `Console_log`: Enable/disable console logging (BOOLEAN)

- **Outputs:** 
  - Response text (STRING)

- **Category:** `advanced/loaders`

### ConcatenateText (`concatenate.py`)

- **Inputs:**
  - `instruction`: Instructional text (STRING, multiline)
  - `prompt`: Prompt text (STRING, multiline)
  - `separator`: Separator string (STRING)

- **Outputs:** 
  - Concatenated text (STRING)

- **Category:** `text`

## Donation

Your support is appreciated:

- USDt (TRC20): `TGCVbSSJbwL5nyXqMuKY839LJ5q5ygn2uS`
- BTC: `13GS1ixn2uQAmFQkte6qA5p1MQtMXre6MT`
- ETH (ERC20): `0xdbc7a7dafbb333773a5866ccf7a74da15ee654cc`
- LTC: `Ldb6SDxUMEdYQQfRhSA3zi4dCUtfUdsPou`

## Author and Contact

- GitHub: [FairyRoot](https://github.com/fairy-root)
- Telegram: [@FairyRoot](https://t.me/FairyRoot)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.