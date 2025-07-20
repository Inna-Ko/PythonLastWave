import torch
from transformers import BertTokenizer
from transformers import BertForSequenceClassification


# Создайте экземпляр модели
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Загрузите сохранённые веса
model.load_state_dict(torch.load('my_model.pth'))

# Переведите модель в режим оценки
model.eval()

# Загрузка токенизатора
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


# Функция для предсказания
def predict(text):
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        return_tensors='pt',
        padding='max_length',
        truncation=True,
        max_length=512
    )

    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=-1).item()

    return predicted_class


# Интерактивный ввод
while True:
    user_input = input("Введите текст (или 'exit' для выхода): ")
    if user_input.lower() == 'exit':
        break
    prediction = predict(user_input)
    # print(f"Предсказанный класс: {'позитивный' if prediction == 1 else 'негативный'}")
    print(prediction)
