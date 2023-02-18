# Week 0 - Homework

# Setting a Billing Alarm → Hard Assignment

I have successfully enabled billing alerts within the AWS Billing and Cost Management Console, this utilizes CloudWatch to collect comprehensive billing data for my AWS account and services. I have created a billing alarm in the CloudWatch console, specifying a custom threshold limit that aligns with my requirements. This alarm is connected to an Amazon SNS topic, allowing me to receive prompt email notifications and effectively track my AWS spending costs. In addition, the billing alerts feature keeps me informed of any usage exceeding the Free tier, facilitating ease of expense management.

Although using CloudWatch for billing alerts is considered a legacy option in AWS (in favour of Budgets), I have taken the initiative to configure both services for added redundancy. By utilizing billing alerts and Budgets, I ensure that I have multiple sources of information on my AWS costs and usage, reducing the risk of relying solely on a single service for this critical data. In addition, this approach enhances the clarity and reliability of my cost monitoring within AWS.

Below are the screenshots of the steps I took to configure a $10 dollar billing alarm using cloud watch.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%201.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%202.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%203.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%204.png)

# Setting an AWS budget → Hard Assignment

I have developed a comprehensive set of budget plans for my AWS workspace, which includes a zero-expenditure budget, a $5 budget, a $10 budget, and a $100 budget. These budgets serve as guidelines to keep me informed of my spending habits and provide a clear understanding of my expected monthly billing.

While the budgets are not strictly enforced, they are a useful tool to monitor my AWS account usage and stay informed of any unexpected spikes in spending. In order to maximize my visibility into my spending, I have implemented multiple alerting mechanisms for each budget. These include an alarm when actual spending exceeds 85% of the budget, an alarm when the forecasted spend exceeds 100% of the budget, and an alert to notify me once I have surpassed 100% of the budget.

To optimize my visibility into my spending, I have configured the budgets to send email notifcaitons to my personal email address so that I am kept up-to-date with infromation on my spending, ensuring that I am promptly alerted to any changes in my budgest. This poractice aporach helps me stay informed and amke infrormed decisions that allign with my budgeting goals.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%205.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%206.png)

# Using AWS CLI → Stretch

## Creating Budgets using AWS CLI

The previous sections describe how I set up Billing alerts and budgets in my AWS account. I gained a better understanding of both services by using them hands-on. I also followed the same steps using the AWS CLI, with some changes in options. In the next sections, I'll show you how I created a $50 budget in AWS and a Billing Alarm in CloudWatch to keep an eye on my spending.

Code snippet of `JSON` files.

```json
{
  "BudgetLimit": {
      "Amount": "50",
      "Unit": "USD"
  },
  "BudgetName": "50 Dollar Budget",
  "BudgetType": "COST",
  "CostTypes": {
      "IncludeCredit": true,
      "IncludeDiscount": true,
      "IncludeOtherSubscription": true,
      "IncludeRecurring": true,
      "IncludeRefund": true,
      "IncludeSubscription": true,
      "IncludeSupport": true,
      "IncludeTax": true,
      "IncludeUpfront": true,
      "UseBlended": false
  },
  "TimePeriod": {
      "Start": 1477958399,
      "End": 3706473600
  },
  "TimeUnit": "MONTHLY"
}
```

```json
[
  {
      "Notification": {
          "ComparisonOperator": "GREATER_THAN",
          "NotificationType": "ACTUAL",
          "Threshold": 80,
          "ThresholdType": "PERCENTAGE"
      },
      "Subscribers": [
          {
              "Address": "kamran.abid.c@gmail.com",
              "SubscriptionType": "EMAIL"
          }
      ]
  }
]
```

I created the budget using the above `JSON` files and the below command.

```bash
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ aws budgets create-budget --account-id $AWS_ACCOUNT_ID --budget file://aws/json/budget.json --notifications-with-subscribers file://aws/json/budget-notification.json
```

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%207.png)

## Creating Alarms

The following screenshots and code snippets show how I have used the AWS CLI to create a billing alarm using CloudWatch metrics. This approach is now considered the legacy method of billing metrics and the screenshots and code above using AWS budgets is the recommended method by AWS. However, I found using both methods to be a great way of enhancing my knowledge and understanding of cost management in AWS and therefore I chose to use both methods.

```bash
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ aws sns create-topic --name billing-alarm
{
    "TopicArn": "arn:aws:sns:eu-west-2:287280928033:billing-alarm"
}
```

```bash
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ aws sns subscribe \
>     --topic-arn "arn:aws:sns:eu-west-2:287280928033:billing-alarm" \
>     --protocol email \
>     --notification-endpoint "kamran.abid.c@gmail.com"
{
    "SubscriptionArn": "pending confirmation"
}
```

