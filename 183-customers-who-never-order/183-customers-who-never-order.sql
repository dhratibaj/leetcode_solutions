select name as customers from Customers c
where Not exists (select customerId from Orders o where o.customerId = c.id)