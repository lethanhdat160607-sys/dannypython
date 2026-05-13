# ============================================================
#  DỰ ÁN: PHÂN LOẠI ĐỘNG VẬT HOANG DÃ - WorldQuant University
#  File này dùng training.py có sẵn từ WQU
#  Chạy từng cell trong Jupyter Notebook
# ============================================================
 
# %% [markdown]
# ## 1. Import thư viện
 
# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from PIL import Image
 
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms
 
# File training.py của WQU (đặt cùng thư mục)
from training import train, score, predict
 
# ============================================================
# 2. CẤU HÌNH
# ============================================================
 
# %%
# Đường dẫn (sửa nếu cần)
DATA_DIR  = Path("data_p1/data_multiclass")   # thư mục chứa train/ và test/
TRAIN_DIR = DATA_DIR / "train"
TEST_DIR  = DATA_DIR / "test"
MODEL_DIR = Path("model")
MODEL_DIR.mkdir(exist_ok=True)
 
# Đúng với submission.csv của WQU
CLASS_NAMES = [
    "antelope_duiker",
    "bird",
    "blank",
    "civet_genet",
    "hog",
    "leopard",
    "monkey_prosimian",
    "rodent",
]
NUM_CLASSES = len(CLASS_NAMES)   # 8
 
# Hyperparameters
IMG_SIZE    = 224
BATCH_SIZE  = 32
NUM_EPOCHS  = 20
LR          = 1e-3
VAL_SPLIT   = 0.2
SEED        = 42
 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")
 
# ============================================================
# 3. TÍNH MEAN / STD (chuẩn hóa đúng với dataset thực)
# ============================================================
 
# %%
def compute_mean_std(folder, img_size=224, max_samples=2000):
    """Tính mean/std trên tập train để dùng cho Normalize."""
    t = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
    ])
    s, sq, cnt, n = torch.zeros(3), torch.zeros(3), 0, 0
    for root, _, files in os.walk(folder):
        for f in files:
            if not f.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            try:
                img = Image.open(os.path.join(root, f)).convert("RGB")
                x   = t(img)
                s  += x.sum(dim=[1,2]);  sq += (x**2).sum(dim=[1,2])
                cnt += x.shape[1]*x.shape[2];  n += 1
                if n >= max_samples: break
            except Exception: pass
        if n >= max_samples: break
    mean = s / cnt
    std  = (sq / cnt - mean**2).sqrt()
    return mean.tolist(), std.tolist()
 
mean, std = compute_mean_std(TRAIN_DIR)
print(f"Mean: {mean}")
print(f"Std : {std}")
 
# ============================================================
# 4. TRANSFORMS & DATASET
# ============================================================
 
# %%
train_transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std),
])
 
val_transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std),
])
 
# ImageFolder tự đọc subfolder → nhãn
# (thứ tự class phải khớp CLASS_NAMES, ImageFolder sort theo alphabet → đúng)
full_dataset = datasets.ImageFolder(root=TRAIN_DIR, transform=train_transform)
print(f"Class → index: {full_dataset.class_to_idx}")
 
# Kiểm tra thứ tự class có khớp CLASS_NAMES không
assert list(full_dataset.class_to_idx.keys()) == CLASS_NAMES, \
    f"Thứ tự class không khớp!\nDataset: {list(full_dataset.class_to_idx.keys())}"
 
# Split train / val
torch.manual_seed(SEED)
val_size   = int(len(full_dataset) * VAL_SPLIT)
train_size = len(full_dataset) - val_size
train_ds, val_ds = random_split(full_dataset, [train_size, val_size])
 
# Val dùng transform không augment
val_ds.dataset.transform = val_transform
 
train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                          num_workers=4, pin_memory=True)
val_loader   = DataLoader(val_ds,   batch_size=BATCH_SIZE, shuffle=False,
                          num_workers=4, pin_memory=True)
 
print(f"Train: {train_size} ảnh  |  Val: {val_size} ảnh")
 
# ============================================================
# 5. MÔ HÌNH CNN
# ============================================================
 
# %%
class WildlifeCNN(nn.Module):
    """
    CNN 3-block: 16 → 32 → 64 filters
    Phân loại 8 lớp động vật hoang dã (WQU dataset)
    """
    def __init__(self, num_classes=NUM_CLASSES, dropout=0.5):
        super().__init__()
        self.features = nn.Sequential(
            # Block 1
            nn.Conv2d(3, 16, 3, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),          # 224→112
 
            # Block 2
            nn.Conv2d(16, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),          # 112→56
 
            # Block 3
            nn.Conv2d(32, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),          # 56→28
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),                # 64*28*28 = 50176
            nn.Linear(64*28*28, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(dropout),
            nn.Linear(512, 128),
            nn.ReLU(inplace=True),
            nn.Dropout(dropout / 2),
            nn.Linear(128, num_classes),
        )
        self._init_weights()
 
    def _init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
            elif isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                nn.init.zeros_(m.bias)
 
    def forward(self, x):
        return self.classifier(self.features(x))
 
 
