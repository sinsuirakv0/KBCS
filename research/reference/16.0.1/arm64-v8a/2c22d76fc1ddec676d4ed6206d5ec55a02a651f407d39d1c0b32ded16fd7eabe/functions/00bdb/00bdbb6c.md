# 00bdbb6c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bdbb6c",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e98a4822ad9572cd130b4125dca121ce42f8de9e081d6c2bc2e2719212c1c84c",
  "source_text_sha256": "e98a4822ad9572cd130b4125dca121ce42f8de9e081d6c2bc2e2719212c1c84c"
}
~~~

## 呼び出し元

- [00c5dde0](../00c5d/00c5dde0.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5ae40](../00c5a/00c5ae40.md)
- [00c5ddf0](../00c5d/00c5ddf0.md)

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
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_58,param_2,param_3,uVar2,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv_00c9b9e8
            );
  _ZN8firebase12FutureHandleC1ERKS0_(param_1,auStack_58);
  _ZN8firebase12FutureHandleD2Ev(auStack_58);
                    /* try { // try from 00bdbbe8 to 00cdbbf7 has its CatchHandler @ 00bdeec4 */
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00bdbbf8 to 00cdc323 has its CatchHandler @ 00bd6f4c */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
