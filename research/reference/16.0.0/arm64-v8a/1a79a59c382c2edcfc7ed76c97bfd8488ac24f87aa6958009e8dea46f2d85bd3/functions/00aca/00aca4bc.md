# 00aca4bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aca4bc",
  "name": "FUN_00aca4bc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8fb8009f2be3fa5e2ec23b593376268ed3c52ed207722452b4371a2ff546171",
  "source_text_sha256": "d8fb8009f2be3fa5e2ec23b593376268ed3c52ed207722452b4371a2ff546171"
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [00a79a0c](../00a79/00a79a0c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [00ac9580](../00ac9/00ac9580.md)

## 疑似コード / UTF-8 128 bytes

~~~c

void FUN_00aca4bc(long param_1)

{
  if (*(char *)(param_1 + 0x3c) != '\0') {
    FUN_00ac9580();
    return;
  }
  return;
}

~~~
