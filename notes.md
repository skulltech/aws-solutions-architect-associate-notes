## Route53


__Main functions of Route53__ —
1. Register domain names.
2. Route internet traffic to the resources for your domain.
3. Check the health of your resources.

It's not used to _distribute_ traffic.

__CNAME vs ALIAS__ —  

- For routing to S3 bucket // Elastic load balancer use A record with ALIAS.  
- For routing to RDS instance use CNAME with NO ALIAS // without ALIAS.

ALIAS only supports the following services —
- API Gateway
- VPC interface endpoint
- CloudFront distribution
- Elastic Beanstalk environment
- ELB load balancer
- S3 bucket that is configured as a static website
- Another Route 53 record in the same hosted zone


Route53 does not directly log to S3 bucket, we can forward that from Cloudwatch, but can't do it directly.

Types of __Route53 health checks__ —
1. Health checks that monitor an endpoint.
2. Health checks that monitor other health checks.
3. Health checks that monitor Cloudwatch alarms. 

__Multivalue answer routing policy__ responds with upto 8 healthy records selected at __random__.

__Weighted routing policy__ is a good fit for __blue-green deployments__.



## S3

In a newly created S3 bucket, everything // every additional option is turned off by default. Also, no bucket policy exists.

__S3 bucket properties__ are —
1. Versioning
2. Server access logging
3. Static website hosting
4. Object level logging // Essentially CloudTrail
5. Transfer acceleration
6. Events

__Object level properties__—  
Metadata and Storage class are object level properties. All object level properties are
1. Storage class
2. Encryption
3. Metadata
4. Tags
5. Object lock

__DELETE operation__ does not keep a copy unless you have versioning enabled. From the docs
> The DELETE operation removes the null version (if there is one) of an object and inserts a delete marker, which becomes the current version of the object. If there isn't a null version, Amazon S3 does not remove any objects. 

S3 is a __managed service__. It can't be part of a VPC.

__S3 object metadata__—
1. System metadata
2. User-defined metadata

User defined metadatas must start with `x-amz-meta`.

When you enable logging on a bucket, the console both enables logging on the source bucket and adds a grant in the target bucket's access control list (ACL) granting write permission to the Log Delivery Group.

__S3 bucket endpoints formats__ —
1. http://bucket.s3.amazonaws.com
2. http://bucket.s3-aws-region.amazonaws.com
3. http://s3.amazonaws.com/bucket
4. http://s3-aws-region.amazonaws.com/bucket

__Object sizes__ —
S3 can store objects of size 0 bytes to 5 TB.
A single PUT can transfer 5 GB max. For files larger than 100MB, multipart upload is recommended.

__Cross-region replication__ requires that versioning be enabled on both the source bucket and the destination bucket.

__AWS Glacier archive retrieval__ options —
- Expedited: Costly, 1-5 minutes.
- Standard: Default, 3-5 hours.
- Bulk: Cheapest, 5-12 hours.

To increase performance, we can __prefix each object name with a hash key__ along with the current date. But, according to the new S3 performance announcement, this is __not needed anymore__.

__Increasing performance in S3__ —
- If workload is mainly GET requests, integrate Cloudfront with S3.
- If workload consists of PUT requests, use S3 transfer accleration.

In the __CORS__ configuration, the __exact URLs__ must be added, with the correct protocol, i.e. __http vs https__.

__S3__ does not support `OPTIONS`, `CONNECT` and `TRACE` __methods__. 

__S3 encryptions__ —
- SSE-S3: Data and master keys managed by S3.
- SSE-C: The user manages the encryption keys.
- SSE-KMS: AWS manages the data key, the user manages the master key.

To make sure that S3 objects are only accessible from Cloudfront, create an __Origin Access Identity (OAI) for Cloudfront__ and grant access to the objects to that OAI.

We can create __event notification in S3__ to __invoke lamdba__ function.

__Customer managed S3 encryption workflow__ —  
Generate a data key using Customer managed CMK. Encrypt data using data key and delete data key. Store encrypted data key and data in S3 buckets. For decryption, use CMK to decrypt data key into plain text and then decrypt data using plain text data key.



## RDS, Redshift and ElastiCache

Amazon __Redshift Enhanced VPC Routing__ provides VPC resources the access to Redshift.

Amazon __ElastiCache__ offers fully managed __Redis and Memcached__. 

