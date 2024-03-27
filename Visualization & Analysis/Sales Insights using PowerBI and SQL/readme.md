# Sales Analysis of Hardware Components at Centronics Systems

 ## Problem Statement
  This project was conducted for Centronics Systems, an Indian-based hardware company, to analyze sales data and gain valuable insights. Centronics Systems distributes computer hardware and peripherals across India, with its main office in Hyderabad and several regional branches nationwide. The sales director encountered challenges due to the market's dynamic growth and declining overall sales. Despite having regional managers, communication of sales insights was primarily verbal and lacked concrete data. This resulted in frustration for the sales director, as he couldn't obtain a comprehensive overview of the business's performance. To address this issue and enable data-driven decision-making, the project aimed to develop a Power BI-based data visualization tool. Project planning utilized the AIMS Grid, involving stakeholders such as the sales director, marketing and customer service teams, data analysts, and IT personnel. The goal was to create an automated dashboard providing timely insights to support informed decision-making. Success criteria included uncovering sales order insights, achieving cost savings, and reallocating time from manual data gathering to value-added tasks.


## Data Discovery :

- #### Project Planning using AIMS Grid -

  It is a project management tool which consists of four components-
  
     - Purpose - (What to do exactly)
     - Stackholder - (Who will be involved)
     - End result - (What do you want to achieve)
     - Success Criteria - (Cost optimization and time save)
 - #### AIMS Grid -
     **1. Purpose :-** To unlock sales insights that are not visible before for the sales them for decision support and automate them to reduced manual time spent in data gathering.
     
     **2. Stakeholders :-** 
     - Sales Director
     - Marketing Team 
     - Customer Service Team
     - Data and Analytics Team
     - IT 
     
     **3. End result :-** An automated dashboard providing quick and latest sights in order to support Data driven decision making.
     
     **4. Success Criteria :-**
     - Dahboard uncovering sales order insights with latest data available
     - Sales team able to take better decisions and prove 10% cost saving of total spend.
     - Sales analysis stop data gathering manually in order to save 20% business time andreinvest it value added activity.
   
