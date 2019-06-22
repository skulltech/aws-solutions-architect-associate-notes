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
