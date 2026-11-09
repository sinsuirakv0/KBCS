# 00ac1aec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00ac1aec",
  "name": "FUN_00ac1aec",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "11b9218a203934f242ba19781223e1077799d3860be3e3144323c93578f420e6",
  "source_text_sha256": "11b9218a203934f242ba19781223e1077799d3860be3e3144323c93578f420e6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)

## 疑似コード / UTF-8 502 bytes

~~~c

void FUN_00ac1aec(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
                    /* try { // try from 00ac1b04 to 00bc1b0f has its CatchHandler @ 00ac23f8 */
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00ac1b10 to 00bc1b1f has its CatchHandler @ 00ac23d8 */
  *puVar1 = &PTR_FUN_00c8cf20;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
  return;
}

~~~
