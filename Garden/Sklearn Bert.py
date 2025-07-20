from transformers import BertTokenizer, BertForSequenceClassification
import torch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from torch.utils.data import DataLoader, Dataset
import numpy as np


# ======= Подготовка данных
data = [
    {"text": "Я люблю программирование!", "label": "позитивный"},
    {"text": "Это ужасный фильм.", "label": "негативный"},
    {"text": "Прекрасная погода сегодня.", "label": "позитивный"},
    {"text": "Мне не нравится этот продукт.", "label": "негативный"},
    {"text": "Я в восторге от этой книги!", "label": "позитивный"},
    {"text": "Это было разочарование.", "label": "негативный"},
]

texts = [item["text"] for item in data]
labels = [1 if item["label"] == "позитивный" else 0 for item in data]  # Преобразуем метки в числовые значения

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)


# ======= Создание пользовательского датасета
class TextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length=512):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_length,
            return_token_type_ids=False,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt',
        )
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }


# ======= Инициализация модели и токенизатора
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# ======= Подготовка данных для DataLoader
train_dataset = TextDataset(X_train, y_train, tokenizer)
test_dataset = TextDataset(X_test, y_test, tokenizer)

train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=2)


# ======= Обучение модели
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

model.train()
for epoch in range(5):  # Обучаем модель на 3 эпохи
    total_loss = 0
    for batch in train_loader:
        optimizer.zero_grad()
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        total_loss += loss.item()
        loss.backward()
        optimizer.step()

    avg_loss = total_loss / len(train_loader)
    print(f'Epoch {epoch + 1}, Loss: {avg_loss:.4f}')


# ======= Оценка модели
model.eval()
predictions = []
with torch.no_grad():
    for batch in test_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        preds = torch.argmax(outputs.logits, dim=-1)
        predictions.extend(preds.cpu().numpy())

accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')


# ======= Функция для генерации ответа
def chat_with_model(prompt):
    inputs = tokenizer(prompt, return_tensors='pt', padding=True, truncation=True).to(device)
    with torch.no_grad():  # Отключение градиентов для предсказаний
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)
    return predictions.item()  # Возвращаем предсказанную метку


# # Интерактивный ввод
# while True:
#     user_input = input("Вы: ")
#     if user_input.lower() == 'выход':
#         break
#     response = chat_with_model(user_input)
#     label_response = "позитивный" if response == 1 else "негативный"
#     print("Модель:", label_response)  # Вывод предсказанной метки