```bash
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ aws cloudwatch put-metric-alarm --cli-input-json file://aws/json/alarm.config.json
```

```bash
{
  "AlarmName": "DailyEstimatedCharges",
  "AlarmDescription": "This alarm would be triggered if the daily estimated charges exceeds 1$",
  "ActionsEnabled": true,
  "AlarmActions": [
      "arn:aws:sns:eu-west-2:$ACCOUNT_ID:billing-alarm"
  ],
  "EvaluationPeriods": 1,
  "DatapointsToAlarm": 1,
  "Threshold": 1,
  "ComparisonOperator": "GreaterThanOrEqualToThreshold",
  "TreatMissingData": "breaching",
  "Metrics": [{
      "Id": "m1",
      "MetricStat": {
          "Metric": {
              "Namespace": "AWS/Billing",
              "MetricName": "EstimatedCharges",
              "Dimensions": [{
                  "Name": "Currency",
                  "Value": "USD"
              }]
          },
          "Period": 86400,
          "Stat": "Maximum"
      },
      "ReturnData": false
  },
  {
      "Id": "e1",
      "Expression": "IF(RATE(m1)>0,RATE(m1)*86400,0)",
      "Label": "DailyEstimatedCharges",
      "ReturnData": true
  }]
}
```

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%208.png)

# Generating AWS Credentials → Hard Assignment

As part of my AWS account management tasks, I created a new IAM user called **`GitPodUser`**. I will use this user and their associated credentials to authenticate myself to GitPod. Since I am managing authentication to multiple AWS accounts through the AWS Identity Center, I did not create a user for myself. 

To simplify user permissions management, I created a new user group called **`Admins`** and assigned the **`administrator access`** policy to the group. This policy will allow all users who are part of the **`Admins`** group to inherit the group's permissions. I then added the **`GitPodUser`** to the **`Admins`** group, which granted the user admin access by inheriting the group's permissions.

This approach ensures that user permissions are managed effectively and efficiently, providing a streamlined process for adding and removing users and granting permissions. With this setup, I can easily manage user access to my AWS resources and securely authenticate myself to GitPod using the **`GitPodUser`** IAM user."

Enable MFA → Enabled MFA for our GitPod IAM User

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%209.png)

Then get the AWS CLI credentials → Access keys to authenticate when using GitPod

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2010.png)

Then authenticate to GitPod and show that here

Used the command `gp env AWS_CRED_HERE=<creds>` to persist my credentials. I also copied the gitpod.yml configuration to ensure that I can have the AWS CLI ready for me each time I open GitPod.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2011.png)

# Using Cloud Shell → Hard Assignment

AWS CloudShell is a feature that provides an interactive, browser-based shell environment for administering AWS services. The shell environment is built into the AWS Management Console and comes pre-installed with the AWS Command Line Interface (AWS CLI). This feature allows for convenient and efficient execution of commands directly from within the console, as it automatically authenticates as the current user. The following is an example of how you might use AWS CloudShell to run a simple command.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2012.png)

# Conceptual Architecture Diagarm or you Napkins → Hard Assignment

## Conceptual Diagram

