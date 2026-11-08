# 00bafaf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bafaf4",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "975907a8ae54983651d58d8323847def352da2816f62eb4662a67826a74c835d",
  "source_text_sha256": "975907a8ae54983651d58d8323847def352da2816f62eb4662a67826a74c835d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bafb60](../00baf/00bafb60.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)

## 疑似コード / UTF-8 404 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv(void)

{
  int iVar1;
  
  if (((DAT_010a2aa8 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_010a2aa8), iVar1 != 0)) {
    FUN_00bafb60();
    DAT_010a2aa0 = &DAT_010a2ba0;
    __cxa_guard_release(&DAT_010a2aa8);
                    /* try { // try from 00bafb5c to 00cafbab has its CatchHandler @ 00bb0d00 */
  }
  return DAT_010a2aa0;
}

~~~
