## 📢 Blackduck IT Service Cloud Migration 

We are migrating on-premise BlackDuck instance to a cloud. This migration will improve performance, scalability, and security. 
To ensure a smooth transition, this document outlines the necessary steps that users need to take and the overall migration plan.

### Migration Details:
Migration Date:  <br/>
Downtime Window: <br/>


### Required User Actions:
- **Update the Integrations: <br/>**
Update any scripts, CI/CD pipelines, or tools that point to the current on-premise BlackDuck instance. <br/>
BlackDuck Cloud URL: https://mercedes-benz.app.blackduck.com/

- **Review and Adjust Firewall and Network Policies:  <br/>**
Please test your accessibility to the new blackduck cloud instance and if required ensured that the new IP address  and domain name are whitelisted in your firewall settings. <br/>
IP Address: <br/>
Domain Name: <br/>

- **Reconfigure Integration and API Endpoints: <br/>**
If you have automated integrations, API calls, or scripts pointing to the old BlackDuck instance, update them to use the new domain.

- **Verify Access and Perform Testing: <br/>**
Please log in to the new BlackDuck cloud instance and please verify that scans, policies, and integrations work as expected.

### Post-Migration: How Scans and Integrations Work 
After the BlackDuck Admin Team has migrated all projects and necessary data to the cloud on [INSERT DATE], users will be provided with a grace period of one week to make the necessary changes, such as updating URLs and modifying configurations.

At the end of the grace period, the Admin Team will perform a final synchronization of data from the on-premise instance to the cloud, ensuring that all the latest changes are reflected. After this point, the on-premise instance will be decommissioned, and users must fully operate on the cloud instance.
![Your paragraph text (4)](https://git.i.mercedes-benz.com/SHETRAKS/Python_BD/assets/1625/475600d5-3c68-4da6-92b7-1c80ab527216)



### Support and Assistance
For any issues or concerns, please reach out to the [BlackDuck support team](https://git.i.mercedes-benz.com/foss/BlackDuckSupport/issues). <br/>
We appreciate your cooperation and support during this migration process.


