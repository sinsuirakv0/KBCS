# 00bcef9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcef9c",
  "name": "_ZN8firebase4auth4Auth14UseAppLanguageEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67526a7909c327e15ebe1e116e5b7fd827281f1a09e9a47c887418c4b5300b11",
  "source_text_sha256": "67526a7909c327e15ebe1e116e5b7fd827281f1a09e9a47c887418c4b5300b11"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574cac](../00574/00574cac.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 疑似コード / UTF-8 643 bytes

~~~c

void _ZN8firebase4auth4Auth14UseAppLanguageEv(long *param_1)

{
  undefined8 uVar1;
  
  if ((undefined8 *)*param_1 != (undefined8 *)0x0) {
    uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
                    /* try { // try from 00bcefbc to 00ccf247 has its CatchHandler @ 00bcefbc
                       catch() { ... } // from try @ 00bcefbc with catch @ 00bcefbc
                       catch() { ... } // from try @ 00bcf250 with catch @ 00bcefbc */
    FUN_00574cac(uVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_01126358);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
    return;
  }
  return;
}

~~~
