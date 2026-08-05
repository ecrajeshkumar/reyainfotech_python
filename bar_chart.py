import matplotlib.pyplot as plt
import time
import random

# Initialize data
times = []
concentrations = []

plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

for i in range(3600):  # simulate 20 updates
    # Simulate live data
    current_time = i
    co2_value = random.randint(350, 450)  # ppm
    
    times.append(current_time)
    concentrations.append(co2_value)
    
    ax.clear()
    ax.bar(times, concentrations, color='green')
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("CO₂ Concentration (ppm)")
    ax.set_title("Live CO₂ Concentration")
    
    plt.pause(1)  # wait 1 second before next update

plt.ioff()
plt.show()
