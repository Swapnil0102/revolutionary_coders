import pandas as pd

if __name__ == '__main__':
    csv_file = pd.DataFrame(pd.read_csv("Address_data.csv", sep = ",", header = 0, index_col = False))
    csv_file.to_json("Address_data.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
