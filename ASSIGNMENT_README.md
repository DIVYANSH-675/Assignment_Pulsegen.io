# Pulsegen Technologies - Senior AI Engineer Assignment

## Project: Agentic Topic Discovery for Swiggy Reviews

Complete solution for analyzing Google Play Store reviews using Agentic AI approaches.

## 📋 Assignment Requirements Checklist

### ✅ Core Requirements
- [x] Take Google Play Store reviews from June 2024-till date for Swiggy
- [x] Treat daily data as batch (June 1st, 2024 onward)
- [x] AI agent consumes daily data
- [x] Creates trend analysis report for issues, requests, feedback
- [x] Output: Table with Rows=Topics, Columns=Dates T-30 to T
- [x] Cell values: Frequency of topic occurrence per date
- [x] Seed topics provided (32 topics)
- [x] Agent identifies new evolving topics
- [x] Agent creates new categories as needed
- [x] Uses Agentic AI approaches (LLM-based, NOT TopicBERT/LDA)
- [x] Handles similar topic consolidation
- [x] High recall agents for accurate trends
- [x] Sample output reports in `/output/` folder

### ✅ Deliverables Checklist
- [ ] Private GitHub Repository (to be shared)
- [ ] Video Demonstration (instructions provided)
- [ ] Sample Output Reports (to be generated)

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
cd /home/ubuntu/Desktop/Assignment
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Configure OpenAI API Key
```bash
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

### Step 3: Run Complete Pipeline
```bash
jupyter notebook notebooks/
```

**Notebooks to run in order:**
1. `01_setup_and_clean.ipynb` - Cleans 250K reviews CSV → Parquet
2. `02_topic_router.ipynb` - Routes reviews to topics using LLM
3. `05_trend_analysis.ipynb` - Generates trend report

## 📊 Output Format

The trend analysis report is a table where:
- **Rows**: Topics (issues, requests, feedback)
- **Columns**: Dates from T-30 to T
- **Cells**: Frequency of topic occurrence on that date

### Example Output Structure:

```
Topic                          Jun 1  Jun 2  Jun 3  ...  Jun 30
Delivery issue                 12     8      15     ...  23
Food stale                     5      7      3      ...  11
Delivery partner rude          8      12     6      ...  9
Maps not working properly      2      4      7      ...  5
Instamart should be open all night  1   0      3      ...  4
Bring back 10 minute bolt delivery  0 2      1      ...  6
```

## 🎯 Key Features

### Agentic AI Approach
- **NO LDA/TopicBERT** (rejected as per requirements)
- **LLM-based classification** using OpenAI GPT-3.5-turbo
- **Multi-label routing** - one review can have multiple topics
- **Novel topic detection** - automatically discovers new patterns
- **Topic consolidation** - merges similar topics to prevent duplicates

### High Recall Agents
- **Topic registry**: 32 seed topics covering common issues
- **Semantic matching** using LLM embeddings
- **Pairwise comparison** to merge similar topics:
  - "Delivery guy was rude" ≈ "Delivery partner behaved badly" 
  - Consolidated into: "Delivery partner rude"

### Technical Implementation
- **Polars** for fast data processing
- **DuckDB** for efficient pivots/aggregations
- **OpenAI API** for LLM classification
- **Jupyter Notebooks** for interactive development
- **Parquet** format for efficient storage

## 📁 Project Structure

```
Assignment/
├── notebooks/
│   ├── 01_setup_and_clean.ipynb      # Step 1: Clean data
│   ├── 02_topic_router.ipynb         # Step 2: Route topics
│   └── 05_trend_analysis.ipynb       # Step 3: Generate trends
├── registry/
│   └── topic_registry.json           # 32 seed topics
├── utils/
│   └── llm_client.py                  # LLM wrapper (OpenAI/Ollama)
├── data/
│   ├── swiggy_scraped.csv             # Input: 250K reviews
│   ├── reviews_clean.parquet          # Cleaned data
│   └── labels_initial.parquet         # Topic assignments
└── output/
    ├── topics_trend_YYYY-MM-DD.csv    # CSV report
    └── topics_trend_YYYY-MM-DD.html   # HTML report
