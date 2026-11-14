# 00bfbf7c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfbf7c",
  "name": "_ZNSt6__ndk117iostream_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dce136c0224875bfd9511dc82621a8ceaf038f0778d5671f2820e9a63e98776c",
  "source_text_sha256": "dce136c0224875bfd9511dc82621a8ceaf038f0778d5671f2820e9a63e98776c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58ef0](../00c58/00c58ef0.md)
- [00c58f10](../00c58/00c58f10.md)

## 疑似コード / UTF-8 243 bytes

~~~c

undefined ** _ZNSt6__ndk117iostream_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01128450 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01128450), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01128450);
  }
  return &PTR_PTR_00ca58a0;
}

~~~
