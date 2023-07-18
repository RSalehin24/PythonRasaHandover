#* Any task that scheduled through crons is called a cron job

#* Cron is a job scheduling utility present in Unix like systems
#* crond daemon enables cron functionality and runs in background
#* cron reads the crontab (cron tables) for running predefined scripts
#* By using a specific syntax, a cron job can be configured to schedule scripts or other commands to run automatically

#log in as a super user first
sudo -s

#switch to crontabs
cd /var/spool/cron/crontabs

# check the schedule task or script
ls -lrt

# manage access to crontab using the file /etc/cron.allow: use the following syntax to allow a user for crontab
sudo cat cron.allow user_name

# to deny: '/etc/cron.d/cron.deny'
sudo cat cron.deny user_name

#check cron service
sudo systemctl status cron.service


##* Cron job syntax

crontab -e  # edit crontab : e->edit
            # add, delete or edit cronjobs
crontab -l  # list all the cronjobs of the current user: l->list

crontab -u username -l   # list another user's crons
crontab -u username -e   # edit another user's crons


##  cronjob example:     * * * * * sh /path/to/script.sh

##*     * * * * *  represents min, hour, day, month, weekday respectively
#* min : 0-59
#* hours : 0-23
#* days: 1-31
#* months: 1-12
#* weekday: 0-6  : here 0 is Sunday


# 5 6 * 8 6 : At 6:05 every Saturday in August 
export EDITOR=nano; crontab -e    # to open the crontab 

# remove all cronjobs
crontab -r 

# check cron log: need super user
grep 'CRON' /var/log/syslog
