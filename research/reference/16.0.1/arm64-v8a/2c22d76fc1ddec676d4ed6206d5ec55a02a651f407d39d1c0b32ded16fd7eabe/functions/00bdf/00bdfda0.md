# 00bdfda0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bdfda0",
  "name": "_ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d155173c8c7f9d834392d416373df0c37610d391417feed6646d33278c8256cc",
  "source_text_sha256": "d155173c8c7f9d834392d416373df0c37610d391417feed6646d33278c8256cc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dc00](../00c5d/00c5dc00.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dd30](../00c5d/00c5dd30.md)

## 疑似コード / UTF-8 3999 bytes

~~~c

void _ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE
               (long param_1,long param_2,undefined8 *param_3)

{
  long lVar1;
  undefined *puVar2;
  long *plVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined8 uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00bdfdb8 to 00cdfdbf has its CatchHandler @ 00be06c0 */
  lVar1 = tpidr_el0;
                    /* try { // try from 00bdfdc0 to 00cdfdcb has its CatchHandler @ 00be06bc */
  local_58 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00bdfdcc to 00cdfddf has its CatchHandler @ 00be06a0 */
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
                    /* try { // try from 00bdfe88 to 00cdfe93 has its CatchHandler @ 00be055c */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
                    /* try { // try from 00bdfe94 to 00cdfea7 has its CatchHandler @ 00be053c */
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
              (auStack_68,lVar9,0x12);
                    /* try { // try from 00bdfdf8 to 00cdfe07 has its CatchHandler @ 00be0680 */
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar4 = FUN_00497834(plVar3,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126d60,
                         *param_3);
                    /* try { // try from 00bdfe20 to 00cdfe2b has its CatchHandler @ 00be0660 */
                    /* try { // try from 00bdfe2c to 00cdfe3b has its CatchHandler @ 00be0624 */
    uVar5 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar3,lVar9,auStack_68);
    if ((uVar5 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      puVar10 = *(undefined8 **)(param_2 + 0x98);
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar7 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_78);
      puVar2 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9ba20
      ;
                    /* try { // try from 00bdfe68 to 00cdfe6f has its CatchHandler @ 00be0740 */
      *(undefined8 **)(lVar7 + 0x10) = puVar10;
      *(undefined **)(lVar7 + 0x18) = puVar2;
                    /* try { // try from 00bdfe78 to 00cdfe87 has its CatchHandler @ 00be0570 */
      if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
        lVar8 = (long)puVar10 + 0x141;
      }
      else {
        lVar8 = puVar10[0x2a];
      }
                    /* try { // try from 00bdfec0 to 00cdfecb has its CatchHandler @ 00be0508 */
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar4,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba00
                 ,lVar7,lVar8);
      _ZN8firebase12FutureHandleD2Ev(auStack_78);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
    }
                    /* try { // try from 00bdfeec to 00cdff13 has its CatchHandler @ 00be0740 */
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_68);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* try { // try from 00bdff18 to 00cdff1b has its CatchHandler @ 00be0778 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
