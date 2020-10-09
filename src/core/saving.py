import csv

def save_csv(file_path, owner, data):

    with open(file_path, 'w') as csvfile:
        round_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL) # Writer
        round_writer.writerow([f"{owner}'s Round\n"])
        for names in data:
            round_writer.writerow([f"{names}"])

def save_fave(filepath, dict_):
    with open(filepath, 'w') as csvfile:
        round_writer = csv.writer(csvfile, delimiter="\t") # Writer
        for name, drink in dict_.items():
            round_writer.writerow([f"{name},{drink}"])