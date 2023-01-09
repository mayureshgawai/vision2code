FROM python:3.9
COPY . /app
WORKDIR /app

RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN pip install -r requirements.txt
RUN pip install -r components/mmocr_ocr/requirements/build.txt
RUN pip install -r components/mmocr_ocr/requirements/optional.txt
RUN pip install -r components/mmocr_ocr/requirements/runtime.txt
RUN pip install -r components/mmocr_ocr/requirements/tests.txt

ENTRYPOINT ["python"]
CMD ["app.py"]