Conceptual diagram with labels - [https://lucid.app/lucidchart/833d468a-7171-4129-a5e9-cbb9f58c3697/edit?invitationId=inv_b6bb36f4-ac26-4ea5-9c90-e56db85a5394](https://lucid.app/lucidchart/833d468a-7171-4129-a5e9-cbb9f58c3697/edit?invitationId=inv_b6bb36f4-ac26-4ea5-9c90-e56db85a5394)

The following diagram represents the conceptual design for the Cruddur application. As a high-level illustration, I have employed a red barrier to indicate areas accessible only to authenticated users and a green barrier to represent sections restricted to internal employees, including databases and backend systems. To accommodate public API access, users have the option to authenticate either through their username and password or API keys. The diagram also depicts several security features, including a firewall, which can be achieved through the use of AWS Shield, a service offering protection against both layer 3 and layer 4 Distributed Denial of Service (DDoS) attacks.

Labeling has been incorporated into the diagram to enhance its readability. Although the extent of labeling may not be standard for a conceptual diagram, I felt that adding it would be beneficial in providing clarity on the function and operation of each component. Please note that this is only a conceptual diagram and therefore does not feature AWS-authorized icons. Instead, I utilized icons from flaticon, a website offering a vast selection of icons.

![Cruddur - Conceptual Diagram.png](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Cruddur_-_Conceptual_Diagram.png)

## Create Archiectural daigram → Logical Diagram CI/CD Pipeline → Stretch Assignment

Logal Diagram - [https://lucid.app/lucidchart/deaaf313-ce92-452f-b00d-0672322a84f3/edit?invitationId=inv_abb065cc-dd1c-4624-9081-5e50304746b7](https://lucid.app/lucidchart/deaaf313-ce92-452f-b00d-0672322a84f3/edit?invitationId=inv_abb065cc-dd1c-4624-9081-5e50304746b7)

I am presenting below my endeavor to create a logical diagram for the Cruddur application. This diagram utilizes AWS authorized icons and provides additional details on the interworking of the application components to deliver the Cruddur service to our users.

![Cruddur Logical Diagram.png](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Cruddur_Logical_Diagram.png)

Unfortunately, due to time constraints, I was unable to utilize the AWS Cost Estimation tool to determine the cost of each service. The AWS Cost Estimation tool would have been an invaluable resource in obtaining a rough estimate of the infrastructure costs associated with setting up the application, as well as the ongoing maintenance costs for the Cruddur application.

In response to Andrew's request, I am presenting my rough sketch, in the style of a "napkin diagram," of the Cruddur application architecture. While I did not have access to an actual napkin, I utilized a notebook as a substitute to simulate the scenario often depicted in movies where a protagonist presents initial ideas for their application.

![IMG_0380.JPEG](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/IMG_0380.jpeg)

# Destroy your root account → Stretch Assignment

## Create an IAM user & Set up MFA

Enable MFA → Enabled MFA for our GitPod IAM User

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%209.png)

I have not created an IAM user for myself, as I will be using the AWS Identity Center feature to simplify authentication management across multiple AWS accounts. AWS Identity Center allows for easy console and CLI access, with configuration options to define the expiration time of your AWS CLI credentials. This enhances security by preventing compromised AWS CLI credentials from being misused, while also making it easier to manage as the credentials are automatically rotated for you.

## Setting up AWS Organisations

Before enabling the AWS Identity and Access Management (IAM) service, I established an AWS Organization. This organization encompasses all four of my AWS accounts, providing enhanced management capabilities and enabling consolidated billing. Additionally, this structure facilitates the segregation of environments and enables the deployment of Service Control Policies (SCPs) to restrict access to my Root user accounts, except for the management Root user account. I have also created an Organization Unit to house my AWS account, separating my test workloads from my production workloads. As I add more testing accounts in the future, I can apply SCPs to the Organization Unit, cascading those restrictions to all AWS accounts within that unit.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2013.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2014.png)

## Setting up Identity center → To manage my multiple AWS accounts

After establishing the AWS Organization, I proceeded to set up the AWS Identity and Access Management (IAM) service. This service enables me, as the single user "kamranabid", to authenticate into AWS using a single set of credentials to access all four of my accounts. I have also enabled three different types of authentication for each of these accounts:

1. "AdministratorAccess", which grants me full administrative access to the target account,
2. "Billing, Admin, and Organizational Access", which grants me access to billing information, organizational access, and administrative access to the accounts,
3. "Read Only" permissions, which allows me to use these credentials to scan my AWS account using tools such as AWS LS and AWS Nuke to monitor deployed resources.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2015.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2016.png)

With the successful authentication as user "kamranabid", I now have the ability to easily access my AWS accounts programmatically or via the AWS Management Console with a simple click of a button.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2017.png)

# Use EventBrdige to hookup Health dashboard to SNS & send Notificaiton when there is a service health issue → Stretch

In this section, I outline and demonstrate the steps taken to set up AWS EventBridge to monitor the AWS Health dashboard and proactively notify me, as the AWS architect, of potential AWS-level downtimes or issues that could impact my running applications. The EventBridge configuration has been tailored to only notify me of issues related to the EC2 service, reducing the number of notifications received.

EventBridge is a widely used tool in AWS and provides great versatility in creating chain reactions that can interact with almost all AWS services. The following example is a straightforward demonstration of how an AWS administrator can utilize EventBridge to receive proactive email notifications regarding events within AWS that may impact their cloud applications.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2018.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2019.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2020.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2021.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2022.png)

# Reviewing each pillar in the Well Architected Tool → Stretch

The AWS Well-Architected Tool is a valuable resource for AWS application developers, as it enables them to assess whether their application or infrastructure aligns with the AWS Well-Architected Framework. By answering a series of questions, developers can identify potential areas of concern and receive recommendations for improvement. I have completed the Well-Architected Tool for the Cruddur application and exported a report that summarizes the results. The report follows a similar format to a penetration testing report, clearly labeling and highlighting any areas of concern that require further attention to ensure the Cruddur application adheres to best practices.

