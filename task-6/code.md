# Retail Billing with Multiple Discount Rules Using Python

## 1. Problem Statement

The Retail Billing System is designed to calculate the final bill for customers purchasing multiple products from a retail store.

The system accepts product names, quantities, prices, and product categories. It calculates category-specific taxes, applies discounts based on purchase amounts, and ensures that the total discount does not exceed the maximum concession limit.

The system performs the following operations:

1. Accepts multiple product details.
2. Calculates the total price based on quantity.
3. Applies category-specific taxes.
4. Provides discounts based on purchase amount.
5. Applies maximum concession limits.
6. Generates an itemized invoice.
7. Displays the final payable amount.

Billing rules used:

| Category    | Tax rate |
| ----------- | -------- |
| Electronics | 18%      |
| Clothing    | 5%       |
| Food        | 0%       |

Discount rules:

- Purchase above ₹5,000: 10% discount.
- Purchase above ₹10,000: 15% discount.
- Maximum discount limit: ₹2,000.

## 2. Algorithm

1. Start the program.
2. Create an empty product list.
3. Set tax rates for different categories.
4. Set discount rules and maximum concession limit.
5. Enter the number of products.
6. Enter product name, category, price, and quantity.
7. Calculate the total price of each product.
8. Calculate category-specific tax.
9. Calculate the subtotal of all products.
10. Check the subtotal for discount eligibility.
11. Apply the appropriate discount.
12. Check the maximum concession limit.
13. Calculate the final bill.
14. Generate an itemized invoice.
15. Display the final payable amount.
16. Stop the program.

## 3. Flowchart with Mermaid Code
```

flowchart TD
    A([START]) --> B[Set Category-wise Tax Rates]
    B --> C[Set Discount Rules and Maximum Limit]
    C --> D[/Enter Number of Products/]
    D --> E[/Enter Product Name, Category, Price and Quantity/]
    E --> F[Calculate Product Amount]
    F --> G[Calculate Category-specific Tax]
    G --> H[Store Product Details]
    H --> I{More Products?}
    I -- Yes --> E
    I -- No --> J[Calculate Total Subtotal]
    J --> K{Subtotal Greater Than 10000?}
    K -- Yes --> L[Apply 15% Discount]
    K -- No --> M{Subtotal Greater Than 5000?}
    M -- Yes --> N[Apply 10% Discount]
    M -- No --> O[No Discount]
    L --> P[Apply Maximum Discount Limit ₹2000]
    N --> P
    O --> P
    P --> Q[Calculate Final Bill]
    Q --> R[Generate Itemized Invoice]
    R --> S[/Display Product Details, Tax and Discount/]
    S --> T[/Display Final Payable Amount/]
    T --> U([STOP])


## 5. Source Input

Sample Input:

```
Enter number of products: 3

Product 1
Enter product name: Laptop
Enter category: electronics
Enter product price: 40000
Enter quantity: 1

Product 2
Enter product name: Shirt
Enter category: clothing
Enter product price: 2000
Enter quantity: 2

Product 3
Enter product name: Rice
Enter category: food
Enter product price: 1000
Enter quantity: 1
```

## 6. Source Output

```
========== RETAIL INVOICE ==========

Product: Laptop
Category: electronics
Price: 40000.0
Quantity: 1
Amount: 40000.0
Tax: 7200.0

Product: Shirt
Category: clothing
Price: 2000.0
Quantity: 2
Amount: 4000.0
Tax: 200.0

Product: Rice
Category: food
Price: 1000.0
Quantity: 1
Amount: 1000.0
Tax: 0.0

Subtotal: 45000.0
Total Tax: 7400.0
Discount: 2000
Final Amount: 50400.0

Thank you for shopping!
```

## 7. Python Concepts Used

| Concept              | Purpose                                   |
| -------------------- | ----------------------------------------- |
| List                 | Stores product details                    |
| Tuple                | Stores individual product information     |
| Dictionary           | Stores category tax rates                 |
| For loop             | Processes multiple products               |
| If-elif-else         | Applies discount rules                    |
| Functions            | `min()` calculates maximum discount limit |
| Arithmetic operators | Calculates price, tax and discount        |

## 8. Conclusion

The Retail Billing System calculates product prices, quantities, category-specific taxes, and discounts. It applies maximum concession limits and generates an itemized invoice with the final payable amount using Python.
