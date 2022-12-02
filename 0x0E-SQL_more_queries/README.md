# More SQL Queries
How to create a new MySQL user  
How to manage privileges for a user to a database or table  
What’s a PRIMARY KEY  
What’s a FOREIGN KEY  
How to use NOT NULL and UNIQUE constraints  
How to retrieve datas from multiple tables in one request  
What are subqueries  
What are JOIN and UNION  

## How to Import a SQL dump
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:  
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows  
Enter password:  
