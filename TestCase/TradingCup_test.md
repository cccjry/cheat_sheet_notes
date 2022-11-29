# Data Varification

## Content

### [1. Problem Define](#1-Problem-Define)
### [2. Terminology](#2-Terminology)
### [3. Findings and Discover](#3-Findings-and-Discover)



## 1. Problem Define

### Data Source: [Trading Cup](https://www.tradingcup.com/en)

Question: Provide a test solution to verify those data. (Open question, think about how you will test the delivery from development team, you don’t have to implement any automation code or detail test steps here, methodology/solution/overview/strategy is expected here)

#### **Ranked On**

- Average return
- Winning percetage
- Sum profit v.s. sum loss
- Maximum drawdown
- Sharpe ratio
- Calmar ratio
- Standard deviation

## 2. Terminology

| Terms                    | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| Balance                  | amount of money present in a financial repository            |
| Drawdown                 | difference between the high point and the next low point of account balance |
| Best/Worst trade/ trades |                                                              |
| Standard Deviation       |                                                              |
| Sharpe Ratio             | excess expected return of investment (over risk-free rate) per unit of volatility or standard deviation |
| Calmar Ratio             | average annual rate of return per maximum drawdown           |



- `Sharpe Ratio = (Rx – Rf) / StdDev(x)`

Where, `x` is the investment `Rx` is the average rate of return of `x`, `Rf` is the risk-free rate of return `StdDev(x)` is the standard deviation of `Rx`.

> -    The Sharpe ratio adjusts a portfolio’s past performance—or expected future performance—for the excess risk that was taken by the investor.
>
> -    A high Sharpe ratio is good when compared to similar portfolios or funds with lower returns.
> -    The Sharpe ratio has several weaknesses, including an assumption that investment returns are normally distributed.

`Calmar Ratio = (Rx – Rf) / Max(Drawdown)`

Where `Rp` is the portfolio return, `Rf` is the risk-free return.



## 3. Findings and Discover

**Step1.** Parsing ranking board hourly

​	Collecting trader information, including long-tern and short-tern trading information.

**Step2.** Checking Collinearity of trading statistics

​	To make sure we don't use duplicated information from the data (This will increase the variance inflation factor(方差), make the prediction more meaningless).

**Step3.** Perform an ordinal regression (classification)

​	Using ranking as a response (our interest), while trading statistics as variables. Reviewing coefficients and there significance.

**Step4.** Comparing long-tern and short-tern trading

​	Comparing long-tern and short-tern trading model result in order to inspect the difference.

**Step5.** Using Shapley value to find out how variables exactly affect the ranking

​	This methodology tells exactly how variables affect the response. Finding the trends and some interactions in between.

**Step6.** Comparing the different significance of variables between long-tern and short-tern trading data, try adding weighted combination of these information.

​	Try using some linear (or nonlinear) combination of long-tern and short-tern results, i.e., using a weighted model to re-construct the hole ordinal modeling.

**Step7.** Using newest ranking result as validation data

​	Discuss the performance of the final model. Try perform some DOE to test the weight setting.

**Step8.** Repeat step6~7

​	Find out the relationships of response, variables, weight settings. Try add financial knowledge into the experiments.

