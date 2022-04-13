select employee_id from employees
union
select employee_id from salaries
except
select employee_id from employees
intersect 
select employee_id from salaries