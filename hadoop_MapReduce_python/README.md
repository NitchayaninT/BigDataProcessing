# Hadoop MapReduce (Python compilation)🍮

# Steps
## 0. Create cluster
`export BUCKET_NAME=anything`
`nano create_cluster.sh `
`./create_cluster.sh $BUCKET_NAME  "REGION"`
## 1. ssh to a cluster 
## 2. Upload files (mapper, reducer and input) to the bucket
## 3. Run hadoop streaming using bucket storage
<pre>```hadoop jar ///usr/lib/hadoop/hadoop-streaming-3.3.6.jar \
-files gs://yourbucketname//mapper.py,gs://yourbucketname/reducer.py   \
-mapper mapper.py  \
-numReduceTasks 1  \
-reducer reducer.py \
-input gs://yourbucketname/covid.txt  \
-output gs://yourbucketname/output3/ ```</pre>

