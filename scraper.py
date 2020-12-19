from bs4 import BeautifulSoup
import requests
import os.path
import pickle as pickle
import datetime
import re


def wf_get_data(alert=True, refresh=False):
    # Checks to see if the cache file is present and if the user wants a refresh
    if os.path.isfile('page.pkl') and not refresh:
        if alert:
            print("file exists")
        with open('page.pkl', 'rb') as inp:
            page = pickle.load(inp)
    else:
        if alert:
            print("file does not exist")
        url = "https://skiwhitefish.com/snowreport/"
        page = requests.get(url)
        with open('page.pkl', 'wb') as output:
            pickle.dump(page, output)

    # Parses the HTML and selects the results that are relevant
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(id='content')
    results = content.find_all(class_='col-sm-6')

    # Selects the different sections and compiles into array
    line1 = results[0].text.replace("\t", '')[1:]
    line2 = results[1].text.replace("\t", '')[1:]
    final_list = line1.split("\n") + line2.split("\n")

    # Creates dictionary of the statistics and values
    data_dict = {}
    for index, line in enumerate(final_list, start=0):
        value = line.split(": ")
        if index < 6:
            data_dict[value[0].replace(" ", "_")] = value[1].split('/')[0]
        elif index is 7:
            data_dict[value[0].split('/')[0]] = value[1].split('/')[0]
            data_dict[value[0].split('/')[1]] = value[1].split('/')[1]
        else:
            data_dict[value[0].replace(" ", "_")] = value[1]

    result_list = []
    for i in data_dict.keys():
        if data_dict[i][0].isdigit():
            value_int = re.sub('[^0-9]', '', data_dict[i])
            result_list.append(value_int)
        else:
            result_list.append(data_dict[i])
    tp = tuple(result_list)
    return tp


def print_dic(data):
    print("current time: ", end='\n')
    print(datetime.datetime.now())
    for d in data:
        print("{:25s} {:1s}".format(d + ":", data[d]))
    print()


def scrape_wf(refresh=False):
    wf_dict = wf_get_data(refresh=refresh)
    # print_dic(wf_dict)
    # print(wf_dict)
    return wf_dict


# TODO build bridger Scraper
def bridger_get_data():
    pass


def main(resort="wf", refresh=False):
    if resort is "wf":
        wf_tuple = wf_get_data(refresh=refresh)
        # print_dic(wf_tuple)
        # print(wf_tuple)
        # print(wf_tuple)
        return wf_tuple

    elif resort is "bridger":
        return bridger_get_data()
    else:
        print("resort not found")


if __name__ == '__main__':
    main()
