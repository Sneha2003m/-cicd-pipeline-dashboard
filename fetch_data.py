import requests
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

JENKINS_URL = os.getenv("JENKINS_URL")
USER = os.getenv("JENKINS_USER")
TOKEN = os.getenv("JENKINS_TOKEN")

JOBS = ["build-app", "run-tests", "deploy-app"]

all_builds = []

for job in JOBS:
    url = f"{JENKINS_URL}/job/{job}/api/json?tree=builds[number,result,duration,timestamp]"
    response = requests.get(url, auth=(USER, TOKEN))
    data = response.json()

    for build in data["builds"]:
        all_builds.append({
            "job_name": job,
            "build_number": build["number"],
            "result": build["result"],
            "duration_sec": round(build["duration"] / 1000, 2),
            "timestamp": datetime.fromtimestamp(build["timestamp"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
        })

df = pd.DataFrame(all_builds)
df.to_csv("data/pipeline_data.csv", index=False)
print("✅ Data saved to data/pipeline_data.csv")
print(df)