  I worked on the dataset of used cars that are listed on the russian reselling websites. Data analysis on used cars typically involves examining various factors such as 
Condition and model of car age, mileage and brand loyalty. The term brand loyalty defines that how well a customer considers a car brand as a investable asset.

## Project objective: 
To Find the are Cars that can be rebuilt to set good profit margins

## Source data of Project:
Data is picked from the popular car re-selling websites like 
1. https://petropavlovsk-kamchatskiy.drom.ru/
2. https://vilyuchinsk.drom.ru/

## Columns of the Dataset

- BrandName
- Body Type
- Color
- Fuel Type
- Year
- Mileage
- Transmission
- Power
- Vehicle Configuration
- Engine Name
- Price($)

## Data Cleaning
### Percent of Nulls
![image](https://github.com/PriyankWebpage/Projects/assets/65448205/aa9d20a3-4adb-400e-a389-b70415a13c54)

### Replacing Nulls
- Replaced nulls with mode for all the categorical columns with lessthan 3% of nulls
- Replaced nulls with median for all the numerical columns with lessthan 3% of nulls.
- Categorical columns with more than 30% of nulls are replaced by creating a new category called Unknown

## Data Analysis

**Top 10 brands of that are listed on reselling websites**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/46cb047c-577b-403e-8ac0-1e8bf1d66031)
**Insights**
- Toyota is leading data followed by Nissan, Honda, Lexus

**Contribution of fuel type for each car brand**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/a15aceac-6b18-4514-b1c9-0b3491fb55d3)
**Insights**
- The proportion of gasoline and diesel is dominated by the gasoline in all the car brands.
- The reason is diesel required high maintenance than gasoline
- Electric cars are only found in the Nissan.

**Histogram of Mileage**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/8a49192f-a41a-4ccc-8486-0b84cf34dc82)

**Insights**
- Histogram of mileage has traits of skewed normal distribution
- Cars with mileage greater than 100K and less than 250K are greater in number

**Histogram of Price**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/2220fe64-e0a5-4adf-a3b2-770efb7ae8e6)

**Insights**
- Histogram of  price has gives the info that most of the used cars are priced less than $5000
- Focussing on these cars to rebuilt can actually get good profit margins.

**Average Price for each car brand**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/a505a5eb-d13d-45a3-ac79-d25d164256d6)

**Insights**
- Re-building the super luxury cars like Lamborghini, Maserati, Lexus is expensive.
Cars like Honda, Toyota, Nissan and UAZ are affordable for re-building.

**Average Mileage for each car brand**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/1b4e4aa1-8020-4a9f-8da9-934d0340dde7)

**Insights**
- The average mileage of  most of the car brands is more than 170K
- This is the possible reason why they are listed on reselling websites.

**Ads of cars of the period of the time**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/59d20ee1-c073-4844-ba3d-5f261bd1a553)

**Insights**
- Toyota has stand out from all other car brands.
- The frequency of ads of other car brands has not shown rapid fluctuations as Toyota
- The year of manufacturing could be the factor that is making Toyota stand out, lets find  


## What are the cars that can be rebuilt?

**Cars that are price ranged below $5000 and mileage greater than 170k**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/eabaa65f-db5d-4cb0-bcc1-d7f2fa28c4e4)


**Contribution of car brands to each of the car body type**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/258bbe6f-0e10-405b-9a2b-cd60e491cd2f)

**Insights**
- Sedans, Station wagon and minivan are found to have most number of listings in the reselling websites.

**Top 5 records in the previous defined parameters**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/89fc1c48-a7ac-46b8-8e51-103fb8540d1a)

**Insights**
- Sedans, Station wagon and Jeep 3 door are found to have most number of listings in the reselling websites.
Nissan and Toyota are the two leading manufacturers that occupies the market in the defined parameters like price < $5000 and mileage > 170K

**Finding the most listed cars of Toyota and Nissan**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/2f1de887-5f40-4862-9846-39957a7f69e6)

**Insights**
- Corolla, Mark II and carnia are the leading car models of Toyota listed in the reselling websites.
Similarly, Nissan has Sunny and AD models

**Getting other details of top 10 car names of Toyota and Nissan**

![image](https://github.com/PriyankWebpage/Projects/assets/65448205/7137dec0-b674-4e1f-b369-d91fbaf95eaf)

**Insights**
- It observed most of the cars are located in the Petropavlovsk-Kamchatskij.
It is good idea to set up the rebuilding unit near to the Petropavlovsk-Kamchatskij for the cost cutting. 

## Conclusion
- From the all the analysis made, the rebuilding firm should be ready with the parts of the cars like transmission, Alternator, Engine and suspension and battery of  all the car models listed in the before slides and get  the inspection done in order to make profits. 





