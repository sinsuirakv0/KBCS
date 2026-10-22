# 00b0edbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b0edbc.md)

## 関数情報

~~~json
{
  "address": "00b0edbc",
  "name": "flatbuffers::Parser::Warning",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab050f2ebc7822d0780a5d6a11f2d7f257d9cb99ee6cc19a107d787c58e9d0c5",
  "source_text_sha256": "ab050f2ebc7822d0780a5d6a11f2d7f257d9cb99ee6cc19a107d787c58e9d0c5"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdf8d0](../00bdf/00bdf8d0.md)

## 関連文字列（未確認候補）

~~~text
"warning: "
~~~
## 疑似コード 1/1 / UTF-8 1594 bytes

~~~c

/* flatbuffers::Parser::Warning(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> > const&) */

void flatbuffers::Parser::Warning(basic_string *param_1)

{
  long lVar1;
  char *in_x1;
  basic_string *in_x2;
  basic_string local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  std::__ndk1::operator+((__ndk1 *)"warning: ",in_x1,in_x2);
  Message((Parser *)param_1,local_40);
  if (((byte)local_40[0] & 1) != 0) {
    operator_delete(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00b0ee28 to 00c0eef7 has its CatchHandler @ 00b0ee28
                       catch() { ... } // from try @ 00b0ee28 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0ef18 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f028 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f0a8 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f17c with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f2b0 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f4b4 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f5d4 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f744 with catch @ 00b0ee28 */
  __stack_chk_fail();
}

~~~
