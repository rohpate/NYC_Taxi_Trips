#Initally loading the file into memory and printing first 5 rows
import csv
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
n=0
for row in reader:
    print(row)
    n+=1
    if n > 5:
        break
    
#1.a) Range of Pick-up Datetime in the dataset
import csv
import datetime
import time
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
n=0
min_val = None
max_val = None
for row in reader:
    if n > 0:
        dto = None
        try:
            dto = datetime.datetime.strptime(row[5],'%Y-%m-%d %H:%M:%S')
        except Exception as e:
            print(e)
        if dto is not None:
            if n == 1:
                min_val = dto
                max_val = dto   
            if dto < min_val:
                min_val = dto
            elif dto > max_val:
                max_val = dto
    n+=1
    if n > 10000000000:
        break
print('Pickup_DateTime: Min_val =',min_val , '\nPickup_DateTime: max_val =',max_val)

#1.a) Range of Drop-off Datetime in the dataset
import csv
import datetime
import time
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
n=0
min_val = None
max_val = None
for row in reader:
    if n > 0:
        dto = None
        try:
            dto = datetime.datetime.strptime(row[6],'%Y-%m-%d %H:%M:%S')
        except Exception as e:
            print(e)
        if dto is not None:
            if n == 1:
                min_val = dto
                max_val = dto   
            if dto < min_val:
                min_val = dto
            elif dto > max_val:
                max_val = dto
    n+=1
    if n > 10000000000:
        break
print('Dropoff_DateTime: Min_val =',min_val , '\nDropoff_DateTime: max_val =',max_val)

#1.b) Total number of rows
import csv
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
n=0
for row in reader:
    if n % 1000000 == 0:
        print("Row:",n)
    n+=1
print("Total number of rows:",n)

#2) Field names of the Dataset
import csv
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
for row in reader:
    print(row)
    break

#3) Some Sample data for each field
import csv
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
n=0
for row in reader:
    print(row)
    n+=1
    if n > 10:
        break

#5) What is the geographic range of your data (min/max - X/Y)
import csv

pickup_latitude_min = 90
pickup_latitude_max = -90
pickup_longitude_min = 180
pickup_longitude_max = -180
dropoff_latitude_min = 90
dropoff_latitude_max = -90
dropoff_longitude_min = 180
dropoff_longitude_max = -180
n = 0

