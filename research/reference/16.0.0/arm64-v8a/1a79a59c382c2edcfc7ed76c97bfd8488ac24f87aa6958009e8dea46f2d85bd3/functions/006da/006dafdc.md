# 006dafdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "006dafdc",
  "name": "FUN_006dafdc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01727eb86aa498afba91932f53d48032b909896b0ad395ae6d5328cbc0caf44a",
  "source_text_sha256": "01727eb86aa498afba91932f53d48032b909896b0ad395ae6d5328cbc0caf44a"
}
~~~

## 呼び出し元

- [00a2b0f0](../00a2b/00a2b0f0.md)

## 呼び出し先

- [00480af8](../00480/00480af8.md)
- [00480b50](../00480/00480b50.md)
- [00480d08](../00480/00480d08.md)
- [00481058](../00481/00481058.md)

## 疑似コード / UTF-8 255 bytes

~~~c

void FUN_006dafdc(undefined4 *param_1,undefined8 param_2)

{
  FUN_00480b50(param_2,*param_1);
  FUN_00481058(*(undefined8 *)(param_1 + 2),param_2);
  FUN_00480af8(param_2,param_1[4]);
  FUN_00480d08(param_2,*(undefined1 *)(param_1 + 0xe));
  return;
}

~~~
