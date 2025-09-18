import pandas as pd
import random

# === Load Dataset ===
# Attempt to load the phishing email dataset from the local directory
print("Loading dataset...")
try:
    df = pd.read_csv("Phishing_Email.csv")  # Ensure this file is in the same folder
except FileNotFoundError:
    print("File not found. Please verify that 'Phishing_Email.csv' exists in the working directory.")
    exit()

# === Sample 1000 Emails ===
# Randomly select 1000 email samples for threat detection analysis
df_sample = df.sample(n=1000, random_state=42)

# === Detection Function ===
# Define a function to simulate threat detection based on email content and synthetic features
def Detect_Email_Threat(email_text):
    # Simulated visual-semantic features (e.g., layout anomalies, branding)
    visual_semantic_features = {
        "has_logo": True,
        "layout_anomaly": random.choice([True, False])
    }

    # Construct a synthetic feature vector for threat evaluation
    feature_vector = {
        "text_length": len(str(email_text)),  # Length of the email text
        "has_link": "http" in str(email_text),  # Presence of hyperlinks
        "user_behavior_score": random.uniform(0, 1),  # Simulated user interaction risk
        "global_threat_score": random.uniform(0, 1),  # Simulated global threat intelligence score
        "impersonation_risk": random.choice(["Low", "High"]),  # Risk of sender impersonation
        "robustness": random.choice([True, False])  # Model confidence in detection
    }

    # Decision logic based on feature thresholds
    if feature_vector["global_threat_score"] > 0.85:
        return "Confirmed Threat: Block/Quarantine"
    elif feature_vector["user_behavior_score"] > 0.7 and not feature_vector["robustness"]:
        return "High Suspicion: User Alert & Sandboxing"
    elif feature_vector["impersonation_risk"] == "High":
        return "Impersonation Risk: Quarantine & Identity Verification"
    elif feature_vector["user_behavior_score"] > 0.7:
        return "Moderate Suspicion: User Alert & Further Analysis"
    elif not feature_vector["robustness"]:
        return "Potential Evasion: Flag for Review"
    else:
        return "Legitimate: Deliver"

# === Run Detection ===
# Apply the detection function to each email sample
print("Running threat detection on 1000 samples...")
results = df_sample.apply(lambda row: Detect_Email_Threat(row.get("EmailText", "")), axis=1)

# === Summarize Results ===
# Display the frequency of each detection outcome
summary = results.value_counts()
print("\nDetection Summary:")
print(summary)
