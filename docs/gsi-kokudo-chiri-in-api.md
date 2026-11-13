---
tags:
    - tech
---
# 国土地理院API
## 住所から緯度経度（ジオコーディング）
`https://msearch.gsi.go.jp/address-search/AddressSearch?q=【住所】`

（返却形式: JSONの geometry.coordinates に [経度, 緯度] で格納）
## 緯度経度から住所（逆ジオコーディング）
`https://mreversegeocoder.gsi.go.jp/reverse-geocoder/LonLatToAddress?lat=【緯度】&lon=【経度】`

（返却形式: JSONで市区町村コードや町字名を取得）

（2026年11月12日現在、タイムアウトエラーになる）

OSMを使った <https://nominatim.org/release-docs/latest/api/Reverse/> こういうのもある。

## 緯度経度から標高（海抜高）
`https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon=【経度】&lat=【緯度】&outtype=JSON`

（返却形式: JSONの elevation にメートル単位で格納）

## メモ
Comapsで記録したデータの標高がずれるのは
ジオイド補正というのがされていないから、らしい。

## 関連
- [国土地理院基盤地図情報](./gsi-kokudo-chiri-in-data.md)
## リンク
<https://maps.gsi.go.jp/help/tech.html>
