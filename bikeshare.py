import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new York City': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
    	(str) city - (name of the city to analyze)
        (str) month - (name of the month to filter by, or "all" to apply no month filter)
        (str) day - (name of the day of week to filter by, or "all" to apply no day filter)
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("Choose New York City, Chicago or Washington?\n").lower()
      if city not in ('new York City', 'chicago', 'washington'):
        print("Try again")
        continue
      else:
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("Choose from the following list: January, February, March, April, May, June\n or type 'all' if you do not want a specific one\n").title()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        print("Try again")
        continue
      else:
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("Choose a day from the following list: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n or type 'all' if you don't want a specific one\n").title()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        print("Try again")
        continue
      else:
        break
    print('-'*40)
    return city, month, day

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'All':
        all_months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = all_months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    st_time = time.time()
    # TO DO: display the most common month
    pop_month = df['month'].mode()[0]
    print('Most Common Month:', pop_month)
    # TO DO: display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print('Most Common day:', pop_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('Most Common Hour:', pop_hour)
    print("\nThis took %s seconds." % (time.time() - st_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    st_time = time.time()
    # TO DO: display most commonly used start station
    st_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', st_station)
    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', end_station)
    # TO DO: display most frequent combination of start station and end station trip
    mix_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', st_station, " & ", end_station)
    print("\nThis took %s seconds." % (time.time() - st_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    st_time = time.time()
    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print('Total travel time:', total_time/86400, " Days")
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_time/60, " Minutes")
    print("\nThis took %s seconds." % (time.time() - st_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    st_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)
    # TO DO: Display counts of gender
    try:
        gend_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gend_types)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early_year = df['Birth Year'].min()
        print('\nEarliest Year:', early_year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")
    try:
        rec_year = df['Birth Year'].max()
        print('\nMost Recent Year:', rec_year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")
    try:
        comm_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', comm_year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")
        print("\nThis took %s seconds." % (time.time() - st_time))
    print('-'*40)
def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    if(view_data=='no'):
        return
    start_loc = 0
    while (True):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: \n").lower()
        if(view_display=='no'):
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()