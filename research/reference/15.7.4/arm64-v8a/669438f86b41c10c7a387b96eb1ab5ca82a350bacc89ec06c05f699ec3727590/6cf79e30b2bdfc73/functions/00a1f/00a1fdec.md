# 00a1fdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00a1fdec.md)

## 関数情報

~~~json
{
  "address": "00a1fdec",
  "name": "FUN_00a1fdec",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8060844e4292cb0105d28455cc2b5d22b7d7418fc3f6ae5217e4f36042264052",
  "source_text_sha256": "8060844e4292cb0105d28455cc2b5d22b7d7418fc3f6ae5217e4f36042264052"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード 1/1 / UTF-8 515 bytes

~~~c

void FUN_00a1fdec(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00a1fdf0 to 00b1fdfb has its CatchHandler @ 00a2a8c8 */
                    /* try { // try from 00a1fdfc to 00b1fe0f has its CatchHandler @ 00a2a8a4 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00a1fe10 to 00b1fe37 has its CatchHandler @ 00a2a878 */
  *puVar1 = &PTR_FUN_00c0c400;
  puVar1[1] = uVar2;
  return;
}

~~~
