# Snow Report API



<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="##about-the-project">About The Project</a></li>
    <li><a href="##Installation">Installation</a></li>
    <li><a href="##System Architecture">System Architecture</a>
    <ul><li><a href="####Diagrams">Diagrams</a></li>
        <li><a href="####Snow Report Attributes">Report Attributes</a></li>
      </ul>
    <li><a href="####Important Controller Methods">Important Controller Methods</a></li>
    <li><a href="####API Paths">API Paths</a></li>
    <li><a href="####TODO">TODO</a></li>
    <li><a href="####Future Project">Future Project</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>

## About The Project
Like most snow sport enthusiasts, I aim to leave my house at different times depending on how much new snow there is at the mountain.
I wanted my raspberry Pi to access the most rececent snow report in and decide what time my alarm would go off. Since my local resort didn't seem to have a public API to give me the morning snow report I decided to build my own.

The main purpose of this project is to learn the process of building an API with Flask and will be used to collect, store and distribute the snow report for two resorts. The next project will be building the alarm clock and writing the alarm application. 

## Installation

1. Clone the repo
   ```bash
   git clone https://github.com/hi2gage/snow-report-api.git
   ```
2. Install Pip Requirements
   ```bash
   pip install -r requirements.txt
   ```

## System Architecture
#### Diagrams:
Current API architecture for the system

![System Diagram](https://github.com/hi2gage/snow-report-api/blob/main/diagrams/main-layout.png)

#### Snow Report Attributes:
* day_id (Primary Key)
* data_time
* overnight_snow 
* settled_base 
* total_to_date 
* six_am_temp 
* twenty_four_hr_snow 
* seven_day_snow 
* current_conditions 
* visibility 
* wind 



#### Important Controller Methods
```python
# get all snow reports
def get_all():
   returns #all snow reports from database


# get most recent snow reports
def get_recent_sql():
   returns #most recent snow report from database


# commits data frin current object to database
def web_to_sql():
   scraps webside and adds snow report to database
   return #most recent snow report from database


# resets database
def delete_all_entries():
   deletes all database entries and restarts primary key auto increments
```

#### API Paths
```python
api.add_resource(fetchAll, '/')
api.add_resource(fetchRecentSQL, '/recent-sql')
api.add_resource(fetchByDate, '/date')
api.add_resource(scrap, '/scrap')
```



#### TODO
- [ ] Clean up requirements.txt
- [ ] Test that the automated scheduler works
- [ ] Comment all code
- [ ] Remove all unnecessary code
- [ ] Build front side website

#### Future Projects:
* Alarm Clock
* IOS app

#License
Distributed under the MIT License. See `LICENSE` for more information.



