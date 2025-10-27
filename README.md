# Agentic Topic Discovery System for Swiggy Reviews

An end-to-end pipeline that automatically discovers, categorizes, and tracks topics from Google Play reviews using LLM-powered agentic workflows in **Jupyter Notebooks**.

## Quick Start

### 1. Setup Environment

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
# Create .env file (or use environment variables)
echo "OPENAI_API_KEY=your-key-here" > .env
```

### 3. Run Notebooks

```bash
# Launch Jupyter
jupyter notebook notebooks/

# Then run notebooks in order:
# 1. 01_setup_and_clean.ipynb        # Load and clean CSV
# 2. 02_topic_router.ipynb            # Route reviews to topics  
# 3. 05_trend_analysis.ipynb          # Generate trend tables
```

## Project Structure

```
Assignment/
├── data/                              # Data storage
│   ├── swiggy_scraped.csv             # Original 250K reviews
│   ├── reviews_clean.parquet          # Cleaned data (from notebook 1)
│   └── labels_initial.parquet         # Topic assignments (from notebook 2)
├── registry/
│   └── topic_registry.json            # 32 seed topics
├── notebooks/                          # Main pipeline
│   ├── 01_setup_and_clean.ipynb      # Data cleaning
│   ├── 02_topic_router.ipynb          # LLM topic routing
│   ├── 03_novel_discovery.ipynb      # Discover new topics
│   ├── 04_canonicalizer.ipynb         # Merge duplicates
│   ├── 05_trend_analysis.ipynb        # 30-day trends
│   └── 06_audit_ui.ipynb              # Quality audits
├── utils/
│   └── llm_client.py                  # Unified OpenAI/Ollama wrapper
├── output/                             # Generated reports
│   ├── topics_trend_YYYY-MM-DD.csv    # Trend data
│   └── topics_trend_YYYY-MM-DD.html   # Interactive HTML
├── requirements.txt
└── README.md
```

## Notebook Workflow

### Notebook 1: Setup & Clean (`01_setup_and_clean.ipynb`)
- Load 250K reviews from CSV
- Parse datetimes (IST timezone)
- Normalize text (lowercase, strip)
- Add computed columns (length, short review flag)
- Save to Parquet (efficient for analytics)

**Output**: `data/reviews_clean.parquet`

### Notebook 2: Topic Router (`02_topic_router.ipynb`)
- Load topic registry (32 seed topics)
- Use LLM to assign topics to reviews
- Multi-label classification (one review → multiple topics)
- Mark novel reviews (don't fit existing topics)
- Cache results for performance

**Output**: `data/labels_initial.parquet`

### Notebook 3: Novel Discovery (`03_novel_discovery.ipynb`)
- Cluster NOVEL reviews using embeddings
- Generate candidate topic proposals
- Interactive review interface

**Output**: Candidate topics for canonicalization

### Notebook 4: Canonicalizer (`04_canonicalizer.ipynb`)
- Compare candidate vs existing topics
- Merge duplicates using pairwise judge
- Update topic registry

**Output**: Updated `registry/topic_registry.json`

### Notebook 5: Trend Analysis (`05_trend_analysis.ipynb`)
- Load topic labels
- Generate 30-day pivot table using DuckDB
- Compute 7-day change percentages
- Create sparklines (Unicode bar charts)
- Export CSV + HTML

**Output**: `output/topics_trend_YYYY-MM-DD.csv` and `.html`

### Notebook 6: Audit UI (`06_audit_ui.ipynb`)
- Browse topics with examples
- Precision/recall audits
- Manual topic management
- View drift metrics

## Topic Registry

32 seed topics across 7 facets:

- **Logistics** (5): Order Incomplete, ETA Jump, Late Delivery, Can't Find Address, No Cancel Option
- **Food** (4): Stale Food, Wrong Item, Packaging Leak, Poor Quality
- **Pricing** (3): High Fees, Surge Pricing, Overpriced Items
- **Support** (3): Bot Only No Human, Refund Friction, No Response
- **App/Payments** (5): Payment Failure, Login Bug, Cart Bug, OTP Issue, COD Not Available
- **Partner** (2): Rude Delivery Person, Unprofessional
- **Merch** (2): Out of Stock, Limited Options
- **Sentiment** (8): Positive Experience, Negative Generic, Fast Delivery, Good Quality Food, Very Good Service, Great App

## LLM Setup

### OpenAI API (Recommended)
```python
# In notebook cells
llm = LLMClient(provider='openai', model='gpt-3.5-turbo')
```
- Fast processing (~20 min for 1000 reviews)
- Costs ~$5-10 for full 250K dataset
- High accuracy

### Ollama Local (Free)
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.1:8b

# In notebooks
llm = LLMClient(provider='ollama', model='llama3.1:8b')
```
- No API costs
- Slower (10-20x)
- Good for development/testing

