


incidents = [
    ["I101", "Electrical fault", "Laboratory", 4, 3],
    ["I102", "Water leakage", "Classroom", 3, 4],
    ["I103", "Broken chair", "Library", 2, 1],
    ["I104", "Network failure", "Server Room", 5, 2],
    ["I105", "Fan not working", "Classroom", 2, 4]
]

critical_locations = ["Laboratory", "Server Room"]
results = []

for item in incidents:
    incident_id = item[0]
    issue = item[1]
    location = item[2]
    severity = item[3]
    frequency = item[4]

    # Assign priority using predefined rules
    if severity >= 5 or frequency >= 5:
        priority = "HIGH"
        rank = 1

    elif location in critical_locations and severity >= 3:
        priority = "HIGH"
        rank = 1

    elif severity >= 3 or frequency >= 3:
        priority = "MEDIUM"
        rank = 2

    else:
        priority = "LOW"
        rank = 3

    results.append([
        rank, incident_id, issue,
        location, severity, frequency, priority
    ])

# Sort by priority, severity and frequency
results.sort(key=lambda x: (x[0], -x[4], -x[5]))

# Display incident report
print("SMART CAMPUS MAINTENANCE REPORT")
print("-" * 45)

high = 0
medium = 0
low = 0

for item in results:
    print("Incident ID:", item[1])
    print("Issue:", item[2])
    print("Location:", item[3])
    print("Severity:", item[4])
    print("Frequency:", item[5])
    print("Priority:", item[6])
    print("-" * 45)

    if item[6] == "HIGH":
        high += 1
    elif item[6] == "MEDIUM":
        medium += 1
    else:
        low += 1

# Display priority summary
print("PRIORITY SUMMARY")
print("HIGH Priority Cases:", high)
print("MEDIUM Priority Cases:", medium)
print("LOW Priority Cases:", low)
print("Total Incidents:", len(results))

