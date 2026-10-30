# Hospital Resource Allocation and Capacity Monitoring – Python Program

## 1. Problem Statement

Develop a Python program to monitor hospital resources across different wards using nested lists. The program analyses bed occupancy, available staff, and medical equipment. It identifies resource shortages and assigns priorities to wards based on critical patients and resource availability.

The main objective is to help hospital management understand resource requirements and identify wards that need immediate attention.

## 2. Algorithm

1. Start the program.
2. Create a nested list containing hospital ward details.
3. Store total beds and occupied beds.
4. Store available staff and required staff.
5. Store available equipment and required equipment.
6. Calculate the number of available beds.
7. Identify shortages in staff and equipment.
8. Count the resource shortages in each ward.
9. Assign HIGH, MEDIUM, or LOW priority using the given rules.
10. Sort wards according to priority and critical patients.
11. Display the complete resource report.
12. Stop the program.

## 3. Flowchart with Mermaid Code
```

flowchart TD
    A([START]) --> B[Create Nested List of Hospital Wards]
    B --> C[Enter Bed, Staff and Equipment Details]
    C --> D[Calculate Available Beds]
    D --> E[Calculate Staff Shortage]
    E --> F[Calculate Equipment Shortage]
    F --> G[Count Total Resource Shortages]
    G --> H{Critical Patients >= 5 OR Shortages >= 2?}
    H -- Yes --> I[Assign HIGH Priority]
    H -- No --> J{Any Shortage OR Critical Patients > 0?}
    J -- Yes --> K[Assign MEDIUM Priority]
    J -- No --> L[Assign LOW Priority]
    I --> M[Store Ward Information]
    K --> M
    L --> M
    M --> N{Are More Wards Available?}
    N -- Yes --> C
    N -- No --> O[Sort Wards by Priority and Critical Patients]
    O --> P[Display Hospital Resource Report]
    P --> Q([STOP])


## 5. Source Input

The following data is given to the program:

| Ward      | Total beds | Occupied beds | Available staff | Required staff | Available equipment | Required equipment | Critical patients |
| --------- | ---------- | ------------- | --------------- | -------------- | ------------------- | ------------------ | ----------------- |
| General   | 50         | 45            | 8               | 10             | 12                  | 15                 | 3                 |
| ICU       | 20         | 20            | 5               | 8              | 6                   | 10                 | 7                 |
| Emergency | 30         | 20            | 10              | 10             | 15                  | 12                 | 2                 |

## 6. Source Output

```
HOSPITAL RESOURCE REPORT
--------------------------------------------------
Ward: ICU
Available Beds: 0
Staff Shortage: 3
Equipment Shortage: 4
Critical Patients: 7
Priority: HIGH
--------------------------------------------------
Ward: General
Available Beds: 5
Staff Shortage: 2
Equipment Shortage: 3
Critical Patients: 3
Priority: HIGH
--------------------------------------------------
Ward: Emergency
Available Beds: 10
Staff Shortage: 0
Equipment Shortage: 0
Critical Patients: 2
Priority: MEDIUM
--------------------------------------------------
Resource analysis completed.
```

## 7. Conclusion

The Python program uses nested lists, loops, conditional statements, and sorting to analyse hospital resources. It identifies resource shortages and assigns priorities to different wards. This helps hospital management understand resource availability and plan resource allocation.

Note: This is an educational example. Actual patient-care priorities must be determined by qualified medical professionals.
