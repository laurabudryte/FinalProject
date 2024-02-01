# VILNIUS-TOKYO-VILNIUS FLIGHTS OVERVIEW FOR MAY 2024

## Details
Created by Ugnė Petravičiūtė ir Laura Budrytė

This is the final project of Data analysis course at Vilnius Coding School.

Project theme: Vilnius-Tokyo-Vilnius flights overview for May 2024.

The main goal of the project is to analyse outbound and return flights' data of Vilnius-Tokyo route for May 2024, focusing on factors that impact flights' prices.

In this project we used Python and CSV files. 

## Applied knowledge
Used libraries: Selenium, BeautifulSoup, Pandas, MatplotLib, SeaBorn, Scikit-learn

## Project files
### scraping.py 
_Used imports_: BeautifulSoup, Selenium and Pandas

In this project file below URLs were used in order to obtain data needed for analysis:
- https://www.skyscanner.net/transport/flights/vno/tyoa/240503/240510/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- https://www.skyscanner.net/transport/flights/vno/tyoa/240510/240517/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- https://www.skyscanner.net/transport/flights/vno/tyoa/240517/240524/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- https://www.skyscanner.net/transport/flights/vno/tyoa/240524/240531/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1

### data_cleaning.py
_Used imports_: Pandas

This project file was used to clean obtained data and transfer it to CSV file

### tables.py
_Used imports_: Pandas, Scikit-learn, SeaBorn and MatplotLib

In this project file all analyses and graphs were made:

* **Vilnius-Tokyo-Vilnius Flight Prices vs Time and Predicted Prices**

  This visualization shows how the flight prices depend on the flight time in the analyzed data and what are the predictions.

![image](https://github.com/laurabudryte/FinalProject/blob/1937055de7c4a92969210e776c5bee59e71012c2/Screenshots/Vilnius-Tokyo-Vilnius%20Flight%20Prices%20vs%20Time%20and%20Predicted%20Prices.JPG)


* **Average prices (Vilnius-Tokyo-Vilnius) by dates**

  In this visualization average flights' prices are displayed by outbound and return flight dates.

![image](https://github.com/laurabudryte/FinalProject/blob/1937055de7c4a92969210e776c5bee59e71012c2/Screenshots/Average%20prices%20(Vilnius-Tokyo-Vilnius)%20by%20dates.JPG)


* **Average prices per airline**

  This visualization shows what are the average prices for each airline when both outbound and return flights are operated by the same airline.

![image](https://github.com/laurabudryte/FinalProject/blob/1937055de7c4a92969210e776c5bee59e71012c2/Screenshots/Average%20prices%20per%20airline.JPG)


* **Prices & departure time from VNO airport correlation**

  The correlation between outbound flights from Vilnius departure time and flights' prices is shown in this visualization. It is also shown the frequency of flights for each time.

![image](https://github.com/laurabudryte/FinalProject/blob/1937055de7c4a92969210e776c5bee59e71012c2/Screenshots/Prices%20%26%20departure%20time%20from%20VNO%20correlation.JPG)


* **Most common international airports**

  This visualization shows most common connecting international airports for Vilnius-Tokyo-Vilnius route.

![image](https://github.com/laurabudryte/FinalProject/blob/1937055de7c4a92969210e776c5bee59e71012c2/Screenshots/Most%20common%20international%20airports.JPG)


## Conclusion




