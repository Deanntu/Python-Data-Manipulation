import csv
import statistics
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def task1(name, country, number):
    #Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.
    #Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero).
    stats = []
    countries = {}
    with open(name) as csvfile:
        csvreader = csv.reader(csvfile)
        first = True
        for row in csvreader:
            if first:
                stats.append(row)
                first = False
                continue
            stats.append(row)
            if row[number]:
                if row[country] not in countries:
                    countries.update({row[country]: row[number]})
                elif row[country] < countries.get(row[country]):
                    countries.update({row[country]: row[number]})
    csvfile.close()
    for row in stats:
        if first:
            stats.append(row)
            first = False
            continue
        if not row[number]:
            if row[country] in countries:
                row[number] = countries.get(row[country])
            else:
                row[number] = 0
    with open(name, 'w', newline='') as csvfile_out:
        writer = csv.writer(csvfile_out)
        for row in stats:
            writer.writerow(row)
    csvfile_out.close()
def task2(name):
    #Code Implementation Task: Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.
    with open(name) as csvfile:
        csvreader = csv.reader(csvfile)
        lastCountry = ""
        first = True
        list = []
        countries = []
        for row in csvreader:
            if first:
                first = False
                continue
            if lastCountry == "":
                lastCountry = row[0]
                list.append(int(row[2]))
            elif lastCountry == row[0]:
                list.append(int(row[2]))
            else:
                countries.append([lastCountry,list])
                lastCountry = row[0]
                list = [int(row[2])]
        for i in range(len(countries)):
            countries[i] = [statistics.median(countries[i][1]),countries[i][0]]
        countries.sort(reverse=True)
        print("top-3 countries with highest median daily vaccination numbers are: {}, {}, and {}.".format(countries[0][1],countries[1][1],countries[2][1]))
    csvfile.close()
def task3(name,date):
    #What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) by considering missing values imputed version of dataset?
    total=0
    with open(name) as csvfile:
        csvreader = csv.reader(csvfile)
        lastCountry = ""
        first = True
        for row in csvreader:
            if first:
                first = False
                continue
            if row[1] == date:
                total += int(row[2])
    print(total)
if __name__ == '__main__':
    task1("country_vaccination_stats.csv",0,2)
    task2("country_vaccination_stats.csv")
    task3("country_vaccination_stats.csv","1/6/2021")
