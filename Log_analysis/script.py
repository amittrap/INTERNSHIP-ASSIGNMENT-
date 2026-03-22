import pandas as pd

# =========================
# LOAD FILE (FIXED STRUCTURE)
# =========================
log_file = r"C:\Users\ankit\OneDrive\Desktop\log anaysis tool\windows_security_log.csv"

df = pd.read_csv(
    log_file,
    encoding='utf-8',
    engine='python',
    on_bad_lines='skip'
)

# Fix shifted columns
df = df.reset_index()

# Rename columns properly
df.columns = [
    "Keywords",
    "Date and Time",
    "Source",
    "Event ID",
    "Task Category",
    "Message"
]

# Clean Event ID column (extract numeric part)
df["Event ID"] = df["Event ID"].astype(str).str.extract(r'(\d+)')
df["Event ID"] = pd.to_numeric(df["Event ID"], errors="coerce")

# Convert date
df["Date and Time"] = pd.to_datetime(
    df["Date and Time"],
    format="%d-%m-%Y %H:%M:%S",
    errors="coerce"
)

print("\n===== 🔎 Windows Security Log Analysis =====\n")

# =========================
# COUNT IMPORTANT EVENTS
# =========================

important_events = {
    4624: "Successful Login",
    4625: "Failed Login",
    4740: "Account Lockout",
    4672: "Special Privileges Assigned",
    4688: "Process Created",
    4798: "User Group Enumeration"
}

for event_id, description in important_events.items():
    count = len(df[df["Event ID"] == event_id])
    print(f"{description} ({event_id}): {count}")

# =========================
# SHOW TOP 5 MOST COMMON EVENTS
# =========================
print("\n📊 Top 5 Most Frequent Event IDs:")
print(df["Event ID"].value_counts().head())

print("\n===== ✅ Analysis Complete =====")