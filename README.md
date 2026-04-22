# trader-performance-sentiment-analysis
# 📊 Trader Performance vs Market Sentiment Analysis

This project analyzes how market sentiment (Fear/Greed) impacts trader behavior and performance using real trading data.

---

## 📌 Objective

To understand the relationship between market sentiment and trading outcomes, and derive actionable strategies for improving performance.

---

## 📂 Datasets Used

1. **Bitcoin Market Sentiment Dataset**
   - Contains daily sentiment classification (Fear, Greed, Extreme levels)

2. **Hyperliquid Trading Data**
   - Includes trade-level data such as:
     - Account
     - Trade size
     - Execution price
     - Side (Buy/Sell)
     - Closed PnL

---

## 🧹 Data Preparation

- Converted timestamps to consistent date format
- Aligned datasets using time-based merge (`merge_asof`)
- Created new features:
  - `win` (profitability indicator)
  - Daily trading metrics
- Cleaned and processed data for analysis

---

## 📊 Key Analysis

### 1. Performance vs Sentiment
- Profitability increases from Fear → Greed
- Extreme Greed shows highest PnL and win rate
- Extreme Fear shows lowest performance

### 2. Trader Behavior
- Trade sizes increase during Greed periods
- Trading activity is higher in bullish markets

### 3. Trader Segmentation
- High-size traders generate higher returns
- Low-frequency traders perform better in Fear markets
- Consistent winners outperform across all sentiments

---

## 💡 Key Insights

- Market sentiment strongly influences trading outcomes
- Greed periods offer higher profitability but involve higher risk
- Fear periods lead to lower returns and inefficient trading behavior

---

## 🎯 Strategy Recommendations

1. **Reduce risk during Fear periods**
   - Lower position sizes
   - Avoid overtrading

2. **Capitalize on Greed momentum**
   - Increase exposure during bullish sentiment
   - Apply proper risk management

3. **Optimize trade frequency**
   - Avoid excessive trading in volatile markets

---

## 🤖 Bonus Work

### Predictive Model
- Built a Random Forest model to predict trade profitability
- Achieved ~73% accuracy

### Trader Clustering
- Identified behavioral archetypes:
  - High-risk traders
  - Consistent performers
  - Low-activity traders

### Streamlit Dashboard
- Interactive dashboard for:
  - PnL analysis
  - Behavior exploration
  - Sentiment filtering

---

## 🖥️ Streamlit App

To run locally:

```bash
pip install streamlit pandas matplotlib seaborn scikit-learn
streamlit run app.py