model     = WildlifeCNN().to(device)
loss_fn   = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LR)
 
total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Tổng tham số: {total_params:,}")
 
# ============================================================
# 6. HUẤN LUYỆN  (dùng hàm train() từ training.py của WQU)
# ============================================================
 
# %%
# Hàm train() từ WQU training.py sẽ in loss/accuracy mỗi epoch
train(
    model=model,
    optimizer=optimizer,
    loss_fn=loss_fn,
    train_loader=train_loader,
    val_loader=val_loader,
    epochs=NUM_EPOCHS,
    device=device,
)
 
# Lưu model
torch.save(model, MODEL_DIR / "deepnet")
print("✅ Model đã lưu → model/deepnet")
 
# ============================================================
# 7. ĐÁNH GIÁ CUỐI (dùng hàm score() từ training.py)
# ============================================================
 
# %%
val_loss, val_acc = score(
    model=model,
    data_loader=val_loader,
    loss_fn=loss_fn,
    device=device,
)
print(f"\nVal Loss: {val_loss:.4f}  |  Val Accuracy: {val_acc:.4f}")
 
# ============================================================
# 8. CONFUSION MATRIX
# ============================================================
 
# %%
from sklearn.metrics import confusion_matrix, classification_report
import torch.nn.functional as F
 
def get_predictions(model, loader, device):
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for imgs, labels in loader:
            out   = model(imgs.to(device))
            preds = out.argmax(dim=1).cpu().numpy()
            all_preds.extend(preds)
            all_labels.extend(labels.numpy())
    return np.array(all_labels), np.array(all_preds)
 
y_true, y_pred = get_predictions(model, val_loader, device)
 
# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=CLASS_NAMES, yticklabels=CLASS_NAMES, ax=ax)
ax.set_xlabel("Predicted"); ax.set_ylabel("True")
ax.set_title("Confusion Matrix – Validation Set")
plt.xticks(rotation=45, ha="right"); plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
plt.show()
 
print("\n[Classification Report]")
print(classification_report(y_true, y_pred, target_names=CLASS_NAMES))
 
# ============================================================
# 9. PREDICT TEST SET & XUẤT submission.csv
#    (dùng hàm predict() từ training.py của WQU)
# ============================================================
 
# %%
# Dataset test — WQU để ảnh phẳng trong test/, không subfolder
# Dùng ImageFolder trick: tạo 1 class giả
from torch.utils.data import Dataset
 
class TestDataset(Dataset):
    """Test set không có nhãn. Trả về (tensor, filename_không_đuôi)."""
    def __init__(self, test_dir, transform=None):
        self.paths     = sorted(Path(test_dir).glob("*.jpg"))
        self.transform = transform
 
    def __len__(self): return len(self.paths)
 
    def __getitem__(self, idx):
        p   = self.paths[idx]
        img = Image.open(p).convert("RGB")
        if self.transform:
            img = self.transform(img)
        return img, p.stem   # stem = tên file không đuôi, e.g. "ZJ016488"
 
test_ds     = TestDataset(TEST_DIR, transform=val_transform)
test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE,
                         shuffle=False, num_workers=4)
 
print(f"Test set: {len(test_ds)} ảnh")
 
# %%
# predict() của WQU trả về tensor xác suất [N, 8]
# Nhưng nó cần targets trong batch → ta wrap lại
# (WQU predict() lấy (inputs, targets) trong loop)
# → Dùng hàm predict riêng không cần targets
 
def predict_no_label(model, loader, device):
    """Predict test set không có nhãn, trả về (probs, image_ids)."""
    model.eval()
    all_probs, all_ids = [], []
    with torch.no_grad():
        for imgs, ids in loader:
            out   = model(imgs.to(device))
            probs = F.softmax(out, dim=1).cpu().numpy()
            all_probs.extend(probs)
            all_ids.extend(ids)
    return np.array(all_probs), all_ids
 
probs, image_ids = predict_no_label(model, test_loader, device)
 
# Tạo DataFrame đúng format submission.csv của WQU
df_sub = pd.DataFrame(probs, columns=CLASS_NAMES)
df_sub.insert(0, "", image_ids)       # cột đầu không có tên (như file mẫu)
df_sub.to_csv("submission.csv", index=False)
 
print("✅ submission.csv đã lưu!")
print(df_sub.head())
