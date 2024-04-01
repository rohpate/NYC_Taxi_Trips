# **Big Data Inspection - NYC Taxi Trips Project**
### This is a repo which describes about dataset which contains information about taxi rides in NYC. The data used consists of the following `list of Attributes`:
* ['medallion', ' hack_license', ' vendor_id', ' rate_code', ' store_and_fwd_flag', ' pickup_datetime', ' dropoff_datetime', ' passenger_count', ' trip_time_in_secs', ' trip_distance', ' pickup_longitude', ' pickup_latitude', ' dropoff_longitude', ' dropoff_latitude']
### These attributes provide a wide range as a user to introspect throughly and make decision on the data.
---
---
### Using Python, I have analised throughly about the dataset. Also, use of different modules made my job easier. Here are some descriptive analytical questions :
### First let's load the file into the memory and print some data
### **File used: trip_data_12.csv**
---
#### This code imports csv module, reads the file into the memory and then prints the first 5 rows incliding the header.
```python
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
```
### **What are the field names?  Give descriptions for each field.**
---
#### This code gives the first row i.e the header of the dataset which consists of the different field names.
```python
import csv
fn ='trip_data_12.csv'
f = open(fn,'r')
reader = csv.reader(f)
for row in reader:
    print(row)
    break
```
#### Output:
```
['medallion', ' hack_license', ' vendor_id', ' rate_code', ' store_and_fwd_flag', ' pickup_datetime', ' dropoff_datetime', ' passenger_count', ' trip_time_in_secs', ' trip_distance', ' pickup_longitude', ' pickup_latitude', ' dropoff_longitude', ' dropoff_latitude']
```
### Description:
* **medallion**: It is a unique identifier for the taxi cab
* **hack_license**: A unique license ID assigned for the taxi driver
* **vendor_id**: A unique identification provided to the taxi company
* **rate_code**: The rate code for the trip (e.g. standard rate, JFK airport rate, etc.)
* **store_and_fwd_flag**: A flag indicating whether the trip data was held in vehicle memory before sending to the vendor (Y=store and forward; N=not a store and forward trip)
* **pickup_datetime**: The date and time when the passengers were picked up
* **dropoff_datetime**: The date and time when the passengers were dropped off
* **passenger_coun**: Total number of passengers onboard the vehicle for each trip(driver entered value)
* **trip_time_in_secs**: Duration of each trip in seconds
* **trip_distance**: Each trip distance in miles
* **pickup_longitude**: Longitude coordinate of the pickup location
* **pickup_latitude**: Latitude coordinate of the pickup location
* **dropoff_longitude**: Longitude coordinate of the dropoff location
* **dropoff_latitude**: Latitude coordinate of the dropoff location 
### **What datetime range does the dataset cover?  How many rows are there in total?**
---
#### First, importing csv and datetime modules then initialising the min_val and max_val to None and then iterating through each row of the file, there is a chance that the datetime values may be in different format and so firstly converting the entire `row[5]` to datetime format and initialising it to datetime object `dto` and then performing the operation.
#### code for pick_datetime:
```python
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
```
#### Output:
Pickup_DateTime: Min_val = 2013-12-01 00:00:00
Pickup_DateTime: max_val = 2013-12-31 23:59:57
#### code for dropoff_datetime:
```python
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
```
#### Output:
Dropoff_DateTime: Min_val = 2013-12-01 00:00:00 
Dropoff_DateTime: max_val = 2014-01-03 16:31:27
#### Description:
* From the above code we can conclude that we have a dataset of NewYork City taxi's for the months DECEMBER and JANUARY for the years 2013 and 2014 specifically from 2013-12-01 00:00:00 to 2014-01-03 16:31:27.
#### Code for total number of rows:
```python
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
```
#### Output:
```python
Row: 0
Row: 1000000
Row: 2000000
Row: 3000000
Row: 4000000
Row: 5000000
Row: 6000000
Row: 7000000
Row: 8000000
Row: 9000000
Row: 10000000
Row: 11000000
Row: 12000000
Row: 13000000
Total number of rows: 13971119
```
#### Description:
* In the output we see that we have iterated from 0th row and then checked for 1000000th row and then proceeded with the entire dataset. As a result we print each 1000000th iteration and we see that the there are `13971119` total rows in the dataset which includes the header rows also.
### **Give some sample data for each field:**
---
#### Code:
```python
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
```
#### Description:
* Result is first 10 rows of the dataset and then breaking the iteration after 10th row.
### **What MySQL data types / len would you need to store each of the fields?**
---
Data types / len needed are:
* **medallion**: VARCHAR(32)
* **hack_license**: VARCHAR(32)
* **vendor_id**: VARCHAR(3)
* **rate_code**: INT(3)
* **store_and_fwd_flag**: VARCHAR(3)
* **pickup_datetime**: DATETIME in the format YYYY-MM-DD HH:MM:SS
* **dropoff_datetime**: DATETIME in the format YYYY-MM-DD HH:MM:SS
* **passenger_coun**: INT(3)
* **trip_time_in_secs**: INT(11)
* **trip_distance**: FLOAT(10,4)
* **pickup_longitude**: DECIMAL(10,4)
* **pickup_latitude**: DECIMAL(10,4)
* **dropoff_longitude**: DECIMAL(10,4)
* **dropoff_latitude**: DECIMAL(10,4)
### **What is the geographic range of the data?**
---
The Geographical range can be calculated by using the Geospacial coordinates which are pickup_longitude, pickup_latitude, dropoff_longitude and dropoff_latitude. 
#### Code to find the Maximun and Minimum pickup and dropoff coordinates:
```python
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
  
```
#### Output:
```python
pickup_latitude_min: 40.401424
pickup_latitude_max: 41.01965
pickup_longitude_min: -74.399956
pickup_longitude_max: -72.403671
dropoff_latitude_min: 40.75
dropoff_latitude_max: 40.999977
dropoff_longitude_min: -74.491203
dropoff_longitude_max: -72.344879
```
#### Description:
* As the dataset contains many Null values and Zero's , there is a lot of unrelavant data in the longitude and latitude section which is misleading the decision.
* So, while mapping the coordinates we get to know that there is a huge difference and practically it is impossible that the Taxi would go to those coordinates for either pickup or dropoff and so by assuming and fixing the maximun Radius of NewYork City as:
```
pickup_latitude_min = 90
pickup_latitude_max = -90
pickup_longitude_min = 180
pickup_longitude_max = -180
dropoff_latitude_min = 90
dropoff_latitude_max = -90
dropoff_longitude_min = 180
dropoff_longitude_max = -180
```
* By this we are able to conclude that the range of pickup and dropoff are:
```
pickup_min = ( 40.401424, -74.399956 ) pickup_max = ( 41.01965, -72.403671 )
dropoff_min = ( 40.75, -74.491203 ) dropoff_max = ( 40.999977, -72.344879 )
```
### Map can be plotted as
![Image Link](/Taxi%20Map.png)
### **What is the average computed trip distance?**
---
#### Here, to compute the average distance we will use the Haversine Distance method as it deals with the circle distance in kilometers between two points on the earth (specified in decimal degrees)
#### For Earth radius in kilometers use `6372.8 km`, as the deals with distance in miles, I have used Earth radius as `3956 miles` approx.
#### Code to calculate the Average trip distance:
```python
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
```
#### Output:
```python
The average travel distance is: 11.466179304084072 miles. 
```
#### Description:
* we see that the average trip distance comes out to be 11.466179304084072 miles
### **What are the distinct values for each field? (If applicable)**
---
#### Code to calculate the Distinct Values:
```python
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
```
#### Output:
```
Distinct values in medallion: 13460
['5328490D7C89EB6EAB9A349B39BB0D3E', '451A13DA90DF8FA7D25380DF79CF61A3', '89AC2013723DAC319A06BB59B812F546', 'B0F3531B277039535393DBA582D5109F', '20A85CDF09AC1BE3A87E33B36670150E', 'FFA00BDFE6BC7DD95D36D20154B06A53', '952AFBC963A32508692B2223D5D2ECEE', 'C61EBE0BFDD0A348B083267DE989FEF5', '66C472B47E225FD01F0E7C73F11E7099', 'D242F08982116B6C6EBEF33FBCC14513']
Distinct values in  hack_license: 33381
['ED8FBCE44AFA50E3DA2A109BCC080FF7', '3AAB0BF924B7A2F16E2C5EFF5A023BCF', '591A17D9508D09E188882D92B8832BF9', '912404A3298EF01CD1B16AEB0B2A782A', '660043AE9457CE04A3778E1B6BBFBFA7', 'AB14EC9A69071CF933FB1BDACED21E3D', 'C46ED46075FA55646CAC3CB06C3819B2', 'D6380649B3555AEB75D36C2DF286FEA7', '40DF4E271DA64F01236A26B89F9BBED3', '5EC0025A1C1BC5B906FF6E8CB49AA63C']
Distinct values in  vendor_id: 2
['VTS', 'CMT']
Distinct values in  rate_code: 14
['210', '6', '5', '4', '15', '2', '0', '8', '1', '13']
Distinct values in  store_and_fwd_flag: 3
['', 'Y', 'N']
Distinct values in  pickup_datetime: 2289920
['2013-12-23 11:59:42', '2013-12-27 11:17:41', '2013-12-02 21:17:35', '2013-12-03 22:59:57', '2013-12-28 04:44:49', '2013-12-07 13:21:17', '2013-12-02 16:08:49', '2013-12-09 14:27:14', '2013-12-13 04:34:30', '2013-12-26 21:47:09']
Distinct values in  dropoff_datetime: 2291803
['2013-12-23 11:59:42', '2013-12-27 11:17:41', '2013-12-02 21:17:35', '2013-12-07 13:21:17', '2013-12-02 16:08:49', '2013-12-03 22:59:57', '2013-12-13 04:34:30', '2013-12-09 14:27:14', '2013-12-18 15:13:44', '2013-12-26 21:47:09']
Distinct values in  passenger_count: 10
['6', '5', '4', '2', '0', '8', '1', '3', '7', '9']
Distinct values in  trip_time_in_secs: 7279
['4422', '2729', '1944', '892', '5689', '2916', '6659', '1517', '2661', '1755']
Distinct values in  trip_distance: 4328
['5.37', '20.61', '26.18', '26.56', '25.54', '10.73', '6.05', '40.68', '3.80', '15.92']
Distinct values in  pickup_longitude: 38908
['-73.837273', '-74.066177', '-73.426033', '-74.368401', '-73.849487', '-73.716934', '-73.81916', '-73.993301', '-73.83606', '-73.815781']
Distinct values in  pickup_latitude: 64164
['40.656872', '40.854946', '40.795265', '40.867077', '40.849617', '40.747601', '40.811249', '40.783142', '40.822773', '40.747463']
Distinct values in  dropoff_longitude: 56641
['-73.837273', '', '-74.066177', '-73.595436', '-74.045227', '-73.849487', '-73.750809', '-73.81916', '-74.087845', '-74.026344']
Distinct values in  dropoff_latitude: 89436
['', '40.854946', '40.867077', '40.849617', '40.747601', '40.893242', '40.822773', '40.747463', '40.85355', '40.782398']
```
### **For other numeric types besides lat and lon, what are the min and max values?**
---
#### We see that apart from Latitude and Longitude we have `passenger_count`, `trip_time` and `trip_distance` which are numeric and so we can find the Minimum and Maximum values for them.
#### Code to calculate Minimum and Maximum values for `passenger_count`, `trip_time` and `trip_distance` :
```python
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
```
#### Output:
```python
Minimun passengers per trip = 1 
Maximun passengers per trip = 9


Minimun trip time = 1 
Maximun trip time = 9996


Minimun distance covered = .00 
Maximun distance covered = 99.10
```
#### Description:
* we can conclude that there were maximum of `9` passengers and a minimum of `1` passenger for a trip of Taxi for the dataset.
* The Minimum trip time comes out to be `1 sec` and Maximum to be `9996sec= 2.77 hours`. There could be a chance that the driver recorded the minimum trip distnce incorrectly in this case.
* The minimum trip distance is `0.00 miles` which again accounts for incorrectly recorded data and the maximum is `99.10 miles` .
### **Create a chart which shows the average number of passengers each hour of the day. (X axis should have 24 hours)**
---
#### Code to calculate average number of passengers each hour of the day:
```python
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
```
#### Output:
![Image Link](/Average%20number%20of%20passengers.png)
#### Description:
* From the chart we can say that, The average number of Passengers started gradually dropping from 4th hour and the 6th hour marked the lowest and then slowly started increasing untill 15th hour and the bar hovering from 15th to 20th hour. 
* In the interval (0-3)Hours and (21-23)Hours there were maximum Average number of passengers noticed.
### **Create a new CSV file which has only one out of every thousand rows.**
---
#### Code to create new csv file which has only one out of every thousand rows:
```python
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
```
#### Output/Description:
We get a sub set of the original dataset which has every 1000 rows. To cross verify, the original data set has 13971119 rows and the sub set has `13972 rows` including the Header.
### **Create a chart which shows the average number of passengers each hour of the day for the reduced dataset i.e the subset and compare the two charts.**
---
#### Code to calculate average number of passengers each hour of the day:
```python
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
```
#### Output:
![Image Link](/subset%20data.png)
#### Description To compare two charts:
* we see that this chart is not consistent as that of the previous one because the bar doestn't strictly increase or decrease uniformly in any interval of the hour.
* 6th and the 8th hour of this chart mark the lowest average number of passengers. It was same in the previous chart for the 6th hour.
* 2nd hour marks the maximun and however after 4th hour there is a steep decline in the average in both the charts.
