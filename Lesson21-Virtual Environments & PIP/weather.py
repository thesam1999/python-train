# py -m pip install requests 安裝requests這個模組
# py -m pip list 列出現在已經安裝的模組
# py -m pip install requests==2.30.0 ，選擇requests這個模組特定的版本
# py -m pip install -U(or --u) requests 更新 requests這個模組到最新版本
# py -m uninstall requests 移除requests這個模組
# py -m venv .venv 創建一個虛擬環境，檔案名字為.venv
# .venv/Scripts/activate 激活虛擬環境  !!! 每次離開關閉這個資料夾，再次回來時，都要再次激活!!
# deactivate就是關閉虛擬環境，回到全域環境
# py -m pip show requests 其中requires顯示這個requests套件同時也需要其他套件(安裝requests時會自動安裝其他套件)

# https://pypi.org/
# 這裡可以找到每種套件的介紹

# py -m pip freeze > requirements.txt  將當前 Python 虛擬環境中已安裝的套件及其版本輸出到一個名為 requirements.txt 的文件中
# VS Code 中，requirements.txt 文件名稱具有特別的意義，因為這是 Python 專案中慣用的標準文件名稱，VS Code 和一些相關的插件（如 Python 插件）會對這個特定名稱提供額外的支持，例如連結到套件的官方網站或 PyPI 頁面。這是因為 requirements.txt 是 Python 生態系統中用來處理依賴的一個標準文件名，許多工具和插件預設會識別並處理這個文件。


import requests  # 使用 requests 模組，你可以下載網頁內容，或者與 Web API 進行交互。
# 有GET、POST、PUT、DELETE 等不同類型的請求
# load_dotenv 這個函數的主要作用是加載 .env 文件中的環境變數，並將這些變數自動加入到 Python 運行時的環境中
from dotenv import load_dotenv
import os  # os 是 Python 標準庫中用來與操作系統進行交互的模塊，能夠處理環境變量、文件系統操作、系統屬性檢查、進程管理等，為開發者提供了與底層系統進行溝通的強大工具。

# 主要用途:
# 讀取環境變量：獲取系統的關鍵參數，比如 API 密鑰、用戶設置等。
# 文件和目錄操作：用來創建、修改或刪除文件和目錄。
# 系統屬性檢查：獲取當前操作系統和環境的相關信息。
# 執行系統命令：從 Python 代碼中執行系統命令或腳本。
from pprint import pprint  # pretty-print，以更可讀的方式格式化和輸出 Python 對象，讓輸出更具可讀性

# pip是acronym for preferred installer program 首選安裝程式

# Virtual environment 虛擬環境，有時候執行一個專案時，python會需要一個較舊版的module，用virtual environment可以用來隔離 Python 專案的工具，讓每個專案能夠擁有自己獨立的 Python 執行環境和套件。這樣的隔離機制可以避免不同專案之間的套件衝突，因為不同專案可能需要不同版本的套件或 Python 版本。

# 不要把任何virtual environment的檔案上傳到git或github，也就是.ven

load_dotenv()


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()
    # requests.get(request_url)是用來向指定的 URL（這裡是 request_url）發送 GET 請求。GET 請求通常用來從服務器(就是網頁)獲取數據。
    # .json()，通常，API 返回的數據是 JSON 格式，.json() 方法將其轉換為 Python 中的字典或列表，方便Python操作。
    # pprint(weather_data)

    # JSON 是一種輕量級的數據交換格式，易於讀取和寫入，同時也易於解析和生成。JSON 格式通常用於 Web 應用程序中來傳輸數據

    print(f'\nCurrent weather for {weather_data["name"]}:')
    print(f'\nThe temp is {weather_data["main"]["temp"]:.1f}°')
    # weather是一個list裡面包含了dictionary，先輸入0，選擇第一個屬性，再從字典(第一元素)裡面找description的value
    print(
        f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')


if __name__ == "__main__":
    get_current_weather()
