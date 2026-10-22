# 00bdad9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdad9c.md)

## 関数情報

~~~json
{
  "address": "00bdad9c",
  "name": "operator.new",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "546115caf3801888d1dd8e0afe168579545892b38f9cf8a97bf91aff12ca1671",
  "source_text_sha256": "546115caf3801888d1dd8e0afe168579545892b38f9cf8a97bf91aff12ca1671"
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

## 疑似コード 1/1 / UTF-8 1005 bytes

~~~c

/* operator new(unsigned long) */

void * operator_new(ulong param_1)

{
  void *pvVar1;
  code *pcVar2;
  bad_alloc *this;
  
  if (param_1 < 2) {
    param_1 = 1;
  }
  while( true ) {
    pvVar1 = malloc(param_1);
    if (pvVar1 != (void *)0x0) {
      return pvVar1;
    }
    pcVar2 = (code *)std::get_new_handler();
    if (pcVar2 == (code *)0x0) break;
    (*pcVar2)();
                    /* try { // try from 00bdadcc to 00cdadf3 has its CatchHandler @ 00bdadcc
                       catch() { ... } // from try @ 00bdadcc with catch @ 00bdadcc
                       catch() { ... } // from try @ 00bdae2c with catch @ 00bdadcc */
  }
  this = (bad_alloc *)__cxa_allocate_exception(8);
  std::bad_alloc::bad_alloc(this);
                    /* try { // try from 00bdadf4 to 00cdae2b has its CatchHandler @ 00bdae5c */
                    /* WARNING: Subroutine does not return */
  __cxa_throw(this,PTR_typeinfo_00c1aef8,PTR__bad_array_new_length_00c1af00);
}

~~~
