# Multi-Branch Sales Matrix Comparison Using Python

## 1. Problem Statement

The Multi-Branch Sales Matrix Comparison System is designed to analyze product sales across multiple branches and days using Python nested lists.

The system stores daily product sales for different branches and performs calculations to compare sales performance.

The system performs the following operations:

1. Stores product sales across multiple branches and days using nested lists.
2. Calculates the total sales of each product.
3. Calculates the total sales of each branch.
4. Compares sales between different branches.
5. Identifies the best-performing product in each branch.
6. Displays the final sales analysis report.

Example: A company has three branches selling three products over three days. The system calculates totals and identifies the highest-selling product in each branch.

## 2. Algorithm

1. Start the program.
2. Initialize the number of branches, products, and days.
3. Create a nested list to store sales data.
4. Enter the daily sales of each product for every branch.
5. Calculate the total sales of each product in each branch.
6. Calculate the total sales of every branch.
7. Compare the total sales of all branches.
8. Identify the best-performing product in each branch.
9. Display product-wise sales totals.
10. Display branch-wise sales totals.
11. Display the highest-selling branch.
12. Display the best-performing product in each branch.
13. Stop the program.

## 3. Flowchart with Mermaid Code
```

flowchart TD
    A([START]) --> B[Initialize Branches, Products and Days]
    B --> C[Create Nested Sales List]
    C --> D[/Enter Daily Sales of Each Product/]
    D --> E[Store Sales in Nested Lists]
    E --> F[Calculate Product-wise Total Sales]
    F --> G[Calculate Branch-wise Total Sales]
    G --> H[Compare Total Sales of All Branches]
    H --> I[Identify Highest Performing Branch]
    I --> J[Find Best Performing Product in Each Branch]
    J --> K[/Display Product-wise Sales Totals/]
    K --> L[/Display Branch-wise Sales Totals/]
    L --> M[/Display Best Performing Product/]
    M --> N[/Display Highest Performing Branch/]
    N --> O([STOP])


## 5. Source Input

Sample Input:

```
Enter sales for Branch A
Laptop Day 1: 100
Laptop Day 2: 150
Laptop Day 3: 200
Mobile Day 1: 200
Mobile Day 2: 250
Mobile Day 3: 300
Tablet Day 1: 100
Tablet Day 2: 120
Tablet Day 3: 150

Enter sales for Branch B
Laptop Day 1: 200
Laptop Day 2: 250
Laptop Day 3: 300
Mobile Day 1: 300
Mobile Day 2: 350
Mobile Day 3: 400
Tablet Day 1: 150
Tablet Day 2: 180
Tablet Day 3: 200

Enter sales for Branch C
Laptop Day 1: 150
Laptop Day 2: 180
Laptop Day 3: 200
Mobile Day 1: 250
Mobile Day 2: 300
Mobile Day 3: 350
Tablet Day 1: 200
Tablet Day 2: 220
Tablet Day 3: 250
```

## 6. Source Output

```
--- Branch A ---
Laptop Total: 450
Mobile Total: 750
Tablet Total: 370
Branch Total: 1570
Best Product: Mobile

--- Branch B ---
Laptop Total: 750
Mobile Total: 1050
Tablet Total: 530
Branch Total: 2330
Best Product: Mobile

--- Branch C ---
Laptop Total: 530
Mobile Total: 900
Tablet Total: 670
Branch Total: 2100
Best Product: Mobile

--- Branch Comparison ---
Branch A Sales: 1570
Branch B Sales: 2330
Branch C Sales: 2100

Highest Performing Branch: Branch B
Highest Sales: 2330

Sales Analysis Completed!
```

## 7. Python Concepts Used

| Python concept | Purpose                         |
| -------------- | ------------------------------- |
| Nested lists   | Store branch and product sales  |
| For loop       | Repeat sales calculations       |
| Nested loop    | Process products and days       |
| Sum()          | Calculate total sales           |
| If condition   | Find best-performing product    |
| Max()          | Find highest branch sales       |
| Index()        | Identify highest-selling branch |

## 8. Conclusion

The Multi-Branch Sales Matrix Comparison System successfully stores and analyzes product sales using Python nested lists. It calculates product-wise and branch-wise totals, compares branch performance, and identifies the best-performing product in each branch.
