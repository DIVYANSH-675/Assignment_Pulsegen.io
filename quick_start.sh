#!/bin/bash
# Quick Start Script for Assignment
# This sets up everything you need to run the pipeline

set -e  # Exit on error

echo "🚀 Setting up Assignment Pipeline..."
echo ""

# Step 1: Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Creating..."
    python3 -m venv venv
fi

# Step 2: Activate venv
echo "✓ Activating virtual environment"
source venv/bin/activate

# Step 3: Install dependencies
echo "✓ Installing dependencies..."
pip install -q polars pyarrow duckdb openai httpx jupyter ipykernel sentence-transformers hdbscan scikit-learn tqdm python-dotenv

# Step 4: Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "⚠️  No .env file found. Creating template..."
    echo "OPENAI_API_KEY=sk-your-key-here" > .env
    echo "📝 Please edit .env and add your OpenAI API key"
    echo "   Or you can use Ollama (local LLM, free)"
fi

# Step 5: Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo ""
    echo "⚠️  Ollama not installed. Install it with:"
    echo "   curl -fsSL https://ollama.com/install.sh | sh"
    echo "   ollama pull llama3.1:8b"
else
    echo "✓ Ollama is installed"
    # Check if model is downloaded
    if ! ollama list | grep -q llama3.1:8b; then
        echo "⚠️  Model not downloaded. Run: ollama pull llama3.1:8b"
    else
        echo "✓ Model llama3.1:8b available"
    fi
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Run: jupyter notebook"
echo "2. Open notebooks/01_setup_and_clean.ipynb"
echo "3. Follow the EXECUTE_NOW.md guide"
echo ""
echo "For OpenAI API: Make sure .env has your API key"
echo "For Ollama: Make sure Ollama is running (ollama serve)"

