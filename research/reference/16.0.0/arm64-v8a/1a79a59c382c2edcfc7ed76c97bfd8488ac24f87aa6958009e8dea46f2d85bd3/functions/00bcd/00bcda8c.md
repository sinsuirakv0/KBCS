# 00bcda8c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcda8c",
  "name": "FUN_00bcda8c",
  "size": 532,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "397d1e0ac0006c0069af0f06299e75eb91d2b0ef50709f29e0b249a4a943fc7d",
  "source_text_sha256": "397d1e0ac0006c0069af0f06299e75eb91d2b0ef50709f29e0b249a4a943fc7d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00576278](../00576/00576278.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5af90](../00c5a/00c5af90.md)
- [00c5b120](../00c5b/00c5b120.md)
- [00c5d160](../00c5d/00c5d160.md)

## 関連文字列（未確認候補）

~~~text
"!success || result != nullptr"
~~~

## 疑似コード / UTF-8 3821 bytes

~~~c

void FUN_00bcda8c(long param_1,long param_2,ulong param_3,long *param_4)

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
    lVar7 = FUN_004977f4(plVar6,param_1,DAT_011263e0);
    uVar8 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
    if (((uVar8 & 1) == 0) && (lVar7 != 0)) {
      uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(2);
      uVar5 = FUN_00576278(plVar6,lVar7,uVar9);
      pbVar1 = (byte *)param_4[1];
      uVar12 = (ulong)(int)uVar5;
      lVar10 = (long)pbVar1 - *param_4 >> 3;
      uVar8 = lVar10 * -0x5555555555555555;
      if (uVar8 < uVar12) {
        _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm
                  (param_4,uVar12 + lVar10 * 0x5555555555555555);
                    /* try { // try from 00bcdb64 to 00ccdb7b has its CatchHandler @ 00bce818 */
      }
      else if (uVar8 - uVar12 != 0) {
        pbVar11 = (byte *)(*param_4 + uVar12 * 0x18);
        if (pbVar11 != pbVar1) {
          bVar2 = pbVar1[-0x18];
          pbVar4 = pbVar1 + -0x18;
          while( true ) {
            if ((bVar2 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar1 + -8));
            }
            if (pbVar11 == pbVar4) break;
            bVar2 = pbVar4[-0x18];
            pbVar1 = pbVar4;
            pbVar4 = pbVar4 + -0x18;
          }
        }
        param_4[1] = (long)pbVar11;
      }
      if (0 < (int)uVar5) {
        lVar10 = 0;
        uVar8 = 0;
        do {
                    /* try { // try from 00bcdbfc to 00ccdc03 has its CatchHandler @ 00bce6e4 */
          uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(0);
          uVar9 = FUN_004977f4(plVar6,lVar7,uVar9,uVar8 & 0xffffffff);
          _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_80,plVar6,uVar9);
          lVar13 = *param_4;
          pbVar1 = (byte *)(lVar13 + lVar10);
          if ((*pbVar1 & 1) == 0) {
            *(undefined2 *)(lVar13 + lVar10) = 0;
          }
          else {
                    /* try { // try from 00bcdc38 to 00ccdc3f has its CatchHandler @ 00bce6dc */
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
                    /* try { // try from 00bcdc6c to 00ccdc8b has its CatchHandler @ 00bce6cc */
  if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* try { // try from 00bcdc98 to 00ccdcb7 has its CatchHandler @ 00bce6bc */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
