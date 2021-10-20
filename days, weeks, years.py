n = int(input('Enter no. of days to convert into days,week & years'))
if n < 365:
    print('No. of years are 0 , no. of weeks are',int(n/7),'no. of days',n%int(n/7))
else:
    print('No. of years',int(n/365),'no. of weeks are',int(n/365)% int(n*7/365), 'no. of days',n%(int(n*7/365)))