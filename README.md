# Weather Data Analysis

## Introduction
There are 106,200 stations from around the world containing five
weather common measurements: precipitation total (PRCP), snow-
fall (SNOW), snow base depth (SNWD), max temperature (TMAX),
min temperature (TMIN) for each day of the year. Other additional
meteorological measurements are included for stations where the
data is available. This dataset contains data from 1750 to 2023. This
totals over 106 GB of data when uncompressed.

### The Data Set
The NOAA Global Historical Climatology Network Daily (GHCN-
Daily) dataset contains daily observations over global land areas.
It contains station-based measurements from land-based stations
worldwide. GHCN-Daily is a composite of climate records from
numerous sources that were merged together and subjected to a
common suite of quality assurance reviews. b vThe directory is
structured by year from 1750 to present, with each file named after
the respective year. The data is available in CSV file format and as
.csv.gzip files, so any particular year will be named yyyy.csv and
yyyy.csv.gz

## Problem
Manipulate the dataset to retrieve the median of "TMAX" for a
specific subset of weather stations for all 365 days for each available
year. Make a plot showing the average annual temperatures for
5 weather stations. Use parallel programming and a single pass
through the data to make the data processing as fast as it can
possibly be.
• The 5 weather stations with longest recorded data for "TMAX"

### Hypothesis
With global temperatures rising due to global warming, the maxi-
mum temperature recorded at different stations will trend upwards
over time.

### Approach Overview
I selected the 5 weather stations with the most overall data to
analyze:
• Selecting Stations: Using zgrep, determine which station
ID’s have "TMAX" data for the longest amount of time into
the past.
• Python Script: A python script to obtain all 365 days of data
for each given year then calculate the median temperature
at a given station for each year.
• Bash Script: Finds all "TMAX" records in each year file
for each given station ID. Feeds data into python script to
calculate median and saves result to CSV.
• CSV Output: The output of both scripts in [Station ID],
[Year], [Median Temperature] format for easy graphing.

## System/Algorithm Design
### Data Preprocessing
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### System Architecture
The dataset for this project was stored on an external Sacramento
State server for the Statistics Department. The directory is struc-
tured by year from 1750 to present, with each file named after the
respective year. The data is available in CSV file format and as
.csv.gzip files, so any particular year will be named yyyy.csv and
yyyy.csv.gz

### Python Script
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Shell Script
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### CSV Output
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Evaluation
### Methodology
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Conclusion
Historical data trends upward for all five weather stations in various parts of the world. This supports my initial hypothesis that the effects of global warming can be seen by plotting the median temperature, thus removing the influence of outliers, for every year.

### Learning Experience
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

