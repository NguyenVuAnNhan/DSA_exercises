# Write your MySQL query statement below
select name
from Customer
where ISNULL(referee_id) or referee_id != 2