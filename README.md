# 圖片時間戳與日誌記錄工具 (Image Timestamp and Logger)

這是一個 Python 工具，主要功能是接收圖片列表，為每張圖片加上目前時間的時間戳，將處理過的圖片儲存到指定的資料夾結構中，並將相關資訊記錄在一個 CSV 檔案中，方便日後追蹤與管理。

專案中的範例程式會擷取整個螢幕畫面，將其切割成四個象限，然後利用核心的 `imageSave` 類別來處理這四張圖片。

## 主要功能

- **自動加上時間戳**：在每張圖片的右下角自動嵌入帶有白色背景的目前時間（年-月-日_時:分:秒.毫秒）。
- **結構化儲存**：將圖片分門別類儲存，預設路徑結構為 `[儲存路徑]/[相機名稱][編號]/[時間戳].jpg` (例如：`./my_captures/CAM0/2023-10-27_15-30-00.123.jpg`)。
- **CSV 日誌記錄**：自動生成或更新一個 CSV 檔案，記錄每張圖片的 `timestamp`, `camera_id`, 和 `file_path`。
- **高度可配置性**：可以自訂儲存路徑、資料夾名稱、字體大小、CSV 檔名，甚至可以選擇是否要儲存圖片檔案。

## 專案結構

```
your_project/
├── main.py         # 主要的 Python 腳本
├── arial.ttf       # (需要自行準備) 時間戳使用的字型檔案
└── README.md       # 本說明文件
```

執行後會產生：

```
your_project/
└── my_captures/
    ├── CAM0/
    │   └── 2023-10-27_15-30-00.123.jpg
    ├── CAM1/
    │   └── 2023-10-27_15-30-00.123.jpg
    ├── CAM2/
    │   └── ...
    ├── CAM3/
    │   └── ...
    └── image_log.csv   # CSV 日誌檔
```

## 安裝依賴套件

您需要安裝 Pillow 和 pyautogui 函式庫。

```bash
pip install Pillow pyautogui
```

> **注意**: `main.py` 中使用了 `ImageFont.truetype('arial.ttf', ...)`。請確保您的系統中有 `arial.ttf` 字型檔案，或者將其更換為您系統上存在的其他 `.ttf` 字型檔路徑。

## 使用方法

### 1. 執行範例

直接執行 `main.py` 將會觸發 `if __name__ == "__main__"` 區塊中的範例程式。

```bash
python main.py
```

此範例會：
1. 擷取當前螢幕畫面。
2. 將畫面切割成四等分。
3. 將這四張圖片傳入 `imageSave` 類別進行處理與儲存。

### 2. 在您的專案中使用 `imageSave`

您可以匯入 `imageSave` 類別並在您的程式中使用它。

```python
from main import imageSave
from PIL import Image

# 假設您有一個包含 PIL Image 物件的列表
list_of_images = [Image.open("image1.jpg"), Image.open("image2.png")]

# 初始化 imageSave 類別，它會自動處理圖片並儲存
imageSave(list_of_images, 
          path='./my_custom_captures', 
          dirName='FRONT_CAM', 
          log='activity.csv')
```

#### `imageSave` 初始化參數

在建立 `imageSave` 物件時，您可以傳入以下可選參數：

- `imageList` (list): **(必須)** 一個包含 Pillow Image 物件的列表。
- `fontSize` (int): 時間戳的字體大小。預設為 `12`。
- `dirName` (str): 儲存圖片的基礎資料夾名稱。預設為 `'CAM'`。
- `path` (str): 圖片和 CSV 的根儲存路徑。預設為 `'./my_captures'`。
- `log` (str): CSV 日誌檔案的名稱。預設為 `'image_log.csv'`。
- `enableSaveImg` (bool): 是否要將圖片儲存到硬碟。設為 `False` 則只會更新 CSV 檔 (如果圖片已存在)。預設為 `True`。