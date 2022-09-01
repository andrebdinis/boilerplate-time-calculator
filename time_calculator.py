# add_time("11:43 PM", "24:20", "tueSday")
# OUTPUT: "12:03 AM, Thursday (2 days later)"

def add_time(start, duration, startingWeekDay = None):
  #print(start, duration, startingWeekDay)
  
  # convert to 24-hour time
  time24 = twelveHourTo24HourTime(start)

  # get total time sum
  totalTime = getTotalTimeSum(time24, duration)

  # process minutes
  totalMinutes = getMinutesFrom24HourTime(totalTime)
  extraHours = getQuotientInteger(totalMinutes, 60)
  minutesValue = getBaseIntervalValue(totalMinutes, extraHours, 60)

  # process hours
  totalHours = getHoursFrom24HourTime(totalTime) + extraHours
  extraDays = getQuotientInteger(totalHours, 24)
  hoursValue = getBaseIntervalValue(totalHours, extraDays, 24)
    
  # construct 24-hour time with processed hours and minutes
  calculatedTime = fillOneDigit(hoursValue) + ':' + fillOneDigit(minutesValue)

  # convert (back) to 12-hour time format
  time12 = twentyFourHourTo12HourTime(calculatedTime)

  # construct week day (if bool(startingWeekDay) == True)
  if startingWeekDay:
    finalWeekDay = getFinalWeekDay(startingWeekDay, extraDays)
    time12 += ', ' + finalWeekDay

  # construct days subtitle (if extraDays >= 1)
  daysSubtitle = getDaysSubtitle(extraDays)
  if daysSubtitle:
    time12 += ' ' + daysSubtitle

  # return final 12-hour time
  #print(time12)
  return time12

  
# /////////////////////////////////////////////////////
# /////////////////////////////////////////////////////
# /////////////////////////////////////////////////////
# /////////////////////////////////////////////////////


weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def getWeekDayIndex(weekDay):
  return weekDays.index(weekDay)

def getWeekDayByIndex(index):
  return weekDays[index]

def getFinalWeekDay(startingWeekDay, extraDays):
  weekDay = startingWeekDay.lower().capitalize()
  weekDayIndex = getWeekDayIndex(weekDay)
  totalWeekDays = weekDayIndex + extraDays
  extraWeeks = getQuotientInteger(totalWeekDays, 7)
  finalWeekDayIndex = getBaseIntervalValue(totalWeekDays, extraWeeks, 7)
  finalWeekDay = getWeekDayByIndex(finalWeekDayIndex)
  return finalWeekDay

def getDaysSubtitle(extraDays):
  if extraDays == 1: return '(next day)'
  elif extraDays >= 2: return '(' + str(extraDays) + ' days later)'
  return ''

def getQuotientInteger(number, base):
  return (number/base).__trunc__()

def getBaseIntervalValue(number, quotient, base):
  if quotient >= 1:
    return (number - (quotient * base))
  else:
    return number

def fillOneDigit(number):
  if number >= 0 and number <= 9:
    return str(number).rjust(2, '0')
  return str(number)


def getTotalTimeSum(twentyFourHour, duration):
  time24Hours = getHoursFrom24HourTime(twentyFourHour)
  durHours = getHoursFrom24HourTime(duration)
  totalHours = time24Hours + durHours
  
  time24Minutes = getMinutesFrom24HourTime(twentyFourHour)
  durMinutes = getMinutesFrom24HourTime(duration)
  totalMinutes = time24Minutes + durMinutes
  
  return fillOneDigit(totalHours) + ':' + fillOneDigit(totalMinutes)


def getHoursFrom24HourTime(twentyFourHour):
  return int(twentyFourHour.split(':')[0])

def getMinutesFrom24HourTime(twentyFourHour):
  return int(twentyFourHour.split(':')[1])

def twelveHourTo24HourTime(twelveHour):
  # "12:00 AM", "1:05 AM", "11:59 AM"
  # "12:00 PM", "1:05 PM", "11:59 PM"
  time = twelveHour.split(':')
  h = int(time[0])
  m = time[1].split(' ')[0]
  meridiem = twelveHour.split(' ')[1]

  twentyFourHour = ""
  
  if meridiem == 'AM':
    if h == 12: twentyFourHour += "00"
    elif h >= 10 and h <= 11: twentyFourHour += str(h)
    elif h >= 1 and h <= 9: twentyFourHour += fillOneDigit(h)
    else: return 'Error: invalid hour input.'

  elif meridiem == 'PM':
    if h == 12: twentyFourHour += str(h)
    if h >= 1 and h <= 11: twentyFourHour += str(h + 12)
    else: return 'Error: invalid hour input.'

  return twentyFourHour + ':' + m


def twentyFourHourTo12HourTime(twentyFourHour):
  # "00:05" / "12:05" / "23:05"
  time = twentyFourHour.split(':')
  h = int(time[0])
  m = time[1]
  
  twelveHour = ''
  meridiem = ''
  
  if h >= 0 and h <= 11:
    meridiem = 'AM'
    if h == 0: twelveHour += '12'
    elif h >= 1 and h <= 11: twelveHour += str(h)
    else: return 'Error: invalid hour input.'
  
  elif h >= 12 and h <= 23:
    meridiem = 'PM'
    if h == 12: twelveHour += '12'
    elif h >= 13 and h <= 23: twelveHour += str(h - 12)
    else: return 'Error: invalid hour input.'

  return twelveHour + ':' + m + ' ' + meridiem
  