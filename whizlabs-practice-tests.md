## Practice Test 1

Adding __lifecycle hooks__ to ASGs put instances in __wait state__ before termination. During this wait state, we can perform custom activities. Default wait period is 1 hour.

AWS __Elastic Beanstalk__ can be used to create —
- Web application using DB
- Long running worker process
- Static website

__AWS Glacier archive retrieval__ options —
- Expedited: Costly, 1-5 minutes.
- Standard: Default, 3-5 hours.
- Bulk: Cheapest, 5-12 hours.

__CloudFormation Drift Detection__ can be used to detect changes in the environment. Drift Detection only __checks property values which are explicitly set__ by stack templates or by specifying template parameters. It does not determine drift for property values which are set by default.

To increase performance, we can __prefix each object name with a hash key__ along with the current date. But, according to the new S3 performance announcement, this is __not needed anymore__.

Amazon __Redshift Enhanced VPC Routing__ provides VPC resources the access to Redshift.

Amazon __ElastiCache__ offers fully managed __Redis and Memcached__. 

Default __visibility timeout__ for SQS is __30 seconds__.

AWS __DynamoDB__ is durable, ACID compliant, can go through multiple schema changes, and changes to the database does not result in any database downtime.

We can create __secondary indexes__ for __DynamoDB__ tables. Always choose DynamoDB when possible.

__Cross-region replication__ can be setup for __Redshift Clusters__.
 
__Redshift encryption__ —
- Using AWS KMS to encrypt the underlying data.
- Using S3 and its encryption.


__EBS volume types__ —
- For throughput, Throughput optimized HDD.
- For large number of transaction, i.e. IOPS, Provisioned IOPS SSD.
 

ASG __Dynamic Scaling Policies__ —
- Target tracking scaling
- Step scaling
- Simple scaling

If you are scaling based on a utilization metric that increases or decreases proportionally to the number of instances in an Auto Scaling group, we recommend that you use target tracking scaling policies. Otherwise, we recommend that you use step scaling policies. 

We can create a __CloudTrail log across all regions__.

__ELB__ can only balance traffic in one region and __not across multiple regions__.

__Multivalue answer routing policy__ responds with upto 8 healthy records selected at __random__.


## Practice Test 2

__RDS data size limits__ —
- Aurora: 64 TB
- Others: 16 TB.

The ELB service does not consume an IP address, it's the nodes that cosume one IP address each.

DynamoDB streams can be used to monitor changes made to a database, and they can trigger lambda functions.

During automated backup, Amazon RDS performs a storage volume snapshot of entire Database instance. Also, it captures transaction logs every 5 minutes.

__AWS EMR__ — AWS Elastic MapReduce, Hadoop based big data analytics.

__Amazon Cognito__ has two __authentication methods__, __independent__ of one another —
- Sign in via third party federation
- Cognito user pools

__AWS RDS is a service__ whereas __AWS Aurora is a database engine__.

__AWS Server Migration Service (SMS)__ is an agentless service which makes it easier and faster for you to migrate thousands of on-premise workloads to AWS.

__KMS__ master keys are region specific.

AWS __VPC Endpoints support S3 and DynamoDB__. For __Amazon ECR__, we have to use __AWS PrivateLink__.

For __Redshift__, spot instances are not an option.

__Auto-scaling__ ensures —
- Fault tolerance
- Availability

__Increasing performance in S3__ —
- If workload is mainly GET requests, integrate Cloudfront with S3.
- If workload consists of PUT requests, use S3 transfer accleration.

With __Amazon SNS__, there is a possibility of the client receiving __duplicate messages__.

__AWS Athena__ is a managed service which can be used to make interactive __search queries to S3 data__. 

