

## 1. Problem Statement

The Student Timetable Conflict Detection System is designed to check and validate a student's proposed class timetable.

The system stores course schedules using strings and tuples. It compares course timings to detect overlapping periods and checks whether the assigned classrooms are available.

The system performs the following operations:

1. Accepts course names and classroom details.
2. Stores course schedules using tuples.
3. Detects overlapping class timings.
4. Identifies unavailable classrooms.
5. Validates the proposed timetable.
6. Displays whether the timetable is valid or contains conflicts.

Example: If Python is scheduled from 9:00 AM to 10:00 AM and Mathematics is scheduled from 9:30 AM to 10:30 AM, the system identifies a time conflict.

## 2. Algorithm

1. Start the program.
2. Define the list of unavailable rooms.
3. Enter the number of courses.
4. Enter course name, day, start time, end time, and room number.
5. Store the details using tuples.
6. Check whether the assigned room is unavailable.
7. Compare each course schedule with other courses.
8. Check whether the courses have overlapping timings on the same day.
9. Display all detected conflicts.
10. If no conflicts are found, display "Timetable is Valid".
11. Otherwise, display "Timetable is Invalid".
12. Stop the program.

## 3. Flowchart with Mermaid Code

```

flowchart TD
    A([START]) --> B[Define Unavailable Rooms]
    B --> C[/Enter Number of Courses/]
    C --> D[/Enter Course Name, Day, Start Time, End Time and Room/]
    D --> E[Store Course Details in Tuples]
    E --> F{Are More Courses Available?}
    F -- Yes --> D
    F -- No --> G[Check Room Availability]
    G --> H{Is Room Unavailable?}
    H -- Yes --> I[Display Room Conflict]
    H -- No --> J[Compare Course Schedules]
    I --> J
    J --> K{Same Day and Overlapping Time?}
    K -- Yes --> L[Display Time Conflict]
    K -- No --> M[Check Next Course Pair]
    L --> M
    M --> N{More Course Pairs?}
    N -- Yes --> J
    N -- No --> O{Any Conflicts Found?}
    O -- Yes --> P[Display Timetable INVALID]
    O -- No --> Q[Display Timetable VALID]
    P --> R([STOP])
    Q --> R


## 5. Source Input

Example input:

```
Enter number of courses: 3

Course 1
Enter course name: Python
Enter day: Monday
Enter start time (24-hour): 9
Enter end time (24-hour): 11
Enter room number: R1

Course 2
Enter course name: Mathematics
Enter day: Monday
Enter start time (24-hour): 10
Enter end time (24-hour): 12
Enter room number: R2

Course 3
Enter course name: English
Enter day: Tuesday
Enter start time (24-hour): 9
Enter end time (24-hour): 10
Enter room number: R3
```

## 6. Source Output

```
--- Timetable Validation ---

Conflict: English has unavailable room R3
Conflict: Python overlaps with Mathematics

Timetable is INVALID

--- Course Schedule ---
('Python', 'Monday', 9, 11, 'R1')
('Mathematics', 'Monday', 10, 12, 'R2')
('English', 'Tuesday', 9, 10, 'R3')

Timetable checking completed!
```

## 7. Explanation of Python Concepts Used

| Python concept | Purpose                            |
| -------------- | ---------------------------------- |
| List           | Stores course details              |
| Tuple          | Stores individual course schedules |
| String         | Stores course names and days       |
| For loop       | Repeats course entry and checking  |
| If condition   | Checks timetable conflicts         |
| Nested loop    | Compares two course schedules      |
| Append()       | Adds conflicts to the list         |

## 8. Conclusion

The Student Timetable Conflict Detection System checks course schedules, identifies overlapping class periods, detects unavailable classrooms, and validates the proposed timetable. It helps students and universities prepare conflict-free timetables using Python.
