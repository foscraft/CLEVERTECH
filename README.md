Problem Description:

You are tasked with creating a Python script that analyzes log files from a server and extracts meaningful information. The log files are in a custom format, and each entry in the log file represents an event on the server.

The log entries have the following format:

```css

[timestamp] [severity] [source] [message]
```

timestamp: The time when the event occurred, formatted as YYYY-MM-DD HH:MM:SS.

severity: The severity level of the event (INFO, WARNING, ERROR).

source: The source module or component where the event originated.

message: The detailed message describing the event.

Your task is to write a Python script that can perform the following tasks:

Parse Log File:
Read a log file (provided as input) and parse each log entry into a structured format.

Filter by Severity:
Allow the user to filter log entries based on severity (INFO, WARNING, ERROR).

Count Events:
Provide a count of events for each source.

Error Analysis:
Identify and display the top 5 error messages (entries with ERROR severity).

Time Range Analysis:
Allow the user to specify a time range and display events within that range.

Please make sure to handle edge cases gracefully and provide clear instructions on how to run your script. Additionally, include a sample log file for testing purposes.

Note to the Candidate:
You are encouraged to use any standard Python libraries to accomplish this task.
    Pay attention to code readability, maintainability, and efficiency.
    Provide comments and docstrings where necessary.
    The goal is to create a solution that is not only correct but also well-organized and easy to understand.

This problem covers aspects of file I/O, string parsing, data manipulation, and user interaction. It assesses the candidate's ability to design a solution for a real-world problem and implement it using Python.