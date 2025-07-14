# Databricks notebook source
import pandas as pd

# Detect dataset type
file_path = "file:/Workspace/Users/akvincen@syr.edu/facebook_ads.csv"  # CHANGE THIS
if "ads" in file_path:
    dataset = "facebook_ads"
elif "fb_posts" in file_path:
    dataset = "fb_posts"
else:  # twitter_posts
    dataset = "twitter_posts"

# Load data with numeric cleaning
df = pd.read_csv(file_path.replace("file:", ""), thousands=',')

print(f"Analyzing {dataset} ({len(df)} records)")

# Dataset-specific configuration
if dataset == "facebook_ads":
    value_cols = ["estimated_audience_size", "estimated_impressions", "estimated_spend"]
    group1 = "page_id"
    group2 = ["page_id", "ad_id"]
elif dataset == "fb_posts":
    value_cols = ["Total Interactions", "Likes", "Comments", "Post Views"]
    group1 = "Facebook_Id"
    group2 = ["Facebook_Id", "post_id"]
else:  # twitter_posts
    value_cols = ["retweetCount", "replyCount", "likeCount", "viewCount"]
    group1 = "source"
    group2 = ["source", "id"]

# Global statistics
print("\n=== Global Statistics ===")
print(df[value_cols].describe())

# Categorical analysis
categorical_cols = [col for col in df.columns if col not in value_cols and df[col].nunique() < 20]
for col in categorical_cols[:3]:  # First 3 categoricals
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts().head(5))

# Grouped analysis
print("\n=== Grouped by Primary Key ===")
grouped = df.groupby(group1)[value_cols[0]].agg(["mean", "min", "max", "count"])
print(grouped.head(5))

print("\n=== Grouped by Composite Key ===")
grouped = df.groupby(group2)[value_cols[0]].agg(["mean", "min", "max", "count"])
print(grouped.head(5))