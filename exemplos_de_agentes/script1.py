import os
import time

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


prompt = "As mulheres podem dirigir na Àrabia Saudita?"

# Tokenizar
inputs = tokenizer(prompt, return_tensors="pt")

# Gerar resposta
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=100, do_sample=True)

# Decodificar e imprimir
print(tokenizer.decode(outputs[0], skip_special_tokens=True))