__Cross-region replication__ can be setup for __Redshift Clusters__.

__Redshift encryption__ —
- Using AWS KMS to encrypt the underlying data.
- Using S3 and its encryption.

__RDS data size limits__ —
- Aurora: 64 TB
- Others: 16 TB.

During automated backup, Amazon RDS performs a storage volume snapshot of entire Database instance. Also, it captures transaction logs every 5 minutes.

__AWS RDS is a service__ whereas __AWS Aurora is a database engine__.

For __Redshift__, spot instances are not an option.

__Encryption of RDS__ — Have to enable it on database creation. Also, not all instance classes support encryption, we have to choose one which supports it.

To enable __multi-region replication of RDS__, we have to use __Read Replicas__. Multi-AZ is not the solution here.

__RDS Read Replicas__ are __synced asynchronously__, so it can have __replication lag__.

__Redshift automated snapshot retention period__ — 1 day to 35 days.

We can't use auto-scaling with __RDS__. To improve __performance__, we should look to __sharding__ instead.

We configure __RDS engine configurations__ using __parameter groups__.

To use __REDIS AUTH with ElastiCache__, __in-transit encryption__ must be enabled for clusters.




## EC2 and EBS

__Instance store__ —
You cannot add instance store volume to an instance after it's launched.
Not all EC2 instance types support instance store volume.

Persistence — Instance store persists during reboots, but not stop or terminate. EBS volumes however persists accross reboot, stop, and terminate.

__EBS volume types__ —
1. General purpose SSD. For web applications // most use cases.
2. Provisioned IOPS SSD. For critical high performing databases.
3. Throughput optimized HDD. For Big Data.

Also, to note, __HDDs cannot be boot volumes__.

We can use Amazon __Data Lifecycle Manager__ to automate taking backups // snapshots of EBS volumes, and protect them from accidental or unwanted deletion.

__EBS-optimized EC2 instances__ provide additional, dedicated capacity for EBS IO. Helps squeeze out the last ounce of performance.

Encrypted EBS volumes are not supported on all instance types.

__To get more performance out of EBS volumes__ —
1. Use a more modern Linux Kernel.
2. Use RAID 0.

VolumeRemainingSize is not an Cloudwatch metric for EBS volumes.

__EBS volume types__ —
- For throughput, Throughput optimized HDD.
- For large number of transaction, i.e. IOPS, Provisioned IOPS SSD.

By default, __EBS volumes are automatically replicated within their availalibilty zone__, and offers a significant high availability.

__AWS Cloudwatch Logs__ can be used to monitor and store logs from EC2 instances. The instance needs __awslogs log driver__ installed to be able to send logs to CloudWatch.

With __EC2 dedicated hosts__ we have control over __number of cores__, not anywhere else.

Placement groups —
- Cluster
- Spread. Maximum number of instances in an AZ is 7.
- Partitioned

The __console does not support placement groups__, have to do it from CLI.

__Cluster Placement groups__ have very __low inter-note latency__.


__Hibernation of EC2 instances__ —
- When EC2 instance is hibernated and brought back up, the public IP4 address is renewed. All the other IP addresses are retained.
- When EC2 instance is in hibernate, you are only charged for elastic IP address and EBS storage space.



## EFS

EFS supports cross availability zone mounting, but it is not recommended. The recommended approach is __creating a mount point in each availability zone__.

You can mount an EFS file system in only one VPC at a time. If you want to access it // mount it from another VPC, you have to create a __VPC peering connection__. You should note that all of these must be within the same region.

__NFS port 2049__ for EFS.

__Encryption__

1. Encryption at rest must be specified at the creation of file system. If you want to modify it later on, create a new EFS file system with encryption enabled and copy the data over.
2. Encryption at transit is supported by EFS // NFS, and must be enabled from the client side. It simply uses SSL to encrypt the connection.

__Performance mode__

1. General purpose must be used for most purposes, it has low latency, so ideal for web applications.
2. Max IO is ideal for big data and parallel connection and processing from a large number of hosts. It has higher latency but large throughput.

__Throughput mode__

1. Bursting is ideal for arbitrary large amount of data, because it scales properly.
2. But for cases with high throughput to storage ratio, such as common in web applications, provisioned mode is better.



## ELB and Autoscaling

