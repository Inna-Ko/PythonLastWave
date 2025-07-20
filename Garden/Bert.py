from transformers import BertTokenizer, BertForSequenceClassification
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import AdamWeightDecay

# Загрузка токенизатора
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Загрузка модели для классификации
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)  # Пример для бинарной классификации

# ======= Подготовка данных

texts = ["Это пример текста.", "Это другой пример."]
labels = [0, 1]  # Пример меток

# Токенизация текста
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

# ======= Обучение модели


class CustomDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Создание датасета
dataset = CustomDataset(inputs, labels)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Оптимизатор
optimizer = AdamWeightDecay(model.parameters(), lr=5e-5)

# Обучение
model.train()
for epoch in range(3):  # Количество эпох
    for batch in dataloader:
        optimizer.zero_grad()
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        print(f"Loss: {loss.item()}")

# ======= Использование модели для предсказаний

model.eval()  # Переключение в режим оценки

# Новый текст для предсказания
new_texts = ["Это новый текст для классификации."]
new_inputs = tokenizer(new_texts, padding=True, truncation=True, return_tensors='pt')

with torch.no_grad():  # Отключение градиентов для предсказаний
    outputs = model(**new_inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
    print(predictions)  # Вывод предсказанных меток

# ======= Использование модели для предсказаний

# Сохранение модели

model.save_pretrained('./my_model')
tokenizer.save_pretrained('./my_model')

# Загрузка модели

model = BertForSequenceClassification.from_pretrained('./my_model')
tokenizer = BertTokenizer.from_pretrained('./my_model')

# ======= Использование Jupyter Notebook


# Функция для генерации ответа
def chat_with_model(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Интерактивный ввод
while True:
    user_input = input("Вы: ")
    if user_input.lower() == 'выход':
        break
    response = chat_with_model(user_input)
    print("Модель:", response)