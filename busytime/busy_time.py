from datetime import datetime
from dateutil import tz
import time
import uuid 

def lambda_handler(event, context):

    print("busy_time handler: start, dev version: 200323")
    print("==== event ==== ")
    print(event)
    print("==== event ==== ")
    
    # stats  
    hours           = dict()
    fulldays        = dict()
    busyday         = dict()
    busyevening     = dict()
    
    totalevents     =     totalhours  =     totalfullday    = 0
    daytimeevents   =     daytimehours    = 0
    eveningevents   =     eveninghours    = 0
    shortevents     =     shorthours      = 0
    mediumevents    =     mediumhours     = 0
    longevents      =     longhours       = 0
    weekdayevents   =     weekdayhours    = 0
    weekendevents   =     weekendhours    = 0
    
    enddate     = datetime(1970, 1, 1)
    startdate   = datetime(3000, 1, 1)
    
    #insights = event['request']['data']['she/insights/emotions']
    events = event['request']['data']['calendar/google/events']
    
    print("busy_time handler: iterate the events")
    
    for row in events:
        if 'data' not in row:
            continue
        
        if row['data']['status'] != 'confirmed':
                continue

        print("busy_time handler: this event is confirmed")
                
        record  = row['data']
        fullday = 0
            
        if 'start' in record and 'end' in record and 'status' in record:
            print("busy_time handler: this event has start, end and status ")
    
            if 'date' in record['start']:
                print("busy_time handler: a fullday event")
    
                start = datetime.strptime(record['start']['date'], '%Y-%m-%d')
                end = datetime.strptime(record['end']['date'], '%Y-%m-%d')
                hour = 8
                fullday = 1
            elif 'dateTime' in record['start'] and 'dateTime' in record['end']:
                print("busy_time handler: not a fullday event")
    
                start = datetime.strptime(record['start']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
                end = datetime.strptime(record['end']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
                d1_ts = time.mktime(start.timetuple())
                d2_ts = time.mktime(end.timetuple())
                hour = (d2_ts - d1_ts)/3600
            else:
                print("busy_time handler: unexpected data format, continue to next")    
                continue

            datetag = start.strftime('%Y-%m-%d')
            today   =datetime.strptime(datetag, '%Y-%m-%d')

            if today > datetime.now():
                continue 

            if datetag not in hours:
                hours[datetag] = hour
            else:
                hours[datetag] = hour + hours[datetag]

            if (today < startdate):
                startdate = today
            if (today > enddate):
                enddate = today
                
            # stats 
            totalevents += 1
            totalhours += hour
            if fullday == 1:
                totalfullday += 1
                longevents  += 1
                longhours   += hour 
                if datetag not in busyday:
                        busyday[datetag] = 1
                if datetag not in fulldays:
                    fulldays[datetag] = 1
            elif hour <= 1:
                shortevents += 1
                shorthours  += hour 
            elif hour > 1 and hour <= 4:
                mediumevents    += 1
                mediumhours     += hour 
            elif hour > 4:
                longevents      += 1
                longhours       += hour 
            
            if fullday == 0:
                if start.hour < 17:
                    daytimeevents   += 1
                    daytimehours    += hour 
                    if datetag not in busyday:
                        busyday[datetag] = 1
                if start.hour >= 17:
                    eveningevents   += 1
                    eveninghours    += hour 
                    if datetag not in busyevening:
                        busyevening[datetag] = 1
            
            if start.weekday() < 5:
                weekdayevents   += 1
                weekdayhours    += hour
            else:
                weekendevents   += 1
                weekendhours    += hour 
            print("busy_time handler: finish this event, move on to next")    
                
    if enddate > datetime.now():
        enddate = datetime.now()

    print("busy_time handler: done iterating the events, analyzing total hours")
    
    period = (enddate - startdate).days
    busypercent = 100 * len(hours) / period 
    busydaytimepercent = 100 * len(busyday) / period 
    busyeveningpercent = 100 * len(busyevening) / period 
    
    allhourdata = list()
    
    for date in hours:
        record = dict()
        record['endpoint'] = 'busy_time'
        record['recordId'] = str(uuid.uuid1())
        
        d = dict()
        d['hours'] = hours[date]
        d['fullday'] = False
        if date in fulldays:
            d['fullday'] = True               
                 
        d['period'] = 'daily'
        d['date'] = date

        record['data'] = d
        
        allhourdata.append(record)
        
    result = {
        "id": "busy-time",
        "name": "Busy Time",
        "description": "This tool produces the number of busy hours on a daily basis from Google Calendar. Short events are shorter than 1 hour, medium events are between 1 and 4 hours, and long events are longer than 4 hours.",
        "summary": {
            "totalEvents": totalevents,
            "totalEventHours": totalhours,
            "totalFulldayEvents": totalfullday,
            "totalDaytimeEvents": daytimeevents,
            "totalDaytimeEventHours": daytimehours,
            "totalEveningEvents": eveningevents,
            "totalEveningEventHours": eveninghours,
            "totalShortEvents": shortevents,
            "totalShortEventHours": shorthours,
            "totalMediumEvents": mediumevents,
            "totalMediumEventHours": mediumhours,
            "totalLongEvents": longevents,
            "totalLongEventHours": longhours,
            "totalWeekdayEvents": weekdayevents,
            "totalWeekdayEventHours": weekdayhours,
            "totalWeekendEvents": weekendevents,
            "totalWeekendEventHours": weekendhours,
            "percentBusyDays": busypercent,
            "percentBusyDaytime": busydaytimepercent,
            "percentBusyEvening": busyeveningpercent,
            "startDate": startdate.strftime('%Y-%m-%d'),
            "endDate": enddate.strftime('%Y-%m-%d'),        
            "totalDays": period
        },
        "data": []
    }

    result["data"] = allhourdata

    return [{
        "namespace": "drops",
        "endpoint": "insights/busy-time",
        "data": [result],
        "linkedRecords": []
    }]


