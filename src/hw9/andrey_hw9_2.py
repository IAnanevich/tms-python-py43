# 2) Реализовать любой метакласс (сами придумываете что ваш метакласс будет делать)
import json


class Meta(type):
    def __new__(cls, name: str, bases: tuple, attrs: dict, *args: tuple, **kwargs: dict) -> object:
        if name == 'Get':
            def date(self, datas: str) -> None:
                """
                converts string data to dict
                :param self:
                :param datas:
                :return:
                """
                import json
                self.body = json.loads(datas)

            attrs.setdefault('date', date)
        if name == 'Post':
            def return_body(self) -> str:
                """
                converts dict data to string
                :param self:
                :return:
                """
                return json.dumps(self.body)

            attrs.setdefault('return_body', return_body)

        return super().__new__(cls, name, bases, attrs)


class Get(metaclass=Meta):
    def __init__(self, body: str, head: dict) -> None:
        self.body = body
        self.head = head


class Post(metaclass=Meta):
    def __init__(self, body: dict, head: dict) -> None:
        self.body = body
        self.head = head


get = Get(body='', head={'Content-Type': ''})
get.date('{ "id": 121, "name": "Naveen", "course": "MERN Stack"}')
print(get.body)
print(type(get.body))

post = Post(body={"id": 121, "name": "Naveen", "course": "MERN Stack"}, head={'Content-Type': ''})
response = post.return_body()
print(response)
print(type(response))
