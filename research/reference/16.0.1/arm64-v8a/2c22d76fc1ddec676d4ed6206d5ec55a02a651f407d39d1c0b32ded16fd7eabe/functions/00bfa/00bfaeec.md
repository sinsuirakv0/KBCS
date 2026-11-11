# 00bfaeec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfaeec",
  "name": "_ZNSt6__ndk117iostream_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f475e7628c8811590bcd4c0b128ddc9327a9dc40ae279fa30aff00e83a44b70",
  "source_text_sha256": "8f475e7628c8811590bcd4c0b128ddc9327a9dc40ae279fa30aff00e83a44b70"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)

## 疑似コード / UTF-8 243 bytes

~~~c

undefined ** _ZNSt6__ndk117iostream_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01127390 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127390), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01127390);
  }
  return &PTR_PTR_00ca4800;
}

~~~
