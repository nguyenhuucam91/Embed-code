FROM python:latest

RUN pip install youtube_dl && pip install beautifulsoup4 && pip install requests && pip install selenium

RUN pip install webdriver-manager

RUN pip install pytest
