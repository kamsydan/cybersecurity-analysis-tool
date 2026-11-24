
# Simple Security Log Analyzer

def analyze_logs(logs):
    for log in logs:
        if "FAILED" in log:
            print("Warning: Failed login detected")
        else:
            print("Login successful")


logs = [
    "SUCCESS - User logged in",
    "FAILED - Incorrect password",
    "SUCCESS - Admin logged in",
    "FAILED - Invalid username"
]

analyze_logs(logs)
