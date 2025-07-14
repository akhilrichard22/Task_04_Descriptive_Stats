# Databricks notebook source
import csv
from collections import defaultdict
import math
import sys

def main(file_path):
    # Detect dataset type from filename
    if "ads" in file_path:
        dataset = "facebook_ads"
    elif "fb_posts" in file_path:
        dataset = "fb_posts"
    elif "tw_posts" in file_path:
        dataset = "twitter_posts"
    else:
        print("Unknown dataset type!")
        return

    # Dataset-specific configuration
    if dataset == "facebook_ads":
        key_cols = ["page_id", "ad_id"]
        value_cols = ["estimated_audience_size", "estimated_impressions", "estimated_spend"]
        group1 = "page_id"
        group2 = ["page_id", "ad_id"]
    elif dataset == "fb_posts":
        key_cols = ["Facebook_Id", "post_id"]
        value_cols = ["Total Interactions", "Likes", "Comments", "Post Views"]
        group1 = "Facebook_Id"
        group2 = ["Facebook_Id", "post_id"]
    else:  # twitter_posts
        key_cols = ["id"]
        value_cols = ["retweetCount", "replyCount", "likeCount", "viewCount"]
        group1 = "source"
        group2 = ["source", "id"]

    # Load data
    data = []
    with open(file_path.replace("file:", ""), "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Clean numeric values
            cleaned = {}
            for col, val in row.items():
                if col in value_cols:
                    try:
                        val = float(val.replace(",", "").replace('"', ''))
                    except:
                        val = 0.0
                cleaned[col] = val
            data.append(cleaned)
    
    print(f"Analyzing {dataset} ({len(data)} records)")
    
    # Global statistics
    print("\n=== Global Statistics ===")
    for col in value_cols:
        values = [row[col] for row in data]
        print(f"{col}:")
        print(f"  Mean: {sum(values)/len(values):.2f}")
        print(f"  Min: {min(values)}")
        print(f"  Max: {max(values)}")
        print(f"  StdDev: {math.sqrt(sum((x - sum(values)/len(values))**2 for x in values)/len(values)):.2f}")
    
    # Grouped by primary key
    print("\n=== Grouped by Primary Key ===")
    grouped = defaultdict(list)
    for row in data:
        key = row[group1]
        grouped[key].append(row)
    
    for key, group in list(grouped.items())[:5]:  # Show top 5
        for value_col in value_cols[:1]:  # First value column only
            values = [row[value_col] for row in group]
            print(f"{group1} {key}:")
            print(f"  Avg {value_col}: {sum(values)/len(values):.2f}")
            print(f"  Min: {min(values)}")
            print(f"  Max: {max(values)}")
    
    # Grouped by composite key
    print("\n=== Grouped by Composite Key ===")
    grouped = defaultdict(list)
    for row in data:
        key = tuple(row[col] for col in group2)
        grouped[key].append(row)
    
    for key, group in list(grouped.items())[:5]:  # Show top 5
        for value_col in value_cols[:1]:  # First value column only
            values = [row[value_col] for row in group]
            print(f"{group2} {key}:")
            print(f"  Avg {value_col}: {sum(values)/len(values):.2f}")

if __name__ == "__main__":
    file_path = "file:/Workspace/Users/akvincen@syr.edu/fb_posts.csv"  # CHANGE THIS Filename
    main(file_path)