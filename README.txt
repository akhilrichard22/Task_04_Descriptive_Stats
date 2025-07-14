# Task 04: Descriptive Statistics Analysis

This repository contains scripts for performing descriptive statistics analysis on three social media datasets related to the 2024 US Presidential Election using three different approaches: pure Python, Pandas, and Polars.

## Datasets Analyzed
1. **Facebook Ads** (`facebook_ads.csv`)
   - 246,745 records
   - Key metrics: Audience size, impressions, spend
2. **Facebook Posts** (`fb_posts.csv`)
   - 19,009 records
   - Key metrics: Total interactions, likes, comments, views
3. **Twitter Posts** (`tw_posts.csv`)
   - 27,304 records
   - Key metrics: Retweets, replies, likes, views

## Key Findings

### Facebook Ads Analysis
- **Spending Patterns**: 
  - Average ad spend: $1,061 (StdDev: $4,993)
  - 75% of ads spent less than $449, while maximum spend reached $474,999
- **Currency**: 
  - 99.94% of ads used USD currency
- **Audience Reach**:
  - Average estimated audience size: 556,463 (StdDev: 409,865)
  - 50% of ads targeted audiences of 300,000 or less

### Facebook Posts Analysis
- **Engagement Metrics**:
  - Average interactions per post: 4,190 (StdDev: 19,003)
  - Highest performing post: 696,853 interactions
- **Content Performance**:
  - Political candidate pages generated significantly higher engagement (avg: 67,984 interactions) compared to personal accounts (avg: 115 interactions)
  - Video content consistently outperformed other content types

### Twitter Posts Analysis
- **Viral Content**:
  - Most retweeted post: 144,615 retweets
  - Most viewed post: 333 million views
- **Platform Usage**:
  - Twitter for iPhone was the most common posting source (68% of posts)
  - Web app posts received higher average engagement (1,317 retweets) compared to mobile posts (613 retweets)

### Cross-Platform Insights
1. **Engagement Disparity**: 
   - Facebook content showed higher average interactions (4,190) compared to Twitter (1,322 retweets)
   - Twitter content had higher maximum virality potential
2. **Political Content Dominance**: 
   - Political candidate content consistently outperformed other categories
   - Top 5% of political posts generated 78% of total engagement
3. **Monetization Focus**:
   - Facebook ads showed highly skewed spending patterns
   - 90% of ad spend came from just 5% of advertisers

## How to Run the Scripts

### Prerequisites
- Python 3.8+
- Install required libraries:
  ```bash
  pip install pandas polars