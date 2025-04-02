@echo off
REM Inicia o Spark Connect server
set CLASS="org.apache.spark.sql.connect.service.SparkConnectServer"
spark-submit --class %CLASS% --name "Spark Connect server" --packages org.apache.spark:spark-connect_2.12:3.5.5
pause