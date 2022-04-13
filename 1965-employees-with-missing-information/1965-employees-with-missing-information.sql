select employee_id from(
select employee_id, name, null as salary from Employees
union all
select employee_id, null as name, salary from Salaries)
group by employee_id
having count(*) <= 1
order by employee_id