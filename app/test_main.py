from main import prediction_form, array_converter
import numpy as np
import pytest


def test_prediction_form_return():
    res = prediction_form()
    assert type(res) == str

def test_array_converter():
    # Document de test, qui a la forme de ce qui est envoyé quand l'API
    # est requêtée avec un document encodé avec USE
    document = "[-1.07934652e-02  1.10973353e-02  1.88557450e-02 -1.01408432e-03 -2.37439983e-02 -7.54840523e-02 -4.83562192e-03]"
    doc = array_converter(document)
    assert isinstance(doc, np.ndarray)
