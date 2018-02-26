# python-openstack-examples

# Configure your development environment
1. Install Python

2. Add Python to your PATH environment variable<br>
   ##### For Windows
   computer -> properties -> Environment variables -> System variables -> Path<br>
   add `;C:\Python27;C:\Python27\Scripts`
   
   ##### For Linux
   `export PATH=$PATH;YOUR-PYTHON-PATH`
   
3. (Option) Install git on your server/computer<br>
   ##### For Windows
   https://git-scm.com/download/win

   ##### For Liunx
   `pip install git`

4. Download the source code from the GitHub website<br>
   Here `huawei-python-openstacksdk` is your local directory.<br>
   `git clone https://github.com/Huawei/python-openstacksdk huawei-python-openstacksdk`<br>
   
5. Install the SDK<br>
**ATTENTION: If you have installed the OpenStack SDK from the Openstack community.Please uninstall it first. <br> 
             Otherwise, the SDK for Open Telekom Cloud may work improperly.**<br>
   Open a command line, <br>
   `cd huawei-python-openstacksdk`<br>
   `git checkout master`<br>
   `pip install -r requirements.txt`<br>
   `python setup.py install`<br>

# Configure your credentials
Then we need to get the credentials to access to the Open Telekom Cloud.

_auth = {
    'auth_url': "https://iam.eu-de.otc.t-systems.com:443/v3",<br>
    'project_id': 'YOUR-PROJECT-ID',<br>
    'user_domain_id': 'YOUR-DOMAIN-ID',<br>
    'username': 'YOUR-USER-NAME',<br>
    'password': 'YOUR-PASSWORD'<br>
}

1. How Do I Query a Project ID?<br>
Please refer to https://docs.otc.t-systems.com/en-us/usermanual/ac/en-us_topic_0046606344.html

2. How Do I Query a Domain ID?<br>
Please refer to https://docs.otc.t-systems.com/en-us/usermanual/ac/en-us_topic_0048830758.html<br>
**ATTENTION: The value of Domain ID is just blow the Domain Name.**

3. How Do I Query Regions and Endpoints?<br>
Please refer to https://docs.otc.t-systems.com/en-us/endpoint/index.html

4. How Do I Query a API URI?<br>
Please refer to https://docs.otc.t-systems.com/en-us/api_list/index.html
