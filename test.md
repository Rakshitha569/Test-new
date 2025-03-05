## 📢 Blackduck IT Service Cloud Migration 

### Migration Details:
Migration Date:  <br/>
Downtime Window: <br/>

### What is migrated ?
All data present in on-prem instance till the migration date, this includes projects, scans, groups, users, api tokens.

### Immediate Action required by user before migration 
1. If you are using GitHub road-runners for your blackduck scans - no action required.
2. If you use any other self hosted runners/machine which requires firewall clearance, please ensure the below domain/ip is whitelisted 
- IP Address: 104.18.39.43
- Domain Name: mercedes-benz.app.blackduck.com <br/>

__⚠️**Note: Please don't update your workflows to point to cloud url prior to migration date.**__

### Action required after migration to cloud:
- **Verify your existing data: <br/>**
Please login to https://mercedes-benz.app.blackduck.com and verify if existing projects, scans, user group data are present as expected.
- **Update the CI/CD pipelines <br/>**
Update blackudck url  in your existing workflows/ configurations from https://bdscan.i.mercedes-benz.com/  to  new domain  https://mercedes-benz.app.blackduck.com/ <br/>
- **Reconfigure custom scripts/ integration end points <br/>**
Update the blackduck url endpoints in your custom integration scripts from https://bdscan.i.mercedes-benz.com/ to https://mercedes-benz.app.blackduck.com/
- **Testing: <br/>**
After reconfiguring scan to new instance,  please ensure scan is successful checking scan logs, login to UI and verify if all data (policies, scan result) is available as expected.

__⚠️**Note: The current API tokens will function with the new cloud instance, so users won't need to generate new tokens.**__

### What happens after migration date?
1. All new projects, groups requests are onboarded only to cloud instance.
2. After the migration date, both the on-prem and cloud instances will run in parallel to ensure that no pipelines are disrupted.
3. Users are provided with a 2 week grace period to ensure that all their workflows are reconfigured to point to the cloud URL "https://mercedes-benz.app.blackduck.com/"
4. Please note that after the migration, all scans directed to the on-prem instance will not be transferred to the cloud. (After updating the URL to point to the cloud instance in your pipeline, rescanning will update all the scan data.)
5. The On-prem instance "https://bdscan.i.mercedes-benz.com/" will be decommissioned on March 31st 2025

### Support and Assistance
For any issues or concerns, please reach out to the [BlackDuck support team](https://git.i.mercedes-benz.com/foss/BlackDuckSupport/issues). <br/>


