FROM python:3.9
COPY . /app
WORKDIR /app

RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN pip install -r requirements.txt
RUN mim install mmcv-full==1.7.0
RUN git clone https://github.com/facebookresearch/detectron2.git
RUN python -m pip install -e detectron2
RUN pip install -r components/mmocr_ocr/requirements/build.txt
RUN pip install -r components/mmocr_ocr/requirements/optional.txt
RUN pip install -r components/mmocr_ocr/requirements/runtime.txt
RUN pip install -r components/mmocr_ocr/requirements/tests.txt

ENTRYPOINT ["python"]
CMD ["app.py"]