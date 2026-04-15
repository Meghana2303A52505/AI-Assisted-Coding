-- SQL Query: Find all customers from USA with orders over $100
SELECT 
    c.customer_id,
    c.customer_name,
    c.email,
    COUNT(o.order_id) as total_orders,
    SUM(o.order_amount) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE c.country = 'USA' 
    AND o.order_amount > 100
GROUP BY c.customer_id, c.customer_name, c.email
HAVING COUNT(o.order_id) > 0
ORDER BY total_spent DESC;

// MongoDB Query equivalent
db.customers.aggregate([
    {
        $match: { country: "USA" }
    },
    {
        $lookup: {
            from: "orders",
            localField: "_id",
            foreignField: "customer_id",
            as: "orders"
        }
    },
    {
        $addFields: {
            orders: {
                $filter: {
                    input: "$orders",
                    as: "order",
                    cond: { $gt: ["$$order.order_amount", 100] }
                }
            }
        }
    },
    {
        $match: { "orders.0": { $exists: true } }
    },
    {
        $project: {
            customer_id: "$_id",
            customer_name: 1,
            email: 1,
            total_orders: { $size: "$orders" },
            total_spent: { $sum: "$orders.order_amount" }
        }
    },
    {
        $sort: { total_spent: -1 }
    }
])
