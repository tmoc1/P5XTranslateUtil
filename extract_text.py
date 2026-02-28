import json
import sys
import time

def extract_field_text(input_file, output_file, field_name):
    start_time = time.time()

    # Read JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON root must be a list of objects.")

    count = 0

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data:
            try:
                value = item["original_content"][field_name]

                if isinstance(value, str):
                    # Preserve Unicode and escape newlines as \n
                    escaped = json.dumps(value, ensure_ascii=False)[1:-1]
                    f.write(escaped + "\n")
                    count += 1

            except (KeyError, TypeError):
                continue

    end_time = time.time()
    elapsed = end_time - start_time

    print(f"Finished. Wrote {count} records.")
    print(f"Elapsed time: {elapsed:.4f} seconds")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_text.py <input_json_file> <output_file> <field_name>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    field_name = sys.argv[3]

    extract_field_text(input_filename, output_filename, field_name)