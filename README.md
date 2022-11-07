this project pulls the jewish holiday via api request for the next 3 months, and displays it in json format on localhost on port 8082 127.0.0.1:8082


it deploys Centos7 on virtualbox , install the required components to accomplish the mission, e.g. python3, pip, etc (can be seen in Vagrant file), and than runs a python app to display the requested content.

pre-requiesists- (for windows machine):

1- vagrant installed. 

2- virtualbox installed. 

how to activate the script:

-open cmd 

-do git clone https://github.com/edenmor1989/jewish-holidays-vagrant.git

-cd to the downloaded directory

-now do vagrant.exe up 

NOTE- please wait until it deploys the VM compeletly, it should take several minutes

go to browser and type : https://127.0.0.1:8082
