import os
import sys

def compare_files(file1, file2):
    """Compare two files line by line, ignoring whitespace."""
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line_number, (line1, line2) in enumerate(zip(f1, f2), start=1):
            if line1.strip() != line2.strip():
                return line_number

        # Check for extra lines in either file
        for line_number, _ in enumerate(f1, start=line_number + 1):
            return line_number

        for line_number, _ in enumerate(f2, start=line_number + 1):
            return line_number

    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python comparer.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        sys.exit(1)

    xml_files = {file for file in os.listdir(folder_path) if file.endswith('.xml')}
    cmp_files = {file for file in os.listdir(folder_path) if file.endswith('.xml.cmp')}

    all_identical = True

    for xml_file in xml_files:
        cmp_file = f"{xml_file}.cmp"
        if cmp_file in cmp_files:
            xml_path = os.path.join(folder_path, xml_file)
            cmp_path = os.path.join(folder_path, cmp_file)

            difference_line = compare_files(xml_path, cmp_path)
            if difference_line is not None:
                print(f"Difference found between {xml_file} and {cmp_file} starting at line {difference_line}.")
                all_identical = False
        else:
            print(f"No matching .cmp file for {xml_file}")
            all_identical = False

    if all_identical:
        print("All files are identical (ignoring whitespace).")

if __name__ == "__main__":
    main()
