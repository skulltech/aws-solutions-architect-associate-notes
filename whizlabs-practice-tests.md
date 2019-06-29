# Whizlabs Practice Tests

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

## Practice Test 4

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


## Practice Test 5

We can create __event notification in S3__ to __invoke lamdba__ function.

To setup __AWS VPN CloudHub__ —
- Each regional site should have non overlapping IP prefixes.
- BGP ASN should be unique at each site.
- If BGP ASN are not unique, addional ALLOW-INs will be required.

Amazon __Quicksight__ is a managed service for __creating dashboards__ with data visualization.

AWS __Athena pricing__ is based upon per query and amount of data scanned in each query. To __reduce price__ —
- Partition data based on different parameters so that amount of data scanned gets reduced.
- Create separate workgroups based upon user groups.

Increasing __auto-scaling cooldown timer__ value would give scaling activity sufficient time to stabilize.

__AWS CloudSearch__ helps us add search to our website or application. __Like Elasticsearch__.

__AWS Glue__ is a fully __managed ETL service__ for data.  
AWS Glue __keeps a track of processed data using Job Bookmark__. Enabling Job Bookmark will help to __scan only changes since last bookmark__ and prevent processing of whole data again.

__AWS X-Ray__ — Helps debug and __analyze microservices architecture__.

__Reducing cost with AWS X-Ray__ — Sampling at a lower rate.

By default, __EBS volumes are automatically replicated within their availalibilty zone__, and offers a significant high availability.

__Amazon WorkDocs__ has a __poweruser__ facility, which on enabling restricts sharing of documents to that user only.

Each __FIFO Queue__ uses —
- Message Deduplication ID 
- Message Group ID. Message Group ID helps preserve order.

For application with identical message bodies, use unique deduplication ID, while for unique message bodies, use content-based deduplication ID.

__EMR__ can use __spot instances__ as underlying nodes.

We can enable __cross-region replication for Redshift clusters__.

__AWS Cloudwatch Logs__ can be used to monitor and store logs from EC2 instances. The instance needs __awslogs log driver__ installed to be able to send logs to CloudWatch.

__AWS Data Pipeline__ can automate the movement and transformation of data for data-driven workflows.

We configure __RDS engine configurations__ using __parameter groups__.

__Customer managed S3 encryption workflow__ —  
Generate a data key using Customer managed CMK. Encrypt data using data key and delete data key. Store encrypted data key and data in S3 buckets. For decryption, use CMK to decrypt data key into plain text and then decrypt data using plain text data key.

To use __REDIS AUTH with ElastiCache__, __in-transit encryption__ must be enabled for clusters.

__Disaster recovery solutions__ —
- Backup and Restore. Cheapest.
- Pilot Light
- Warm Standby
- Multi-Site
- Multiple AWS Regions

With __AWS Config__, we can get a snapshot of the current configuration of our AWS account.


## Practice Test 6

To automatically trigger __CodePipeline__ with changes in source __S3__ bucket, use __CloudWatch Events rule__ and __CloudTrail trail__.

__Amazon Data Lifecycle Manager__ can be used for creation, retention and deletion of EBS snapshots.

__AWS Direct Connect__ doesn't __encrypt in transit data__, while __VPN__ does.

With __AWS Organizations__, we can centrally manage policies across multiple AWS accounts. With __Service Control Policies (SCPs)__, we can ensure security policies are in place.

__AWS WAF__ is a web application firewall.

To establish a __VPN connection__, we need —
- A public IP address on the customer gateway for the on-premise network.
- A virtual private gateway attached to the VPC.

With __AWS CoudHSM__, we can control the entire lifecycle around the keys.

__Network Load Balancer__ can be used to __terminate TLS connections__. For this, NLB uses a security policy which consists of protocols and ciphers. The certificate used can be provided by __AWS Certificate Manager__.

__Cluster Placement groups__ have very __low inter-note latency__.

In __AWS Managed Blockchain network__. The format for __resource endpoint__ is — `ResourceID.MemberID.NetworkID.managedblockchain.us-east-1.amazonaws.com:PortNumber`.

__Hibernation of EC2 instances__ —
- When EC2 instance is hibernated and brought back up, the public IP4 address is renewed. All the other IP addresses are retained.
- When EC2 instance is in hibernate, you are only charged for elastic IP address and EBS storage space.

## Practice Test 7

__Connecting AWS SSO to On-Premise Active Directory__ —
- __Two-way trust relationship__: __Preferred__. Users can do everything from both portals.
- __AD connector__: SSO does not cache user credentials. Users can't reset password from SSO protal, have to do it from on-premise portal.

For __two-step verification__, SSO sends __code to registered email__. It can set to be either —
- Always-on
- Context-aware

For __queue based processing__, scaling EC2 instances based on the size of the queue is a preferred architecture.

We can turn on __autoscaling for DynamoDB__.

For __write heavy__ use cases in __DynamoDB__, use partition keys with large number of distinct values.

It's best practice to launch Amazon __RDS instance outside an Elastic Beanstalk environment__.

For __Kinesis__, we have to use __VPC Interface Endpoint__, powered by __AWS PrivateLink__.

__AWS Athena is simpler__ and requires less effort to set up __than AWS Quicksight__.

__RI Coverage Budget__ reports number of instances that are part of Reserved Instance. For an organisation using default IAM policy, each member account owner needs to create a budget policy for individual accounts and not by master account.

With __EC2 dedicated hosts__ we have control over __number of cores__, not anywhere else.

__Consolidated Billing__ in AWS Organisations combines usage from all accounts and billing is generated based upon total usage. Services like __EC2 and S3 have volume pricing tiers__ where with more usage volume the overall charge decreases.

Amazon __Kinesis Scaling Utility__ is a __less cost-effective__ solution compared to doing it with __Cloudwatch alarms + API Gateway + Lambda function__.

__Cross-account IAM roles__ allow customers to securely grant access to AWS resources in their account to a third party.

__Port based routing__ is supported by __Application Load Balancer__.

Placement groups —
- Cluster
- Spread. Maximum number of instances in an AZ is 7.
- Partitioned

The __console does not support placement groups__, have to do it from CLI.
