# 00c2dfdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00c2dfdc",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE3__cEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afef491d8d40edb7d987125c8bbbe1b20d89fc82d1aeb1d93a7a8f723db869df",
  "source_text_sha256": "afef491d8d40edb7d987125c8bbbe1b20d89fc82d1aeb1d93a7a8f723db869df"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)

## 関連文字列（未確認候補）

~~~text
"(%a %b %d %H:%M:%S %Y"
~~~

## 疑似コード / UTF-8 784 bytes

~~~c

char * _ZNKSt6__ndk120__time_get_c_storageIcE3__cEv(void)

{
  int iVar1;
  
  if (((DAT_01127b58 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127b58), iVar1 != 0)) {
    __cxa_atexit(PTR__ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev_00c9a7f8
                 ,s___a__b__d__H__M__S__Y_00ca4440,&PTR_LOOP_00c62b90);
                    /* catch() { ... } // from try @ 00c2db08 with catch @ 00c2e038 */
                    /* catch() { ... } // from try @ 00c2da80 with catch @ 00c2e03c */
                    /* catch() { ... } // from try @ 00c2d9f8 with catch @ 00c2e040 */
    __cxa_guard_release(&DAT_01127b58);
                    /* catch() { ... } // from try @ 00c2d968 with catch @ 00c2e044 */
  }
  return s___a__b__d__H__M__S__Y_00ca4440;
}

~~~