## Usage Examples

### Run Pipeline on Sample
```python
# In notebook 02_topic_router.ipynb
MAX_REVIEWS = 1000  # Process first 1000 for testing
llm = LLMClient(provider='openai', model='gpt-3.5-turbo')
# Execute cells...
```

### Generate Trend Report
```bash
jupyter notebook notebooks/05_trend_analysis.ipynb
# Run all cells to generate HTML report
```

### View Results
```bash
# Open HTML report
open output/topics_trend_2025-10-27.html

# Or browse CSV
head -n 20 output/topics_trend_2025-10-27.csv
```

## Key Features

✅ **Multi-label classification** - One review can have multiple topics  
✅ **Novel topic discovery** - Automatically detect new patterns  
✅ **Pairwise canonicalization** - Merge duplicate topics  
✅ **30-day rolling trends** - Track topic evolution over time  
✅ **Sparklines** - Visual trend indicators  
✅ **7-day delta** - See recent changes  
✅ **Dual LLM support** - OpenAI API + local Ollama  
✅ **Efficient caching** - SQLite cache for LLM calls

## Quality Targets

- ≥85% precision on top-10 topics
- ≤10% missed assignments (recall)
- Novel topic time-to-canonicalize ≤48h
- Registry stability (≤5 merges/week after warm-up)

## Requirements

```
polars>=0.20.0          # Data processing
duckdb>=0.10.0          # Analytics
openai>=1.10.0          # LLM API
langchain-ollama>=0.1.0 # Local LLMs
sentence-transformers>=2.5.0  # Embeddings
hdbscan>=0.8.33         # Clustering
jupyter>=1.1.0          # Notebooks
tqdm>=4.66.0            # Progress bars
```

## Troubleshooting

### OpenAI API errors
```bash
# Check API key
echo $OPENAI_API_KEY

# Or set in .env
export OPENAI_API_KEY=sk-...
```

### Ollama not responding
```bash
# Start Ollama service
ollama serve

# Test connection
curl http://localhost:11434/api/generate
```

### Import errors
```python
# In notebook, add path
import sys
sys.path.append('../')
```

## Output Format

### CSV: `topics_trend_2025-10-27.csv`
```csv
topic_id,2025-09-27,2025-09-28,...,2025-10-26,7d_change_pct
ORDER_INCOMPLETE,45,52,...,61,+12.3
ETA_JUMP_AFTER_PAYMENT,23,19,...,31,+8.5
```

### HTML: `topics_trend_2025-10-27.html`
- Sortable table
- Sparklines (▁▂▃▅▇█)
- Color-coded 7d Δ (green ↑, red ↓)
- Responsive layout

## Next Steps

1. **Run notebook 1** to clean the 250K reviews CSV
2. **Run notebook 2** to route topics (start with 1000 reviews sample)
3. **Check results** in `data/labels_initial.parquet`
4. **Run notebook 5** to generate trends
5. **View HTML report** for visualizations

## License

MIT
