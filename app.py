import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

st.title("📊 Trader Performance vs Market Sentiment")
st.markdown("Analyze how sentiment impacts trading behavior and profitability")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("merged_data.csv")

df = load_data()

# Sidebar filter
st.sidebar.header("Filters")

sentiment_options = df['sentiment'].dropna().unique()

selected_sentiment = st.sidebar.multiselect(
    "Select Sentiment",
    options=sentiment_options,
    default=sentiment_options
)

# Handle empty selection
if len(selected_sentiment) == 0:
    st.warning("Please select at least one sentiment.")
    st.stop()

df_filtered = df[df['sentiment'].isin(selected_sentiment)].copy()

# 📊 Key Metrics
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg PnL", round(df_filtered['Closed PnL'].mean(), 2))
col2.metric("Win Rate", round(df_filtered['win'].mean()*100, 2))
col3.metric("Total Trades", len(df_filtered))

# Dataset preview
st.subheader("Dataset Overview")
st.dataframe(df_filtered[['Account','Coin','Size USD','Closed PnL','sentiment']].head())

# Sentiment order
order = ['Extreme Fear','Fear','Neutral','Greed','Extreme Greed']

# 📉 PnL Distribution
st.subheader("PnL Distribution by Sentiment")

fig1, ax1 = plt.subplots(figsize=(8,5))
sns.boxplot(x='sentiment', y='Closed PnL', data=df_filtered, order=order, ax=ax1)
plt.xticks(rotation=30)
st.pyplot(fig1)

# 📊 Behavior
st.subheader("Average Trade Size")

behavior = df_filtered.groupby('sentiment')['Size USD'].mean().reindex(order)
st.bar_chart(behavior)

# 📊 Long vs Short
st.subheader("Trading Direction")

ls_data = df_filtered.groupby(['sentiment','Side']).size().reset_index(name='count')

fig2, ax2 = plt.subplots(figsize=(8,5))
sns.barplot(data=ls_data, x='sentiment', y='count', hue='Side', order=order, ax=ax2)
plt.xticks(rotation=30)
st.pyplot(fig2)

# 📊 Segmentation
st.subheader("Trader Segmentation")

df_filtered['size_group'] = pd.qcut(df_filtered['Size USD'], 2, labels=['Low','High'])

seg = df_filtered.groupby(['size_group','sentiment'])['Closed PnL'].mean().unstack()
st.dataframe(seg)

# 📊 Performance summary
st.subheader("Performance Summary")

perf = df_filtered.groupby('sentiment').agg({
    'Closed PnL':'mean',
    'win':'mean'
}).reindex(order)

st.dataframe(perf)

# 💡 Insights
st.subheader("Key Insights")

st.write("""
- Profitability increases from Fear to Greed
- Extreme Greed shows highest returns and win rate
- Traders take larger positions during Greed
- Fear markets show lower performance and higher inefficiency
""")