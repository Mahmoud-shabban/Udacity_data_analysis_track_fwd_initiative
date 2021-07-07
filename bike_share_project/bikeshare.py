# Importing our liberaries
import pandas as pd
import numpy as np
import time

# Asking the user for the city to do analysis?
# Checked correctly
def choose_city():
	Our_cites = {'chicago':'chicago.csv','washington':'washington.csv','NY':'new_york_city.csv'}
	while True:
		city= input('What city you wnat to look in? "use the same format as [chicago,washington,NY]":\n')
		if city in Our_cites.keys():
			return Our_cites[city]
		else:
			print('wrong iput Please try again\n')
			continue

# Asking for the month filter?
# Checked correctly
def choose_month():
	while True:
		month = input('choose month to filter with "first six month of the year" or cohoose "all" for all month:\n')
		months = ['all','january', 'february', 'march', 'april', 'may', 'june']
		if month.lower() in months:
			return month.title()
		else:
			print('\nincorrect input  Please choose a month or choose all')
			continue

# Asking for the day to filter with?
# Checked correctly
def choose_day():
	days = ['Tuesday','Monday','Friday','Thursday','Wednesday','Saturday','Sunday','All']
	while True:
		day = input('Choose day to filter with or choose all for all days:\n')
		if day.title() in days:
			return day.title()
		else:
			print('\nincorrect input Please try again')
			continue

# loadig Data
# Checked correctly
def data_load(city,month,day):
	"""
	data_load function loads the data and performes data preprossing steps:
		- removes unlabled data
		- converting time strings into timestamp
		- fills the gabs (NaN values) with forward fill method
	
	arg:
		city(str): city data file in csv
		month(str): optional if you want to filter the data if not inster it as 'All' 
		day(str): optional if you want to filter the data with specific day if not insert it as 'All'
	
	returns the data ready for analysis
	"""
	
	start_time = time.time()
	df = pd.read_csv(city)

	# Removing unnecessary data (unnammed data)
	try:
		df.pop('Unnamed: 0')
	except:
		pass
	
	#filling the Nan values if present
	df = df.fillna(method='ffill')
	#converting time string into time stamp useing pd.to_datetime
	df['Start Time'] = pd.to_datetime(df['Start Time'])	
	df['End Time'] = pd.to_datetime(df['End Time'])

	# Making the new columns for analysis
	df['month'] = df['Start Time'].apply(lambda x:x.month_name())
	df['start_day_name'] = df['Start Time'].apply(lambda x:x.day_name())
	df['start_hour'] = df['Start Time'].apply(lambda x:x.hour)
	df['trip']=df['Start Station'] + ' --to--> '+ df['End Station']

	# Performing the filteration
	if month != 'All':
		df = df[df['month']==month]

	if day != 'All':
		df = df[df['start_day_name']==day]

	print("\nThis took %s seconds to load the data with filters." % (time.time() - start_time))
	print('-'*80,'\n')
	print('\nstarting the analysis....../')
	print('-'*60)
	return df

