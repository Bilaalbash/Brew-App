import csv

def save_csv(file_path, owner, data):

    with open(file_path, 'w') as csvfile:
        round_writer = csv.writer(csvfile, delimiter="\t") # Writer
        round_writer.writerow([f"{owner}'s Round"])
        for names in data:
            round_writer.writerow([f"{names}"])

def save_fave(filepath, dict_):
    with open(filepath, 'w') as csvfile:
        round_writer = csv.writer(csvfile, delimiter="\t") # Writer
        for name, drink in dict_.items():
            round_writer.writerow([f"{name},{drink}"])

def load_csv(filepath):
    try:
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            dict_ = {}
            for line in csv_reader:
                dict_[line[0]] = line[1]
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return
    except Exception as e:
        print('An error occurred: ' + str(e))
        return   
    finally:
        pass#csv_file.close()
    return dict_