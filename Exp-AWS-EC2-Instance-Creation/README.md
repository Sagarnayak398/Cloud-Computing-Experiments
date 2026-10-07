# AWS-EC2-Instance-Creation

## Aim

To create and connect to an **EC2 instance in Amazon Web Services (AWS)**.

## Technologies Used

- Amazon Web Services (AWS)
- Amazon EC2
- Amazon Machine Image (AMI)
- SSH
- Key Pair

## Experiment Setup

Amazon EC2 (Elastic Compute Cloud) is used to create a virtual server in the AWS cloud.

In this experiment, an EC2 instance is created by selecting an operating system, instance type, storage, and network settings. The instance is then accessed using an SSH key pair.

---

## Procedure

### Step 1: Open Amazon EC2

1. Login to your **AWS account**.
2. Open the **AWS Management Console**.
3. Click **Services**.
4. Search for and select **EC2**.

---

### Step 2: Launch an EC2 Instance

1. Open the **EC2 Dashboard**.
2. Click **Launch Instance**.
3. Enter a name for the instance.
4. Configure the required settings.

---

### Step 3: Select an AMI

1. Select the required **Amazon Machine Image (AMI)**.
2. Choose the operating system according to your requirement.
3. Select an available AMI suitable for the experiment.

---

### Step 4: Select Instance Type

1. Select an instance type according to the required CPU and memory.
2. For a free-tier eligible instance, select:

```text
t2.micro
```
3. Make sure the selected instance type is eligible for the applicable AWS Free Tier.

### Step 5: Configure Network and Storage

1. Keep the default network settings unless changes are required.
2. Configure the required storage.
3. For a free-tier eligible configuration, use the applicable EBS storage limit.
4. Review the selected settings.
   
### Step 6: Launch the Instance

1. Check all the selected configurations.
2. Make sure the selected resources are eligible for the applicable Free Tier.
3. Click Launch Instance.
4. The EC2 instance will be created.
Connect to EC2 Instance Using SSH

### Step 1: Select the EC2 Instance

1. Open the EC2 Dashboard.
2. Select the instance you want to connect to.
3. Click Connect.
   
### Step 2: Select SSH Connection

1. In the Connect page, select the SSH client option.
2. AWS will display the required SSH connection information.
3. Note the SSH command and key-pair requirements.
   
### Step 3: Open Terminal

1. Open Command Prompt / Terminal.
2. Navigate to the folder where your .pem key file is stored.
Example:
cd path/to/key-folder

3. Use the SSH command provided by AWS to connect to the EC2 instance.
Example format:
ssh -i "your-key.pem" username@public-ip-address

4. If prompted, confirm the connection.
5. After successful authentication, you will be connected to the EC2 instance.
   
## Result

An EC2 instance was successfully created in AWS and connected using an SSH key pair.

## Conclusion

This experiment demonstrates how to create a virtual server using Amazon EC2 and access the server remotely using SSH and a key pair.
```
