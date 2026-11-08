# 00affa2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00affa2c",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d53e6a9e91a065ed42626fbb2bd1b28fadbf90b30728853e89b42ab3d0ef65e",
  "source_text_sha256": "9d53e6a9e91a065ed42626fbb2bd1b28fadbf90b30728853e89b42ab3d0ef65e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

## 疑似コード / UTF-8 1596 bytes

~~~c

undefined4
_ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  undefined4 uVar4;
  long *plVar5;
  undefined4 *puVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af6188 with catch @ 00affa38 */
  lVar1 = param_1 + 8;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar5 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar5;
  plVar2 = plVar5;
  if (plVar3 == (long *)0x0) {
LAB_00affa94:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af617c with catch @ 00affa8c */
    if ((plVar2 == plVar5) || (uVar7 < (ulong)plVar2[4])) goto LAB_00affa94;
                    /* catch() { ... } // from try @ 00af60a4 with catch @ 00affabc */
    puVar6 = (undefined4 *)plVar2[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af6094 with catch @ 00affac8 */
    if (puVar6 != (undefined4 *)0x0) {
      uVar4 = *puVar6;
                    /* catch() { ... } // from try @ 00af6078 with catch @ 00affad0 */
      goto LAB_00affaa0;
    }
  }
  uVar4 = 2;
LAB_00affaa0:
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af612c with catch @ 00affaac */
  return uVar4;
}

~~~
