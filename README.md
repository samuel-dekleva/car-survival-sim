# Car Survival Simulator
Welcome to the car survival simulator!
This is a calculation of simulated survival probability of a car to a certain mileage given its current mileage, with adjustable parameters.

## About

This is a Monte Carlo model which can run over 1,000,000 simulations per vehicle in just a few seconds.

The model operates by calculating the mileage at which the car will be totaled from wear and tear and the mileage at which the car will be totaled in an accident. The minimum of these values is the total mileage reached before the car dies. It formats this data into a dataframe and displays histograms and survival curves to visualize the data.

The simulation conditions on the number of miles the car already has. As an example, a car with 100,000 miles on it will be closer, on average, to mechanical failure than a car with 0 miles on it.

## Model Assumptions

* Mileage at a vehicle's death from normal wear is assumed to follow a Weibull distribution with parameter *k*. While *k* can vary, it is set to a default of 2.5.
* Mileage at which a vehicle is totaled due to accident is assumed to follow an exponential distribution.

## Sample Output

The three outputs will be a dataframe, a grid of histograms, and a survival chart.
An example dataframe follows below.

### DataFrame

|    miles  |mean_life | median_life  |mech_fail_pct | <2.5k|
|-------------|----------|--------------|--------------|------|
| 0  | 129272.8  |   113557.9   |        35.4  |  1.2|
| 80000 |  100858.2   |   84955.0   |        49.5 |   1.7|
| 160000 |   77625.3   |   62394.9    |       61.2  |  2.4|
| 240000 |   60367.6  |    46748.4    |       69.9  |  3.4 |
| 320000  |  47782.1    |  35945.9    |       76.1  |  4.5 |
| 400000  |  38598.9    |  28457.6    |       80.7  |  5.7 |
| 480000  |  31825.3   |   23083.1    |       84.1  |  7.1 |
| 560000  |  26635.6   |   19143.2    |       86.6  |  8.5 |
| 640000 |   22715.7   |   16192.6     |      88.7  | 10.0 |
| 720000 |   19595.2   |   13915.9    |       90.2  |  11.6 |

* The "miles" column gives the number of miles already on the vehicle, which for each vehicle is inputted by the user.
* The "mean_life" and "median_life" columns give the mean and median remaining miles on the car, respectively.
* The "mech_fail_pct" column expresses the percentage of cars that broke down, rather than being involved in an accident.
* The "<2.5k" column computes the percentage of simulations which end before a user-defined threshold. In this case, the user chose 2,500 miles.

### Histograms

Below are some sample histograms. One car has 100,000 miles on it, and the other has 400,000. This is how the distribution of accident versus mechanical failure breaks down per miles traveled.

![](https://imgur.com/myoMIJp.png) 

### Survival Chart

Here are the survival curves for the above histograms.

![](https://imgur.com/8NUD1oA.png)

From the chart, we can see at a glance that while about 40 percent of cars with 100,000 miles make it another 100,000, less than 10 percent of cars with 400,000 miles complete the same feat.

## Motivation

* Calculating the expected miles until a car is no longer functional is crucial to vehicle owners in determining whether to purchase a vehicle, and estimating their total unexpected expenses.
* Calculating the probability that a car will fail in the next month can help a vehicle owner to assess the value of an insurance policy, given their risk.

## How To Run

You can run the code using 
