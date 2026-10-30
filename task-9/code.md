# Environmental Monitoring Data Analyzer – Python Program

## 1. Problem Statement

Develop a Python program to analyse environmental monitoring data using nested lists. The program stores air-quality readings from different locations and calculates the average, minimum, and maximum pollution levels.

It classifies each location based on supplied threshold values as Good, Moderate, or Poor and displays the environmental monitoring report.

## 2. Algorithm

1. Start the program.
2. Create a nested list containing location names and air-quality readings.
3. Set threshold values for air quality.
4. Read the readings of each location.
5. Calculate the average air-quality reading.
6. Find the minimum and maximum readings.
7. Compare the average with the threshold values.
8. Classify the air quality as Good, Moderate, or Poor.
9. Display the results for each location.
10. Stop the program.

Classification rules used in this example:

- Average up to 50: Good
- Average above 50 and up to 100: Moderate
- Average above 100: Poor

These are simplified example thresholds for an academic program, not official environmental standards.

## 3. Flowchart with Mermaid Code
```

flowchart TD
    A([START]) --> B[Create Nested List of Environmental Readings]
    B --> C[Set Good and Moderate Threshold Values]
    C --> D[Enter Location and Air Quality Readings]
    D --> E[Calculate Average Reading]
    E --> F[Find Minimum Reading]
    F --> G[Find Maximum Reading]
    G --> H{Is Average <= 50?}
    H -- Yes --> I[Classify as GOOD]
    H -- No --> J{Is Average <= 100?}
    J -- Yes --> K[Classify as MODERATE]
    J -- No --> L[Classify as POOR]
    I --> M[Store Analysis Results]
    K --> M
    L --> M
    M --> N{Are More Locations Available?}
    N -- Yes --> D
    N -- No --> O[Display Environmental Monitoring Report]
    O --> P([STOP])


## 5. Source Input

The following nested list is given as input:

| Location   | Reading 1 | Reading 2 | Reading 3 |
| ---------- | --------- | --------- | --------- |
| Hyderabad  | 35        | 40        | 45        |
| Vijayawada | 60        | 75        | 90        |
| Guntur     | 110       | 130       | 150       |

## 6. Source Output

```
ENVIRONMENTAL MONITORING REPORT
---------------------------------------------
Location: Hyderabad
Readings: [35, 40, 45]
Average: 40.0
Minimum: 35
Maximum: 45
Quality: GOOD
---------------------------------------------
Location: Vijayawada
Readings: [60, 75, 90]
Average: 75.0
Minimum: 60
Maximum: 90
Quality: MODERATE
---------------------------------------------
Location: Guntur
Readings: [110, 130, 150]
Average: 130.0
Minimum: 110
Maximum: 150
Quality: POOR
---------------------------------------------
Environmental analysis completed.
```

## 7. Conclusion

This Python program uses nested lists, loops, conditional statements, and built-in functions such as `sum()`, `min()`, and `max()` to analyse environmental readings. It calculates averages, identifies extreme values, and classifies environmental quality based on threshold values.
