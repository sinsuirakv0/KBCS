# 00bafaf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bafaf4.md)

## 関数情報

~~~json
{
  "address": "00bafaf4",
  "name": "std::__ndk1::__time_get_c_storage<char>::__weeks",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29ea55e8643f2480ef1186efda785a10352e2e8f11abd170911e63917af10496",
  "source_text_sha256": "29ea55e8643f2480ef1186efda785a10352e2e8f11abd170911e63917af10496"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bafb60](../00baf/00bafb60.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)

## 疑似コード 1/1 / UTF-8 485 bytes

~~~c

/* std::__ndk1::__time_get_c_storage<char>::__weeks() const */

undefined1 * std::__ndk1::__time_get_c_storage<char>::__weeks(void)

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
