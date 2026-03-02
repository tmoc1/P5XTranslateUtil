# P5XTranslateUtil

`python text_check.py <directory_path>`

Enter the translation files directory as parameter. It will collect all words in the `_Substitutions.txt` file and check every non-auto generated file whether the regex and non-regex text includes any substitutions. If any match is found, it will create a detailed `results.txt` file that lists every occurence including the filename, line number, substitution and regex text.

---

`python extract_text.py <input_json_file> <output_file> <field_name>`

First parameter is the path of the datamined dialogue.json file, second parameter is the output file path, and the third parameter is the language format ('cn', 'kr', 'tw' or 'glb'). The output file will have all text of the chosen language.

---

`python onomatopoeia_check.py <onomatopoeia_file> <translation_directory> <all_dialogs_file> <output_file>`

Create a file with all onomatopoeia and their translations and pass it as first parameter. Second parameter is the translation directory path. Third parameter is the dialog text file you extracted using the previous script. Lastly enter a filename for the output file. This script checks all lines that have a substitution placeholder, and will attempt to guess whether a onomatopoeia was used, and if it does, which one it is. It will create a detailed results file which includes filename, line number, text with placeholder, the translated onomatopoeia, the untranslated onomatopoeia and the assumed original dialog line. Not all matching is guaranteed to be accurate. Use this script with caution.

---

`python onomatopoeia_replace.py <onomatopoeia_results> <translation_directory> <output_file>`

A basic replacement script that only handles lines with {{A}} as substitution placeholder. Enter the results file generated with the previous script and the directory path as parameters to automatically perform the onomatopoeia replacement. The output file will include the results that could not be automatically replaced, i.e. multiple substitution placeholders. The modified translation files must be checked as it will likely perform inaccurate replacements. Use this script with caution. 