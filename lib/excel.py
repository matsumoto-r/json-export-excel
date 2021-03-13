import json
import os
import configparser


def getTableData(path):
    """jsonファイルからexcelに書き込むテーブルデータを取得する
    Args:
        path (str): jsonファイルのパス
    Returns:
        list: テーブルデータ
    """
    # 設定値取得
    config = configparser.ConfigParser()
    config.read(os.getcwd() + '/' + 'config.ini', encoding='utf-8')
    tableHeader = eval(config['EXCEL']['TABLE_HEADER'])
    useIndex = eval(config['EXCEL']['USE_INDEX'])
    tableIndex = []
    # jsonファイル読み込み
    fd = open(path, mode='r')
    data = json.load(fd)
    fd.close()
    tables = []
    # データ作成
    for item in data['data']:
        table = []
        for idx in range(len(tableHeader)):
            table.append(item[tableHeader[idx]])
        if useIndex is True:
            # 表の行の名前を追加
            if 'index' in item:
                tableIndex.append(item['index'])
            else:
                tableIndex.append('--')
        tables.append(table)
    return tables, tableIndex
