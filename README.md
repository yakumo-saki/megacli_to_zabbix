# MegaCli to zabbix

megacli を使用して取得したRAIDアレイの情報をZABBIXに送信します。
Linuxに対応しています。
外部コマンドとしてMegaCliに依存します。なお、zabbix_senderは使用しません。

## 使い方

### 起動

`python3 megacli_to_zabbix.py [adp|pd|vd]`

特に指定しなければ adp, pd , vd をすべて実行。

### MegaCLIの出力をファイルに落としてそれを読み込みたい場合

`python3 megacli_to_zabbix.py [adp|pd|vd] filepath` 

想定しているコマンドは以下の通り

* adp: MegaCli64 -Adpallinfo -Aall
* pd: MegaCli64  -Pdlist -Aall
* vd: MegaCli64 -Ldinfo -Lall -Aall

## 初めての場合

### 一式を取得

`git clone https://github.com/yakumo-saki/megacli_to_zabbix.git`

### 設定

環境変数で設定可能です。設定可能項目は以下の通り。

| 変数名 | 設定例 | 用途 | 
| ZABBIX_SERVER | 192.168.1.123 | Zabbixサーバーのホスト名orIPアドレス。省略不可 |
| ZABBIX_PORT | 10051 | Zabbixサーバーのポート。省略時は10051 |
| ZABBIX_HOST | test | Zabbixホスト名。省略不可 |

#### 設定方法

以下の2つの方法があります。同時に行われた場合は、exportされた環境変数が優先されます。

##### exportで設定する 

```
export ZABBIX_SERVER=192.168.1.123
export ZABBIX_PORT=10051
export ZABBIX_HOST=test
```

##### .envファイルで設定する

.env.sample ファイルを .env にコピーして内容を編集してください。
.envファイルは存在しなくても動作します。

### Zabbixにテンプレートを登録する

Zabbixの設定 → テンプレート → インポート（右上） を押す
`zabbix_templates/zbx_export_templates.xml` を選択。

### ホストにテンプレートを紐付け

`MegaCLI to ZABBIX xxxxxxxx by yakumo-saki` テンプレートをホストに紐付け。
（テンプレート名がアレだと思う場合はリネームしてください。）

## known issue

* （特にテンプレートに値を追加したとき）discovery後にアイテムが生成されるのに時間がかかり（？）値の送信がfailedになることがある。
