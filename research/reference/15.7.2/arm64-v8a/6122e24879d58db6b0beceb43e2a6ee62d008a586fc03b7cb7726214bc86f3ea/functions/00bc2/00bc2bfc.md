# 00bc2bfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bc2bfc.md)

## 関数情報

~~~json
{
  "address": "00bc2bfc",
  "name": "FUN_00bc2bfc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c14e5ac9cd511dd03a784fdb6e4c7751835d64c86bc0115a693ec6cb36db0330",
  "source_text_sha256": "c14e5ac9cd511dd03a784fdb6e4c7751835d64c86bc0115a693ec6cb36db0330"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 692 bytes

~~~c

byte FUN_00bc2bfc(long param_1)

{
  byte bVar1;
  long *plVar2;
  
  if ((*(byte *)(param_1 + 0x20) & 1) == 0) {
    plVar2 = *(long **)(param_1 + 0x18);
    *(undefined1 *)(param_1 + 0x20) = 1;
                    /* try { // try from 00bc2c30 to 00cc2c37 has its CatchHandler @ 00bc8844 */
    if ((*(byte *)((long)plVar2 + 10) & 3) == 2) {
      bVar1 = (**(code **)(*plVar2 + 8))(plVar2);
    }
    else {
      bVar1 = (*(byte *)((long)plVar2 + 10) & 3) == 0;
    }
    *(undefined1 *)(param_1 + 0x20) = 0;
  }
  else {
    bVar1 = 0;
  }
                    /* try { // try from 00bc2c64 to 00cc2ce3 has its CatchHandler @ 00bc89fc */
  return bVar1 & 1;
}

~~~
