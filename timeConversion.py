import datetime
import pytz

# Convert the timestamp to a datetime object
timestamp = 1685454341
dt = datetime.datetime.fromtimestamp(timestamp)

# Define the timezone as Asia/Jakarta (GMT+7)
timezone = pytz.timezone('Asia/Jakarta')

# Convert the datetime to the desired timezone
dt = datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc).astimezone(timezone)

# Format the datetime as a string in the expected format
formatted_time = dt.strftime("%d %B %Y %H:%M")

print(formatted_time)