import csv

def process_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile, delimiter='|')
        writer = csv.writer(outfile, delimiter='|')

        for row in reader:
            if len(row) == 2:
                filename, text = row
                new_row = [filename, text, text]
                writer.writerow(new_row)
            else:
                print(f"Skipping malformed row: {row}")

if __name__ == "__main__":
    input_file = "output/all_in_one/metadata.csv"
    output_file = "output/all_in_one/processed_metadata.csv"
    process_csv(input_file, output_file)
    print(f"Processing complete. Output saved to {output_file}")