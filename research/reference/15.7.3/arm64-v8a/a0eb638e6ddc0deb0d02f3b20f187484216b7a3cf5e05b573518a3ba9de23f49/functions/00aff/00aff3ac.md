# 00aff3ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aff3ac",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8f2b9e76245a92640bc8a89ff7af82762c46eedf8000f8838409ff0371a3aa9",
  "source_text_sha256": "c8f2b9e76245a92640bc8a89ff7af82762c46eedf8000f8838409ff0371a3aa9"
}
~~~

## 呼び出し元

- [00bddfb0](../00bdd/00bddfb0.md)

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

## 疑似コード / UTF-8 2805 bytes

~~~c

long _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(long param_1,ulong param_2)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  long *plVar4;
  
                    /* catch() { ... } // from try @ 00afceac with catch @ 00aff3ac */
                    /* catch() { ... } // from try @ 00afce7c with catch @ 00aff3b0 */
                    /* catch() { ... } // from try @ 00afcdc8 with catch @ 00aff3b8 */
                    /* catch() { ... } // from try @ 00afcd98 with catch @ 00aff3bc */
                    /* catch() { ... } // from try @ 00afcd68 with catch @ 00aff3c4 */
                    /* catch() { ... } // from try @ 00afccdc with catch @ 00aff3c8 */
                    /* catch() { ... } // from try @ 00afccac with catch @ 00aff3cc */
  _ZN8firebase5Mutex7AcquireEv(param_1 + 8);
  plVar4 = (long *)(param_1 + 0x38);
  plVar2 = (long *)*plVar4;
                    /* catch() { ... } // from try @ 00afcbf4 with catch @ 00aff3d4 */
  plVar1 = plVar4;
  if (plVar2 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00afcae8 with catch @ 00aff3dc */
                    /* catch() { ... } // from try @ 00afca2c with catch @ 00aff3e4 */
                    /* catch() { ... } // from try @ 00afc9fc with catch @ 00aff3e8 */
      if ((ulong)plVar2[4] >= param_2) {
        plVar1 = plVar2;
      }
      plVar2 = (long *)plVar2[(ulong)plVar2[4] < param_2];
                    /* catch() { ... } // from try @ 00afc9cc with catch @ 00aff3f0 */
    } while (plVar2 != (long *)0x0);
                    /* catch() { ... } // from try @ 00afc934 with catch @ 00aff3f4 */
                    /* catch() { ... } // from try @ 00afbdd8 with catch @ 00aff3f8 */
    if ((plVar1 != plVar4) && ((ulong)plVar1[4] <= param_2)) {
                    /* catch() { ... } // from try @ 00afbc98 with catch @ 00aff410 */
      lVar3 = plVar1[5];
      goto LAB_00aff414;
    }
  }
                    /* catch() { ... } // from try @ 00afbd90 with catch @ 00aff408 */
  lVar3 = 0;
                    /* catch() { ... } // from try @ 00afbd40 with catch @ 00aff40c */
LAB_00aff414:
                    /* catch() { ... } // from try @ 00afbbfc with catch @ 00aff414 */
                    /* catch() { ... } // from try @ 00afbbcc with catch @ 00aff418 */
  _ZN8firebase5Mutex7ReleaseEv(param_1 + 8);
                    /* catch() { ... } // from try @ 00afbba0 with catch @ 00aff41c */
                    /* catch() { ... } // from try @ 00afbb70 with catch @ 00aff420 */
                    /* catch() { ... } // from try @ 00afbb30 with catch @ 00aff424 */
                    /* catch() { ... } // from try @ 00afbb00 with catch @ 00aff428 */
                    /* catch() { ... } // from try @ 00afbad4 with catch @ 00aff42c */
  return lVar3;
}

~~~
