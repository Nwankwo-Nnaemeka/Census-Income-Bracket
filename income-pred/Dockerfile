FROM frolvlad/alpine-miniconda3:python3.7
COPY requirements.txt .
COPY ./app /app
RUN pip install -r requirements.txt && \
	rm requirements.txt
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
