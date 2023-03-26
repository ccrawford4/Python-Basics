from datetime import datetime, date, time
currDateTime = datetime.now()
space_index = str(currDateTime).index(' ')
print(f'Today\'s date and time =  {currDateTime}')
print(f'Time component from now using string methods: {str(currDateTime)[space_index+1:]}')
print(f'Time component from now using time object: {currDateTime.time()}')
print(f'Year: {currDateTime.isocalendar()[0]}')
print(f'Week: {currDateTime.isocalendar()[1]}')
print(f'Day: {currDateTime.isocalendar()[2]}')