# Peforming Data analysis
# Checked correctly
def data_analysis(DF,city):
	'''
	Calculating the required statistics for the data
	'''
	start_time = time.time()

	# The most common month
	print('Which month is the most common ')
	print('-'*20)
	print('Calculating statistics..../')
	msc_month = DF['month'].value_counts().head(1).index[0]
	msc_month_counts = DF['month'].value_counts().head(1).values[0]
	print(f'the most common month is {msc_month} and count: {msc_month_counts}\n')
	print('-'*40)

	# The most common day of the week
	print('which day is more busy?')
	print('-'*20)
	print('Calculating statistics..../')
	msc_day = DF['start_day_name'].value_counts().head(1).index[0]
	msc_day_counts = DF['start_day_name'].value_counts().head(1).values[0]
	print(f'the most common day of the week is {msc_day} and count: {msc_day_counts}\n')
	print('-'*40)

	# The most common hour of the day
	print('Which hour Our Cutomers prefer?')
	print('-'*20)
	print('Calculating statistics..../')
	msc_hour=DF['start_hour'].value_counts().head(1).index[0]
	msc_hour_counts=DF['start_hour'].value_counts().head(1).values[0]
	print(f'the most common hour is {msc_hour} and count: {msc_hour_counts}\n')	
	print('-'*40)

	# The most common Stations?
	print('Which start station is more preffered among the Cutomers?')
	print('-'*20)
	print('Calculating statistics..../')
	msc_start_station=DF['Start Station'].value_counts().head(1).index[0]
	msc_start_station_count=DF['Start Station'].value_counts().head(1).values[0]
	print(f'the most common Start Station is: {msc_start_station}, count: {msc_start_station_count}\n')
	
	print('\nWhcih destination is more used?')
	print('-'*20)
	msc_end_station=DF['End Station'].value_counts().head(1).index[0]
	msc_end_station_count=DF['End Station'].value_counts().head(1).values[0]
	print(f'the most common End Station is: {msc_end_station}, count: {msc_end_station_count}\n')
	
	print('Whcih trip is more used [start --to--> end]?')
	print('-'*20)
	msc_trip=DF['trip'].value_counts().head(1).index[0]
	msc_trip_count=DF['trip'].value_counts().head(1).values[0]
	print(f'the most common Trip is from: {msc_trip} and count: {msc_trip_count}\n')
	print('-'*40)

	# The trip duration information
	print('What about the trip duration?')
	print('-'*20)
	print('Calculating statistics..../')
	mask = DF[DF['trip']== DF['trip'].mode().values[0]]
	total_travel_time = mask['Trip Duration'].sum()
	average_travel_time = mask['Trip Duration'].mean()
	print(f'"{msc_trip}" "the most used trip" total travel duration is: {total_travel_time} seconds\nand the average travel time is: {round(average_travel_time)} seconds\n')
	print('-'*40)

	# The users info
	print('And Cutomers....?')
	print('-'*20)
	print('Calculating statistics..../')
	user_info = DF['User Type'].value_counts()
	print(f'the User counts are:\n{user_info.index[0]} count: {user_info.values[0]} , {user_info.index[1]} count: {user_info.values[1]}\n')
	print('-'*40)

	# The user Gender info
	if city !='washington':
		print(f'This users gender info for {city} city')
		print('-'*20)
		print('Calculating statistics..../')
		user_gender = DF['Gender'].value_counts()
		user_birth_date = DF['Birth Year'].value_counts()
		print(f'the Users Genders are: {user_gender.index[0]} count: {user_gender.values[0]} and {user_gender.index[1]} count: {user_gender.values[1]}\n')
		print(f'the Most recent year of birth is: {int(user_birth_date.index.max())}\nthe earliest year of birth is: {int(user_birth_date.index.min())}\nthe most common year is: {int(user_birth_date.head(1).index[0])}\n')

	print("\nThis took %s seconds to  calculate the statistics.\n" % (time.time() - start_time))
	print('-'*80,'\n')
# Showing the Raw Data?
# Checked correctly
def raw_data(data):
	step =5
	while True:
		raw = input('Do you want to see the raw data(Y/N)?\n')
		if raw == 'y' or raw ==  'Y':
			view = data[step-5:step]
			# As the screen only shows 2 columns we use for loop to show all data frame
			for i in range(0,len(view.columns)-2):
				print(view[[view.columns[i],view.columns[i+1]]],'\n')
			step +=5
		elif raw == 'n' or raw == 'N':
			print('-'*80,'\n')
			break
		else:
			print('wrong input!!')
			continue

# Performing another analysis?
# Checked correctly
def restart():
	while True:
		restart = input('Want another analysis(Y/N)?\n')
		if restart == 'Y' or restart=='y':
			return True
		elif restart == 'n' or restart=='N':
			return False
		else:
			print('wrong input Please try again\n')
			continue

# The main Function
def main():
	print("\nWelcome!! let's analyse some data\n")
	analyse = True
	while analyse:
		city_file = choose_city()
		month = choose_month()
		day = choose_day()
		print('\nloading data.../')
		print('-'*20,'\n')
		data_frame = data_load(city_file,month,day)
		city = city_file.split('.')[0]
		data_analysis(DF=data_frame,city=city)
		raw_data(data=data_frame)
		analyse=restart()

if __name__=='__main__':
	main()






