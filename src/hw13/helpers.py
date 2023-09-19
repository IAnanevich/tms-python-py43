from sqlalchemy import inspect
import re


class Helpers:
    @staticmethod
    def htmlspecialchars(text) -> str:
        text = str(text)
        return (
            text.replace("&", "&amp;").
            replace('"', "&quot;").
            replace("<", "&lt;").
            replace(">", "&gt;")
        )

    @staticmethod
    def validate_email(email: str) -> bool:
        # pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,4}+$"
        if re.match(pattern, email) is not None:
            return True
        return False

    @staticmethod
    def print_pretty_table(data, cell_sep=' | ', header_separator=True) -> None:
        rows = len(data)
        cols = len(data[0])

        col_width = []
        for col in range(cols):
            columns = [data[row][col] for row in range(rows)]
            col_width.append(len(max(columns, key=len)))

        separator = "-+-".join('-' * n for n in col_width)

        for i, row in enumerate(range(rows)):
            if i == 1 and header_separator:
                print(separator)

            result = []
            for col in range(cols):
                item = data[row][col].rjust(col_width[col])
                result.append(item)

            print(cell_sep.join(result))

    @staticmethod
    def object_as_dict(obj) -> dict:
        return {c.key: str(getattr(obj, c.key))
                for c in inspect(obj).mapper.column_attrs}

    @staticmethod
    def print_list(data=list) -> None:

        if data is None or len(data) == 0:
            return False

        data_dict = []
        for item in data:
            data_dict.append(Helpers.object_as_dict(item))

        table_data = []
        for key, item in enumerate(data_dict):
            if key == 0:
                table_data.append(list(item.keys()))
            table_data.append(list(item.values()))

        Helpers.print_pretty_table(table_data)

    @staticmethod
    def print_color(text: str, color: str) -> None:
        access_color = {
            "green": "\033[32m",
            "blue": "\033[34m",
            "red": "\033[31m",
        }
        if color in access_color:
            print(f"{access_color[color]}{text}\033[0m")
        else:
            print(text)
