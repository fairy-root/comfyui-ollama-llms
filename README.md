# ComfyUI Ollama Integration

This repository, maintained by [fairy-root](https://github.com/fairy-root), provides custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), integrating with the Ollama API for language model interactions and offering text manipulation capabilities.

![Ollama](https://i.imgur.com/60snV9O.png "Displaying help")

## Installation Guide

## Features

- **Load Ollama LLMs**: Interact with Ollama's language models, including streaming and logging capabilities.
- **Concatenate Text LLMs**: Concatenate instructional text with prompts, offering customizable text formatting.
- **Load Llava Vision LLMs**: Loads Llava model and interacts with loaded images based on the user prompts.

## Workflow

![Ollama](https://i.imgur.com/JRlQQXr.png "Displaying help")

- Visit this Link to get the workflow [openart ai](https://openart.ai/workflows/toad_jaunty_59/comfyui-ollama-node-for-prompt-creation/u5P5TiFlFfKbsx2TCcK5)

## Installation

### Requirements

- Python 3.x
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

### Steps

1. Installing the node:
- Goto `ComfyUI/custom_nodes` dir in **terminal(cmd)**
- Clone the repository
   ```bash
   git clone https://github.com/fairy-root/comfyui-ollama-llms.git
   ```
- Restart ComfyUI

2. Install required Python packages:
   ```bash
   pip install ollama
   ```

## Getting Started

### Obtaining Ollama Model

**Phi3 is just an example since it is small and fast. You can choose any other models as well.**

- To use the **Load Ollama LLms** node, you'll need to install **Ollama**. Visit [Ollama](https://ollama.com) and install the Ollama App for your OS, then in the terminal use the command:
   ```bash
   ollama pull phi3
   ```
   **or**
   ```bash
   ollama run phi3
   ```

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
