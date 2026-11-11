# 00bbcab4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bbcab4",
  "name": "FUN_00bbcab4",
  "size": 592,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "350cb53bad5dcbc3c2495683574a8cf1a746d387ae68f396988f4bf2ba7ff1ea",
  "source_text_sha256": "350cb53bad5dcbc3c2495683574a8cf1a746d387ae68f396988f4bf2ba7ff1ea"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53f5c](../00c53/00c53f5c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58000](../00c58/00c58000.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ad60](../00c5a/00c5ad60.md)
- [00c5ade0](../00c5a/00c5ade0.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5b090](../00c5b/00c5b090.md)
- [00c5b390](../00c5b/00c5b390.md)
- [00c5b5c0](../00c5b/00c5b5c0.md)
- [00c5d270](../00c5d/00c5d270.md)

## 関連文字列（未確認候補）

~~~text
"Failed to complete Future as it was likely already deleted."
~~~

## 疑似コード / UTF-8 3585 bytes

~~~c

void FUN_00bbcab4(undefined8 param_1,long param_2,int param_3,undefined8 param_4,void *param_5)

{
  long lVar1;
  ulong __n;
  undefined1 *__src;
  long lVar2;
  undefined8 uVar3;
  undefined1 *__dest;
  ulong uVar4;
  undefined1 auStack_b0 [16];
  ulong local_a0;
  ulong uStack_98;
  undefined1 *local_90;
  ulong local_80;
  ulong uStack_78;
  undefined1 *local_70;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
            (&local_a0,&DAT_002a63ea);
  if ((param_2 != 0) && (param_3 == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_80,param_1,param_2);
    if ((local_a0 & 1) != 0) {
      *local_90 = 0;
      uStack_98 = 0;
      if ((local_a0 & 1) != 0) {
        _ZdlPv(local_90);
      }
    }
    uStack_98 = uStack_78;
    local_a0 = local_80;
    local_90 = local_70;
  }
  _ZN8firebase5Mutex7AcquireEv(&DAT_01126280);
  lVar2 = _ZN8firebase9messaging10FutureData3GetEv();
  if ((lVar2 == 0) || (lVar2 = _ZN8firebase9messaging10FutureData3GetEv(), lVar2 == 0)) {
    _ZN8firebase10LogWarningEPKcz("Failed to complete Future as it was likely already deleted.");
    goto joined_r0x00bbcbc4;
  }
  uVar3 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* try { // try from 00bbcb88 to 00cbcb93 has its CatchHandler @ 00bbce40 */
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_b0,param_5);
  __src = local_90;
  __n = uStack_98;
  uStack_78 = 0;
  local_70 = (undefined1 *)0x0;
  local_80 = 0;
  if ((local_a0 & 1) == 0) {
    uStack_78 = uStack_98;
    local_80 = local_a0;
    local_70 = local_90;
  }
  else {
    if (0xffffffffffffffef < uStack_98) {
      uVar3 = _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_length_errorEv(&local_80);
      _ZN8firebase12FutureHandleD2Ev(auStack_b0);
      _ZN8firebase5Mutex7ReleaseEv(&DAT_01126280);
      if ((local_a0 & 1) != 0) {
        _ZdlPv(local_90);
      }
                    /* WARNING: Subroutine does not return */
      FUN_00c53f5c(uVar3);
    }
                    /* try { // try from 00bbcc38 to 00cbcc7b has its CatchHandler @ 00bbc8d8 */
    if (uStack_98 < 0x17) {
      __dest = (undefined1 *)((ulong)&local_80 | 1);
      local_80 = (ulong)(byte)((int)uStack_98 << 1);
      if (uStack_98 != 0) goto LAB_00bbcc74;
    }
    else {
      uVar4 = uStack_98 + 0x10 & 0xfffffffffffffff0;
      __dest = (undefined1 *)_Znwm(uVar4);
      local_80 = uVar4 | 1;
      uStack_78 = __n;
      local_70 = __dest;
LAB_00bbcc74:
                    /* try { // try from 00bbcc7c to 00cbcc7f has its CatchHandler @ 00bbce28 */
      memcpy(__dest,__src,__n);
    }
    __dest[__n] = 0;
  }
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26CompleteWithResultInternalIS8_EEvRKNS_12FutureHandleEiPKcRKT_EUlPS8_E_EEvSC_iSE_RKT0_
            (uVar3,auStack_b0,(ulong)(param_3 != 0) << 2,param_4,&local_80);
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  _ZN8firebase12FutureHandleD2Ev(auStack_b0);
joined_r0x00bbcbc4:
  if (param_5 != (void *)0x0) {
    _ZN8firebase12FutureHandleD2Ev(param_5);
                    /* try { // try from 00bbcbd0 to 00cbcc37 has its CatchHandler @ 00bbce78 */
    _ZdlPv(param_5);
  }
  _ZN8firebase5Mutex7ReleaseEv(&DAT_01126280);
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  if (*(long *)(lVar1 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
