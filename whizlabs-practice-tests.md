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


## Practice Test 3
 
__Encryption of RDS__ — Have to enable it on database creation. Also, not all instance classes support encryption, we have to choose one which supports it.

To enable __multi-region replication of RDS__, we have to use __Read Replicas__. Multi-AZ is not the solution here.

__AWS Directory Service__ options —
- AWS Managed Microsoft AD
- AD Connector
- Simple AD
- Amazon Cloud Directory
- Amazon Cognito

__Elastic Beanstalk__ can be used to host __Docker containers__.

__Difference between DirectConnect and VPN__ — DirectConnect does not involve the Internet, while VPN does.

__Amazon Inspector__ is a security assessment service, which helps improve security and compliance of applications.

__AWS Opsworks__ is a configuration management service for Chef and Puppet. With __Opsworks Stacks__, we can model our application as __a stack containing different layers__.

__ELBs__ can manage traffic within a region and not between regions.

In the __CORS__ configuration, the __exact URLs__ must be added, with the correct protocol, i.e. __http vs https__.

We can configure __IAM policies__ that allows __access to specific tags__.

## Pratice Test 4

__RDS Read Replicas__ are __synced asynchronously__, so it can have __replication lag__.

By default, __CloudTrail logs are encrypted__ using S3 server-side encryption (SSE). We can also choose to encrypt with AWS KMS.

__S3__ does not support `OPTIONS`, `CONNECT` and `TRACE` __methods__. 

__Redshift automated snapshot retention period__ — 1 day to 35 days.

__Amazon ECS for Kubernets (EKS)__ exists, it's a managed service.

__AWS EMR__ is preferred for __processing log files__.

__S3 encryptions__ —
- SSE-S3: Data and master keys managed by S3.
- SSE-C: The user manages the encryption keys.
- SSE-KMS: AWS manages the data key, the user manages the master key.

Changes to __CloudTrail global service event logs__ can only be done via the CLI or the SDKs, not the console.

For __CloudFront query string__ forwarding, the parameter names and values used are __case sensitive__.

__Kinesis stream data retention period__ — 24 hours (default) to 168 hours.

__CloudHSM backup procedure__ — Ephemeral backup key (EBK) is used to encrypt data and Persistent backup key (PBK) is used to encrypt EBK before saving it to an S3 bucket in the same region as that of AWS CloudHSM cluster.

__Weighted routing policy__ is a good fit for __blue-green deployments__.

__AWS Polly__ — Lexicons are specific to a region. For a single text appearing multiple times, we can create alias using multiple Lexicons.

We can't use auto-scaling with __RDS__. To improve __performance__, we should look to __sharding__ instead.

To make sure that S3 objects are only accessible from Cloudfront, create an __Origin Access Identity (OAI) for Cloudfront__ and grant access to the objects to that OAI.

