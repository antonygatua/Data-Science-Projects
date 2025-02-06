import matplotlib.pyplot as plt
import seaborn as sns

def plot_pie_chart(day_booking_counts, save_path):
    # visualize using a pie chart 
    fig, ax = plt.subplots(figsize=(8, 6))

    labels = list(day_booking_counts.keys())
    sizes = list(day_booking_counts.values())

    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90) # plot the chart

    ax.axis('equal') # equal aspect ratio: ensure pie is drawn as a circle

    ax.set_title("Bookings by Day", fontsize=15) # label the chart

    # adjust layout
    plt.tight_layout()

    # save the image
    fig.savefig(save_path, dpi=300, bbox_inches='tight')

def plot_gross_booking_value_by_service(data, save_path):
    # visualize
    fig, ax = plt.subplots(figsize=(8,6))

    sns.barplot(x='service_name', y='total_amount', data=data, ax=ax, width=0.3, palette='viridis', hue='service_name')

    # annotate with booking count on each bar
    for i, row in data.iterrows():
        ax.text(i, row['total_amount'], f"{row['booking_count']}",
            ha='center', va='bottom', fontsize=10)
    
    # label the graph
    ax.set_title("Total Amount by Serive with Booking Count", fontsize=15)
    ax.set_ylabel("Total Amount INR", fontsize=14)
    ax.set_xlabel("Service Name", fontsize=14)

    # adjust layout
    plt.tight_layout()

    # save 
    fig.savefig(save_path, dpi=300, bbox_inches='tight')

def plot_heatmap(correlation_matrix, save_path):
    # plotting correlation heatmap
    fig, ax = plt.subplots(figsize=(8,6))

    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, ax=ax)

    # set title 
    ax.set_title("Correlation Heatmap", fontsize=15)

    plt.tight_layout()

    # save the figure 
    fig.savefig(save_path, dpi=300, bbox_inches='tight')

def plot_time_series(yearly_data, quarterly_data, save_path):
    # create subplots
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 12), sharex=False) # dont share X axis between suplots

    # yearly plot
    for device in yearly_data.columns:
        ax[0].plot(yearly_data.index, yearly_data[device], marker='o', label=device)

    ax[0].set_title("Number of Bookings by Device Type (Yearly)", fontsize=14)
    ax[0].set_xlabel("Year", fontsize=13)
    ax[0].set_ylabel("Bookings Count", fontsize=13)
    ax[0].legend(title="Device Type", fontsize=10)
    ax[0].grid(True)

    # quarterly plot
    quarterly_data.index = [f"{y} Q{q}" for y, q in quarterly_data.index]
    for device in quarterly_data.columns:
        ax[1].plot(quarterly_data.index, quarterly_data[device], marker='o', label=device)

    ax[1].set_title("Number of Bookings by Device Type (Quarterly)", fontsize=14)
    ax[1].set_xlabel("Year and Quarter", fontsize=13)
    ax[1].set_ylabel("Bookings Count", fontsize=13)
    ax[1].legend(title="Device Type", fontsize=10)
    ax[1].grid(True)
    ax[1].tick_params(axis='x', rotation=45)

    # adjust layout
    plt.tight_layout()

    # save the figure 
    fig.savefig(save_path)

def plot_obsr(daily_obsr, monthly_obsr, save_path):
    # visualize
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 6), sharey=False)

    # daily oBSR
    sns.lineplot(x=daily_obsr.index, y=daily_obsr['oBSR'], data=daily_obsr, ax=ax[0], marker='o', color='green')

    ax[0].set_title("Daily Overall Booking-to-Search Ratio (oBSR)", fontsize=14)
    ax[0].set_ylabel("oBSR", fontsize=13)
    ax[0].set_xlabel("Day", fontsize=13)
    ax[0].tick_params(axis='x', rotation=45)
    ax[0].grid(True)

    # monthly oBSR
    sns.lineplot(x=monthly_obsr.index, y=monthly_obsr['oBSR'], data=monthly_obsr, ax=ax[1], marker='o', color='black')

    ax[1].set_title("Monthly Overall Booking-to-Search Ratio (oBSR)", fontsize=14)
    ax[1].set_ylabel("oBSR", fontsize=13)
    ax[1].set_xlabel("Month", fontsize=13)
    ax[1].tick_params(axis='x', rotation=45)
    ax[1].grid(True)

    # adjust layout
    plt.tight_layout()


    # save the plot 
    fig.savefig(save_path)