| Pillar | Explanation | Examples |
| --- | --- | --- |
| Security | Ensuring that the systems are secure from external and internal threats | Enabling MFA, Use of Identity and Access Management, Enabling CloudTrail, Using CloudWatch Alarms |
| Reliability | Ensuring that the system is reliable and running optimally | Using Auto-Scaling, Multi-AZ, CloudFormation and CloudWatch Alarms |
| Performance Efficiency | Ensuring that the system is running optimally and efficiently | Utilizing Auto Scaling, Caching, CloudWatch Logs and Alarms, and CloudFront |
| Cost Optimization | Ensuring that the system is operating at the lowest cost | Utilizing CloudWatch Alarms and AWS Budgets, Utilizing Spot Instances, AWS Savings Plans and Reserved Instances |
| Operational Excellence | Ensuring that the system is running and managed effectively | Utilizing CloudFormation, CloudWatch Alarms, CloudTrail, and AWS Config |

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2023.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2024.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2025.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2026.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2027.png)

# Research service limits for the servies and how they could impact techincal path for techincal flexibility → Stretch

| Service | Service Limit | Can request service increase? | Description | Impact on techincal Flexibility |
| --- | --- | --- | --- | --- |
| EC2 | 20 instances per region | Yes | Elastic Compute Cloud (EC2) is a service that provides scalable, secure, and resizable compute capacity in the cloud. | Depending on the number of EC2 instances that will be deployed through Amazon Elastic Container Service (ECS), it may present limitations on our technical flexibility. While it may be possible to distribute the EC2 instances across regions or increase the size of the instances to enhance their ability to fulfill user requests and computation, this limit could still potentially impact the performance of our application. To mitigate this, I have submitted a request to increase the service limit, taking into consideration the aforementioned reasons. |
| S3 | 100 buckets per account | Yes | Simple Storage Service (S3) is a service that provides object storage for any amount of data, with high durability, availability, and performance. | In our use case, 100 Amazon Simple Storage Service (S3) buckets should be sufficient. I do not anticipate the limit of S3 buckets within our account to impede our technical flexibility. Although a single S3 bucket can theoretically accommodate an unlimited number of objects, this approach is not practical and not recommended. However, it does illustrate that the 100 S3 buckets should provide ample capacity for the successful deployment and operation of the Cruddur application. |
| Lambda | 1000 concurrent executions per region | Yes | Lambda is a service that lets you run code without provisioning or managing servers. You pay only for the compute time you consume. | The limit of 1000 concurrent executions per region for AWS Lambda should be sufficient for our needs. I anticipate that this limit will not pose any constraints on our technical flexibility during the design and architecture of the Cruddur application. |
| DynamoDB | 40,000 read capacity units and 40,000 write capacity units per region | Yes | DynamoDB is a service that provides a fast, flexible, and scalable NoSQL database that supports key-value and document data models. | Amazon DynamoDB is a potential alternative to Momento for the Cruddur application. Even if we were to use DynamoDB, the limit of 40,000 read and write capacity units per region should be more than enough to support our users at scale and provide them with a fast and responsive user experience. |
| SNS | 100,000 topics per account | No | Simple Notification Service (SNS) is a service that provides a fully managed pub/sub messaging service that enables you to send messages to subscribers or other AWS services. | Each AWS account has a limit of 100,000 Amazon Simple Notification Service (SNS) topics. At this time, I do not anticipate that the Cruddur application will reach this limit, and therefore do not foresee any technical limitations in this regard. However, if the 100,000 topic limit proves to be a significant restriction on our technical flexibility in the future, implementing multiple AWS accounts through the creation of an AWS Organization and utilizing AWS Organization Units could be a viable solution to increase the number of available SNS topics. It is important to note that there is currently no option to request a service limit increase for the number of SNS topics. |
| VPC | 5 VPCs per region | Yes | Virtual Private Cloud (VPC) is a service that provides a logically isolated section of the AWS cloud where you can launch AWS resources in a virtual network that you define. | The limit of 5 Virtual Private Clouds (VPCs) per region may pose technical flexibility constraints for certain applications. After reviewing the architectural diagrams and proposed implementations for the Cruddur application, I have determined that this limit will not present any technical limitations in providing a comprehensive AWS native application. As a result, I have not submitted a request for a service limit increase for this aspect of the Cruddur application. |

# Open a support ticket and request a service limit increase → Stretch

Building on the information presented in the previous table, I submitted a request for an increase in the number of Amazon Elastic Compute Cloud (EC2) instances available per region through the AWS Support Portal. This request was later approved, enabling us to utilize up to 35 EC2 instances within a single AWS account. This increase eliminates any foreseeable technical limitations that would impact the Cruddur application's ability to provide high-quality services to our users.

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2028.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2029.png)

![Untitled](Week%200%20-%20Homework%20d07752cb1db74bafb90c2aaa2bfb39db/Untitled%2030.png)