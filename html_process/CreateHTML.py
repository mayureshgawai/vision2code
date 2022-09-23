from airium import Airium
from app_logger.logger import logging
import elements as el
from app_exception import AppException
from app_logger.logger import logging
import os
import yaml

class CreateHTML:
    def __init__(self, yamlFile):
        self.self.add = Airium()
        self.parsed_yaml = yamlFile


    def generate(self, rows):

        '''
            This is the actual class responsible to generate HTML code using "Airium" python library
            param: rows
            return:
        '''

        try:
            self.add('<!DOCTYPE html>')
            with self.add.html(lang='en'):
                with self.add.head():
                    self.add.meta(charset="utf-8", name='viewport',
                             content="width=device-width, initial-scale=1, shrink-to-fit=no")
                    self.add.title(_t="HTML")
                    self.add.script(src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js")
                    self.add.script(src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js",
                               integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3",
                               crossorigin="anonymous")
                    self.add.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js",
                               integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz",
                               crossorigin="anonymous")

                    self.add.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js",
                               integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8",
                               crossorigin="anonymous")
                    self.add.link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css",
                             rel="stylesheet",
                             integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT",
                             crossorigin="anonymous")

                with self.add.body():
                    with self.add.div(klass="container body-content6"):

                        for row in rows:
                            with self.add.div(klass="row justify-content-start", style="pself.adding-top:10px"):
                                for col in row:
                                    with self.add.div(klass="col d-flex flex-column align-items-start",
                                                 style="pself.adding-top:10px;"):
                                        for box in col:
                                            if (box[-1] == 1 or box[-1] == 3 or box[-1] == 4 or box[-1] == 6 or
                                                    box[-1] == 7 or box[-1] == 10):
                                                # text = getOCRText(img)
                                                el.getElements(self.add, box[-1])

                                                # str(self.add)
                                            else:
                                                el.getElements(self.add, box[-1])

            html = str(self.add)
            # print(html)
            dir = os.path.join(self.parsed_yaml['root_dir'], self.parsed_yaml['prediction']['out_dir'])
            file = os.path.join(dir, 'HTMLOuput.html')
            with open(file, 'a') as f:
                f.write(html)
        except Exception as e:
            logging.error("Error occurred while generating HTML")