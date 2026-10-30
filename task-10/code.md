# Smart Campus Incident and Maintenance Prioritization – Python Program

## 1. Problem Statement

Develop a Python program to manage and prioritize campus maintenance reports using nested lists. The program analyses incidents based on severity, location, and reported frequency.

It classifies incidents into HIGH, MEDIUM, and LOW priority using predefined rules. It ranks the incidents and generates a priority summary to help campus management identify which maintenance issues need immediate attention.

## 2. Algorithm

1. Start the program.
2. Create a nested list containing incident ID, issue, location, severity, and reported frequency.
3. Read the details of each maintenance report.
4. Check the severity of each incident.
5. Check whether the incident is reported frequently.
6. Apply predefined priority rules.
7. Assign HIGH, MEDIUM, or LOW priority.
8. Store the incident details and priority.
9. Sort incidents according to priority and frequency.
10. Count the HIGH, MEDIUM, and LOW priority incidents.
11. Display the ranked maintenance report and priority summary.
12. Stop the program.

Priority rules used in this example:

- HIGH: Severity is 5 or above, or frequency is 5 or above.
- MEDIUM: Severity is 3 or above, or frequency is 3 or above.
- LOW: All other cases.

Location is also considered: incidents in critical locations such as laboratories and server rooms receive higher priority when severity is 3 or above.

## 3. Flowchart with Mermaid Code
```

flowchart TD
    A([START]) --> B[Create Nested List of Incident Reports]
    B --> C[Enter Incident ID, Issue and Location]
    C --> D[Enter Severity and Reported Frequency]
    D --> E[Check Severity and Frequency]
    E --> F{Severity >= 5 OR Frequency >= 5?}
    F -- Yes --> G[Assign HIGH Priority]
    F -- No --> H{Is Location Critical and Severity >= 3?}
    H -- Yes --> G
    H -- No --> I{Severity >= 3 OR Frequency >= 3?}
    I -- Yes --> J[Assign MEDIUM Priority]
    I -- No --> K[Assign LOW Priority]
    G --> L[Store Incident Details]
    J --> L
    K --> L
    L --> M{Are More Reports Available?}
    M -- Yes --> C
    M -- No --> N[Sort Incidents by Priority]
    N --> O[Count HIGH, MEDIUM and LOW Cases]
    O --> P[Generate Priority Summary]
    P --> Q[Display Maintenance Report]
    Q --> R([STOP])


## 5. Source Input

The following nested list is used as input:

| ID   | Maintenance issue | Location    | Severity | Frequency |
| ---- | ----------------- | ----------- | -------- | --------- |
| I101 | Electrical fault  | Laboratory  | 4        | 3         |
| I102 | Water leakage     | Classroom   | 3        | 4         |
| I103 | Broken chair      | Library     | 2        | 1         |
| I104 | Network failure   | Server Room | 5        | 2         |
| I105 | Fan not working   | Classroom   | 2        | 4         |

## 6. Source Output

```
SMART CAMPUS MAINTENANCE REPORT
---------------------------------------------
Incident ID: I104
Issue: Network failure
Location: Server Room
Severity: 5
Frequency: 2
Priority: HIGH
---------------------------------------------
Incident ID: I101
Issue: Electrical fault
Location: Laboratory
Severity: 4
Frequency: 3
Priority: HIGH
---------------------------------------------
Incident ID: I102
Issue: Water leakage
Location: Classroom
Severity: 3
Frequency: 4
Priority: MEDIUM
---------------------------------------------
Incident ID: I105
Issue: Fan not working
Location: Classroom
Severity: 2
Frequency: 4
Priority: MEDIUM
---------------------------------------------
Incident ID: I103
Issue: Broken chair
Location: Library
Severity: 2
Frequency: 1
Priority: LOW
---------------------------------------------
PRIORITY SUMMARY
HIGH Priority Cases: 2
MEDIUM Priority Cases: 2
LOW Priority Cases: 1
Total Incidents: 5
```

## 7. Conclusion

This Python program uses nested lists, loops, conditional statements, and sorting to analyse campus maintenance reports. It classifies incidents based on severity, location, and frequency and generates a priority summary to help campus management plan maintenance activities.
