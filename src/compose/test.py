import sys

import hello

print(hello.msg)
print(sys.path)


from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="data/models/smallGERT",
    tokenizer="data/models/smallGERT"
)
# The sun <mask>.
# =>
fill_mask("Ich liebe <mask>.")
