-- Customer Revenue
SELECT 
    c.customer_id,
    c.name,
    SUM(t.amount) AS total_revenue
FROM customers c
LEFT JOIN transactions t
ON c.customer_id = t.customer_id
GROUP BY c.customer_id, c.name;

-- Engagement Score
SELECT
    customer_id,
    COUNT(*) AS total_events
FROM events
GROUP BY customer_id;
