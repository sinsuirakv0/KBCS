# 00bdaea4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bdad9c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad9c.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bdaea4",
  "name": "_Znwm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8df75496413a9d600368ca2ba604d3d5a8ab7c3a8f627e5764d7dbc1c74c3e7c",
  "source_text_sha256": "8df75496413a9d600368ca2ba604d3d5a8ab7c3a8f627e5764d7dbc1c74c3e7c"
}
~~~

## 呼び出し元

- [00bdb040](../00bdb/00bdb040.md)

## 呼び出し先

- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb0c0](../00bdb/00bdb0c0.md)
- [00bdbbf0](../00bdb/00bdbbf0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00be1e20](../00be1/00be1e20.md)

## 疑似コード / UTF-8 923 bytes

~~~c

void _Znwm(size_t param_1)

{
  void *pvVar1;
  code *pcVar2;
  undefined8 uVar3;
  
  if (param_1 < 2) {
    param_1 = 1;
  }
  while( true ) {
    pvVar1 = malloc(param_1);
    if (pvVar1 != (void *)0x0) {
                    /* try { // try from 00bdaed8 to 00cdaeff has its CatchHandler @ 00bdaed8
                       catch() { ... } // from try @ 00bdaed8 with catch @ 00bdaed8
                       catch() { ... } // from try @ 00bdaf38 with catch @ 00bdaed8 */
      return;
    }
    pcVar2 = (code *)_ZSt15get_new_handlerv();
    if (pcVar2 == (code *)0x0) break;
    (*pcVar2)();
  }
  uVar3 = __cxa_allocate_exception(8);
  _ZNSt9bad_allocC2Ev();
                    /* try { // try from 00bdaf00 to 00cdaf37 has its CatchHandler @ 00bdaf68 */
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar3,PTR__ZTISt9bad_alloc_00c1aff8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c1b000);
}

~~~
