# 🎯 HOW TO RUN - Simple 5-Step Guide

## ✅ Your System is Ready!

You're on Linux with everything set up. Here's how to execute:

---

## Step 1: Open Terminal and Navigate (30 seconds)

```bash
cd /home/ubuntu/Desktop/Assignment
```

---

## Step 2: Activate Python Environment (5 seconds)

```bash
source venv/bin/activate
```

You should see `(venv)` in your prompt.

---

## Step 3: Start Jupyter Notebook (10 seconds)

```bash
jupyter notebook
```

This will:
- Open browser to http://localhost:8888
- Show you the notebook dashboard

**IF you're on remote server**, use port forwarding:
```bash
# On local machine, run:
ssh -L 8888:localhost:8888 your-username@your-server

# Then in browser, go to:
http://localhost:8888
```

---

## Step 4: Run Notebooks (THIS IS THE KEY PART)

### A. Notebook 1: Clean Data (2 minutes)

1. Click on `notebooks/01_setup_and_clean.ipynb`
2. Click **"Run All"** button (or press Shift+Enter in each cell)
3. Wait for it to complete
4. You'll see: ✓ Saved to data/reviews_clean.parquet

### B. Notebook 2: Route Topics (5 minutes)

1. Click on `notebooks/02_topic_router.ipynb`
2. **IMPORTANT**: Find the cell with `MAX_REVIEWS = 1000`
3. Change it to: `MAX_REVIEWS = 100` (for testing)
4. **Choose LLM** (find cell with PROVIDER):
   ```python
   # Option 1: OpenAI (fast, costs $0.10)
   PROVIDER = 'openai'
   MODEL = 'gpt-3.5-turbo'
   ```
   OR
   ```python
   # Option 2: Local Ollama (free, slower)
   PROVIDER = 'ollama'
   MODEL = 'llama3.1:8b'
   ```
5. Click **"Run All"**
6. Wait: ~5 min (OpenAI) or ~15 min (Ollama)

### C. Notebook 5: Generate Trends (30 seconds)

1. Click on `notebooks/05_trend_analysis.ipynb`
2. Click **"Run All"**
3. Done! Check `output/` folder

---

## Step 5: View Results

### Option A: Download Files
```bash
# In new terminal, view CSV
cat output/topics_trend_*.csv

# Or download to your computer
scp your-username@server:/home/ubuntu/Desktop/Assignment/output/*.csv .
scp your-username@server:/home/ubuntu/Desktop/Assignment/output/*.html .
```

### Option B: Open in Browser
```bash
# Copy HTML files to accessible location
cp output/*.html /var/www/html/  # or any web server
# Then access via http://your-server/topics_trend_*.html
```

---

## 🎬 What You'll See

### In Notebook 2 Output:
```
✓ Initialized LLM client: openai with model gpt-3.5-turbo
Processing 100 reviews...
Processing batches: 100%|████████████| 1/1 [00:45<00:00]
✓ Processed 150 topic assignments
📊 Topic Distribution:
topic_id      count
POSITIVE_EXPERIENCE  45
NEGATIVE_GENERIC  12
ORDER_INCOMPLETE  8
...
```

### In Notebook 5 Output:
```
✓ Loaded 150 topic assignments
📅 Date range: 2025-09-27 to 2025-10-26
✓ Created pivot table: 10 topics × 30 dates
✓ Saved CSV to output/topics_trend_2025-10-27.csv
✓ Saved HTML to output/topics_trend_2025-10-27.html
```

### In output/topics_trend_*.csv:
```csv
Topic,T-30,T-29,T-28,...,T
ORDER_INCOMPLETE,2,5,3,...,4
ETA_JUMP_AFTER_PAYMENT,1,0,2,...,1
POSITIVE_EXPERIENCE,15,12,18,...,20
```

---

## ⚙️ Configuration Tips

### For OpenAI (Fast, Recommended):
1. Get API key from: https://platform.openai.com/api-keys
2. Add to `.env` file:
   ```bash
   echo "OPENAI_API_KEY=sk-..." > .env
   ```
3. In notebook 2, use: `PROVIDER = 'openai'`

### For Ollama (Free but Slower):
1. Install Ollama:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ollama pull llama3.1:8b
   ```
2. Start Ollama:
   ```bash
   ollama serve
   ```
3. In notebook 2, use: `PROVIDER = 'ollama'`

---

## 📊 Timeline

| Action | Time |
|--------|------|
| Open Jupyter | 10 sec |
| Notebook 1 | 2 min |
| Notebook 2 (OpenAI) | 5 min |
| Notebook 2 (Ollama) | 15 min |
| Notebook 5 | 30 sec |
| **Total** | **8-18 min** |

---

## ✅ Success Checklist

After running, you should have:

- [ ] `data/reviews_clean.parquet` (cleaned data)
- [ ] `data/labels_initial.parquet` (topics assigned)
- [ ] `output/topics_trend_YYYY-MM-DD.csv` (trend table)
- [ ] `output/topics_trend_YYYY-MM-DD.html` (HTML report)

---

## 🎥 Ready to Record Demo

Once you have the outputs:
1. Record screen (use OBS, QuickTime, etc.)
2. Show Jupyter executing notebooks
3. Show final HTML report
4. Keep it to 5-6 minutes
5. Upload to Google Drive

---

## 🆘 Need Help?

If you encounter errors, check:
- `.env` file exists with OPENAI_API_KEY
- Jupyter is running (terminal shows "Serving notebooks...")
- Not out of disk space (`df -h`)
- Virtual env activated (see `(venv)` in prompt)

---

**START NOW**: Just run the commands in Step 1! 🚀

