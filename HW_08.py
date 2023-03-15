from collections import defaultdict
from datetime import date, datetime, timedelta


users = [{'name': 'Phil', 'birthday': '18-03-1995'},
         {'name': 'Bill', 'birthday': '19-03-2002'},
         {'name': 'Jill', 'birthday': '20-03-2000'},
         {'name': 'Kim', 'birthday': '21-03-1981'},
         {'name': 'Jan', 'birthday': '21-03-1973'}]

def get_birthdays_per_week(users: list):
         
    today = datetime.now()
    cur_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
    cur_year = today.year
    cur_weekday = today.weekday()
    this_week_saturday = cur_day + timedelta(days=5-cur_weekday)   
    next_week_friday = cur_day + timedelta(days=4-cur_weekday+7)
    
    result = defaultdict(list)
           
    for user in users:
        b_day_check = datetime.strptime(user['birthday'], '%d-%m-%Y').replace(year = cur_year)        
        if this_week_saturday <= b_day_check <= next_week_friday:
            if b_day_check.weekday() < 5: 
                result[b_day_check.strftime('%A')].append(user['name'])    
            else:
                result['Monday'].append(user['name']) 
    
    for day in result:
        print (f"{day}: {', '.join(result[day])}")
    
         
if __name__ == '__main__':
            
    get_birthdays_per_week(users)
