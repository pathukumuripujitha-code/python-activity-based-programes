# Repeated Transaction Detection System Using Python

## 1. Problem Statement

The Repeated Transaction Detection System is designed to identify suspicious financial transactions using Python.

The system accepts transaction IDs and transaction amounts in a list. It checks for duplicate transaction IDs and identifies transactions that exceed a predefined amount threshold.

The system performs the following operations:

1. Accepts transaction IDs and amounts.
2. Stores transaction details in a list.
3. Detects duplicate transaction IDs.
4. Identifies transactions exceeding the specified threshold.
5. Generates a list of suspicious transactions.
6. Displays the final transaction report.

Example: If transaction ID `T101` appears twice, it is considered a duplicate. If a transaction amount exceeds ₹50,000, it is considered a threshold violation.

## 2. Algorithm

1. Start the program.
2. Create an empty transaction list.
3. Enter the number of transactions.
4. Enter transaction ID and amount.
5. Store transaction details in the list.
6. Set the transaction amount threshold.
7. Check each transaction ID for duplicates.
8. Check whether the transaction amount exceeds the threshold.
9. Add suspicious transactions to a separate list.
10. Display duplicate transactions.
11. Display threshold violations.
12. Display the suspicious transaction list.
13. Stop the program.

## 3. Flowchart with Mermaid Code
```

flowchart TD
    A([START]) --> B[Create Transaction List]
    B --> C[/Enter Number of Transactions/]
    C --> D[/Enter Transaction ID and Amount/]
    D --> E[Store Transaction Details]
    E --> F{More Transactions?}
    F -- Yes --> D
    F -- No --> G[Set Amount Threshold]
    G --> H[Check Duplicate Transaction IDs]
    H --> I{Duplicate ID Found?}
    I -- Yes --> J[Mark as Duplicate]
    I -- No --> K[Check Transaction Amount]
    J --> K
    K --> L{Amount Greater Than Threshold?}
    L -- Yes --> M[Mark Threshold Violation]
    L -- No --> N[Check Next Transaction]
    M --> O[Add to Suspicious List]
    O --> N
    N --> P{More Transactions?}
    P -- Yes --> H
    P -- No --> Q[Display Duplicate Transactions]
    Q --> R[Display Threshold Violations]
    R --> S[Display Suspicious Transactions]
    S --> T([STOP])



## 5. Source Input

Sample Input:

```
Enter number of transactions: 5
Enter amount threshold: 50000

Transaction 1
Enter transaction ID: T101
Enter transaction amount: 20000

Transaction 2
Enter transaction ID: T102
Enter transaction amount: 60000

Transaction 3
Enter transaction ID: T103
Enter transaction amount: 15000

Transaction 4
Enter transaction ID: T101
Enter transaction amount: 25000

Transaction 5
Enter transaction ID: T104
Enter transaction amount: 80000
```

## 6. Source Output

```
--- Duplicate Transactions ---
T101

--- Threshold Violations ---
('T102', 60000.0)
('T104', 80000.0)

--- Suspicious Transactions ---
('T101', 20000.0, ['Duplicate ID'])
('T102', 60000.0, ['Threshold Violation'])
('T101', 25000.0, ['Duplicate ID'])
('T104', 80000.0, ['Threshold Violation'])

Transaction checking completed!
```

## 7. Python Concepts Used

| Concept      | Purpose                      |
| ------------ | ---------------------------- |
| List         | Stores transactions          |
| Tuple        | Stores ID and amount         |
| Set          | Identifies duplicate IDs     |
| For loop     | Processes transactions       |
| If condition | Checks suspicious entries    |
| Append()     | Adds suspicious transactions |
| Float        | Stores transaction amounts   |

## 8. Conclusion

The Repeated Transaction Detection System identifies duplicate transaction IDs, detects transactions exceeding the predefined amount threshold, and generates a suspicious transaction report using Python.
