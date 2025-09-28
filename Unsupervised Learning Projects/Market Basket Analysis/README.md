# Market Basket Analysis

## Objective
The goal of this project is to uncover **frequent itemsets** and **associations** in transactional data to understand customer purchasing behavior. These insights can be used for **cross-selling, inventory planning, and recommendation systems**.

## Algorithm Used
- **Apriori Algorithm**: Identifies frequent itemsets based on minimum support.
- **Association Rules Mining**: Generates rules from frequent itemsets and calculates **support, confidence, and lift** to evaluate the strength of associations.

## Dataset
- Transactional data of items purchased by customers.
- Data pre-processing involved one-hot encoding of items for analysis.

## Key Findings
- **Strong Associations**
  - **Milk → Eggs**: Confidence = 1.0, Lift = 2.0  
    Every transaction containing milk also includes eggs.
  - **Eggs → Milk**: Confidence ≈ 0.67  
    Indicates a strong but slightly weaker reverse association.

- **Frequent Itemsets**
  - Milk and eggs appear together in **50% of transactions**, highlighting a common purchasing pattern.

## Business Insights
- **Cross-Promotions**: Bundle frequently bought items like milk and eggs.  
- **Inventory Optimization**: Anticipate demand for items that are often bought together.  
- **Recommendation Systems**: Suggest related products to customers based on association rules.

## Hyperparameter Guidelines
- **Support**: 0.1–0.5 (frequent items)  
- **Confidence**: 0.6–1.0 (strong rules)  
- **Lift**: >1 indicates positive correlation, 1.5–3 considered strong

## Conclusion
The Market Basket Analysis provides actionable insights into **customer buying patterns**, enabling businesses to improve **sales strategies, inventory management, and personalized recommendations**.
