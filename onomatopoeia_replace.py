import os
import sys
import string
import time
import re


def process_file(onomatopoeia_results, translation_directory, output_file):
    skipped_lines = []

    # Precompute invalid placeholders {{B}} - {{Z}}
    invalid_placeholders = [f"{{{{{letter}}}}}" for letter in string.ascii_uppercase if letter != "A"]

    with open(onomatopoeia_results, "r", encoding="utf-8") as infile:
        for raw_line in infile:
            line = raw_line.rstrip("\n")
            parts = line.split(" | ")

            # Ensure we have at least 6 parts
            if len(parts) != 6:
                skipped_lines.append(line)
                continue

            target_filename = parts[0].strip()

            try:
                line_number = int(parts[1].replace("Line ", "").strip())
            except ValueError:
                skipped_lines.append(line)
                continue

            third_value = parts[2]
            fourth_value = parts[3]
            fifth_value = parts[4]

            # Must contain {{A}}
            if "{{A}}" not in third_value:
                skipped_lines.append(line)
                continue

            # Skip if contains {{B}} - {{Z}}
            if any(placeholder in third_value for placeholder in invalid_placeholders):
                skipped_lines.append(line)
                continue

            # Skip if contains ellipsis character
            #if "…" in third_value:
            #    skipped_lines.append(line)
            #    continue

            # Search for file in directory
            target_path = None
            for root, _, files in os.walk(translation_directory):
                if target_filename in files:
                    target_path = os.path.join(root, target_filename)
                    break

            if not target_path:
                skipped_lines.append(line)
                continue

            try:
                with open(target_path, "r", encoding="utf-8") as f:
                    file_lines = f.readlines()

                # Validate line number (1-based)
                if line_number < 1 or line_number > len(file_lines):
                    skipped_lines.append(line)
                    continue
                    
                file_line = file_lines[line_number - 1]
                
                left_part = ""
                right_part = ""
                file_line_parts = []
                if file_line.startswith('r:"'):
                    file_line_parts = file_line.split('"="', 1)
                else:
                    file_line_parts = re.split(r'(?<!\\)=', file_line, maxsplit=1)
                if len(file_line_parts) > 1:
                    left_part = file_line_parts[0]
                    right_part = file_line_parts[1]
                
                left_part = left_part.replace("{{A}}", fourth_value)
                right_part = right_part.replace("{{A}}", fifth_value)

                file_lines[line_number - 1] = left_part + '=' + right_part

                with open(target_path, "w", encoding="utf-8") as f:
                    f.writelines(file_lines)

            except Exception:
                skipped_lines.append(line)
                continue

    # Write skipped lines
    with open(output_file, "w", encoding="utf-8") as skipped_file:
        for skipped in skipped_lines:
            skipped_file.write(skipped + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python onomatopoeia_replace.py <onomatopoeia_results> <translation_directory> <output_file>")
        sys.exit(1)
    
    start_time = time.time()

    onomatopoeia_results = sys.argv[1]
    translation_directory = sys.argv[2]
    output_file = sys.argv[3]

    process_file(onomatopoeia_results, translation_directory, output_file)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Operation completed in {elapsed_time:.4f} seconds.")
