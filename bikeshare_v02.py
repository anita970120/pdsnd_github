import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']

weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    city = input("Would you like to see data for Chicago, New York City, or Washington?").lower()
    while city not in CITY_DATA.keys():
        city = input("Please make sure that you give the one of the city names from the question!").lower()

    filter_choice = input("Would you like to filter the data by month, day, or not at all? ?").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    if filter_choice=="month":
        month = input(" Which month - January, February, March, April, May, or June?").lower()
        while month not in months:
            month = input("Please make sure that you give the one of months from the question!").lower()
        day= 'all'
    elif filter_choice=="day":
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Which day - monday, tuesday, wednesday, thursday, friday, saturday, or sunday?").lower()
        while day not in weekdays:
            day = input("Please make sure that you give the one of the weekday names from the question!").lower()
        month= 'all'
    elif filter_choice=="not at all":
        month= 'all'
        day= 'all'
    else:
        while True:
            print("Please make sure that the input is from month, day, or not at all")

    print('-'*40)
    return city, month, day

#city, month, day= get_filters()
#print(city,month,day)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month,day and hours of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\nThe most common month is: {} for the selected filter.'.format(months[common_month-1].title()))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nThe most common weekday is: {} for the selected filter.'.format(common_day))
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('\nThe most common hour is: {} for the selected filter.'.format(str(common_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nThe most common start station is: {} for the selected filter.'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station is: {} for the selected filter.'.format(common_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + ' - ' + df['End Station']
    common_start_end_combination = df['Start-End Combination'].mode()[0]
    print('\nThe most common start-end combination is: {} for the selected filter.'.format(common_start_end_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_travel_time = df['Trip Duration'].sum()
    sum_day = sum_travel_time // 86400
    sum_hour = (sum_travel_time % 86400) // 3600
    sum_minute = ((sum_travel_time % 86400) % 3600) // 60
    sum_second = ((sum_travel_time % 86400) % 3600) % 60
    print('\nThe total travel time is: {} seconds, {}d {}h {}m {}s for the selected filter.'.format(sum_travel_time,sum_day,sum_hour,sum_minute,sum_second))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_day = mean_travel_time // 86400
    mean_hour = (mean_travel_time % 86400) // 3600
    mean_minute = ((mean_travel_time % 86400) % 3600) // 60
    mean_second = ((mean_travel_time % 86400) % 3600) % 60
    print('\nThe mean travel time is: {} seconds, {}d {}h {}m {}s for the selected filter.'.format(mean_travel_time, mean_day,mean_hour,mean_minute,mean_second))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nFollowing are de counts of user types for the selected filter:\n{}'.format(user_types))

    if city == "chicago" or city == "new york city":
        # TO DO: Display counts of gender
        user_gender = df['Gender'].value_counts()
        print('\nFollowing are de counts of user gender for the selected filter:\n{}.'.format(user_gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print('\nThe earliest year of birth is: {} for the selected filter.'.format(earliest_birth_year))
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print('\nThe most recent year of birth is: {} for the selected filter.'.format(most_recent_birth_year))
        common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print('\nThe most common year of birth is: {} for the selected filter.'.format(common_birth_year))
    else:
        print('\nSorry, we don\'t have any gender and birth year data for your selected city!')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    if view_data.lower()=='yes':
        while (start_loc <= df.size-5):
            pd.set_option(“display.max_columns”,200) #see all columns by chekcing data
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue? Enter yes or no?").lower()
            if view_display == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
