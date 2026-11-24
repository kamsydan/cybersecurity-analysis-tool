
# Simple Security Log Analyzer

def analyze_logs(logs):
    failed_count = 0

    for log in logs:
        if "FAILED" in log:
            print("Warning: Failed login detected")
            failed_count += 1
        else:
            print("Login successful")

    print("Total failed login attempts:", failed_count)
    
   if failed_count > 0:
        print("Security alert: Review failed login attempts.")


logs = [
    "SUCCESS - User logged in",
    "FAILED - Incorrect password",
    "SUCCESS - Admin logged in",
    "FAILED - Invalid username"
]

analyze_logs(logs)
