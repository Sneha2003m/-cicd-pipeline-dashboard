import pandas as pd

df = pd.read_csv("data/pipeline_data.csv")

# Add success/failure columns
df["is_success"] = df["result"] == "SUCCESS"
df["is_failure"] = df["result"] == "FAILURE"

# Summary metrics per job
summary = df.groupby("job_name").agg(
    total_builds=("build_number", "count"),
    success_count=("is_success", "sum"),
    failure_count=("is_failure", "sum"),
    avg_duration_sec=("duration_sec", "mean"),
    last_build=("timestamp", "max")
).reset_index()

summary["success_rate_%"] = round((summary["success_count"] / summary["total_builds"]) * 100, 1)
summary["failure_rate_%"] = round((summary["failure_count"] / summary["total_builds"]) * 100, 1)

# Save cleaned files
df.to_csv("data/pipeline_data_clean.csv", index=False)
summary.to_csv("data/pipeline_summary.csv", index=False)

print("✅ Cleaned data saved!")
print("\n--- Pipeline Summary ---")
print(summary[["job_name","total_builds","success_rate_%","failure_rate_%","avg_duration_sec"]])