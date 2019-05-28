ROUTE53
.......


Main functions of Route53.
1. Register domain names
2. Route internet traffic to the resources for your domain
3. Check the health of your resources

It's not used to "distribute" traffic.


For routing to S3 bucket // Elastic load balancer: A record with ALIAS.
For routing to RDS instance: CNAME with ALIAS NO // without ALIAS.

ALIAS only supports the following services.
    API Gateway
    VPC interface endpoint
    CloudFront distribution
    Elastic Beanstalk environment
    ELB load balancer
    S3 bucket that is configured as a static website
    Another Route 53 record in the same hosted zone



Route53 does not directly log to S3 bucket, we can forward that from Cloudwatch, but can't do it directly.


Types of Route53 health checks.
1. Health checks that monitor an endpoint.
2. Health checks that monitor other health checks.
3. Health checks that monitor Cloudwatch alarms. 



S3
..


In a newly created S3 bucket, everything // every additional option is turned off by default. Also, no bucket policy exists.

S3 bucket properties are
1. Versioning
2. Server access logging
3. Static website hosting
4. Object level logging // Essentially CloudTrail
5. Transfer acceleration
6. Events

* Metadata and Storage class are object level properties.
Object level properties are
1. Storage class
2. Encryption
3. Metadata
4. Tags
5. Object lock

DELETE operation does not keep a copy unless you have versioning enabled. From the docs ...
The DELETE operation removes the null version (if there is one) of an object and inserts a delete marker, which becomes the current version of the object. If there isn't a null version, Amazon S3 does not remove any objects. 

* AWS Storage Gateways
1. File gateway
2. Volume gateway: Cached volumes
3. Volume gateway: Stored volumes


There is no default policy ever, anywhere. When permissions are checked, roles and policies are considered together, and in the default case there is no policy, so only the role is considered.

S3 is a managed service. It can't be part of a VPC.

S3 object metadatas...
1. System metadata
2. User-defined metadata

User defined metadatas must start with "x-amz-meta".

When you enable logging on a bucket, the console both enables logging on the source bucket and adds a grant in the target bucket's access control list (ACL) granting write permission to the Log Delivery Group.

S3 bucket endpoints formats
1. http://bucket.s3.amazonaws.com
2. http://bucket.s3-aws-region.amazonaws.com
3. http://s3.amazonaws.com/bucket
4. http://s3-aws-region.amazonaws.com/bucket

S3 can store objects of size: 0 bytes to 5 TB.
A single PUT can transfer 5 GB max. For files larger than 100MB, multipart upload is recommended.

Cross-region replication requires that versioning be enabled on both the source bucket and the destination bucket.


EFS
...

EFS supports cross availability zone mounting, but it is not recommended. The recommended approach is creating a mount point in each availability zone.

You can mount an EFS file system in only one VPC at a time. If you want to access it // mount it from another VPC, you have to create a VPC peering connection. You should note that all of these must be within the same region.

NFS port 2049 for EFS.

Encryption:
1. Encryption at rest must be specified at the creation of file system. If you want to modify it later on, create a new EFS file system with encryption enabled and copy the data over.
2. Encryption at transit is supported by EFS // NFS, and must be enabled from the client side. It simply uses SSL to encrypt the connection.

Performance mode:
1. General purpose must be used for most purposes, it has low latency, so ideal for web applications.
2. Max IO is ideal for big data and parallel connection and processing from a large number of hosts. It has higher latency but large throughput.

Throughput mode:
1. Bursting is ideal for arbitrary large amount of data, because it scales properly.
2. But for cases with high throughput to storage ratio, such as common in web applications, provisioned mode is better.


EBS
...


You cannot add instance store volume to an instance after it's launched.
Not all EC2 instance types support instance store volume.

Persistence: Instance store persists during reboots, but not stop or terminate. EBS volumes however persists accross reboot, stop, and terminate.

EBs volume types...

1. General purpose SSD. For web applications // most use cases.
2. Provisioned IOPS SSD. For critical high performing databases.
3. Throughput optimized HDD. For Big Data.

Also, to note, HDDs cannot be boot volumes.

We can use Amazon Data Lifecycle Manager to automate taking backups // snapshots of EBS volumes, and protect them from accidental or unwanted deletion.

EBS-optimized EC2 instances provide additional, dedicated capacity for EBS IO. Helps squeeze out the last ounce of performance.

Encrypted EBS volumes are not supported on all instance types.

To get more performance out of EBS volumes
1. Use a more modern Linux Kernel.
2. Use RAID 0.

VolumeRemainingSize is not an Cloudwatch metric for EBS volumes.


ELB and Autoscaling
...................


Patching // updating an AMI for an auto scaling group, the procedure is: Create an image out of the main patched EC2 instance, create a new launch configuration with new AMI ID, update auto scaling group with new launch configuration ID. 

Note that AMI ID is set during creation of launch configuration and cannot be modified, so we have to create a new launch configuration.

Default metric types for a load balancer are...
1. Request count per target.
2. Average CPU utlization.
3. Network in.
4. Network out.


Monitoring Application Load Balancers...
1. Cloudwatch metrics
2. Access logs
3. Request tracing
4. Cloudtrail logs.