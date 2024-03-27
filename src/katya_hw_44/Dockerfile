FROM python:3.11

ENV target_name World

ARG num_1
ARG num_2

ENV env_num_1 ${num_1}
ENV env_num_2 ${num_2}

WORKDIR /code

COPY program.py hello.py FAQ.txt ./

ENTRYPOINT ["python"]
