export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
export LANG=en_US.UTF-8
export HADOOP_OS_TYPE=${HADOOP_OS_TYPE:-$(uname -s)}
export HADOOP_LOG_DIR=~/logs
export HADOOP_PID_DIR=~/PID