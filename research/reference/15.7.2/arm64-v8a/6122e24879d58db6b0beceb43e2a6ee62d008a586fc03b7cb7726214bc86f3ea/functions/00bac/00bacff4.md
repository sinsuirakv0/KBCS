# 00bacff4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bad100`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad100.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bacff4",
  "name": "_ZNKSt6__ndk17codecvtIDiDu9mbstate_tE9do_lengthERS1_PKDuS5_m",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b459b08321f23ed85eb196d23987470bb61d71801ca5460ff77eba518b14b4e4",
  "source_text_sha256": "b459b08321f23ed85eb196d23987470bb61d71801ca5460ff77eba518b14b4e4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bacc20](../00bac/00bacc20.md)

## 疑似コード / UTF-8 350 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDiDu9mbstate_tE9do_lengthERS1_PKDuS5_m
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
                    /* catch() { ... } // from try @ 00bace54 with catch @ 00bacff8 */
  FUN_00bacc20(param_3,param_4,param_5,0x10ffff,0);
  return;
}

~~~
