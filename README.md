# P5XTranslateUtil

`python text_check.py <directory_path>`

Enter the translation files directory as parameter. It will collect all words in the `_Substitutions.txt` file and check every non-auto generated file whether the regex and non-regex text includes any substitutions. If any match is found, it will create a detailed `results.txt` file that lists every occurence including the filename, line number, substitution and regex text.
