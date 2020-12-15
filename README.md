# Snow Report API

Like most snow sport enthusiasts, I aim to leave my house at different times depending on how much new snow there is at the mountain.
I wanted my raspberry Pi to access the most rececent snow report in and decide what time my alarm would go off. Since my local resort didn't seem to have a public API to give me the morning snow report I decided to build my own.

The main purpose of this project is to learn the process of building an API with Flask and will be used to collect, store and distribute the snow report for two resorts. The next project will be building the alarm clock and writing the alarm application. 

## Installation

```bash
git clone https://github.com/hi2gage/snow-report-api.git
```
## Requirements
Currently the requirements file is a little larger than it should be, installed some packages that I actually will not be using so I will be updating it soon.
```bash
pip install -r requirements.txt
```
## Diagrams
![alt text](https://github.com/hi2gage/snow-report-api/blob/main/diagrams/main-layout.png)


## TODO
- [ ] Clean up requirements.txt
- [ ] Test that the automated scheduler works
- [ ] Comment all code
- [ ] Remove all unnecessary code
- [ ] Build front side website

## License
[MIT](https://choosealicense.com/licenses/mit/)


