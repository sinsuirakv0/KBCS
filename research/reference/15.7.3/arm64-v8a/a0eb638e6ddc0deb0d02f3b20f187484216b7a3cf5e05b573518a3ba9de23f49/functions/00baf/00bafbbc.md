# 00bafbbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bafbbc",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0a70d9c0e8d33346251f1a55172e67db7ae130e612c7f1d5a1fef0c5f8093ef",
  "source_text_sha256": "b0a70d9c0e8d33346251f1a55172e67db7ae130e612c7f1d5a1fef0c5f8093ef"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bafc28](../00baf/00bafc28.md)
- [00bdafb0](../00bda/00bdafb0.md)
- [00bdafd0](../00bda/00bdafd0.md)

## 疑似コード / UTF-8 404 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv(void)

{
  int iVar1;
  
  if (((DAT_010a2b68 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_010a2b68), iVar1 != 0)) {
    FUN_00bafc28();
    DAT_010a2b60 = &DAT_010a2c60;
    __cxa_guard_release(&DAT_010a2b68);
                    /* try { // try from 00bafc24 to 00cafc73 has its CatchHandler @ 00bb0dc8 */
  }
  return DAT_010a2b60;
}

~~~
