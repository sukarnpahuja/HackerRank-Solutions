/*
Enter your query here.
*/
select distinct city from station where 
(not(city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%')) 
or
(not (city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u'));
