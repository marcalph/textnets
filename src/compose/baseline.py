#!/usr/bin/env python3
# coding: utf-8
########################################
# authors                              #
# marcalph https://github.com/marcalph #
########################################
""" composition baseline
"""
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
torch.manual_seed(42)
tokenizer = GPT2Tokenizer.from_pretrained("distilgpt2")
model = GPT2LMHeadModel.from_pretrained("distilgpt2", pad_token_id=tokenizer.eos_token_id)


def compose(string, possibilities=3):
    """ composition func
    Parameters
    ----------
    string : starting string
    Returns
    -------
    output : completed string
    """
    input = tokenizer.encode(string, return_tensors='pt')
    sampling_outputs = model.generate(
        input,
        do_sample=True,
        max_length=50,
        top_k=50,
        top_p=0.95,
        num_return_sequences=possibilities)
    return [tokenizer.decode(sample, skip_special_tokens=True) for sample in sampling_outputs]


