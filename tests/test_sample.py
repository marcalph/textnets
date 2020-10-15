import os
import sys

import hello

sys.path.append("/home/malphonsus/projects/personal/textnets/src/textnets")
print(os.environ["PYTHONPATH"])


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_msg():
    assert "hello" in hello.msg.lower()
