# 00bcdeb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bcdeb4",
  "name": "FUN_00bcdeb4",
  "size": 532,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "158de284abcd4cdaff92e024303dc3efb7cf5179f35fbee733fb7b316c188a4e",
  "source_text_sha256": "158de284abcd4cdaff92e024303dc3efb7cf5179f35fbee733fb7b316c188a4e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497834](../00497/00497834.md)
- [005762b8](../00576/005762b8.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b390](../00c5b/00c5b390.md)
- [00c5b520](../00c5b/00c5b520.md)
- [00c5d560](../00c5d/00c5d560.md)

## 関連文字列（未確認候補）

~~~text
"!success || result != nullptr"
~~~

## 疑似コード / UTF-8 4162 bytes

~~~c

void FUN_00bcdeb4(long param_1,long param_2,ulong param_3,long *param_4)

{
  byte *pbVar1;
  byte bVar2;
  long lVar3;
  byte *pbVar4;
  uint uVar5;
  long *plVar6;
  long lVar7;
  ulong uVar8;
  undefined8 uVar9;
  long lVar10;
  byte *pbVar11;
  ulong uVar12;
  long lVar13;
  undefined8 local_80;
  undefined8 uStack_78;
  undefined8 local_70;
  long local_68;
  
                    /* try { // try from 00bcdeb4 to 00ccdf47 has its CatchHandler @ 00bcc5d0 */
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x10));
  if ((param_1 == 0) && ((param_3 & 1) != 0)) {
    _ZN8firebase9LogAssertEPKcz("!success || result != nullptr");
  }
  if ((param_3 & 1) == 0) {
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
  }
  else {
    lVar7 = FUN_00497834(plVar6,param_1,DAT_011267e0);
    uVar8 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
    if (((uVar8 & 1) == 0) && (lVar7 != 0)) {
      uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(2);
                    /* try { // try from 00bcdf48 to 00ccdf4f has its CatchHandler @ 00bce8b0 */
      uVar5 = FUN_005762b8(plVar6,lVar7,uVar9);
      pbVar1 = (byte *)param_4[1];
      uVar12 = (ulong)(int)uVar5;
      lVar10 = (long)pbVar1 - *param_4 >> 3;
      uVar8 = lVar10 * -0x5555555555555555;
                    /* try { // try from 00bcdf78 to 00ccdf8f has its CatchHandler @ 00bce8ac */
      if (uVar8 < uVar12) {
        _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm
                  (param_4,uVar12 + lVar10 * 0x5555555555555555);
      }
      else {
                    /* try { // try from 00bcdfa0 to 00ccdfbf has its CatchHandler @ 00bce8a8 */
        if (uVar8 - uVar12 != 0) {
          pbVar11 = (byte *)(*param_4 + uVar12 * 0x18);
          if (pbVar11 != pbVar1) {
            bVar2 = pbVar1[-0x18];
            pbVar4 = pbVar1 + -0x18;
            while( true ) {
              if ((bVar2 & 1) != 0) {
                _ZdlPv(*(void **)(pbVar1 + -8));
              }
                    /* try { // try from 00bcdfc0 to 00cce077 has its CatchHandler @ 00bcc5d0 */
              if (pbVar11 == pbVar4) break;
              bVar2 = pbVar4[-0x18];
              pbVar1 = pbVar4;
              pbVar4 = pbVar4 + -0x18;
            }
          }
          param_4[1] = (long)pbVar11;
        }
      }
      if (0 < (int)uVar5) {
        lVar10 = 0;
        uVar8 = 0;
        do {
          uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(0);
          uVar9 = FUN_00497834(plVar6,lVar7,uVar9,uVar8 & 0xffffffff);
          _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_80,plVar6,uVar9);
          lVar13 = *param_4;
          pbVar1 = (byte *)(lVar13 + lVar10);
          if ((*pbVar1 & 1) == 0) {
            *(undefined2 *)(lVar13 + lVar10) = 0;
          }
          else {
            **(undefined1 **)(pbVar1 + 0x10) = 0;
            pbVar1[8] = 0;
            pbVar1[9] = 0;
            pbVar1[10] = 0;
            pbVar1[0xb] = 0;
            pbVar1[0xc] = 0;
            pbVar1[0xd] = 0;
            pbVar1[0xe] = 0;
            pbVar1[0xf] = 0;
            if ((*pbVar1 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar1 + 0x10));
                    /* try { // try from 00bce078 to 00cce08f has its CatchHandler @ 00bce8a4 */
              *(undefined8 *)(lVar13 + lVar10) = 0;
            }
          }
          uVar8 = uVar8 + 1;
          lVar10 = lVar10 + 0x18;
          *(undefined8 *)(pbVar1 + 0x10) = local_70;
          *(undefined8 *)(pbVar1 + 8) = uStack_78;
          *(undefined8 *)pbVar1 = local_80;
        } while (uVar5 != uVar8);
      }
      (**(code **)(*plVar6 + 0xb8))(plVar6,lVar7);
    }
  }
                    /* try { // try from 00bce0a0 to 00cce0bf has its CatchHandler @ 00bce8a0 */
  if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* try { // try from 00bce0c0 to 00cce153 has its CatchHandler @ 00bcc5d0 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
