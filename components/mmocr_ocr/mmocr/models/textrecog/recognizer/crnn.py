# Copyright (c) OpenMMLab. All rights reserved.
from components.mmocr_ocr.mmocr.models.builder import RECOGNIZERS
from .encode_decode_recognizer import EncodeDecodeRecognizer


@RECOGNIZERS.register_module()
class CRNNNet(EncodeDecodeRecognizer):
    """CTC-loss based recognizer."""
