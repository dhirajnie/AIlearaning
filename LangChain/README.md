# Ollama Chat with LangChain

Initialize and chat with local Ollama models using LangChain.

## Prerequisites

### 1. Install Ollama
- **macOS**: `brew install ollama` or download from [ollama.ai](https://ollama.ai)
- **Linux**: Download from [ollama.ai](https://ollama.ai)
- **Windows**: Download from [ollama.ai](https://ollama.ai)

### 2. Start Ollama
```bash
ollama serve
```
This starts the Ollama API server on `http://localhost:11434` by default.

### 3. Pull a Model
Ollama models run locally. Popular options:

```bash
ollama pull llama2       # 3.8GB - Fast, good general purpose
ollama pull llama3       # 4.7GB - Latest Llama model (recommended)
ollama pull mistral      # 4.1GB - Fast, strong coding
ollama pull neural-chat  # 3.3GB - Optimized for chat
```

Check installed models:
```bash
ollama list
```

## Installation

Install required Python dependencies:

```bash
pip install langchain-ollama langchain-core
```

## Usage

### Interactive Chat Mode
Run the script and chat interactively:

```bash
python3 task_3_ollama_chat.py
```

Type your messages and press Enter. Type `quit` to exit.

### Demo Mode
Run predefined test prompts:

```bash
python3 task_3_ollama_chat.py --demo
```

## Customization

Edit `task_3_ollama_chat.py` to:

- **Change model**: Modify `model="llama2"` to any model you've pulled
- **Adjust temperature**: Lower = more deterministic, higher = more creative (0-1)
- **Change API port**: Modify `base_url` if Ollama is on a different port
- **Custom prompts**: Add more test prompts in the `demo_chat()` function

## Troubleshooting

**"Connection refused" error**
- Ensure Ollama is running: `ollama serve`
- Check it's listening: `curl http://localhost:11434/api/tags`

**"Model not found" error**
- Pull the model: `ollama pull llama3`
- List available models: `ollama list`

**Slow responses**
- Reduce model size (e.g., use Mistral instead of Llama3)
- Increase temperature for faster, less precise responses
- Ensure no other heavy processes are running

## Available Models on Ollama Hub

- **llama2** - General purpose, fast
- **llama3** - Latest Llama, strongest reasoning
- **mistral** - Fast, excellent for code
- **neural-chat** - Optimized for conversation
- **dolphin-mixtral** - Large, powerful (9GB+)

Find more at [ollama-library](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)

## Performance Tips

1. **GPU Acceleration**: Ollama uses GPU if available (NVIDIA CUDA, Metal on macOS)
2. **RAM**: Ensure sufficient RAM for your model size
3. **First Run**: Model inference is slow on first run; subsequent calls are cached
4. **Background Process**: Run `ollama serve` in a separate terminal

## Task Files

- `task_3_ollama_chat.py` - Main chat script with demo mode
- `task_2_multi_model.py` - Multi-provider setup (OpenAI, Google, X.AI)
- `README.md` - This file
