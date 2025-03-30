@echo off
setx HADOOP_HOME "C:\hadoop"
setx PATH "%PATH%;%HADOOP_HOME%\bin"
echo Hadoop environment variables set permanently!
echo HADOOP_HOME = C:\hadoop
