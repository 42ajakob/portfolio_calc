# A simple Portfolio weight calculator written in python for investment
Takes a file (portfolio_example.txt) that gives [ETFs return value] | [start date] | [end_date] as input.
Returns ETFs weight, annual rate and annual rate based on the weight distribution.
The weight calculation is based on each Index Funds performance over it's period of time.

# Why does it exists?
To have a convient way to do the math of my portfolio for me lol.
I came up with this idea using the beauty of basic math to figure out how much weight each asset should have that depends on it's performance.
Instead of guessing like "Mhmm ok I go 95% on America and 5% distributed equally on all the other ETFs".
I don't say it's the best way to calculate your weight.
It just looks fairly distributed and depending of your portfolios future performance can be readjusted.

# Execution
Open your terminal. If your on windows cry or figure how to download this repository and execute a python script.
```
git clone https://github.com/42ajakob/portfolio_weight_calc && cd portfolio_weight_calc && python main.py portfolio_example.txt
```

# Do I have to consider something when using it?
It's not there to calculate your Stocks/Bonds distribution. Although you certainly can this is ultimatly your decision and depends on your situation.
There is no formular to make this decision for you.

Another thing to consider is if you have 5 stocks in America and 2 for the rest of the world.
Your gonna get a very high precentage for America. At least if America's Stock Market didn't burn by the time you read this.

So you would have to put all the ETFs from America in one portfolio.
Execute the script. Take the annual rate of combined ETFs weight.
Use it for the second portfolio as one ETF starting from 01.01.00 to 01.01.01 for example.
The distribution you got from the first portfolio. Well now you have to make it fit into the second calculated percentage on your own.
Sooooo GL HF with it.

# Most important
Don't forget to touch grass after your long mastermind calculation session!
