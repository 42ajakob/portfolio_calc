# A simple Portfolio weight calculator written in python for investment
Takes a file (portfolio_example.txt) that gives [ETFs return value] | [start date] | [end_date] as input.
Returns ETFs weight, annual rate of each weighted ETF and annual rate of portfolio.
The weight calculation is based on each ETFs performance over it's period of time.

# Why does it exists?
To have a convient way to do the math of my portfolio for me lol.
I came up with this idea using the beauty of basic math to figure out how much weight each asset should have that depends on it's past performance.
Instead of guessing like "Mhmm ok I go 95% on America and 5% distributed equally on all the other ETFs".
I don't say it's the best way to calculate your weight.
It just helps to fairly distributed the weight of your portfolio depending of your past performance.

# Execution
Open your terminal. If your on windows cry or figure how to download this repository and execute a python script.
```
git clone https://github.com/42ajakob/portfolio_weight_calc && cd portfolio_weight_calc
```
```
python main.py portfolio_example.txt
```

# Do I have to consider something when using it?
- It's precise with the same start and end dates of your ETFs across your Portfolio.
- It's not with different start and end dates.
The overall market gave different returns in the past and might lived throw crisis that affected the ETFs performance in the past.
While the other ETFs performance where not affected of it because of missing data.
- The results are rounded up and down and a year is 365.25 days in this calculator.
- It's not there to calculate your Stocks/Bonds distribution. Although you certainly can this is ultimatly your decision and depends on your situation.
There is no formular to make this decision for you.
- The "annual rate weighted" is less precise then the "Annual rate of portfolio"
This is unfortunatly duo to how fixed pointer calculations work and/or how floats are limited by bytes. If you know you know.

Another thing to consider is if you have 5 stocks in America and 2 for the rest of the world.
Your gonna get a very high precentage for America. At least if America's Stock Market didn't burn by the time you read this.

So you would have to put all the ETFs from America in one portfolio.
Execute the script. Take the total interest.

Alternativly if your start and end dates where not the same across it. You can take the annual rate and use a time window of 1 year.

Use it for the second portfolio as one ETF.
The distribution you got from the first portfolio. Well now you have to make it fit into the second calculated percentage on your own.
Sooooo GL HF with it.

# Most important
Don't forget to touch grass after your long mastermind calculation session!