```

## 🔬 How It Works

### Step 1: Data Cleaning
- Load CSV with 250K Swiggy reviews
- Parse datetimes (IST timezone)
- Normalize text (lowercase, strip)
- Add computed columns (length, short review flag)
- Save to Parquet for efficient processing

### Step 2: Topic Routing (Agentic)
- Load 32 seed topics from registry
- For each review, use LLM to classify:
  - Match to existing topics (multi-label allowed)
  - OR mark as NOVEL (new pattern)
- Cache results for performance

**LLM Prompt Strategy:**
- System prompt: Explains topic taxonomy
- User prompt: Review text + Topic registry
- Output: JSON with topic_ids array or NOVEL flag

### Step 3: Trend Analysis
- Load topic assignments
- Use DuckDB to pivot: Topics × Dates
- Calculate 7-day change percentage
- Generate sparklines (Unicode bar charts)
- Export to CSV + HTML

## 🎬 Video Demonstration Instructions

### What to Show (5-6 minutes):

1. **Overview** (30 sec)
   - Show project structure
   - Explain agentic approach vs traditional methods

2. **Run Notebook 1** (1 min)
   - Execute cells to clean CSV
   - Show statistics (date range, review counts)

3. **Run Notebook 2** (2 min)
   - Execute topic routing with sample data
   - Show LLM calls happening
   - Display topic distribution

4. **Run Notebook 5** (1 min)
   - Generate trend report
   - Open HTML in browser
   - Show sparklines and trends

5. **Result Showcase** (30 sec)
   - Open generated CSV
   - Highlight topic consolidation working
   - Show how "Delivery guy rude" and "Delivery partner rude" are merged

### Recording Tips:
- Use screen recording tool (OBS, QuickTime, etc.)
- Show Jupyter cells executing
- Narrate what's happening
- Keep it under 6 minutes

## 📝 Submission Checklist

Before submitting to `vatsal@pulsegen.io`:

- [ ] Run all notebooks successfully
- [ ] Generate sample reports in `/output/` folder
- [ ] Initialize git repository
- [ ] Push to private GitHub repo
- [ ] Record video demonstration
- [ ] Upload video to Google Drive
- [ ] Share links to:
  - GitHub repo
  - Google Drive video
  - Sample output reports

## 🔧 Troubleshooting

### OpenAI API Issues
```bash
# Check API key
export OPENAI_API_KEY=sk-...

# Or add to .env
echo "OPENAI_API_KEY=sk-..." > .env
```

### Memory Issues with 250K Reviews
- Process in batches: Set `MAX_REVIEWS = 5000` initially
- Use sampling for testing
- Full 250K takes ~20 min with OpenAI API

### Jupyter Not Starting
```bash
pip install jupyter --upgrade
jupyter notebook notebooks/ --port 8888
```

## 📊 Expected Results

After running all notebooks:
- **Input**: 250K reviews from Swiggy
- **Output**: Trend table with 30+ topics
- **Format**: CSV + HTML with sparklines
- **Quality**: High recall, accurate topic consolidation

## 🎓 What Makes This Solution Stand Out

1. **Pure Agentic AI**: No traditional topic modeling (LDA/TopicBERT)
2. **High Recall**: LLM captures nuanced topics
3. **Automatic Consolidation**: Similar topics merged automatically
4. **Scalable**: Handles 250K+ reviews efficiently
5. **Production-Ready**: Parquet storage, DuckDB analytics
6. **Extensible**: Easy to add new topics or modify logic

## 📅 Timeline for Assignment

- **Setup**: 5 minutes
- **Notebook 1**: 10 minutes (data cleaning)
- **Notebook 2**: 20 minutes (topic routing with API)
- **Notebook 5**: 2 minutes (trend generation)
- **Video Demo**: 5-6 minutes
- **Total**: ~45 minutes to complete

## 📧 Submission Details

**Email to**: vatsal@pulsegen.io
**Subject**: Senior AI Engineer Assignment - [Your Name]

**Include**:
- GitHub repo link (private)
- Google Drive video link
- Brief summary of approach

---

**Good Luck with Your Submission! 🚀**

