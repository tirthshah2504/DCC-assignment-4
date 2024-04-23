# DCC-assignment-4

This repository is created as a part of the course ES 113 - Data Centric Computing at Indian Institute of Technology, Gandhinagar, under Professor Mayank Singh. 
This repository contains data for the website made for analysing data about electoral bonds purchase and redemption details.

## Setup Details
1. Download the repository as a ZIP file.
2. Using MySQL Workbench, import the data from the dump_data sql dump file.
3. Execute this code on the Workbench. You can change the username testing and password password.
mysql
CREATE USER 'testing'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'testing'@'localhost' WITH GRANT OPTION;

4. Open the file app.py. If you have modified the password or username, change the username and password to the one set by you in the lines:
python
app.config['MYSQL_USER'] = 'testing'
app.config['MYSQL_PASSWORD'] = 'password'


5. Run the python file.
6. Open the browser and search 127.0.0.1. The Website will be loaded.

7. Screenshots of the UI
   ##
   1)Homepage of the website
   <img width="1470" alt="Screenshot 2024-04-23 at 9 24 41 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/a36463ef-3b1c-48c6-810a-c8f53aad1ebd">

   2)Answer of Question 1 for bond number 11448.
   <img width="1470" alt="Screenshot 2024-04-23 at 9 25 41 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/850d2bfe-4259-48f1-b779-d07580393c8e">

   3)Answer of Question 2 for company A B C INDIA LIMITED
   <img width="1470" alt="Screenshot 2024-04-23 at 9 28 03 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/96bad1ba-5780-4e4a-b5cf-fda9c5accbe0">
         3a) Dropdown UI
         <img width="1470" alt="Screenshot 2024-04-23 at 9 30 00 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/d8b02061-d99e-4d71-844f-b87f75da5529">

   4)Answer of Question 3 for the party SIKKIM DEMOCRATIC FRONT
   <img width="1470" alt="Screenshot 2024-04-23 at 9 32 14 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/108da188-e725-466f-8266-848825d98839">
         4a) Dropdown UI
         <img width="1470" alt="Screenshot 2024-04-23 at 9 32 58 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/233fb39c-46a3-48e0-b90b-762c771399ca">

   5)Answer of Question 4 for the party JAMMU AND KASHMIR POLITICAL CONFERENCE
   <img width="1470" alt="Screenshot 2024-04-23 at 9 34 56 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/999df176-226a-4b0a-bd0f-c404d90b75bd">
        5a)Dropdown UI
        <img width="1470" alt="Screenshot 2024-04-23 at 9 37 52 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/e5858c14-918e-4e51-89a3-853c86a8b6a3">

   6)Answer of Question 5 for the company A B C INDIA LIMITED
   <img width="1470" alt="Screenshot 2024-04-23 at 9 36 14 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/f7951360-eb89-4191-89c0-f867ff8f79d2">
        6a)Dropdown UI
        <img width="1470" alt="Screenshot 2024-04-23 at 9 38 55 PM" src="https://github.com/tirthshah2504/DCC-assignment-4/assets/143423973/6266060e-8245-476d-8d64-3e55f2aa1b27">


