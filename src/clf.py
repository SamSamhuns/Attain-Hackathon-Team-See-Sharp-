import phaser
import numpy as np
import joblib


def main():
    flag = input(
        "Enter 1 to search by country and any other value to search by region:")
    C = joblib.load('clf.pkl')

    if flag == "1":
        country = input("Enter country name (i.e. China): ")
        year, week = input("Enter year and week (YYYY WW i.e. 2050 12): ").split()
        country_id = phaser.get_ID_by_name(country)
        region = phaser.get_region(country_id)
        testdata = np.matrix([country_id, region, year, week])
        result = C.predict(testdata)
        result = result[np.newaxis].T
        print(result[0, 0])
    else:
        region = input("Enter region name: ")
        year, week = input("Enter year and week (YYYY WW i.e. 2050 12): ").split()
        region_id = phaser.get_ID_by_region(region)
        r = []
        c = phaser.get_countries(region_id)
        for country in c:
            r.append([country, region_id, year, week])
        testdata = np.matrix(r)
        result = C.predict(testdata)
        result = result[np.newaxis].T
        rr = []
        i = 0
        for row in result:
            rr.append([phaser.get_name_by_ID(c[i]), row[0]])
            i += 1

        print(rr)


if __name__ == '__main__':
    main()