__Patching an AMI for an auto scaling group__, the procedure is —  
1. Create an image out of the main patched EC2 instance
2. Create a new launch configuration with new AMI ID
3. Update auto scaling group with new launch configuration ID. 

Note that AMI ID is set during creation of launch configuration and cannot be modified, so we have to create a new launch configuration.

__Default metric types for a load balancer__ —
1. Request count per target.
2. Average CPU utlization.
3. Network in.
4. Network out.


__Monitoring Application Load Balancers__ —
1. Cloudwatch metrics
2. Access logs
3. Request tracing
4. Cloudtrail logs.

Adding __lifecycle hooks__ to ASGs put instances in __wait state__ before termination. During this wait state, we can perform custom activities. Default wait period is 1 hour.


ASG __Dynamic Scaling Policies__ —
- Target tracking scaling
- Step scaling
- Simple scaling

If you are scaling based on a utilization metric that increases or decreases proportionally to the number of instances in an Auto Scaling group, we recommend that you use target tracking scaling policies. Otherwise, we recommend that you use step scaling policies. 

__ELB__ can only balance traffic in one region and __not across multiple regions__.

The ELB service does not consume an IP address, it's the nodes that cosume one IP address each.

__Auto-scaling__ ensures —
- Fault tolerance
- Availability

__ELBs__ can manage traffic within a region and not between regions.

Increasing __auto-scaling cooldown timer__ value would give scaling activity sufficient time to stabilize.

__Port based routing__ is supported by __Application Load Balancer__.

__Network Load Balancer__ can be used to __terminate TLS connections__. For this, NLB uses a security policy which consists of protocols and ciphers. The certificate used can be provided by __AWS Certificate Manager__.




## SQS

Consumers must __delete an SQS message__ manually after it has done processing the message. To delete a message, use the ReceiptHandle of a message, not the MessageId.

Incoming messages can __trigger a lambda function__.

We can use __dead letter queues__ to isolate messages that can't be processed right now.

SQS does not __encrypt__ messages by default.

Default __visibility timeout__ for SQS is __30 seconds__.

Each __FIFO Queue__ uses —
- Message Deduplication ID 
- Message Group ID. Message Group ID helps preserve order.

For application with identical message bodies, use unique deduplication ID, while for unique message bodies, use content-based deduplication ID.



## SNS

__Available protocols for AWS SNS__ —
- HTTP // HTTPS
- Email
- Email-JSON
- SQS
- Application
- Lambda
- SMS

We can add __filter policies__ to individual subscribers in an SNS topic.

__SNS message attributes__ are —
- Name
- Type
- Value

With __Amazon SNS__, there is a possibility of the client receiving __duplicate messages__.




## API Gateway

API Gateway can __integrate with any HTTP based operations__ available on the public internet, as well as other AWS services.

__Integration types__ —
- Lambda function, can be from __another AWS account__ as well.
- HTTP
- Mock
- AWS Service
- VPC Link

For connecting API Gateway to a set of services hosted in an __on-premise network__, we can use
1. __DirectConnect__ to connect the private network to AWS directly.
2. Then use __VPCLink__ to set up API Gateway connection.


__API Gateway Throttling__ —

- __Burst limit__ refers to the first milisecond.
- __Steady-state limit__ refers to an one second interval.

__Throtting behaviors__ —
- If an user exceeds the burst limit but not the steady-state limit, the rest of the requests are throttled over the one second steady-state interval. 
- If an user exceeds the steady-state limit, AWS returns `429 Too Many Requests` error.

When it comes to throttling settings, you can __override stage settings on an individual method__ within the stage. That is, there is an option for method level throttling to override stage level throttling.

__Acess control mechanisms__ for API Gateway —
- Resource policies
- AWS IAM roles and policies
- CORS or Cross-origin resource sharing
- Lambda authorizers
- Amazon Cognito user pools
- Client side SSL certs
- Usage plans

API Gateway __automatically protects the backend systems from DDoS__ attack.

__Cache properties and settings__ —
- Cache status
- Flush entire cache
- Enable API cache
- Cache capacity
- Encrypt cache data
- Cache TTL
- Require authorization
- Handle unauthorized requests

__Monitoring__ API Gateway usage — we can use __CloudWatch__ or __Access logging__. Access logging logs who accessed the API and how the caller accessed the API, CloudWatch does not include this data.




## Lambda

Lamdba functions __can be run within a private VPC__.

### Event sources

