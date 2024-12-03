FROM python:3.12-latest

COPY requirements.txt reqs.txt
RUN pip install -r reqs.txt

WORKDIR /app

COPY ./backend ./backend

CMD ["python", "backend/main.py"]
