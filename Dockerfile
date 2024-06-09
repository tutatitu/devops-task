FROM python:3.9

WORKDIR /calculator

COPY . .

CMD [ "python", "./calculator.py" ]