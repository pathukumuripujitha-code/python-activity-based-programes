# Progressive Electricity Billing System Using Python

## 1. Problem Statement

The Progressive Electricity Billing System is designed to calculate household electricity bills based on monthly electricity consumption.

The system uses multiple consumption slabs, fixed charges, surcharges, and rebates to calculate the final electricity bill. It also compares electricity bills across several months and identifies unusual increases in billing amounts.

The system performs the following operations:

1. Accepts monthly electricity consumption in units.
2. Calculates charges using different electricity slabs.
3. Adds fixed charges to the bill.
4. Calculates additional surcharges.
5. Applies rebates when eligible.
6. Compares bills across multiple months.
7. Identifies unusual increases in electricity bills.
8. Displays the final monthly billing report.

Billing rules used in this program:

| Electricity units | Rate per unit |
| ----------------- | ------------- |
| 0–100             | ₹2            |
| 101–200           | ₹3            |
| 201–300           | ₹5            |
| Above 300         | ₹7            |

- Fixed charge: ₹50
- Surcharge: 5% of energy charges if consumption exceeds 300 units.
- Rebate: 10% of energy charges if consumption is below 100 units.
- Unusual increase: Bill increases by more than 30% compared with the previous month.

## 2. Algorithm

1. Start the program.
2. Initialize the number of months.
3. Create an empty list to store monthly bills.
4. Enter the month name and electricity consumption.
5. Calculate the first 100 units at ₹2 per unit.
6. Calculate the next 100 units at ₹3 per unit.
7. Calculate the next 100 units at ₹5 per unit.
8. Calculate remaining units at ₹7 per unit.
9. Add fixed charges of ₹50.
10. Apply a 5% surcharge if consumption exceeds 300 units.
11. Apply a 10% rebate if consumption is below 100 units.
12. Calculate the final electricity bill.
13. Store the monthly bill in a list.
14. Compare each month's bill with the previous month's bill.
15. If the increase is more than 30%, identify it as unusual.
16. Display monthly bills and unusual increases.
17. Stop the program.

## 3. Flowchart with Mermaid Code
```

flowchart TD
    A([START]) --> B[Initialize Electricity Billing Slabs]
    B --> C[/Enter Number of Months/]
    C --> D[/Enter Month Name and Units Consumed/]
    D --> E[Calculate Slab-wise Energy Charges]
    E --> F[Add Fixed Charges ₹50]
    F --> G{Units Greater Than 300?}
    G -- Yes --> H[Add 5% Surcharge]
    G -- No --> I{Units Below 100?}
    H --> I
    I -- Yes --> J[Apply 10% Rebate]
    I -- No --> K[Calculate Final Electricity Bill]
    J --> K
    K --> L[Store Monthly Bill]
    L --> M{More Months?}
    M -- Yes --> D
    M -- No --> N[Compare Monthly Bills]
    N --> O{Bill Increase Greater Than 30%?}
    O -- Yes --> P[Identify Unusual Increase]
    O -- No --> Q[Display Normal Change]
    P --> R[Display Monthly Billing Report]
    Q --> R
    R --> S([STOP])

## 5. Source Input

Sample Input:

```
Enter number of months: 3

Month 1
Enter month name: January
Enter electricity units: 80

Month 2
Enter month name: February
Enter electricity units: 150

Month 3
Enter month name: March
Enter electricity units: 350
```

## 6. Source Output

```
Month 1
Energy Charges: 160.0
Fixed Charges: 50
Surcharge: 0
Rebate: 16.0
Final Bill: 194.0

Month 2
Energy Charges: 350.0
Fixed Charges: 50
Surcharge: 0
Rebate: 0
Final Bill: 400.0

Month 3
Energy Charges: 1050.0
Fixed Charges: 50
Surcharge: 52.5
Rebate: 0
Final Bill: 1152.5

--- Monthly Bill Comparison ---

January Bill: 194.0

February Bill: 400.0
Unusual Increase: 106.19 %

March Bill: 1152.5
Unusual Increase: 188.12 %

Electricity Billing Completed!
```

## 7. Python Concepts Used

| Python concept         | Purpose                        |
| ---------------------- | ------------------------------ |
| List                   | Stores monthly bills           |
| For loop               | Processes multiple months      |
| If-elif-else           | Calculates electricity slabs   |
| Float                  | Stores units and bill amounts  |
| Append()               | Adds monthly bill details      |
| Arithmetic operators   | Calculates charges and rebates |
| Conditional statements | Identifies unusual increases   |

## 8. Conclusion

The Progressive Electricity Billing System calculates household electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates. It compares monthly bills and identifies unusual increases using Python.
