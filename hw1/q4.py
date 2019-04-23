import datetime
s = input()
date = s.split("/")
weekday = datetime.date(int(date[2]),int(date[0]),int(date[1])).strftime('%A')
month = datetime.date(int(date[2]),int(date[0]),int(date[1])).strftime('%B')
print(weekday+", "+month+" "+str(int(date[1]))+", "+date[2])