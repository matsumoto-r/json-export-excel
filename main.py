import os
import pandas as pd
from lib.excel import getTableData
import configparser


# 読み込みたいjsonファイルはpublic配下に保存
FULL_PATH = os.getcwd() + "/public/"
# 読み込みたいjsonファイルの名前を指定
FILE_NAME = "sample.json"
# 設定値取得
config = configparser.ConfigParser()
config.read(os.getcwd() + '/' + 'config.ini', encoding='utf-8')
excelFileName = eval(config['EXCEL']['EXCEL_FILE_NAME'])
sheetName = eval(config['EXCEL']['SHEET_NAME'])
startRow = eval(config['EXCEL']['START_ROW'])
startCol = eval(config['EXCEL']['START_COL'])
tableHeader = eval(config['EXCEL']['TABLE_HEADER'])
overwrite = eval(config['EXCEL']['OVERWRITE'])
# テーブルデータとインデックスの取得
tableData, tableIndex = getTableData(FULL_PATH + 'input/' + FILE_NAME)
# テーブルの設定
df = pd.DataFrame(tableData)
df.columns = tableHeader   # ヘッダーを指定
print(tableIndex)
if len(tableIndex) > 0:
    df.index = tableIndex  # インデックスがあれば指定
# エクセル作成のオプションの作成
option = {'startrow': startRow, 'startcol': startCol}
if len(tableIndex) == 0:
    option['index'] = False
if len(sheetName) > 0:
    option['sheet_name'] = sheetName
# 上書きの場合
if overwrite is True:
    with pd.ExcelWriter(
            os.getcwd() + '/public/output/' + excelFileName, mode='a'
            ) as writer:
        df.to_excel(writer, **option)
else:
    df.to_excel(os.getcwd() + '/public/output/' + excelFileName, **option)
