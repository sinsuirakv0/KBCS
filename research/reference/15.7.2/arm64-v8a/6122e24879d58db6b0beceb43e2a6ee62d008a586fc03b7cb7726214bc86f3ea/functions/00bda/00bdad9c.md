# 00bdad9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bdaea4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaea4.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bdad9c",
  "name": "_Znwm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e0d097a891612fbe969d9e379d8f12c24a4775fa996941e7029ddb6caecc5b6",
  "source_text_sha256": "6e0d097a891612fbe969d9e379d8f12c24a4775fa996941e7029ddb6caecc5b6"
}
~~~

## 呼び出し元

- [00bdaf40](../00bda/00bdaf40.md)

## 呼び出し先

- [00bdafa0](../00bda/00bdafa0.md)
- [00bdafc0](../00bda/00bdafc0.md)
- [00bdbaf0](../00bdb/00bdbaf0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)
- [00be1d20](../00be1/00be1d20.md)

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
      return;
    }
    pcVar2 = (code *)_ZSt15get_new_handlerv();
    if (pcVar2 == (code *)0x0) break;
    (*pcVar2)();
                    /* try { // try from 00bdadcc to 00cdadf3 has its CatchHandler @ 00bdadcc
                       catch() { ... } // from try @ 00bdadcc with catch @ 00bdadcc
                       catch() { ... } // from try @ 00bdae2c with catch @ 00bdadcc */
  }
  uVar3 = __cxa_allocate_exception(8);
  _ZNSt9bad_allocC2Ev();
                    /* try { // try from 00bdadf4 to 00cdae2b has its CatchHandler @ 00bdae5c */
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar3,PTR__ZTISt9bad_alloc_00c1aef8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c1af00);
}

~~~
