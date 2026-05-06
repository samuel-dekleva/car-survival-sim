# Car Survival Simulator
A Monte Carlo simulation framework for estimating vehicle longevity under mechanical failure and accident risk.
For each vehicle, expected longevity is simulated given its current mileage, with many adjustable parameters.

## About

This is a Monte Carlo model using NumPy, which can scale very efficiently to a large number of simulation.

The model operates by simulating both the mileage at which the car will no longer be operational due to mechanical failure 
and the mileage at which the car will be totaled in an accident. 
The minimum of these values is the total mileage reached before the vehicle is retired. 
The program formats this data into a dataframe and displays histograms and survival curves to visualize the data.

The simulation conditions on the vehicle's current mileage. As an example, a car with 100,000 miles on it will be closer, on average, to mechanical failure than a car with 0 miles on it.

## Model Assumptions

* Mileage at a vehicle's death from normal wear is assumed to follow a Weibull distribution with parameter *k*. While *k* can vary, it is set to a default of 2.5. The scale's default is 260,000, but can likewise vary.
* Mileage until catastrophic accident is modeled using an exponential distribution, set to a default mean of 200,000.

## Sample Output

The three outputs will be a dataframe, a grid of histograms, and a survival chart.
An example dataframe follows below.

### DataFrame

| miles | mean_life | median_life | mech_fail_pct | <2.5k |
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

Below are some sample histograms. One car has 100,000 miles on it, and the other has 400,000. 
The histograms below illustrate the distribution of remaining vehicle life separated by mechanical failure versus accident-related failure.

![](https://imgur.com/myoMIJp.png) 

### Survival Chart

Here are the survival curves for the above histograms.

![](https://imgur.com/8NUD1oA.png)

From the chart, we can see at a glance that while about 40 percent of cars with 100,000 miles make it another 100,000, less than 10 percent of cars with 400,000 miles survive for 100,000 more miles.

## Motivation

* Calculating the expected miles until a car is no longer functional is crucial to vehicle owners in determining whether to purchase a vehicle and estimating their risk of incurring unplanned expenses in a given month.
* Calculating the probability that a car will fail in the next month can help a vehicle owner to assess the value of an insurance policy, given their risk.

## How To Run

The required inputs are the:
* Number of vehicles to test (recommended to use 10 or less for histogram readability);
* Number of simulations of each vehicle to run (highly scalable, but recommended to use between 50,000 and 1,500,000);
* Current mileage of each vehicle.
  
You can run the code in Python using [Car_Survival_Sim.py](Car_Survival_Sim.py), and you can see the notebook 
[here](Car_Survival_Sim.ipynb).

Have fun!
