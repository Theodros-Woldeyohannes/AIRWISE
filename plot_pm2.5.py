import pandas as pd
import os
import matplotlib.pyplot as plt

# Folder containing CSV files
folder_path = r'C:\Users\Teddy\Documents\P30\PM_data\PurpleAir Download 7-22-2024'

# List to store PM2.5 data for all files
all_pm25_data = []

# Recursively search for CSV files in all subfolders
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.csv'):
            file_path = os.path.join(root, file_name)

            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Convert timestamp to datetime
            df['time_stamp'] = pd.to_datetime(df['time_stamp'])

            # Check if 'pm2.5_atm' column exists
            if 'pm2.5_atm' in df.columns:
                # Extract PM2.5 data
                pm25_data = df['pm2.5_atm']

                #Plot PM2.5 data
                plt.figure(figsize=(10, 5))  # Adjust size as needed
                plt.plot(df['time_stamp'], pm25_data, label='PM2.5 Concentration (µg/m³)')
                plt.xlabel('Time')
                plt.ylabel('PM2.5 Concentration (µg/m³)')
                plt.title(f'{file_name[:-4]}')
                plt.legend()
                plt.grid(True)
                #plt.axhline(y = 9, color = 'r', linestyle = 'dashed')

                # print(df)
                # df.to_csv(r'D:\UNM\P50\INBRE\2024\PurpleAir_data\PurpleAir Download 6-19-2024 (1)/df.csv')

                # f, (ax, ax2) = plt.subplots(1, 2, sharey=True, facecolor='w')
                # # plot the same data on both axes
                # ax.plot(df['time_stamp_UTC'], pm25_data)
                # ax2.plot(df['time_stamp_UTC'], pm25_data)

                # ax.set_xlim(0, 123)
                # ax2.set_xlim(124, 391)

                # # hide the spines between ax and ax2
                # ax.spines['right'].set_visible(False)
                # ax2.spines['left'].set_visible(False)
                # ax.yaxis.tick_left()
                # ax.tick_params(labelright='off')
                # ax2.yaxis.tick_right()

                # d = .015  # how big to make the diagonal lines in axes coordinates
                # # arguments to pass plot, just so we don't keep repeating them
                # kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
                # ax.plot((1-d, 1+d), (-d, +d), **kwargs)
                # ax.plot((1-d, 1+d), (1-d, 1+d), **kwargs)

                # kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
                # ax2.plot((-d, +d), (1-d, 1+d), **kwargs)
                # ax2.plot((-d, +d), (-d, +d), **kwargs)

                # Save the figure as PNG
                output_file_path = os.path.join(root, f'{file_name[:-4]}_PM25_v2.png')
                plt.savefig(output_file_path)

                # Close the figure to release memory
                plt.close()

                # Append PM2.5 data to the list
                all_pm25_data.append(pm25_data)

# Check if any PM2.5 data was extracted
if all_pm25_data:
    print("PM2.5 data extracted from the CSV files.")
else:
    print("No PM2.5 data found in the CSV files.")