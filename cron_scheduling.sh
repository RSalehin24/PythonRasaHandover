# syntax:
#   *      *        *            *           *
# minute  hour  daysOfMonth    month    days of week
# days of week: 1 means Monday
# * means every or all the time
# */5  *  *  *  *  : run a script every 5 mins
# 30  12 1-7 *  *  : run a script at 12:30 noon at first 7 days of the month
#  0   6  *  * 2-6 : run a script at 6 in the morning from tuesday to saturday

crontab -e  # add or edit cron
crontab -l  # list the alrady scheduled scripts for a particular user

