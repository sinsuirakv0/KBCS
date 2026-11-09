# 00c2caec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00c2caec",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5d22c7149ff271b7cd0aac626b542d16846daa23afeb043d125f00283e45ee1",
  "source_text_sha256": "f5d22c7149ff271b7cd0aac626b542d16846daa23afeb043d125f00283e45ee1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c2cb6c](../00c2c/00c2cb6c.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)

## 疑似コード / UTF-8 307 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv(void)

{
  int iVar1;
  
  if (((DAT_01127ac0 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127ac0), iVar1 != 0)) {
    FUN_00c2cb6c();
    DAT_01127ab8 = &DAT_01127d00;
    __cxa_guard_release(&DAT_01127ac0);
  }
  return DAT_01127ab8;
}

~~~
