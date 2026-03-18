import pandas as pd

# Load data
df = pd.read_json("../data/raw/oncology_trials.json")

print("Columns:")
print(df.columns)

print("\nNumber of trials:", len(df))

# Save to CSV
output_path = "../data/results/oncology_summary.csv"
df.to_csv(output_path, index=False)
print(f"\nResults saved to {output_path}")

df.to_csv("../data/results/oncology_summary.csv", index=False)

