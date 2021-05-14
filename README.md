# Restaurant Order System

## Contents

* [Introduction](#introduction) 
  * [Objective](#objective)
* [Architecture](#architecture)
* [Trello Board](#trello-board)
* [Entity Relationship Diagram](#entity-relationship-diagram)
* [Risk Assessment](#risk-assessment)
* [Test Analysis](#analysis-of-testing)
* [Continuous Integration](#continuous-integration)
* [Development](#development)
  * [Unit Testing](#unit-testing)
  * [Front-End Design](#front-end)
  * [Integration Testing](#integration-testing)
* [Footer](#footer)


### Objective
The purpose of this project is to develop an application that implements CRUD Functionality
using all the various technologies & methodologies that have been covered so far during my training

These functionalities include:
- Application with a create, read, update & delete functionality implemented using Python
- A website application implemented using Flask
- Documentation of application created
- Trello board containing the plan for implementation
- Relational database showcasing a one to many relationship between tables
- Risk Assessment
- Testing

 ### My Approach
 
 I have implemented this application by using a Restaurant ordering system in which a user chooses
 what restaurant they want to order from; then chooses the meal they want from the restaurant.
 
**Create**:
* restaurant name
* restaurant location
* customer name
* customer order (food)
* time in which order was made

**Read**:
* customer name
* customer order
* restaurant name
* restaurant location
* time ordered

**Update**:
* customer name
* customer order

**Delete**:
* user/profile containing their name & food ordered


## Architecture
### Trello Board
I have utilised a trello board to showcase the progress of my project implementation over Jira as it is free to use

# First Trello Board
![Trello board 1](https://user-images.githubusercontent.com/48153566/118319076-2d4c6a00-b4f2-11eb-9741-ad327b91d687.png)

# Final Trello Board
![finaltrello](https://user-images.githubusercontent.com/48153566/118318508-659f7880-b4f1-11eb-8d24-2821b2381e80.png)

The full board can be found at https://trello.com/b/G39Z6rIk/restaurant



### Entity Relationship Diagram

My original ERD is shown aswell as the final ERD after implementation of application.

I have used a one to many relationship as one restaurant can have many orders but an order can only
be linked to one restaurant

# Original ER Diagram

![erdiagram1](https://user-images.githubusercontent.com/48153566/118319199-5967eb00-b4f2-11eb-91e0-459544cf44c5.jpg)

![erdiagram2 (2)](https://user-images.githubusercontent.com/48153566/118319206-5a991800-b4f2-11eb-90ef-cabe81fd40c7.png)


# Final ER Diagram
![ER diagram 3](https://user-images.githubusercontent.com/48153566/118318743-b4e5a900-b4f1-11eb-9dbd-8b18c0b15956.png)

![erdiagram4](https://user-images.githubusercontent.com/48153566/118318793-c75fe280-b4f1-11eb-8e21-97f6cd7f0937.png)

### Risk Assessment

A risk assessment register was made to show the risks associated with the project. Shown below was the original planned risk assessment aswell as the
new risk assessment created after implementation

# Original Risk Assessment
![risk assessment 1](https://user-images.githubusercontent.com/48153566/118321087-07749480-b4f5-11eb-9fc6-49e53fd18b76.png)

# Final Risk Assessment

![final risk assessment](https://user-images.githubusercontent.com/48153566/118323000-e5304600-b4f7-11eb-811c-d5dba32a06d5.png)


### Continuous Integration

### Unit & Integration Testing


#### Jenkins Script
The build script can be broken into five stages, shown below.  
<br/>

**1.** Installation of the virtual environment

```
sudo apt install chromium-chromedriver -y
sudo apt-get install python3-venv

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```
<br/>

**2.** Stopping existing processes that may interfere

```
sudo systemctl stop recipe-project
sudo rm pytest-result
```

**3.** Unit and integration testing

```
python3 -m pytest tests --cov=application --cov-report term-missing --disable-warnings
```
<br/>

**4.** Running as-live environment on systemd process
```
sudo cp -r . /opt/project

sudo systemctl daemon-reload
sudo systemctl start recipe-project
```

**5.** Checking for reported failures from earlier testing - marks the build as failed if appropriate
```
if [ -f pytest-result ] && [ $(cat pytest-result) == 'FAIL' ]; 
	then echo "TESTING FAILED - MARKING BUILD AS FAILED"; exit 1;
fi;
```

As outlined in the pipeline diagram, the testing coverage report is then available on the Jenkins console.

### Front-End
#### Home Page
Screenshot of the home page

![website1](https://user-images.githubusercontent.com/48153566/118324621-2de8fe80-b4fa-11eb-980d-99c259c9beb3.png)

#### Restaurant Creation
Screenshot of the create a restaurant page

![website2](https://user-images.githubusercontent.com/48153566/118324628-2f1a2b80-b4fa-11eb-8d37-22031ca1cc66.png)

#### Order Creation
Screenshot of the create an order page

![website3](https://user-images.githubusercontent.com/48153566/118324633-30e3ef00-b4fa-11eb-9945-60e033d19d4f.png)

### Author
Goke Tegbe

 
