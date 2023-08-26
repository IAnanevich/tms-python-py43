# В конец существующего текстового файла записать три новые строки текста.
import datetime

file_name = "GIT.ME"
with open(file_name, "a") as some_file:
    some_file.write("\n")
    some_file.write("\n")
    some_file.write("Klenovsky Alexandr")
    some_file.write("\n")
    some_file.write(str(datetime.datetime.now()))
