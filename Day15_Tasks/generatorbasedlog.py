"""Generator-based Log Reader 
Scenario: 
A large log file needs to be processed. 
Task: 
● Create a generator to read file line by line 
● Use loop to process logs 
● Use condition to filter errors 
● Count occurrences using a dictionary """

def read_logs(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line.strip()

log_count = {}

with open("logs.txt", "w") as f:
    f.write("INFO Login success\n")
    f.write("ERROR File not found\n")
    f.write("INFO Data loaded\n")
    f.write("ERROR Connection failed\n")
    f.write("INFO Logout success\n")

for log in read_logs("logs.txt"):

    log_type = log.split()[0]
    log_count[log_type] = log_count.get(log_type, 0) + 1

    if log_type == "ERROR":
        print("Error found:", log)

print("\nLog Summary:")
for key, value in log_count.items():
    print(key, ":", value)

