import csv
import random
import time
from datetime import datetime, timedelta
# Define directory

dir_path = '/home/cloudera/Desktop/RawData'
# Define the start and end timestamps for the intervals
start_time = datetime(2023, 6, 12, 0, 0, 1)
start_content_time = start_time - timedelta(minutes=5)
end_content_time = start_time #+ timedelta(minutes=5)  # Assuming 5-minute intervals

print(start_content_time)
print(end_content_time)
# Define the number of files
file_num = 2
# Define the number of row to generate
row_num = 23

# Generate multiple CSV files
for i in range(file_num):
    # Format the date and time for the file name
    file_date = start_time.strftime('%y%d%m')
    file_time = start_time.strftime('%H%M')

    # Generate the file name
    csv_file = f"{dir_path}/MSFMEMORYUSAGE.{file_date}-{file_time}.csv"

    # Open the CSV file in write mode
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['#STARTTIMESTAMP', 'STOPTIMESTAMP', 'MSFNODEID', 'MSFSLOTID',
                        'MSFCPUID', 'MSFMEMORYINUSE'])
        for j in range(row_num):
            # Write the data row
            if j+1 == 7 or j+1 == 8:
                row_data1 = [
                    start_content_time.strftime('%Y-%m-%d %H:%M:%S'),
                    end_content_time.strftime('%Y-%m-%d %H:%M:%S'),
                    5,  # MSFNODEID
                    j + 1,  # MSFSLOTID
                    0,  # MSFCPUID
                    random.randint(5,30) # MSFMEMORYINUSE
                ]
                row_data2 = [
                    start_content_time.strftime('%Y-%m-%d %H:%M:%S'),
                    end_content_time.strftime('%Y-%m-%d %H:%M:%S'),
                    5,  # MSFNODEID
                    j + 1,  # MSFSLOTID
                    1,  # MSFCPUID
                   random.randint(5,30) # MSFMEMORYINUSE
                ]
                writer.writerow(row_data1)
                writer.writerow(row_data2)
            else:
                row_data = [
                    start_content_time.strftime('%Y-%m-%d %H:%M:%S'),
                    end_content_time.strftime('%Y-%m-%d %H:%M:%S'),
                    5,  # MSFNODEID
                    j + 1,  # MSFSLOTID
                    0,  # MSFCPUID
                    random.randint(5,30) # MSFMEMORYINUSE
                ]
                writer.writerow(row_data)

    print(f"CSV file '{csv_file}' generated successfully!")

    # Update the start and end timestamps for the next interval
    start_time = start_time + timedelta(minutes=5)
    start_content_time = end_content_time
    end_content_time = start_time
    # Wait 5 mins for next file
    time.sleep(3)