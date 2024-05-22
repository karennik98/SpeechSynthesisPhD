import csv
import argparse

def parse_tsv_to_csv(input_tsv_file, output_csv_file):
    # Open the input TSV file and the output CSV file
    with open(input_tsv_file, 'r', newline='', encoding='utf-8') as tsv_file, \
         open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        
        # Create a CSV reader for the TSV file and a CSV writer for the CSV file with the specified delimiter
        tsv_reader = csv.DictReader(tsv_file, delimiter='\t')
        csv_writer = csv.writer(csv_file, delimiter='|', quoting=csv.QUOTE_NONE, escapechar='\\')
        
        # Iterate over each row in the TSV file
        for row in tsv_reader:
            # Extract the desired columns
            path = row['path']
            sentence = row['sentence']
                        
            # Write the extracted and transformed columns to the CSV file
            csv_writer.writerow([path, sentence])

    print(f"Data successfully written to {output_csv_file}")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Parse a TSV file and extract specific columns to a CSV file.")
    parser.add_argument('input_tsv_file', help="The path to the input TSV file.")
    parser.add_argument('output_csv_file', help="The path to the output CSV file.")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the function with the provided arguments
    parse_tsv_to_csv(args.input_tsv_file, args.output_csv_file)

if __name__ == "__main__":
    main()
