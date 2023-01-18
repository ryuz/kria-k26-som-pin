# Kria K26 SOM ピン配置作成補助用テーブル生成ツール


## 概要

Kria K26 SOM ピン配置作成補助用テーブル生成ツールです。


KV260 などを利用する際に、回路図から Vivado の xdc に指定するピン名にたどり着くまでに

- K26 SOM コネクタに名付けられた信号名
- K26 SOM コネクタのピン番号
- K26 SOM に搭載された XCK26-SFVC784-2LV-C/I のピン番号

と追っていかなければなりません。

この際、参照する資料も

- KV260 の回路図などの資料
- [Kria K26 SOM Data Sheet (DS987)](https://docs.xilinx.com/r/en-US/ds987-k26-som)
- [Kria SOM Carrier Card Design Guide (UG1091)](https://docs.xilinx.com/r/en-US/ug1091-carrier-card-design)内からリンクしてたどり着く XTP685(xtp685-kria-k26-som-xdc.zip) を解凍して得られる Kria_K26_SOM_Rev1.xdc
  
と、分かれておりなかなか不便です。

特に XTP685 はダウンロードに署名が必要であり、加工したものを勝手に再配布するわけにもいきません。

そこで、各自で正規手順で Kria_K26_SOM_Rev1.xdc を入手して、手元に置いて実行すれば、見やすいテーブルが生成されるスクリプトを作ってみました。

## 内容物

- k26-som-connector-pin.csv : DS987 内のテーブルを csv に変換したもの
- k26_som_xdc_to_csv.py : Kria_K26_SOM_Rev1.xdc を csv に変換する python スクリプト


## 使い方

pandas を使いますので、事前にインストールください。

```
pip install pandas
```

その後、入手した Kria_K26_SOM_Rev1.xdc をカレントディレクトリにコピーして

```
python make_table.py
```

と実行すれば、k26-som-xck26-sfvc784-pin.csv と kria-k26-som-pin.csv が生成されます。











