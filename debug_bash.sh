# set -x enables debugging mode
# print each command it executes to the terminal
set -x

# when bash encounters an error it sets an exit code that indicates the nature of the error
# exit code of the most recent or latest command : $?

if [ $? -ne 0 ]; then
  echo "Error occurred."
fi

# echo command can be helpful to find out where the errors are occurring and what values are passed
x=1
echo "Value of variable x is: $x"

set -e  # exit the script immediately


# troubleshooting cron by varifying logs
/var/log/syslog  #doesn't work for this device
