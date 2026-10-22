# 00aaede0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aaede0.md)

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
  "source_sha256": "b69462e3286e778ed03f2baed84b6b6271b6048fe0ef4df32e870292647017de",
  "source_text_sha256": "b69462e3286e778ed03f2baed84b6b6271b6048fe0ef4df32e870292647017de"
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

## 疑似コード 1/1 / UTF-8 256 bytes

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
