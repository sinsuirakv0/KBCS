# 00af2afc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af2afc",
  "name": "FUN_00af2afc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a19b4035134673fd463f9a4702d2307ff47fafee909bb9c2add169e0f1629bcb",
  "source_text_sha256": "a19b4035134673fd463f9a4702d2307ff47fafee909bb9c2add169e0f1629bcb"
}
~~~

## 呼び出し元

- [005fdc18](../005fd/005fdc18.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 155 bytes

~~~c

undefined4 FUN_00af2afc(int param_1)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + 0x84920);
}

~~~
