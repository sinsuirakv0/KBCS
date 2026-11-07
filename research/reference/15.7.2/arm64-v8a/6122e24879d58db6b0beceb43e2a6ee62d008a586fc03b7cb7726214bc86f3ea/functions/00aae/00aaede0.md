# 00aaede0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aaeeec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaeeec.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aaede0",
  "name": "FUN_00aaede0",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bbe945ff31a8be7ce2466e0782e490f244b4bb40f4a109d7e77089a45d50e64d",
  "source_text_sha256": "bbe945ff31a8be7ce2466e0782e490f244b4bb40f4a109d7e77089a45d50e64d"
}
~~~

## 呼び出し元

- [00695904](../00695/00695904.md)
- [0081c6a0](../0081c/0081c6a0.md)
- [009a2998](../009a2/009a2998.md)
- [009bd6b8](../009bd/009bd6b8.md)
- [009eadc8](../009ea/009eadc8.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 243 bytes

~~~c

void FUN_00aaede0(undefined8 *param_1)

{
  *(undefined1 *)((long)param_1 + 0x2c) = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  *param_1 = 0;
  *(undefined8 *)((long)param_1 + 0x1c) = 0;
  *(undefined4 *)((long)param_1 + 0x24) = 0;
  return;
}

~~~