Lambda can __read events from__ —
- Amazon Kinesis
- Amazon DynamoDB
- Amazon Simple Queue Service

Services that can __invoke Lambda functions__ —
- Elastic Load Balancing (Application Load Balancer)
- Amazon Cognito
- Amazon Lex
- Amazon Alexa
- Amazon API Gateway
- Amazon CloudFront (Lambda@Edge)
- Amazon Kinesis Data Firehose
- Amazon Simple Storage Service
- Amazon Simple Notification Service
- Amazon Simple Email Service
- AWS CloudFormation
- Amazon CloudWatch Logs
- Amazon CloudWatch Events
- AWS CodeCommit
- AWS Config

AWS __CodePipeline__ and AWS __OpsWorks can't invoke lambda__ functions.

__For failures__ we can configure lambda to send non-processed payloads to __SQS Dead letter queue__. Then we can configure __SNS to send a notification__ if we want. Lambda __does not have an in-built mechanism__ for notification upon failure.

A policy on a role defines which API actions can be made on the target, it does not define whether the source can access the target or not.

Each lambda function has an __ephemeral storage of 512 MB__ in the `tmp` directory.  
Both the default and maximum batch size for `ReceiveMessage` call of SQS is 10.

AWS __CloudWatch rule__ can be configured to trigger a lambda function. While configuration, the following can be used as __input to the target lambda function__ —
- Matched event
- Part of the matched event
- Constant (JSON text)

The following __CloudFront events can trigger lambda function__ —
- Viewer request
- Viewer response
- Origin request
- Origin response

__Lambda function update has eventual consistency__. Which means, for a brief window of less than a minute, it may execute either the old version or the new version.

We can use __alias versions__ to point to another version. This can enable easier upgradation from the viewpoint of a consumer.

__Limits__ —
- Function memory allocation: 128 MB to 3008 MB, in 64 MB increments.
- Function timeout: 900 seconds.
- Deployment package: 50 MB * 5 layers.
- `tmp` directory storage: 512 MB.

To grant __cross-account permission to a function__, we have to modify the function policy, not the execution role policy.

The console doesn't support directly __modifying permissions in a function policy__. You have to do it from the CLI or SDK.

__ENI capacity__ = Projected peak concurrent executions * (Memory in GB / 3 GB).

The __lambda console__ provides __encryption and decryption helpers__ for encryption of environment variables.

__CloudWatch metrics for Lambda__ —
- Invocations
- Errors
- Dead Letter Error
- Duration
- Throttles
- IteratorAge
- ConcurrentExecutions
- UnreservedConcurrentExecutions

We can get the __function version__ within the function using —
- `getFunctionVersion` from the Context object.
- `AWS_LAMBDA_FUNCTION_VERSION` environment variable. 

__Lambda Retry upon Failure Behavior__ —
- Event sources that aren't stream-based
    - Synchronous invocation — Returns error with __status code 200__. Includes __FunctionError__ field and __X-Amz-Function-Error__ header.
    - Asynchronous invocation — __Retry twice__, then sent to __Dead Letter Queue__.
- Poll-based and stream-based event source (Kinesis or DynamoDB) — Lambda keeps __retrying until the data expires__. The exception is __blocking__, this ensures the data are processed in order.
- Poll-based but not stream-based event source (SQS) — On unsuccesful processing or if the function times out of the message, it is __returned to the queue__, and ready for further reprocessing after the visibility timeout period. If the function errors out, it is sent to __Dead Letter Queue__.




## VPC

We cannot route traffic to a __NAT gateway__ or __VPC gateway__ endpoints through a __VPC peering__ connection, a __VPN connection__, or __AWS Direct Connect__. A NAT gateway or VPC gateway endpoints cannot be used by resources on the other side of these connections. Conversely, a NAT gateway // VPC gateway endpoints cannot send traffic over VPC endpoints, AWS VPN connections, Direct Connect or VPC Peering connections either.

Every route table contains a __local route__ for communication within the VPC over IPv4. We __cannot modify or delete__ these routes.

__VPC Endpoints always take precedence__ over NAT Gateways or Internet Gateways. 

Network ACL __rules are evaluated in order__, starting with the lowest numbered rule. As soon as a rule matches, it is applied regardless of any higher numbered rule that may contradict it.

SSH connections are between port 22 of the host and __an ephemeral port of the client__. In fact, this is true for any TCP service.

