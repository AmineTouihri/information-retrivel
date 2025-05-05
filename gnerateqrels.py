import pandas as pd

def generate_qrels(queries_df, tweets_df, output_path="qrels.tsv"):
    """
    Generate a new qrels file based on:
    - queries_df: DataFrame containing your evaluation queries
    - tweets_df: DataFrame containing your indexed tweets
    - output_path: Path to save the new qrels file
    """
    qrels = []
    
    # For each query, mark first 30 tweets as relevant (1), rest as non-relevant (0)
    for _, row in queries_df.iterrows():
        qid = row['qid']
        query = row['query']
        
        # Get top 100 tweets for this query (or all if less than 100)
        # Note: You may need to implement actual retrieval here
        # This is just a template - adjust based on your actual data
        for i, tweet in enumerate(tweets_df.itertuples()):
            relevance = 1 if i < 30 else 0
            qrels.append(f"{qid} 0 {tweet.docno} {relevance}")
    
    # Save to file
    with open(output_path, "w") as f:
        f.write("\n".join(qrels))
    print(f"Generated new qrels file at {output_path} with {len(qrels)} judgments")

# Example usage
if __name__ == "__main__":
    # Load your queries (same as in evaluation)
    queries_df = pd.DataFrame([
        {"qid": "MB39", "query": "Gaza under attack"},
        {"qid": "MB40", "query": "Military occupation Gaza"},
        {"qid": "MB41", "query": "Israel Genocide Gaza"},
        {"qid": "MB42", "query": "Ceasefire in Gaza"},
        {"qid": "MB43", "query": "Massacres in Gaza"},
        {"qid": "MB44", "query": "Palestinian rights"},
        {"qid": "MB45", "query": "Refugees from Gaza"},
    ])
    
    # Load your tweets (must contain docno and text)
    tweets_df = pd.read_csv("tweets.tsv", sep="\t")
    
    # Generate new qrels
    generate_qrels(queries_df, tweets_df)