import csv


def get_keys(csv_file_addr):

    keys = list()
    try:

        with open(csv_file_addr) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='=')
            for key_line in csv_reader:
                keys.append(key_line[1])

        return keys
    except FileNotFoundError as e1:
        print(e1)
    except TypeError as e2:
        print(e2)
    except RuntimeError as e3:
        print(e3)
    except AttributeError as e4:
        print(e4)