Security groups are __stateful__, this means any connection initiated successfully will be completed.

We can create __S3 proxy server__ for enabling use cases where S3 has to be accessed privately through VPN connection, AWS Direct Connect or VPC peering.

AWS __reserves 5 IPs for every subnet__, not for every VPC.

Instances in __custom VPCs don't get public DNS hosts by default__, we have to set the `enableDnsHostnames` attribute to true. The `enableDnsSupport` is to be set to true too, but that is done by default.

We can set a __custom route table as the main route table__.

We can add __secondary CIDR ranges__ to an existing VPC. When a secondary CIDR block is added to a VPC, a route for that block with target as "local" is automatically added to the route table.

__VPC peering__ connection route contains Target as `pcx-xxxxxx`.
__VPN connection__ // __Direct Connect__ connection route contains Target as `vgw-xxxxxx`.

__VPN__ is established over a __Virtual Private Gateway__.

AWS __VPC Endpoints support S3 and DynamoDB__. For __Amazon ECR__, we have to use __AWS PrivateLink__.

__Difference between DirectConnect and VPN__ — DirectConnect does not involve the Internet, while VPN does.

__AWS Direct Connect__ doesn't __encrypt in transit data__, while __VPN__ does.

To establish a __VPN connection__, we need —
- A public IP address on the customer gateway for the on-premise network.
- A virtual private gateway attached to the VPC.

To setup __AWS VPN CloudHub__ —

- Each regional site should have non overlapping IP prefixes.
- BGP ASN should be unique at each site.
- If BGP ASN are not unique, addional ALLOW-INs will be required.



## DynamoDB

AWS __DynamoDB__ is durable, ACID compliant, can go through multiple schema changes, and changes to the database does not result in any database downtime.

__DynamoDB Global Tables__ can be used to deploy a multi region, multi AZ, fully managed database solution.

We can create __secondary indexes__ for __DynamoDB__ tables. Always choose DynamoDB when possible.

DynamoDB streams can be used to monitor changes made to a database, and they can trigger lambda functions.

We can turn on __autoscaling for DynamoDB__.

For __write heavy__ use cases in __DynamoDB__, use partition keys with large number of distinct values.



## STS

The __policy of the temporary credentials__ generated by STS are defined by the intersection of your IAM user policies and the policy that you pass as argument.



## ECS

Launch types —

- Fargate
- EC2



## Elastic Beanstalk

AWS __Elastic Beanstalk__ can be used to create —

- Web application using DB
- Long running worker process
- Static website

__Elastic Beanstalk__ can be used to host __Docker containers__.



## Storage Gateway

__AWS Storage Gateways__—

1. File gateway
2. Volume gateway: Cached volumes
3. Volume gateway: Stored volumes



## IAM, Cognito and Directory Services

__Amazon Cognito__ has two __authentication methods__, __independent__ of one another —

- Sign in via third party federation
- Cognito user pools

__AWS Directory Service__ options —

- AWS Managed Microsoft AD
- AD Connector
- Simple AD
- Amazon Cloud Directory
- Amazon Cognito

There is no __default policy__ ever, anywhere. When permissions are checked, roles and policies are considered together, and in the default case there is no policy, so only the role is considered.

We can configure __IAM policies__ that allows __access to specific tags__.

__Connecting AWS SSO to On-Premise Active Directory__ —

- __Two-way trust relationship__: __Preferred__. Users can do everything from both portals.
- __AD connector__: SSO does not cache user credentials. Users can't reset password from SSO protal, have to do it from on-premise portal.

For __two-step verification__, SSO sends __code to registered email__. It can set to be either —

- Always-on
- Context-aware

__Cross-account IAM roles__ allow customers to securely grant access to AWS resources in their account to a third party.



## KMS and CloudHSM

__KMS__ master keys are region specific.

__Cross-account IAM roles__ allow customers to securely grant access to AWS resources in their account to a third party.

__CloudHSM backup procedure__ — Ephemeral backup key (EBK) is used to encrypt data and Persistent backup key (PBK) is used to encrypt EBK before saving it to an S3 bucket in the same region as that of AWS CloudHSM cluster.

With __AWS CoudHSM__, we can control the entire lifecycle around the keys.



## Misc

AWS __VM Import__ // Export can be used to transfer virtual machines from local infrastructure to AWS and vice-versa.

