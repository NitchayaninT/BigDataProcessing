# Hadoop
**Hadoop** is an open-source **framework** designed to **store and process large datasets** across **clusters of computers** using **simple programming models**.
- set of open source program and procedures
- used for processing large amount of data
- hadoop cluster is a **collection of computer working together to perform tasks**
- Split complications into different parallel tasks
- Make efficient use of large commodity clusters and distributed file systems
- Full tolerance, data distribution, monitoring and **load balancing** (Hadoop ensures that **data and computation** are efficiently balanced across the cluster)
### What Hadoop Does
Hadoop solves the problem of **handling massive data** by:
- **Storing** it efficiently across many machines (**HDFS** – Hadoop Distributed File System). Data is divided into directories and files : files are divided into uniform block size (normally 128MB) and are distributed across various nodes
- **Processing** it in parallel (**MapReduce** – a programming model for distributed computing). Its a core processing unit, split data into small units (processing engine that splits jobs across machines)
### When to use hadoop?
- data parallelism -> simultaneous execution
- multiple applications over the same data store
- high volume
- high variety
### Yarn : Resource manager
Resource manager that handles job scheduling & cluster resource management
### HDFS Component 💖
#### NameNode (Primary node)
- Meta data
- Record name, location, directory and other metadata
- Manage and maintain
#### DataNode (Secondary nodes)
- Block storage (store many blocks inside, and can be **from different original files**)
- Listen from Namenode command
- Block creation, deletion, replication
- Read/write request
### Hadoop Distributed Files system
Namenode divide data into chunks (blocks)
**SMALL FILES PROBLEM** :
	- Storing a lot of small files
	- Extremely smaller than the block size
	- Involve lots of seeks
	- If a job needs to read thousands of small files : Each file is usually **stored on different DataNodes** (due to HDFS’s distribution mechanism), The client or MapReduce job has to **connect to each DataNode** in turn to fetch the next file -> lots of hopping between datanode to datanode (A lot of **network overhead and latency**)
#### Block
- A block is the minimum amount of data that can be read or written and provides fault tolerance
- The default block size could be 64 or 128 megabytes
	- 500 MB file -> 128x3MB + 116 MB : Fragmentation, then replication
	
### Hadoop for fault tolerance
- Data replication 
In **Hadoop**, **fault tolerance** means **replicating data blocks across multiple DataNodes** within the **same cluster** (look at page 15 of slide week4)

Example:
- You upload a 256 MB file → split into 2 blocks of 128MB
- Block 1 and Block 2 are each **replicated 3 times** → total of 6 block replicas stored across different machines.
### HDFS Concept (Read/Write)
Write once/ read many
#### Read
- The name node gets location of data (block locations), checks if the file exists
- Name node will verify client's privilege 
- A client send request to the closet data nodes
#### Write
- The name node will verify the client's privilege
- name node check file existence
- if file already exists, client wont allow to write
- if file doesnt exist, client can write
- data nodes start creating replicas
- send confirmation to client
### Why This Design?
HDFS was built for **big data analytics**, where the access pattern is typically:
- Load a **huge dataset** once (e.g., logs, user activity, sensor data)
- Then run **many read-heavy jobs** (MapReduce, Hive, Spark, etc.)
### Example
Let’s say you want to read a 256 MB file split into 2 blocks (128 MB each), stored with 3 replicas:

1. Client asks the NameNode: "Where is `/mydata/file1.txt`?"
2. NameNode replies:
    - Block 1 → DataNodes A, B, C
    - Block 2 → DataNodes D, E, F
        
3. Client chooses:
    - DataNode A (nearest) for Block 1
    - DataNode D (nearest) for Block 2
        
4. Reads both blocks and reconstructs the file.
### Commands in Hadoop
`hadoop fs mkdir /user/<user_name>` : make directory in hadoop fs
`hadoop fs -moveFromLocal Orangecat.jpeg ./` : move file from local (container/bucket) to hadoop fs (different layers)
`hadoop fs -ls` : list file/directories in hadoop fs
`hadoop fs -du` : see size of all replica
`hadoop fs -mv from.txt out/to.txt`: move from.txt file to location out/to.txt
`hadoop fs -touch file.txt` : create file in hadoop fs
`hadoop fs -copyFromLocal file /` : copy file from local -> hdfs
`hadoop fs -copytoLocal file /`: copy a file from hdfs -> local
`hadoop fs -cat file | tail 4` : reading the bottom file
`hadoop fs -cat file | head 4` : read the top of the file
