# 00bdcbfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdcbfc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17c43a04429a38f182a28960e32ae6c6bfc6427b5268e52b1c3da3f742dc0236",
  "source_text_sha256": "17c43a04429a38f182a28960e32ae6c6bfc6427b5268e52b1c3da3f742dc0236"
}
~~~

## 呼び出し元

- [00c5ee80](../00c5e/00c5ee80.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5bee0](../00c5b/00c5bee0.md)
- [00c5ee90](../00c5e/00c5ee90.md)

## 疑似コード / UTF-8 1111 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_
               (undefined8 param_1,undefined8 param_2,undefined4 param_3,undefined8 param_4)

{
  long lVar1;
  undefined8 uVar2;
  undefined1 auStack_58 [16];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = _Znwm(0x138);
  _ZN8firebase4auth10AuthResultC2ERKS1_(uVar2,param_4);
                    /* try { // try from 00bdcc4c to 00cdcc5b has its CatchHandler @ 00bdff28 */
                    /* try { // try from 00bdcc5c to 00cdd387 has its CatchHandler @ 00bd7fb0 */
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_58,param_2,param_3,uVar2,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv_00c9ca88
            );
  _ZN8firebase12FutureHandleC1ERKS0_(param_1,auStack_58);
  _ZN8firebase12FutureHandleD2Ev(auStack_58);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