AWS __Trusted Advisor__ is a resource that helps users with cost management, performance and security.

We can create a __CloudTrail log across all regions__.

__AWS EMR__ — AWS Elastic MapReduce, Hadoop based big data analytics.

__AWS EMR__ is preferred for __processing log files__.

__EMR__ can use __spot instances__ as underlying nodes.

__CloudFormation Drift Detection__ can be used to detect changes in the environment. Drift Detection only __checks property values which are explicitly set__ by stack templates or by specifying template parameters. It does not determine drift for property values which are set by default.

__AWS Server Migration Service (SMS)__ is an agentless service which makes it easier and faster for you to migrate thousands of on-premise workloads to AWS.

__AWS Athena__ is a managed service which can be used to make interactive __search queries to S3 data__.

__Amazon Inspector__ is a security assessment service, which helps improve security and compliance of applications.

__AWS Opsworks__ is a configuration management service for Chef and Puppet. With __Opsworks Stacks__, we can model our application as __a stack containing different layers__.

By default, __CloudTrail logs are encrypted__ using S3 server-side encryption (SSE). We can also choose to encrypt with AWS KMS.

__Amazon ECS for Kubernets (EKS)__ exists, it's a managed service.

Changes to __CloudTrail global service event logs__ can only be done via the CLI or the SDKs, not the console.

For __CloudFront query string__ forwarding, the parameter names and values used are __case sensitive__.

__Kinesis stream data retention period__ — 24 hours (default) to 168 hours.

__AWS Polly__ — Lexicons are specific to a region. For a single text appearing multiple times, we can create alias using multiple Lexicons.

Amazon __Quicksight__ is a managed service for __creating dashboards__ with data visualization.

AWS __Athena pricing__ is based upon per query and amount of data scanned in each query. To __reduce price__ —
- Partition data based on different parameters so that amount of data scanned gets reduced.
- Create separate workgroups based upon user groups.


__AWS CloudSearch__ helps us add search to our website or application. __Like Elasticsearch__.

__AWS Glue__ is a fully __managed ETL service__ for data. It __keeps a track of processed data using Job Bookmark__. Enabling Job Bookmark will help to __scan only changes since last bookmark__ and prevent processing of whole data again.

__AWS X-Ray__ — Helps debug and __analyze microservices architecture__.

__Reducing cost with AWS X-Ray__ — Sampling at a lower rate.

__Amazon WorkDocs__ has a __poweruser__ facility, which on enabling restricts sharing of documents to that user only.

__AWS Data Pipeline__ can automate the movement and transformation of data for data-driven workflows.


__Disaster recovery solutions__ —
- Backup and Restore. Cheapest.
- Pilot Light
- Warm Standby
- Multi-Site
- Multiple AWS Regions

With __AWS Config__, we can get a snapshot of the current configuration of our AWS account.

For __queue based processing__, scaling EC2 instances based on the size of the queue is a preferred architecture.

It's best practice to launch Amazon __RDS instance outside an Elastic Beanstalk environment__.

For __Kinesis__, we have to use __VPC Interface Endpoint__, powered by __AWS PrivateLink__.

Amazon __Kinesis Scaling Utility__ is a __less cost-effective__ solution compared to doing it with __Cloudwatch alarms + API Gateway + Lambda function__.

__AWS Athena is simpler__ and requires less effort to set up __than AWS Quicksight__.

__RI Coverage Budget__ reports number of instances that are part of Reserved Instance. For an organisation using default IAM policy, each member account owner needs to create a budget policy for individual accounts and not by master account.

__Consolidated Billing__ in AWS Organisations combines usage from all accounts and billing is generated based upon total usage. Services like __EC2 and S3 have volume pricing tiers__ where with more usage volume the overall charge decreases.

To automatically trigger __CodePipeline__ with changes in source __S3__ bucket, use __CloudWatch Events rule__ and __CloudTrail trail__.

__Amazon Data Lifecycle Manager__ can be used for creation, retention and deletion of EBS snapshots.

With __AWS Organizations__, we can centrally manage policies across multiple AWS accounts. With __Service Control Policies (SCPs)__, we can ensure security policies are in place.

__AWS WAF__ is a web application firewall.

In __AWS Managed Blockchain network__. The format for __resource endpoint__ is — `ResourceID.MemberID.NetworkID.managedblockchain.us-east-1.amazonaws.com:PortNumber`.

