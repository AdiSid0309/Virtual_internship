import csv
import os

DATA_DIRECTORY = r"./quantium-starter-repo-main/data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

with open(OUTPUT_FILE_PATH, 'w') as op:
    writer = csv.writer(op)

    header = ['sales', 'date', 'region']
    writer.writerow(header)

    for file_name in os.listdir(DATA_DIRECTORY):
        with open(f"{DATA_DIRECTORY}/{file_name}",'r') as ip:
            reader = csv.reader(ip)

            row_index = 0
            for input_row in reader:
                if row_index>0:
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    transaction_date = input_row[3]
                    region = input_row[4]

                    if product == "pink morsel":
                        price = float(raw_price[1:])
                        sale = price*int(quantity)

                        output_row = [sale, transaction_date, region]
                        writer.writerow(output_row)
                row_index+=1