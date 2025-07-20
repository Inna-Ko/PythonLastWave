from transformers import BertTokenizer, BertForSequenceClassification
import torch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from torch.utils.data import DataLoader, Dataset
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import json

# ======= Подготовка данных
with open('data.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Извлечение текстов и меток
texts = [item["text"] for item in data]
labels = [item["label"] for item in data]  # Теперь метки текстовые

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Инициализация токенизатора BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Токенизация данных
train_encodings = tokenizer(X_train, truncation=True, padding=True)
test_encodings = tokenizer(X_test, truncation=True, padding=True)

# Преобразование меток в числовой формат (например, с помощью Label Encoding)
all_labels = list(set(y_train) | set(y_test))  # Уникальные метки из обоих наборов

label_encoder = LabelEncoder()
label_encoder.fit(all_labels)  # Обучаем на всех метках

y_train_encoded = label_encoder.transform(y_train)
y_test_encoded = label_encoder.transform(y_test)


# Преобразование в PyTorch Dataset
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


# Создание объектов Dataset
train_dataset = CustomDataset(train_encodings, y_train_encoded)
test_dataset = CustomDataset(test_encodings, y_test_encoded)

train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=2)

# ======= Инициализация модели и токенизатора
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# ======= Обучение модели
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

model.train()
num_epochs = 5
history = {'loss': [], 'accuracy': []}

for epoch in range(num_epochs):
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
    history['loss'].append(avg_loss)

    # Оценка точности на тестовом наборе
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
    history['accuracy'].append(accuracy)

    print(f'Epoch {epoch + 1}, Loss: {avg_loss:.4f}, Accuracy: {accuracy:.4f}')

# ======= Сохранение истории
results = pd.DataFrame(history)
results.to_csv('training_results.csv', index=False)

# Сохранение модели
torch.save(model.state_dict(), 'my_model.pth')

# ======= Оценка модели (если нужно еще раз)
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
print(f'Final Accuracy: {accuracy:.2f}')
