# 🌡️ Thermy!

### Goals 

Gain hands-on experience with Alexa (Voice), Serverless, REST, and Flask.

### Introduction

This project was created as a proof of concept for voice enabling a home thermostat. The original problem statement was as follows: "Your company makes an awesome home thermostat. You’re trying to convince your boss to 'voice-enable' it. The unit is not Internet-enabled right now, so your boss doesn’t really even know what this would mean. So you decide to [a] simulate the device if Internet-enabling hardware were to be added to it (via a product redesign), and then [b] show how you could then control it via voice. (Yes, you could describe this via a powerpoint presentation, but you want to make it more concrete than that, because – as you know – “Code Wins Arguments”)."

### Setup

Due diligence for any cloud project starts with setting a budget to limit resource usage overflow. Always be sure to consistently change the AWS region to what is physically closest (as seen in the top right of the dashboard). Create a cost budget, giving adequate notification metrics. It is recommended that an email notification would be sent after 75% of the indicated budget. 

### Strategy

The first step of the project was to create a REST based API service to simulate the device. I used a Ubuntu 18.04 EC2 instance to run a lightweight Flask app to operate the API. The following interface needed to be supported at a minimum.

| HTTP Method | URI                                                     | Action                                   |
| ----------- | ------------------------------------------------------- | ---------------------------------------- |
| GET         | http://[hostname]/ThermsAreUs/api/v1.0/current-temp     | Retrieve current temp in room            |
| GET         | http://[hostname]/ThermsAreUs/api/v1.0/current-setpoint | Retrieve current setpoint (desired temp) |
| PUT         | http://[hostname]/ThermsAreUs/api/v1.0/current-setpoint | Update current setpoint (desired temp)   |

The Flask server alone does not support data persistence, and so to secure the setpoint value I stored it locally in a data file on the EC2 instance (see [Next Steps](#next-steps) for a better solution). Below is a screenshot of the browser when accessing <http://[hostname]/ThermsAreUs/api/v1.0/current-temp>.

![pa3-rest](C:\Users\lukep\Desktop\Projects\UVA Engineering Items\4740 Cloud\pa3\img\pa3-rest.png)

The second step was to create an Alexa-hosted python Skill called that I called Thermy. The deployed code was hosted in a Lambda function. The skill was invoked using a keyword string, and an intent was created to return a hard coded temperature value. Below is a picture of the test value being returned. 

![pa3-get](C:\Users\lukep\Desktop\Projects\UVA Engineering Items\4740 Cloud\pa3\img\pa3-get.png)

Then instead of simply returning a hardcoded value, I implemented calls to the REST API hosted on an EC2 instance created earlier. The following screenshot shows an interaction with Alexa, setting and getting the simulated temperature device.

![pa3-full](C:\Users\lukep\Desktop\Projects\UVA Engineering Items\4740 Cloud\pa3\img\pa3-full.png)

As you can see, invoking the Skill with such a long keyword string every time is rather tedious, however, as a commercial product the keyword string would likely be simpler, such as "Thermy". Repetition is necessary to distinguish invocations from other IoT devices.

### Next Steps

Storing the setpoint value in a local file is not the best practice, each component should be separated into individual services. This  value should be stored in a database, perhaps using AWS RDS. The REST API also is not authenticated, which is fine for a mock project, but in a commercial product this is a clear must-have. 

### Notes

This project is no longer being served on AWS due to budget constraints.

### Acknowledgements

Thanks goes to Marty Humphrey (University of Virginia, 2021) for providing project guidelines during CS 4740 S21.
