#!/bin/bash

# -----------------------------------------------------------------------------
#  安裝 image-timestamp-logger 專案所需的 Python 套件
# -----------------------------------------------------------------------------

echo "正在為專案安裝 Python 依賴套件..."

# 檢查 requirements.txt 檔案是否存在
if [ ! -f "requirements.txt" ]; then
    echo "錯誤: 找不到 requirements.txt 檔案。請確保此腳本與 requirements.txt 在同一個目錄下。"
    exit 1
fi

# 使用 pip 安裝 requirements.txt 中列出的所有套件
pip install -r requirements.txt

echo ""
echo "依賴套件安裝完成！"
echo "提醒：請記得將 'arial.ttf' 字型檔案放置在專案根目錄下才能正常執行。"