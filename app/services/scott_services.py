import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

GPTtokenizer = GPT2Tokenizer.from_pretrained("gpt2")
GPTmodel = GPT2LMHeadModel.from_pretrained("gpt2")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def next_word(text, k=5):

    indexed_tokens = GPTtokenizer.encode(text)
    tokens_tensor = torch.tensor([indexed_tokens])
    tokens_tensor = tokens_tensor.to(device)
    GPTmodel.to(device)

    with torch.no_grad():
        outputs = GPTmodel(tokens_tensor)
        predictions = outputs[0]

    probs = predictions[0, -1, :]
    top_next = [GPTtokenizer.decode(i.item()).strip() for i in probs.topk(k)[1]]
    return top_next



if __name__ == '__main__':

    text = "Elon Musk is my favorite"
    print(next_word(text))