# Write your MySQL query statement below
delete p from Person p inner join Person q on p.email=q.email and p.id>q.id