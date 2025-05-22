# Steps to run hadoop MapReduce
### 1. Pull Docker image by running
``` docker pull bde2020/hadoop-namenode:2.0.0-hadoop2.7.4-java8 ```
``` docker pull bde2020/hadoop-datanode:2.0.0-hadoop2.7.4-java8 ```

### 2.Start hadoop network and run both namenode and datanode
``` docker network create hadoop ```
``` docker run -d --net hadoop --name namenode \ ```
``` -e CLUSTER_NAME=test \ ```
``` -p 9870:9870 \ ```
``` bde2020/hadoop-namenode:2.0.0-hadoop2.7.4-java8 ```
``` docker run -d --net hadoop --name datanode \ ```
``` -e CORE_CONF_fs_defaultFS=hdfs://namenode:8020 \ ```
``` -e CLUSTER_NAME=test \ ```
``` bde2020/hadoop-datanode:2.0.0-hadoop2.7.4-java8 ```

### 3.Copy the files to Docker (to namenode)
``` docker cp Downloads/Alice.txt  namenode:/Alice.txt ```
``` docker cp Downloads/words.txt  namenode:/words.txt ```
``` docker cp Downloads/WordCount.java  namenode:/tmp/WordCount.java ```

### 4.Compile Java file
``` docker exec -it namenode javac -classpath $(docker exec namenode hadoop classpath) -d /tmp /tmp/WordCount.java ```
``` Then i changed to work inside the namenode container so that it's easier to run linux commands : docker exec -it namenode bash ```
``` Compile : jar cf WordCount.jar WordCount*.class ```

### 5.Make input directory and put Alice.txt and words.txt there (i’m still running inside the docker)
``` hdfs dfs -mkdir -p /input ```
``` hdfs dfs -put words.txt /input/ ```
``` hdfs dfs -put Alice.txt /input/ ```

### 6.Run
``` hadoop jar tmp/WordCount.jar WordCount /input/words.txt /output_words ```
``` hadoop jar tmp/WordCount.jar WordCount /input/Alice.txt /output_alice ```

### 7.Check if the output files are present in hadoop fs
``` hdfs dfs -ls / ```          

### 8.Move file from hadoop to local (in container/docker)
``` hdfs dfs -copyToLocal /output_alice / ```
``` hdfs dfs -copyToLocal /output_words / ```

### 9.Download output files from docker (in binary files)

