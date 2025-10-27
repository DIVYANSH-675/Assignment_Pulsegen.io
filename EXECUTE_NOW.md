# 🚀 Execute Now - Step-by-Step Guide

## Your Setup
- ✅ Linux server
- ✅ Both local LLM (Ollama) and OpenAI API
- ✅ Small sample (100 reviews)
- ✅ Testing first

## Quick Start (5 minutes to first output)

### Step 1: Install Ollama for Local LLM (2 minutes)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download a model
ollama pull llama3.1:8b
# This will take a few minutes (4GB download)

# Test it works
ollama run llama3.1:8b "Say hello"
```

### Step 2: Setup OpenAI API (30 seconds)

```bash
# Create .env file
cd /home/ubuntu/Desktop/Assignment
echo "OPENAI_API_KEY=sk-your-key-here" > .env

# Replace 'sk-your-key-here' with your actual OpenAI API key
# Get key from: https://platform.openai.com/api-keys
```

### Step 3: Activate Environment and Install Dependencies (1 minute)

```bash
cd /home/ubuntu/Desktop/Assignment
source venv/bin/activate

# Install missing packages (if any)
pip install openai httpx --quiet
```

### Step 4: Run Notebook 1 - Data Cleaning (2 minutes)

```bash
# Start Jupyter
jupyter notebook --no-browser --port 8888

# Then open http://localhost:8888 in your browser
# Or if remote, use SSH port forwarding:
# ssh -L 8888:localhost:8888 user@server
```

**In Jupyter:**
1. Open `notebooks/01_setup_and_clean.ipynb`
2. Click "Run All" (or run each cell with Shift+Enter)
3. You'll see output showing 250K reviews being cleaned
4. File saved to `data/reviews_clean.parquet`

**Expected output:**
```
✓ Loaded 250,000 rows
✓ Datetime and naming transformations complete
✓ Computed columns added
✓ Final dataset: 250,000 rows, 12 columns
✓ Saved to data/reviews_clean.parquet
```

### Step 5: Run Notebook 2 - Topic Routing (THIS IS THE KEY STEP)

Open `notebooks/02_topic_router.ipynb`

**IMPORTANT**: Edit cell with `MAX_REVIEWS = 1000` to:

```python
# Process FIRST 100 reviews as test sample
MAX_REVIEWS = 100
```

**Choose your LLM provider** in the same cell:

```python
# OPTION 1: Use OpenAI API (fast, costs money)
PROVIDER = 'openai'
MODEL = 'gpt-3.5-turbo'

# OPTION 2: Use Local Ollama (free, slower)
PROVIDER = 'ollama'
MODEL = 'llama3.1:8b'
```

**Then run all cells.**

**Expected output (with OpenAI):**
```
✓ Initialized LLM client: openai with model gpt-3.5-turbo
Sample routing result:
{
  "topic_ids": ["ORDER_INCOMPLETE", "NO_RESPONSE_COMPLAINT"],
  "is_novel": false
}
Processing 100 reviews...
Processing batches: 100%|████████████| 1/1 [00:45<00:00]
✓ Processed 150 topic assignments
✓ Saved labels to data/labels_initial.parquet
```

**Expected output (with Ollama, slower):**
```
✓ Initialized LLM client: ollama with model llama3.1:8b
Processing 100 reviews...
Processing batches: 100%|████████████| 1/1 [15:00<00:00]  # Takes ~15 min
```

### Step 6: Run Notebook 5 - Generate Trend Report (30 seconds)

Open `notebooks/05_trend_analysis.ipynb` and click "Run All"

**Expected output:**
```
✓ Loaded 150 topic assignments
✓ Loaded 32 topic definitions
📅 Date range: 2025-09-27 to 2025-10-26
✓ Filtered to 150 assignments in date range
✓ Created pivot table: 10 topics × 30 dates
✓ Generated sparklines
✓ Saved CSV to output/topics_trend_2025-10-27.csv
✓ Saved HTML to output/topics_trend_2025-10-27.html
```

### Step 7: View Results

```bash
# View CSV
head -20 output/topics_trend_2025-10-27.csv

# View HTML in browser
# Files are in: /home/ubuntu/Desktop/Assignment/output/
```

## 🎯 What You'll See

### CSV Output:
```csv
Topic,T-30,T-29,T-28,...,T
ORDER_INCOMPLETE,2,5,3,...,4
ETA_JUMP_AFTER_PAYMENT,1,0,2,...,1
POSITIVE_EXPERIENCE,15,12,18,...,20
```

### HTML Output:
Opens in browser showing:
- Topic names (e.g., "Order Incomplete")
- Sparklines (▁▂▃▅▇█) showing trends
- 7-day change percentages
- Sortable table

## 🐛 Troubleshooting

### Ollama not starting
```bash
# Start Ollama service
ollama serve

# In another terminal, test
curl http://localhost:11434/api/generate
```

### OpenAI API errors
```bash
# Check your key
cat .env

# Or set manually
export OPENAI_API_KEY=sk-...
```

### Memory issues
- Reduce `MAX_REVIEWS` to 50
- Process in smaller batches

### Import errors in notebooks
Add to notebook cells:
```python
import sys
sys.path.append('../')
```

## 📊 Expected Timeline

| Step | Time | What Happens |
|------|------|--------------|
| Install Ollama | 3 min | Download model |
| Setup env | 1 min | API keys |
| Notebook 1 | 2 min | Clean 250K data |
| Notebook 2 (OpenAI) | 5 min | Route 100 reviews |
| Notebook 2 (Ollama) | 15 min | Route 100 reviews |
| Notebook 5 | 30 sec | Generate trends |
| **Total** | **15-25 min** | Complete pipeline |

## ✅ Success Indicators

You're done when you see:
1. ✅ `data/reviews_clean.parquet` (cleaned data)
2. ✅ `data/labels_initial.parquet` (topic assignments)
3. ✅ `output/topics_trend_YYYY-MM-DD.csv` (trend table)
4. ✅ `output/topics_trend_YYYY-MM-DD.html` (HTML report)

## 🎬 Ready to Record Demo

Once you have the outputs:
1. Record 5-min screen capture
2. Show each notebook executing
3. Show final HTML report
4. Upload to Google Drive
5. Submit to vatsal@pulsegen.io

---

**START HERE**: Run the commands above! 🚀

