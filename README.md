# json-export-excel

json からエクセルのシートに書き出しを行います

# ファイル構成

- main.py
  実行ファイル
- config.ini
  設定ファイル。このファイルに記載した値を編集。
- public/input/
  エクセルに書き出すデータの json ファイル
- public/output/
  json ファイルのデータをもとに作成したエクセルファイル
- lib/excel.py
  エクセルに関する関数を定義

# json ファイルの書き方

```
{
    // `data`の中に書く
    "data": [
        {
            // keyが表の列の名前になります
            "age": 20
            // keyに`index`を指定した場合は表の行の名前になります（config.iniでUSE_INDEXをTrueにする必要があります）
            "index": "Taro"
        }
    ]
}
```
