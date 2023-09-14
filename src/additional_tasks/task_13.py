# Создать текстовый файл и записать в него много строк.

file_name = "GIT.ME"
with open(file_name, "w") as some_file:

    # Скопировать проект как origin
    some_file.write("\n")
    some_file.write("\n* Copy project as origin")
    some_file.write("\ngit clone https://github.com/IAnanevich/tms-python-py43.git")

    # Перейти в папку с GIT (из local в remote)
    some_file.write("\n")
    some_file.write("\n* Change workspace")
    some_file.write("\ncd tms-python-py43/")

    # Обновить ветку main как origin
    some_file.write("\n")
    some_file.write("\n* Update branch as origin")
    some_file.write("\ngit pull origin main")

    # Создать новую ветку для домашнего задания в remote
    some_file.write("\n")
    some_file.write("\n* Add new branch")
    some_file.write("\ngit checkout -b ak-10")

    # Вернутся или перейти в ветку
    some_file.write("\n")
    some_file.write("\n* Change branch")
    some_file.write("\ngit checkout main")
    some_file.write("\ngit checkout ak-8")

    # Публикация в remote origin
    some_file.write("\n")
    some_file.write("\n* Update and push branch")
    some_file.write("\ngit add .")
    some_file.write("\ngit commit")
    some_file.write("\ngit push origin ak-10")
