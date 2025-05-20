from transformers import BertTokenizer, BertForSequenceClassification, BertConfig
import torch

pretrained_tokenizer = BertTokenizer.from_pretrained(
    "bert-base-uncased")

config = BertConfig.from_pretrained(
    "bert-base-uncased",
    output_hidden_states=True,
    num_labels=3
)
pretrained_model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    config=config,
)
pretrained_model.eval()  # inference mode


def get_cls_embedding(concept1, concept2, _model=pretrained_model.bert, _tokenizer=pretrained_tokenizer):
    text = f"{concept1} [SEP] {concept2}"
    inputs = _tokenizer(text, return_tensors="pt").to("cpu")  # Force CPU
    _model = _model.to("cpu")  # Ensure model is on CPU too

    with torch.no_grad():
        outputs = _model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :]  # [CLS] token
    return cls_embedding.squeeze().numpy()


def get_layerwise_embeddings(concept1, concept2, _model=pretrained_model.bert, _tokenizer=pretrained_tokenizer):
    text = f"{concept1} [SEP] {concept2}"
    inputs = _tokenizer(text, return_tensors="pt").to("cpu")  # Force CPU
    _model = _model.to("cpu")  # Ensure model is on CPU too

    with torch.no_grad():
        outputs = _model(**inputs)
        # tuple of (layer, batch, seq_len, hidden_size)
        hidden_states = outputs.hidden_states

    # Take [CLS] token from each layer
    layerwise_cls = [layer[:, 0, :].squeeze().numpy()
                     for layer in hidden_states]
    return layerwise_cls  # list of (768,) vectors, one per layer
