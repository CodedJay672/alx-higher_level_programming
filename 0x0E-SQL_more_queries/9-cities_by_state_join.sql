-- script that displays cities by their states
-- We have to join tables cities and states to solve this problem
SELECT c.id, c.name, s.name
FROM cities c JOIN states s
        ON c.id = s.id
ORDER BY c.id ASC;
