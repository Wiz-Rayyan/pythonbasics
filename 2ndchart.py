import pandas as pd
import matplotlib.pyplot as plt

# Meaningful Data for Speechless Population
data = {
    "Categories": [
        "Total Speechless Population", 
        "Educational Dropouts", 
        "Employed Speechless Individuals", 
        "Prevalence of Speech Disorders"
    ],
    "Values": [
        6000000,  # Total speechless population
        2400000,  # Educational dropouts (40% of 6 million)
        1500000,  # Employed individuals (25% of 6 million)
        28000000   # Prevalence of speech disorders (2% of India's population)
    ]
}

df = pd.DataFrame(data)

# Create Pie Chart
plt.figure(figsize=(8, 8))  # Set figure size for better visibility

# Define a function to format the label with percentage
def my_autopct(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f'{pct:.1f}%\n({absolute:,})'

# Create pie chart with increased text size for all text elements
plt.pie(df["Values"], 
        labels=df["Categories"], 
        autopct=lambda pct: my_autopct(pct, df["Values"]),
        startangle=90, 
        colors=plt.cm.tab10.colors,
        explode=(0.1, 0, 0, 0),  # Slightly explode the first slice for emphasis
        textprops={'fontsize': 14})  # Increase label font size

plt.title("Statistics about Speechless Population in India", fontsize=16)  # Increase title font size
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
