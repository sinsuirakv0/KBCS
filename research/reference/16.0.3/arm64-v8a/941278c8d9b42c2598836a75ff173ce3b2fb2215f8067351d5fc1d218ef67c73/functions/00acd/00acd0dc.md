# 00acd0dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00acd0dc",
  "name": "FUN_00acd0dc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ebf3ccc3a82992e29a2035d07d06ac1e657259aca842cdc0cc6fa2ff95c9920c",
  "source_text_sha256": "ebf3ccc3a82992e29a2035d07d06ac1e657259aca842cdc0cc6fa2ff95c9920c"
}
~~~

## 呼び出し元

- [00accdb0](../00acc/00accdb0.md)

## 呼び出し先

- [00accaec](../00acc/00accaec.md)
- [00c58f50](../00c58/00c58f50.md)

## 疑似コード / UTF-8 195 bytes

~~~c

void FUN_00acd0dc(long param_1)

{
  void *__ptr;
  
  __ptr = *(void **)(param_1 + 0x18);
  if (__ptr != (void *)0x0) {
    FUN_00accaec(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
