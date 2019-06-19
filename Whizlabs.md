## ROUTE53


__Main functions of Route53__ —
1. Register domain names.
2. Route internet traffic to the resources for your domain.
3. Check the health of your resources.

It's not used to _distribute_ traffic.

__CNAME vs ALIAS__ —  
For routing to S3 bucket // Elastic load balancer use A record with ALIAS.  
For routing to RDS instance use CNAME with NO ALIAS // without ALIAS.

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

__AWS Storage Gateways__—
1. File gateway
2. Volume gateway: Cached volumes
3. Volume gateway: Stored volumes


There is no __default policy__ ever, anywhere. When permissions are checked, roles and policies are considered together, and in the default case there is no policy, so only the role is considered.

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


## EBS

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


## ELB and Autoscaling

__Patching an AMI for an auto scaling group__, the procedure is —  
1. Create an image out of the main patched EC2 instance
2. Create a new launch configuration with new AMI ID
3. Update auto scaling group with new launch configuration ID. 

Note that AMI ID is set during creation of launch configuration and cannot be modified, so we have to create a new launch configuration.

__Default metric types for a load balancer__ are —
1. Request count per target.
2. Average CPU utlization.
3. Network in.
4. Network out.


__Monitoring Application Load Balancers__ —
1. Cloudwatch metrics
2. Access logs
3. Request tracing
4. Cloudtrail logs.


## SQS

Consumers must __delete an SQS message__ manually after it has done processing the message. To delete a message, use the ReceiptHandle of a message, not the MessageId.

Incoming messages can __trigger a lambda function__.

We can use __dead letter queues__ to isolate messages that can't be processed right now.

SQS does not __encrypt__ messages by default.

## STS

The __policy of the temporary credentials__ generated by STS are defined by the intersection of your IAM user policies and the policy that you pass as argument.

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

To grant _cross-account permission to a function__, we have to modify the function policy, not the execution role policy.

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
