# Snow Report API

Like most snow sport enthusiasts, I aim to leave my house at different times depending on how much new snow there is at the mountain.
I wanted my raspberry Pi to access the most rececent snow report in and decide what time my alarm would go off. Since my local resort didn't seem to have a public API to give me the morning snow report I decided to build my own.

The main purpose of this project is to learn the process of building an API with Flask and will be used to collect, store and distribute the snow report for two resorts. The next project will be building the alarm clock and writing the alarm application. 

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/hi2gage/snow-report-api.git
   ```
2. Install Pip Requirements
   ```bash
   pip install -r requirements.txt
   ```

### Diagrams
Current API architecture for the system

![alt text](https://github.com/hi2gage/snow-report-api/blob/main/diagrams/main-layout.png)

### Important Controller Methods
```python
# get all snow reports
@staticmethod
def get_all():
   returns all snow reports from database


# get most recent snow reports
@staticmethod
def get_recent_sql():
   returns most recent snow report from database


# commits data frin current object to database
@staticmethod
def commit_to_SQL(self):
   SQL commit
   return most recent snow report from database


# returns all snow reports from given date
@staticmethod
def find_by_date(find_date):
   return list of snow reports from database with given date
```

#### API Paths
```python
api.add_resource(fetchAll, '/')
api.add_resource(fetchRecentSQL, '/recent-sql')
api.add_resource(fetchByDate, '/date')
api.add_resource(scrap, '/scrap')
```



### TODO
- [ ] Clean up requirements.txt
- [ ] Test that the automated scheduler works
- [ ] Comment all code
- [ ] Remove all unnecessary code
- [ ] Build front side website

### Future Projects:
* Alarm Clock
* IOS app

## License
Distributed under the MIT License. See `LICENSE` for more information.



