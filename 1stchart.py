import pandas as pd
import matplotlib.pyplot as plt

# Meaningful Data
data = {
    "Categories": [
        "Contributing to economy", 
        "Educational Dropouts", 
        "Employed Deaf Individuals", 
        "Prevalence of Hearing Loss"
    ],
    "Values": [
        18000000,  # Total deaf population
        9000000,   # Educational dropouts (50% of 18 million)
        5400000,   # Employed individuals (30% of 18 million)
        700000      # Prevalence of disabling hearing loss (5% of India's population)
    ]
}

df = pd.DataFrame(data)

# Create Pie Chart
plt.figure(figsize=(8, 8))  # Set figure size for better visibility

# Create pie chart
plt.pie(df["Values"], 
        labels=df["Categories"], 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.tab10.colors,
        explode=(0.1, 0, 0, 0))  # Slightly explode the first slice for emphasis

plt.title("The unfortunate condition of Deaf Population in India")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
