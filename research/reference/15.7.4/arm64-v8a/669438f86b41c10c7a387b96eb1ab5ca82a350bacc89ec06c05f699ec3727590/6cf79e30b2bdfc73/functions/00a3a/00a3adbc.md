# 00a3adbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00a3adbc.md)

## 関数情報

~~~json
{
  "address": "00a3adbc",
  "name": "FUN_00a3adbc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35a78429e0ace9c42412fde99538ab910470c948d3a50c6871fc94bc0385436e",
  "source_text_sha256": "35a78429e0ace9c42412fde99538ab910470c948d3a50c6871fc94bc0385436e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード 1/1 / UTF-8 502 bytes

~~~c

void FUN_00a3adbc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00a3add8 to 00b3ade7 has its CatchHandler @ 00a421f8 */
  *puVar1 = &PTR_FUN_00c0cc38;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
                    /* try { // try from 00a3ade8 to 00b3ae6f has its CatchHandler @ 00a2e43c */
  return;
}

~~~
