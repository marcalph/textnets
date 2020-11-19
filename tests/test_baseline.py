import sys
sys.path.append("/home/malphonsus/projects/personal/textnets/src/compose")
import baseline


def test_baseline(string="hello", possibilities=3):
    res = baseline.compose(string, possibilities)
    for r in res:
        assert len(r) >= len(string)
    assert len(res) == possibilities
