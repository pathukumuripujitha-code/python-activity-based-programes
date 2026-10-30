# Food Supply Chain Stock Reconciliation – Python Program

## 1. Problem Statement

Develop a Python program to manage and analyse food stock across multiple locations using nested lists. The program compares the quantities of food items received, distributed, damaged, and remaining at each location.

It identifies stock discrepancies, calculates the actual remaining quantity, and determines how much stock needs to be replenished.

## 2. Algorithm

1. Start the program.
2. Create a nested list containing location names and food stock details.
3. Enter the received, distributed, damaged, and recorded remaining quantities.
4. Calculate the expected remaining stock.

&#x20;  Expected Stock = Received − Distributed − Damaged

5. Compare expected stock with recorded remaining stock.
6. Identify discrepancies between the two quantities.
7. Calculate replenishment requirements using the minimum stock level.
8. Display the stock details and discrepancies for each location.
9. Stop the program.

## 3. Flowchart with Mermaid Code
```

flowchart TD
    A([START]) --> B[Create Nested List of Food Stock]
    B --> C[Enter Location and Food Item Details]
    C --> D[Enter Received Quantity]
    D --> E[Enter Distributed Quantity]
    E --> F[Enter Damaged Quantity]
    F --> G[Enter Recorded Remaining Stock]
    G --> H[Calculate Expected Remaining Stock]
    H --> I[Compare Expected and Recorded Stock]
    I --> J{Is There Any Discrepancy?}
    J -- Yes --> K[Identify Stock Shortage or Extra Stock]
    J -- No --> L[No Discrepancy]
    K --> M[Check Minimum Stock Level]
    L --> M
    M --> N[Calculate Replenishment Quantity]
    N --> O[Store Stock Details]
    O --> P{More Locations?}
    P -- Yes --> C
    P -- No --> Q[Display Stock Reconciliation Report]
    Q --> R[Display Discrepancies and Replenishment]
    R --> S([STOP])

## 5. Source Input

The following nested list is used as input:

| Location | Food item | Received | Distributed | Damaged | Recorded remaining | Minimum stock |
| -------- | --------- | -------- | ----------- | ------- | ------------------ | ------------- |
| Central  | Rice      | 500      | 300         | 20      | 170                | 200           |
| North    | Wheat     | 300      | 180         | 10      | 115                | 100           |
| South    | Oil       | 200      | 120         | 5       | 70                 | 90            |

## 6. Source Output

```
FOOD STOCK RECONCILIATION REPORT
--------------------------------------------------
Location: Central
Food Item: Rice
Received: 500
Distributed: 300
Damaged: 20
Expected Stock: 180
Recorded Stock: 170
Discrepancy: 10
Status: Stock Shortage
Replenishment: 20
--------------------------------------------------
Location: North
Food Item: Wheat
Received: 300
Distributed: 180
Damaged: 10
Expected Stock: 110
Recorded Stock: 115
Discrepancy: 5
Status: Extra Stock
Replenishment: 0
--------------------------------------------------
Location: South
Food Item: Oil
Received: 200
Distributed: 120
Damaged: 5
Expected Stock: 75
Recorded Stock: 70
Discrepancy: 5
Status: Stock Shortage
Replenishment: 15
--------------------------------------------------
Stock analysis completed.
```

## 7. Conclusion

This Python program uses nested lists, loops, conditional statements, and mathematical operations to manage food stock across multiple locations. It identifies stock discrepancies and calculates replenishment requirements to maintain sufficient food supplies.

Important formulas:

- Expected stock = Received − Distributed − Damaged
- Discrepancy = Absolute difference between expected and recorded stock
- Replenishment = Minimum stock − Expected stock (if positive).
