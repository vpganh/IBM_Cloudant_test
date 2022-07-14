# IBM_Cloudant_test

Using `curl` HTTP API to create and query IBM Cloudant databases.

## Objectives
- Create, query and drop databases
- Perform basic commands such as inserting, updating and deleting documents

## Notice about this lab environment 

Before you start working with the HTTP API to access the Cloudant, you need to collect the below details of your Cloudant instance from *cloud.ibm.com*.
- Your Cloudant username
- Your Cloudant password
- Your Cloudant url

You can get all these details from the Service Credentials.

- Step 1: Go to cloud.ibm.com/resources.
- Step 2: Under Services click on your instance of Cloudant.
- Step 3: On the Cloudant instance page, click on Service Credentials.
- Step 4: Click on the chevron of your Service Credentials. You should see your Service Credentials
- Step 5: Copy the url without the double quotes on either side.

Note: If you do not see the password field in your credentials, it is because you have not selected “IAM and legacy credentials” in Exercise 2, Step 5 of the lab Sign Up for an IBM Cloudant Instance. You can fix it by deleting your current Cloudant instance and following the instructions from the beginning to create a new instance of Cloudant.
