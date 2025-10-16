with open("System.log", 'w') as f:
    file = [
        "INFO: System started at 10:00 AM\n"
        "WARNING: Low disk space\n"
        "ERROR: Failed to connect to server\n"
        "INFO: Backup completed successfully\n"
    ]
    f.writelines(file)

# Read first 30 characters
with open("System.log", 'r') as f:
    file = f.read(30)
    print("First 30 character of log:")
    print(file)

# Current pointer position
    position = f.tell()
    print("\nCurrent position in file (in bytes):", position)

# Move pointer back to start to re-read
    f.seek(0)
    print("\nRe-reading first line:")
    print(f.readline()) # Reads the first full line


with open("System.log", 'a') as f:
    f.seek(0, 2) # Move pointer to end
    file_size = f.tell()
    print("\nCurrent file size:", file_size, "bytes")

# Truncate if file is too big
    if file_size > 100:
        f.truncate(100)
        print("File truncate to 100 bytes.")

with open("System.log", 'r') as f:
    print("\nFinal log file content:")
    print(f.read())