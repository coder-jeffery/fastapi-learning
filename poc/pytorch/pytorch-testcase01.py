from transformers import BertModel
model = BertModel.from_pretrained('bert-base-uncased')
print(model)