# 007aeedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007aeedc",
  "name": "FUN_007aeedc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0edc2898be99fbe0cbd645cc583a434960bf48e6337505d89e5de3b4b5f2fd78",
  "source_text_sha256": "0edc2898be99fbe0cbd645cc583a434960bf48e6337505d89e5de3b4b5f2fd78"
}
~~~

## 呼び出し元

- [007ad944](../007ad/007ad944.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 168 bytes

~~~c

void FUN_007aeedc(void *param_1)

{
  if ((*(byte *)((long)param_1 + 8) & 1) != 0) {
    _ZdlPv(*(void **)((long)param_1 + 0x18));
  }
  _ZdlPv(param_1);
  return;
}

~~~
