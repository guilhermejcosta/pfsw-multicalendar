FROM python:3.9

ENV TZ="America/Sao_Paulo" \
    ROOT_PATH="/app"

EXPOSE 8080 8000

WORKDIR $ROOT_PATH

ADD ./requirements.txt $ROOT_PATH

RUN python -m pip install pip --upgrade

RUN pip install -r $ROOT_PATH/requirements.txt

COPY . $ROOT_PATH

CMD uvicorn main:app --host 0.0.0.0 --port 8080 --reload
# CMD ['/bin']