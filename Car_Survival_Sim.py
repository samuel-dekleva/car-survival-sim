# We are going to start with a simple model.
import numpy as np 
import pandas as pd 
import scipy.stats as ss 
import matplotlib.pyplot as plt

# Here are the inputs.

k = input("How many simulated vehicles would you like to test? ") 
k = int(k) 
n = input("How many simulations of each car would you like to run? ") 
n = int(n) 

# The initial conditions. Currently, they are set to be a mean of 200,000 miles until a devastating (totaling) wreck occurs, 
# and a mean of 260,000 miles until the car breaks down.
# Miles per month is just for the dataframe and will calculate the expected probability the car will break down in the next month.

wreck_mean = 200000 
exp_miles = 260000 
miles_per_month = 2500 

# We iterate through the inputs...

miles_list = [] 
for _ in range(k): 
    miles = input("How many miles does your car have? ") 
    miles = int(miles) 
    miles_list.append(miles)

def car_sim(mi): 
    miles_prob = ss.weibull_min.cdf(mi, c=2.5, scale=exp_miles) 
    randoms = np.random.uniform(miles_prob, 1, size=n) 
    rand_conv = ss.weibull_min.ppf(randoms, c=2.5, scale=exp_miles) 
    miles_left = rand_conv - mi 
    fatal_wreck = np.random.exponential(wreck_mean, size = n) 
    life_left = np.minimum(miles_left, fatal_wreck) 
    death_type = (fatal_wreck > miles_left).astype(int) 
    prob = death_type.mean()*100 
    next_month = (life_left < miles_per_month).mean() * 100 
    return ( life_left, death_type, mi, n, life_left.mean(), np.median(life_left), prob, next_month )

# ... and build a dataframe of the information gathered in the Monte Carlo simulation.

list_ll = [] 
list_dt = [] 
list_n = [] 
list_v = [] 
list_q = [] 
list_p = [] 
list_x = []

for mi in miles_list: 
    ll,dt,miles,m,v,q,p,x = car_sim(mi) 
    list_ll.append(ll) 
    list_dt.append(dt) 
    list_n.append(miles) 
    list_v.append(v) 
    list_q.append(q) 
    list_p.append(p) 
    list_x.append(x)

nmv = pd.DataFrame({ 
    "miles": list_n, 
    "mean_life": list_v, 
    "median_life": list_q, 
    "mech_fail_pct": list_p, 
    f"<{miles_per_month/1000:.1f}k": list_x 
})

print() 
print(nmv.round(1))

# Now, we set up histograms for each car, with global scales on the X and Y axes.

global_min = min(ll.min() for ll in list_ll) 
global_max = max(np.percentile(ll, 99.9) for ll in list_ll) 
bins = np.linspace(global_min, global_max, 50)

rows = int(np.ceil(len(list_ll) / 2)) 
cols = 2

fig, axes = plt.subplots(rows, cols, figsize=(10, 4 * rows), sharex=True, sharey=True) 
axes = axes.flatten()

for idx, (ll, dt, mi) in enumerate(zip(list_ll, list_dt, list_n)): 
    ax = axes[idx]

    ax.hist(ll[dt == 1], bins=bins, alpha=0.6, label="Mechanical")
    ax.hist(ll[dt == 0], bins=bins, alpha=0.6, label="Accident")

    ax.set_title(f"{mi:,} miles")
    ax.set_xlim(global_min, global_max)

if idx == 0:
    ax.legend()
for j in range(idx + 1, len(axes)): 
    fig.delaxes(axes[j])

fig.supxlabel("Miles Remaining") 
fig.supylabel("Density") 
fig.suptitle("Failure Distributions by Vehicle Mileage")

plt.tight_layout() 
plt.show()

plt.figure()

#Finally, we make a survival chart for all the cars.

for ll, mi in zip(list_ll, list_n): 
    sorted_life = np.sort(ll) 
    survival = 1 - np.arange(1, len(sorted_life)+1) / len(sorted_life)

    plt.plot(sorted_life, survival, label=f"{mi:,} miles")
    
plt.xlabel("Miles Remaining") 
plt.ylabel("Survival Probability") 
plt.title("Survival Curves by Vehicle Mileage") 
plt.legend() 
plt.grid(True)

plt.show()