- #### Flowchart of project execution -

  ![1_khhcniAryBdmmfJt0Zk0Lg](https://user-images.githubusercontent.com/118357991/231545034-7f6cc437-5683-44f1-92df-a671540ccae9.jpg)

   

## Data Analysis using MySQL :

Completed the Data discovery and then used mySQL for data analysis.

SQL database dump is in db_dump.sql file above. Download db_dump.sql file to your local computer

- Importing Data to MySQL workbench

![Screenshot (2)](https://user-images.githubusercontent.com/118357991/233262007-c36f58cd-df19-42b5-b9cb-4d72c0ef64a4.png)

![Screenshot (3)](https://user-images.githubusercontent.com/118357991/233262064-b1fb8f0f-8c16-402d-adac-07784b81a2fe.png)


The import of data is done from an already existing MySQL file. This file has to be loaded into MySQL workbench for further data analysis. 

- Analysis of data by looking into different tables and reflecting garbage values

   We can see that garbage value that the table market cantains certain values which are incorrect.
   
     `SELECT * FROM sales.market;`
     
   And then we can check that transacation table we can see that ceratin negative value in amount which is not possible. and we can see that certain transactions are      in USD. Hence, filtration of that is also needed by converting into INR.
     
     `SELECT * FROM sales.transactions;`
     
 - Analysis of different SQL statement on data base
     
   1.To find of all customers records 
     
     `SELECT * FROM sales.customers;`
      
   2.To find total number of customers 
     
     `SELECT count(*) From sales.customers;`

   3.To find transactions for Chennai market (market code for chennai is Mark001
     
      `SELECT * FROM sales.transactions where market_code='Mark001';`

   4.To find distrinct product codes that were sold in chennai
     
      `SELECT distinct product_code FROM sales.transactions where market_code='Mark001';`

   5.To find transactions for Chennai market (market code for chennai is Mark002
     
      `SELECT * FROM sales.transactions where market_code='Mark002';`

   6.To find distrinct product codes that were sold in mumbai
     
      `SELECT distinct product_code FROM sales.transactions where market_code='Mark002';`
      
   7.To find transactions where currency is US dollars
     
      `SELECT * from sales.transactions where currency="USD";` 
      
   8.To find transactions in 2020 join by date table
     
      `SELECT sales.transactions.*, sales.date.* FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020;`  

   8.To find transactions in 2019 join by date table
     
      `SELECT sales.transactions.*, sales.date.* FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2019;`  

   9.To find total revenue in year 2020,
     
      `SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r";` 
      
   10.To find total revenue in year 2019,
     
      `SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2019 and sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r";`       

   11.To find total revenue in year 2020, January Month,
     
      `SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.date.month_name="January" and (sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r");` 

   12.To find total revenue in year 2020, February Month,
     
      `SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.date.month_name="February" and (sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r");` 

   13.To find total revenue in year 2019, January Month,
     
      `SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.date.month_name="January" and (sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r");` 

   14.To find total revenue in year 2019, February Month,
     
      `SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.date.month_name="February" and (sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r");` 

   15.To find total revenue in year 2020 in Chennai
     
      `SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.transactions.market_code="Mark001";` 

   16.To find total revenue in year 2020 in Mumbai
     
      `SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.transactions.market_code="Mark002";` 

Similarly, if we want different of any other particular city the market code of that city is used on the mysql workbench.

## Data Cleaning and ETL (Extract, Transform, Load):
In this process, we are work on data cleaning and ETL.

 Step 1: Connect the MySQL database with the PowerBI desktop.
 
 Step 2: Loading data into the Power BI deskstop.
 This step load all the tables and created in the data base. This load option will connect with the SQL and pull all the records into power BI environment.
         
 In that model view looking up for model which form the star schema.
         
![image](https://github.com/PriyankWebpage/Projects/assets/65448205/13b337fd-e66b-4d14-aa7c-d41fd5cd0800)


 Setp 3: Transform data with the help of Power Query
 
 Perform filtration in market’s table: In the tables perform when we click on the transform data option, we are directed to Power query editor. Power query editor is where we perform out ETL.and then we can perform data transformation i.e. Data Cleaning, Data Wrangling, Data Munging. we need to filter the rows where the values are null and filtering the data and deselecting the blank option. 

 Perform filtration in Transaction’s table: In the table perform when we check the query in the MySQL to filter some negative values and also 0 values that appears in the table, the desired output is received.and we will perform the similar filtration in PowerBI. we have deselecting the values, don’t want in the table. The result after filtration. the zero values represent some garbage values which is not possible so we need to clean that data.

Convert USD into INR in the transaction’s table: the  Hardware only works in India so the USD values are not possible. we need to convert those USD values into INR by using some formulas. Add new column - Conditional column - normalized currency where sales amount will be in INR

In power query editore finding the total values having USD as currency.

     `=Table.AddColumn(#"Filtered Rows", "norm_sales_amount",each if [currency] = "USD" then [sales_amount]*75 else [sales_amount]`
 
 using this correct formula of the conversion,and converted the USD currency into INR.
 
 In MySQL Workbench find that there are duplicates of USD and INR
 
     `SELECT count(*) from sales.transactions where sales.transactions.currency="INR\r";` 
     150000 - can't removed as it is large amount

     `SELECT count(*) from sales.transactions where sales.transactions.currency="INR";` 
     279 - we can remove it as it is small record and can be considered as bad data

     `SELECT count(*) from sales.transactions where sales.transactions.currency="USD\r";` 
 
     `SELECT count(*) from sales.transactions where sales.transactions.currency="USD";`

     `SELECT * from sales.transactions where sales.transactions.currency='USD\r' or sales.transactions.currency='USD';`

we can see that it is duplicate and for analysis its better to delete anyone of them so lets delete USD and keep USD/r. finally we will keep data with INR/r and USD/r-

## Data Modeling:

And then dataset was cleaned and transformed, it was ready to the data modeled.

The sales insights data tables as show below:

![Screenshot (14)](https://user-images.githubusercontent.com/118357991/234016242-369bd02e-1ddf-4047-9be4-324c83bd8761.png)

## Data Analysis  (DAX):

Measures used in all visualization are:

Key Measures:
    
  - Profit Margin % = `DIVIDE([Total Profit Margin],[Revenue],0)` 
  - Profit Margin Contribution % = `DIVIDE([Total Profit Margin],CALCULATE([Total Profit Margin],ALL('sales products'),ALL('sales customers'),ALL('sales markets')))`
  - Revenue = `SUM('sales transactions'[sales_amount])`
  - Revenue Contribution % = `DIVIDE([Revenue],CALCULATE([Revenue],ALL('sales products'),ALL('sales customers'),ALL('sales markets')))`
  - Revenue LY = `CALCULATE([Revenue],SAMEPERIODLASTYEAR('sales date'[date]))`
  - sales quntity = `SUM('sales transactions'[sales_qty])`
  - Total Profit Margin = `SUM('Sales transactions'[Profit_Margin])`

Profit Target:
  
  - `Profit Target1 = `GENERATESERIES(-0.05, 0.15, 0.01)`
  - Profit Target Value = `SELECTEDVALUE('Profit Target1'[Profit Target])`
  - Target Diff = `[Profit Margin %]-'Profit Target1'[Profit Target Value]`
  
## Build Dashboard Or a Report:

Data visualization for the data analysis (DAX) was done in Microsoft Power BI Desktop:

Shows visualizations from Sales insights :

| Key Insights |
| ----------- |
![1](https://github.com/PriyankWebpage/Projects/assets/65448205/cee59661-00c3-44a7-afcd-6ce6877bae0e)



| Profit Analysis |
| ----------- |
![2](https://github.com/PriyankWebpage/Projects/assets/65448205/e1c97a47-59fe-49f6-85c2-b28a16cb8ee0)


| Profit Analysis |
| ----------- |
![3](https://github.com/PriyankWebpage/Projects/assets/65448205/56b764e5-49c0-411f-9e0f-b89beb1a520a)


## Tools, Software and Libraries :

1.MySQL

2.Microsoft Power BI

3.Power Query Editor

3.DAX Language 



