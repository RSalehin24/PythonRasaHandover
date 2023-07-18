# create file in /etc/supervisor/conf.d/file_name
# the following configuration has to be written
[program:super_test]
command=/home/Code/somthing  # command to run
autostart=true    # starts automatically
autorestart=true  # starts automatically in case of failure
stderr_logfile=/var/log/something.err.log
stdout_logfile=/var/log/something.out.log


# after  that write the following cmd in the terminal: shows availability of the program [here something]
supervisorctl reread

supervisorctl update   # [adds the something program to the process group]

# check if the program is running 
supervisorctl

# see the stdout_logfile using nano or vim [use the path to open the file ]
# see or monitor the output in real time using tail -f /var/log/something.out.log [output log file path]