with open('trip_data_12.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if n > 0:
            try:
                pickup_latitude = float(row[' pickup_latitude'])
                pickup_longitude = float(row[' pickup_longitude'])
                dropoff_latitude = float(row[' dropoff_latitude'])
                dropoff_longitude = float(row[' dropoff_longitude'])
                if (-74.4 <= pickup_longitude <= -72.05 and 40.4 <= pickup_latitude <= 41.02):
                    pickup_latitude_min = min(pickup_latitude_min, pickup_latitude)
                    pickup_latitude_max = max(pickup_latitude_max, pickup_latitude)
                    pickup_longitude_min = min(pickup_longitude_min, pickup_longitude)
                    pickup_longitude_max = max(pickup_longitude_max, pickup_longitude)
                if dropoff_longitude is not None and (-74.5 <= dropoff_longitude <= -72.02 and 40.75 <= dropoff_latitude <= 41):
                    dropoff_latitude_min = min(dropoff_latitude_min, dropoff_latitude)
                    dropoff_latitude_max = max(dropoff_latitude_max, dropoff_latitude)
                    dropoff_longitude_min = min(dropoff_longitude_min, dropoff_longitude)
                    dropoff_longitude_max = max(dropoff_longitude_max, dropoff_longitude)
            except ValueError:
                continue
        n+=1
        if n > 1000000000:
            break

print(f"pickup_latitude_min: {pickup_latitude_min}")
print(f"pickup_latitude_max: {pickup_latitude_max}")
print(f"pickup_longitude_min: {pickup_longitude_min}")
print(f"pickup_longitude_max: {pickup_longitude_max}")
print(f"dropoff_latitude_min: {dropoff_latitude_min}")
print(f"dropoff_latitude_max: {dropoff_latitude_max}")
print(f"dropoff_longitude_min: {dropoff_longitude_min}")
print(f"dropoff_longitude_max: {dropoff_longitude_max}")
  
#6) Average computed trip distance using Haversine Distance
import csv
from math import radians, cos, sin, asin, sqrt

fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
    
# skip the header row
next(reader)
total_distance = 0
num_of_trips = 0
n = 0   
for row in reader:
    # extract pickup and dropoff latitude and longitude
    try:
        pickup_lat = float(row[10])
        pickup_lon = float(row[11])
        dropoff_lat = float(row[12])
        dropoff_lon = float(row[13])
    except ValueError:
        pass
    
    # convert pickup and dropoff latitude and longitude to radians
    pickup_lat_rad = radians(pickup_lat)
    pickup_lon_rad = radians(pickup_lon)
    dropoff_lat_rad = radians(dropoff_lat)
    dropoff_lon_rad = radians(dropoff_lon)
    
    # compute the haversine distance
    lon_diff = dropoff_lon_rad - pickup_lon_rad
    lat_diff = dropoff_lat_rad - pickup_lat_rad
    a = sin(lat_diff / 2) ** 2 + cos(pickup_lat_rad) * cos(dropoff_lat_rad) * sin(lon_diff / 2) ** 2
    c = 2 * asin(sqrt(a))
    distance = 3956 * c
    
    # add to the total distance and number of trips
    total_distance += distance
    num_of_trips += 1
    n+=1
    if n > 1000000000:
        break
# compute the average distance
avg_distance = total_distance / num_of_trips if num_of_trips > 0 else 0

print('The average travel distance is:', avg_distance, 'miles')

#7) Distinct values for each field.
import csv
from collections import defaultdict

unique_values = defaultdict(set)

with open('trip_data_12.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for column, value in row.items():
            unique_values[column].add(value)

for column, values in unique_values.items():
    print(f"Distinct values in {column}: {len(values)}")
    print(list(values)[:10])



#8) Min and Max for numeric types other than lat and lon
import csv
import math
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
n=0
passenger_count = None
min_passenger = None
max_passenger = None

trip_time = None
min_triptime = None
max_triptime = None

trip_distance = None
min_dist = None
max_dist = None

for row in reader:
    if n > 0:
        passenger_count = row[7]
        trip_time = row[8]
        trip_distance = row[9]
        #try:
        if passenger_count !='0' and trip_time !='0' and trip_distance !='0':
            if n == 1:
                min_passenger = passenger_count
                max_passenger = passenger_count

                min_triptime = trip_time
                max_triptime = trip_time

                min_dist = trip_distance
                max_dist = trip_distance

            if passenger_count < min_passenger:
                min_passenger = passenger_count
            if passenger_count > max_passenger:
                max_passenger = passenger_count

            if trip_time < min_triptime:
                min_triptime = trip_time
            if trip_time > max_triptime:
                max_triptime = trip_time
                
            if trip_distance < min_dist:
                min_dist = trip_distance
            if trip_distance > max_dist:
                max_dist = trip_distance
        else :
            continue
        #except Exception as e:
            #print(e)
    n+=1
    if n > 1000000000:
        break
print('Minimun passengers per trip =',min_passenger , '\nMaximun passengers per trip =',max_passenger)
print('\n')
print('Minimun trip time =',min_triptime ,'\nMaximun trip time =',max_triptime)
print('\n')
print('Minimun distance covered =',min_dist ,'\nMaximun distance covered =',max_dist)


#9) Average number of passengers each hour of the day
import csv
import matplotlib.pyplot as plt
import datetime
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
passengers_per_hour = {}
trips_per_hour = {}
avg_passengers_per_hour = {}
n = 0
for row in reader:
    if n > 0:
        try:
            pickup_datetime = datetime.datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
            pickup_hour = pickup_datetime.hour
            passenger_count = int(row[7])
        except Exception as e:
            print(e)
        trips_per_hour[pickup_hour] = trips_per_hour.get(pickup_hour, 0) + 1
        passengers_per_hour[pickup_hour] = passengers_per_hour.get(pickup_hour, 0) + passenger_count
    n+=1
    if n > 1000000000:
        break
for hour, passengers in passengers_per_hour.items():
    avg_passengers_per_hour[hour] = passengers / trips_per_hour[hour]
plt.bar(avg_passengers_per_hour.keys(), avg_passengers_per_hour.values())
plt.title('Average Number of Passengers by Hour')
plt.xlabel('Hour of the day')
plt.xticks(range(24))
plt.ylabel('Average number of passengers')
plt.show()


#10) New csv file with one out of every 1000 rows
import csv
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
#n = 0
#clear destination file
with open('sandeep_trip_data_12_new.csv','w') as f1:
    f1.write('')

with open('sandeep_trip_data_12_new.csv','a') as f1:
    writer = csv.writer(f1, delimiter=',', lineterminator='\n')
    header = next(reader)
    writer.writerow(header)
    for i,row in enumerate(reader):
        if i > 0:
            i += 1
            if i % 1000 == 0:
                writer.writerow(row)
        if i > 1000000000:
            break


#11) Average number of passengers each hour of the day
import csv
import matplotlib.pyplot as plt
import datetime
fn ='sandeep_trip_data_12_new.csv'
f = open(fn,'r')
reader = csv.reader(f)
passengers_per_hour = {}
trips_per_hour = {}
avg_passengers_per_hour = {}
n = 0
for row in reader:
    if n > 0:
        try:
            pickup_datetime = datetime.datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
            pickup_hour = pickup_datetime.hour
            passenger_count = int(row[7])
        except Exception as e:
            print(e)
        trips_per_hour[pickup_hour] = trips_per_hour.get(pickup_hour, 0) + 1
        passengers_per_hour[pickup_hour] = passengers_per_hour.get(pickup_hour, 0) + passenger_count
    n+=1
    if n > 1000000000:
        break
for hour, passengers in passengers_per_hour.items():
    avg_passengers_per_hour[hour] = passengers / trips_per_hour[hour]
plt.bar(avg_passengers_per_hour.keys(), avg_passengers_per_hour.values())
plt.title('Average Number of Passengers by Hour')
plt.xlabel('Hour of the day')
plt.xticks(range(24))
plt.ylabel('Average number of passengers')
plt.show()


