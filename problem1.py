import re
from collections import defaultdict
from datetime import datetime

def parse_log_entry(entry):
    # Parse log entry into structured format
    pattern = r"\[(.*?)\] \[(.*?)\] \[(.*?)\] \[(.*?)\]"
    match = re.match(pattern, entry)

    if match:
        timestamp_str, severity, source, message = match.groups()
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return {"timestamp": timestamp, "severity": severity, "source": source, "message": message}
    else:
        return None

def read_log_file(file_path):
    # Read and parse log file
    with open(file_path, "r") as file:
        return [parse_log_entry(line.strip()) for line in file]

def filter_by_severity(log_entries, target_severity):
    # Filter log entries by severity
    return [entry for entry in log_entries if entry["severity"] == target_severity]

def count_events_by_source(log_entries):
    # Count events for each source
    source_counts = defaultdict(int)
    for entry in log_entries:
        source_counts[entry["source"]] += 1
    return dict(source_counts)

def identify_top_errors(log_entries, num_errors=5):
    # Identify and display the top N error messages
    error_entries = [entry["message"] for entry in log_entries if entry["severity"] == "ERROR"]
    top_errors = sorted(error_entries, key=error_entries.count, reverse=True)[:num_errors]
    return top_errors

def filter_by_time_range(log_entries, start_time, end_time):
    # Filter log entries within a specified time range
    return [entry for entry in log_entries if start_time <= entry["timestamp"] <= end_time]

# Example Usage:
log_file_path = "sample_log.txt"
log_entries = read_log_file(log_file_path)

# Example 1: Filter by Severity
filtered_entries = filter_by_severity(log_entries, "ERROR")

# Example 2: Count Events by Source
source_counts = count_events_by_source(log_entries)

# Example 3: Identify Top Errors
top_errors = identify_top_errors(log_entries)

# Example 4: Filter by Time Range
start_time = datetime(2023, 1, 5, 12, 30, 0)
end_time = datetime(2023, 1, 5, 13, 0, 0)
time_filtered_entries = filter_by_time_range(log_entries, start_time, end_time)

# Print or further process the results as needed
print("Filtered Entries:", filtered_entries)
print("Source Counts:", source_counts)
print("Top Errors:", top_errors)
print("Time Filtered Entries:", time_filtered_entries)
