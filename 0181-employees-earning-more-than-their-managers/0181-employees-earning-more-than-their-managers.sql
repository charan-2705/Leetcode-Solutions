# Write your MySQL query statement below
select a.name as Employee from Employee a where salary>(select salary from employee b where a.managerId=b.id)