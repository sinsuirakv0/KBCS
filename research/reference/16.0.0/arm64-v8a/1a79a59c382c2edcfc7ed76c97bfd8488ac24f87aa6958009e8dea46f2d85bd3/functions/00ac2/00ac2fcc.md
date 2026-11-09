# 00ac2fcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00ac2fcc",
  "name": "FUN_00ac2fcc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96fd3067ed80ab2c33226bb442bdfca2b8b6b367e4bec66491b56c721d7919b8",
  "source_text_sha256": "96fd3067ed80ab2c33226bb442bdfca2b8b6b367e4bec66491b56c721d7919b8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b79cc](../008b7/008b79cc.md)
- [00abf2b4](../00abf/00abf2b4.md)

## 疑似コード / UTF-8 552 bytes

~~~c

void FUN_00ac2fcc(long param_1)

{
  long lVar1;
  
  lVar1 = *(long *)(param_1 + 8);
  FUN_00abf2b4(param_1,1);
  if ((*(byte *)(lVar1 + 0x1aec) & 1) != 0) {
                    /* try { // try from 00ac2ff8 to 00bc2ffb has its CatchHandler @ 00ac3114 */
                    /* try { // try from 00ac2ffc to 00bc30b3 has its CatchHandler @ 00ac2c48 */
    return;
  }
  *(undefined1 *)(lVar1 + 0x1aec) = 1;
  *(undefined4 *)((long)&QWORD_0039b1b4 + lVar1) = 2;
  *(undefined4 *)(lVar1 + 0x3478) = 0x22;
  FUN_008b79cc(lVar1 + 0x2f38,0);
  return;
}

~~~
