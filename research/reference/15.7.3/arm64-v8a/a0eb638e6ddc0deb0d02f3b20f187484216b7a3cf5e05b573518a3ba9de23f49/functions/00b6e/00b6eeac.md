# 00b6eeac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6ede4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ede4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-08c4f9b5755264390e2d80d1ec981e7b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6eef0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eef0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0010.md#compare-476745f636c4376b2dc1c8f04ebb89ff)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6eeac",
  "name": "_ZN8firebase4auth4User8GetTokenEb",
  "size": 512,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5addd8f962c8fe7736ef0115899bd1086e370b781081229a65978a951f68129a",
  "source_text_sha256": "5addd8f962c8fe7736ef0115899bd1086e370b781081229a65978a951f68129a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6eeac",
        "00b6f0ab"
      ]
    ],
    "bytes_sha256": "04839956fb299e3a83fd87ade6abf9508ced2afaef02b3e2cdb992161d8751b9",
    "instruction_count": 128,
    "instruction_bytes": 512,
    "body_bytes": 512,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bddbb0](../00bdd/00bddbb0.md)

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddbf0](../00bdd/00bddbf0.md)
- [00bddd30](../00bdd/00bddd30.md)
- [00bdddc0](../00bdd/00bdddc0.md)
- [00bddef0](../00bdd/00bddef0.md)
- [00bddf30](../00bdd/00bddf30.md)
- [00bddf70](../00bdd/00bddf70.md)
- [00bde070](../00bde/00bde070.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00be0e60](../00be0/00be0e60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4148 bytes

~~~c

void _ZN8firebase4auth4User8GetTokenEb(long param_1,long param_2,byte param_3)

{
  long lVar1;
  undefined *puVar2;
  undefined8 *puVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined8 uVar7;
  long lVar8;
  long lVar9;
  long lVar10;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00b6eeb4 to 00c6eebf has its CatchHandler @ 00b70834 */
                    /* try { // try from 00b6eec0 to 00c6ef53 has its CatchHandler @ 00b6e3fc */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
    _ZN8firebase5MutexC2ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    puVar3 = (undefined8 *)_Znwm(0x18);
    puVar3[1] = 0;
    puVar3[2] = 0;
    *puVar3 = 0;
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
              (auStack_68,lVar9,9,puVar3,
               PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv_00c1b868
              );
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
    _ZN8firebase12FutureHandleD1Ev(auStack_68);
    plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    lVar10 = *(long *)(param_2 + 0x98);
    lVar8 = lVar10 + 700;
    _ZN8firebase5Mutex7AcquireEv(lVar8);
                    /* try { // try from 00b6ef54 to 00c6ef5f has its CatchHandler @ 00b707d4 */
    *(byte *)(lVar10 + 0x2b8) = param_3 & 1;
    _ZN8firebase5Mutex7ReleaseEv(lVar8);
                    /* try { // try from 00b6ef7c to 00c6ef97 has its CatchHandler @ 00b707e4 */
    uVar5 = FUN_0047495c(plVar4,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_010a19f0,
                         param_3 & 1);
    uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar4,lVar9,auStack_78);
    if ((uVar6 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
      puVar3 = *(undefined8 **)(param_2 + 0x98);
      uVar7 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
      lVar8 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_88);
      puVar2 = 
      PTR__ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEEbPv_00c1bbd8
      ;
      *(undefined8 **)(lVar8 + 0x10) = puVar3;
      *(undefined **)(lVar8 + 0x18) = puVar2;
      if ((*(byte *)(puVar3 + 0x28) & 1) == 0) {
        lVar10 = (long)puVar3 + 0x141;
      }
      else {
        lVar10 = puVar3[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar7,uVar5,
                 PTR__ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c1bbd0
                 ,lVar8,lVar10);
      _ZN8firebase12FutureHandleD1Ev(auStack_88);
      (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
    }
    else {
                    /* try { // try from 00b6ef98 to 00c6f0db has its CatchHandler @ 00b6e3fc */
      lVar10 = *(long *)(param_2 + 0x98);
      lVar8 = lVar10 + 700;
      _ZN8firebase5Mutex7AcquireEv(lVar8);
      *(undefined1 *)(lVar10 + 0x2b8) = 0;
      _ZN8firebase5Mutex7ReleaseEv(lVar8);
    }
    _ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_78);
    _ZN8firebase12FutureHandleD1Ev(auStack_78);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6eeac"></a> `00b6eeac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b6eeb0"></a> `00b6eeb0` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b6eeb4"></a> `00b6eeb4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6eeb8"></a> `00b6eeb8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b6eebc"></a> `00b6eebc` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b6eec0"></a> `00b6eec0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b6eec4"></a> `00b6eec4` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b6eec8"></a> `00b6eec8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b6eecc"></a> `00b6eecc` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b6eed0"></a> `00b6eed0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b6eed4"></a> `00b6eed4` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b6eed8"></a> `00b6eed8` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00b6eedc"></a> `00b6eedc` | `e9 06 00 b4` | cbz x9,0x00b6efb8 | `CONDITIONAL_JUMP`
<a id="insn-00b6eee0"></a> `00b6eee0` | `28 01 41 f9` | ldr x8,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00b6eee4"></a> `00b6eee4` | `a8 06 00 b4` | cbz x8,0x00b6efb8 | `CONDITIONAL_JUMP`
<a id="insn-00b6eee8"></a> `00b6eee8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b6eeec"></a> `00b6eeec` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00b6eef0"></a> `00b6eef0` | `f7 03 01 2a` | mov w23,w1 | `FALL_THROUGH`
<a id="insn-00b6eef4"></a> `00b6eef4` | `34 41 00 91` | add x20,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00b6eef8"></a> `00b6eef8` | `3e b0 01 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6eefc"></a> `00b6eefc` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00b6ef00"></a> `00b6ef00` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b6ef04"></a> `00b6ef04` | `63 05 00 b0` | adrp x3,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b6ef08"></a> `00b6ef08` | `63 34 44 f9` | ldr x3,[x3, #0x868] | `FALL_THROUGH`
<a id="insn-00b6ef0c"></a> `00b6ef0c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b6ef10"></a> `00b6ef10` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00b6ef14"></a> `00b6ef14` | `21 01 80 52` | mov w1,#0x9 | `FALL_THROUGH`
<a id="insn-00b6ef18"></a> `00b6ef18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6ef1c"></a> `00b6ef1c` | `15 bc 01 94` | bl 0x00bddf70 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef20"></a> `00b6ef20` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b6ef24"></a> `00b6ef24` | `e1 a3 00 91` | add x1,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00b6ef28"></a> `00b6ef28` | `02 bc 01 94` | bl 0x00bddf30 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef2c"></a> `00b6ef2c` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00b6ef30"></a> `00b6ef30` | `30 bb 01 94` | bl 0x00bddbf0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef34"></a> `00b6ef34` | `c8 4e 40 f9` | ldr x8,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b6ef38"></a> `00b6ef38` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00b6ef3c"></a> `00b6ef3c` | `9d bc 01 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef40"></a> `00b6ef40` | `da 4e 40 f9` | ldr x26,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b6ef44"></a> `00b6ef44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6ef48"></a> `00b6ef48` | `58 f3 0a 91` | add x24,x26,#0x2bc | `FALL_THROUGH`
<a id="insn-00b6ef4c"></a> `00b6ef4c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b6ef50"></a> `00b6ef50` | `20 bb 01 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef54"></a> `00b6ef54` | `f7 02 00 12` | and w23,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00b6ef58"></a> `00b6ef58` | `57 e3 0a 39` | strb w23,[x26, #0x2b8] | `FALL_THROUGH`
<a id="insn-00b6ef5c"></a> `00b6ef5c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b6ef60"></a> `00b6ef60` | `20 bb 01 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef64"></a> `00b6ef64` | `c8 4e 40 f9` | ldr x8,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b6ef68"></a> `00b6ef68` | `89 29 00 f0` | adrp x9,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6ef6c"></a> `00b6ef6c` | `22 f9 44 f9` | ldr x2,[x9, #0x9f0] | `FALL_THROUGH`
<a id="insn-00b6ef70"></a> `00b6ef70` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00b6ef74"></a> `00b6ef74` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6ef78"></a> `00b6ef78` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-00b6ef7c"></a> `00b6ef7c` | `78 16 e4 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef80"></a> `00b6ef80` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b6ef84"></a> `00b6ef84` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b6ef88"></a> `00b6ef88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6ef8c"></a> `00b6ef8c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b6ef90"></a> `00b6ef90` | `b4 c7 01 94` | bl 0x00be0e60 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ef94"></a> `00b6ef94` | `40 02 00 36` | tbz w0,#0x0,0x00b6efdc | `CONDITIONAL_JUMP`
<a id="insn-00b6ef98"></a> `00b6ef98` | `d6 4e 40 f9` | ldr x22,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b6ef9c"></a> `00b6ef9c` | `d5 f2 0a 91` | add x21,x22,#0x2bc | `FALL_THROUGH`
<a id="insn-00b6efa0"></a> `00b6efa0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6efa4"></a> `00b6efa4` | `0b bb 01 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6efa8"></a> `00b6efa8` | `df e2 0a 39` | strb wzr,[x22, #0x2b8] | `FALL_THROUGH`
<a id="insn-00b6efac"></a> `00b6efac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6efb0"></a> `00b6efb0` | `0c bb 01 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6efb4"></a> `00b6efb4` | `2c 00 00 14` | b 0x00b6f064 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6efb8"></a> `00b6efb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6efbc"></a> `00b6efbc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b6efc0"></a> `00b6efc0` | `80 bb 01 94` | bl 0x00bdddc0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6efc4"></a> `00b6efc4` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00b6efc8"></a> `00b6efc8` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b6efcc"></a> `00b6efcc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b6efd0"></a> `00b6efd0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b6efd4"></a> `00b6efd4` | `57 bb 01 94` | bl 0x00bddd30 | `UNCONDITIONAL_CALL`
<a id="insn-00b6efd8"></a> `00b6efd8` | `29 00 00 14` | b 0x00b6f07c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6efdc"></a> `00b6efdc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b6efe0"></a> `00b6efe0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b6efe4"></a> `00b6efe4` | `d3 bb 01 94` | bl 0x00bddf30 | `UNCONDITIONAL_CALL`
<a id="insn-00b6efe8"></a> `00b6efe8` | `da 4e 40 f9` | ldr x26,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b6efec"></a> `00b6efec` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00b6eff0"></a> `00b6eff0` | `70 bc 01 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6eff4"></a> `00b6eff4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b6eff8"></a> `00b6eff8` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00b6effc"></a> `00b6effc` | `fd af 01 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6f000"></a> `00b6f000` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00b6f004"></a> `00b6f004` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b6f008"></a> `00b6f008` | `ca bb 01 94` | bl 0x00bddf30 | `UNCONDITIONAL_CALL`
<a id="insn-00b6f00c"></a> `00b6f00c` | `68 05 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b6f010"></a> `00b6f010` | `08 ed 45 f9` | ldr x8,[x8, #0xbd8] | `FALL_THROUGH`
<a id="insn-00b6f014"></a> `00b6f014` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b6f018"></a> `00b6f018` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00b6f01c"></a> `00b6f01c` | `88 00 00 37` | tbnz w8,#0x0,0x00b6f02c | `CONDITIONAL_JUMP`
<a id="insn-00b6f020"></a> `00b6f020` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00b6f024"></a> `00b6f024` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6f028"></a> `00b6f028` | `02 00 00 14` | b 0x00b6f030 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6f02c"></a> `00b6f02c` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00b6f030"></a> `00b6f030` | `62 05 00 90` | adrp x2,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b6f034"></a> `00b6f034` | `42 e8 45 f9` | ldr x2,[x2, #0xbd0] | `FALL_THROUGH`
<a id="insn-00b6f038"></a> `00b6f038` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b6f03c"></a> `00b6f03c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b6f040"></a> `00b6f040` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00b6f044"></a> `00b6f044` | `0b bc 01 94` | bl 0x00bde070 | `UNCONDITIONAL_CALL`
<a id="insn-00b6f048"></a> `00b6f048` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b6f04c"></a> `00b6f04c` | `e9 ba 01 94` | bl 0x00bddbf0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6f050"></a> `00b6f050` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b6f054"></a> `00b6f054` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00b6f058"></a> `00b6f058` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6f05c"></a> `00b6f05c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b6f060"></a> `00b6f060` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b6f064"></a> `00b6f064` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b6f068"></a> `00b6f068` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6f06c"></a> `00b6f06c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b6f070"></a> `00b6f070` | `a0 bb 01 94` | bl 0x00bddef0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6f074"></a> `00b6f074` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b6f078"></a> `00b6f078` | `de ba 01 94` | bl 0x00bddbf0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6f07c"></a> `00b6f07c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b6f080"></a> `00b6f080` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b6f084"></a> `00b6f084` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b6f088"></a> `00b6f088` | `01 01 00 54` | b.ne 0x00b6f0a8 | `CONDITIONAL_JUMP`
<a id="insn-00b6f08c"></a> `00b6f08c` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b6f090"></a> `00b6f090` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b6f094"></a> `00b6f094` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b6f098"></a> `00b6f098` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6f09c"></a> `00b6f09c` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b6f0a0"></a> `00b6f0a0` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b6f0a4"></a> `00b6f0a4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b6f0a8"></a> `00b6f0a8` | `e6 af 01 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6eeac`](#insn-00b6eeac) 範囲 `[['00b6eeac', '00b6eeb3']]`
  - `FALL_THROUGH` [`00b6eeb0`](#insn-00b6eeb0) → [`00b6eeb4`](#insn-00b6eeb4)
- ブロック [`00b6eeb4`](#insn-00b6eeb4) 範囲 `[['00b6eeb4', '00b6eebf']]`
  - `FALL_THROUGH` [`00b6eebc`](#insn-00b6eebc) → [`00b6eec0`](#insn-00b6eec0)
- ブロック [`00b6eec0`](#insn-00b6eec0) 範囲 `[['00b6eec0', '00b6eedf']]`
  - `CONDITIONAL_JUMP` [`00b6eedc`](#insn-00b6eedc) → [`00b6efb8`](#insn-00b6efb8)
  - `FALL_THROUGH` [`00b6eedc`](#insn-00b6eedc) → [`00b6eee0`](#insn-00b6eee0)
- ブロック [`00b6eee0`](#insn-00b6eee0) 範囲 `[['00b6eee0', '00b6eee7']]`
  - `CONDITIONAL_JUMP` [`00b6eee4`](#insn-00b6eee4) → [`00b6efb8`](#insn-00b6efb8)
  - `FALL_THROUGH` [`00b6eee4`](#insn-00b6eee4) → [`00b6eee8`](#insn-00b6eee8)
- ブロック [`00b6eee8`](#insn-00b6eee8) 範囲 `[['00b6eee8', '00b6ef53']]`
  - `FALL_THROUGH` [`00b6ef50`](#insn-00b6ef50) → [`00b6ef54`](#insn-00b6ef54)
- ブロック [`00b6ef54`](#insn-00b6ef54) 範囲 `[['00b6ef54', '00b6ef7b']]`
  - `FALL_THROUGH` [`00b6ef78`](#insn-00b6ef78) → [`00b6ef7c`](#insn-00b6ef7c)
- ブロック [`00b6ef7c`](#insn-00b6ef7c) 範囲 `[['00b6ef7c', '00b6ef97']]`
  - `CONDITIONAL_JUMP` [`00b6ef94`](#insn-00b6ef94) → [`00b6efdc`](#insn-00b6efdc)
  - `FALL_THROUGH` [`00b6ef94`](#insn-00b6ef94) → [`00b6ef98`](#insn-00b6ef98)
- ブロック [`00b6ef98`](#insn-00b6ef98) 範囲 `[['00b6ef98', '00b6efb7']]`
  - `UNCONDITIONAL_JUMP` [`00b6efb4`](#insn-00b6efb4) → [`00b6f064`](#insn-00b6f064)
- ブロック [`00b6efb8`](#insn-00b6efb8) 範囲 `[['00b6efb8', '00b6efdb']]`
  - `UNCONDITIONAL_JUMP` [`00b6efd8`](#insn-00b6efd8) → [`00b6f07c`](#insn-00b6f07c)
- ブロック [`00b6efdc`](#insn-00b6efdc) 範囲 `[['00b6efdc', '00b6f01f']]`
  - `CONDITIONAL_JUMP` [`00b6f01c`](#insn-00b6f01c) → [`00b6f02c`](#insn-00b6f02c)
  - `FALL_THROUGH` [`00b6f01c`](#insn-00b6f01c) → [`00b6f020`](#insn-00b6f020)
- ブロック [`00b6f020`](#insn-00b6f020) 範囲 `[['00b6f020', '00b6f02b']]`
  - `UNCONDITIONAL_JUMP` [`00b6f028`](#insn-00b6f028) → [`00b6f030`](#insn-00b6f030)
- ブロック [`00b6f02c`](#insn-00b6f02c) 範囲 `[['00b6f02c', '00b6f02f']]`
  - `FALL_THROUGH` [`00b6f02c`](#insn-00b6f02c) → [`00b6f030`](#insn-00b6f030)
- ブロック [`00b6f030`](#insn-00b6f030) 範囲 `[['00b6f030', '00b6f063']]`
  - `FALL_THROUGH` [`00b6f060`](#insn-00b6f060) → [`00b6f064`](#insn-00b6f064)
- ブロック [`00b6f064`](#insn-00b6f064) 範囲 `[['00b6f064', '00b6f07b']]`
  - `FALL_THROUGH` [`00b6f078`](#insn-00b6f078) → [`00b6f07c`](#insn-00b6f07c)
- ブロック [`00b6f07c`](#insn-00b6f07c) 範囲 `[['00b6f07c', '00b6f08b']]`
  - `CONDITIONAL_JUMP` [`00b6f088`](#insn-00b6f088) → [`00b6f0a8`](#insn-00b6f0a8)
  - `FALL_THROUGH` [`00b6f088`](#insn-00b6f088) → [`00b6f08c`](#insn-00b6f08c)
- ブロック [`00b6f08c`](#insn-00b6f08c) 範囲 `[['00b6f08c', '00b6f0a7']]`
- ブロック [`00b6f0a8`](#insn-00b6f0a8) 範囲 `[['00b6f0a8', '00b6f0ab']]`

## 命令位置別の参照

- [`00b6eeb0`](#insn-00b6eeb0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eeb4`](#insn-00b6eeb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eeb8`](#insn-00b6eeb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eebc`](#insn-00b6eebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eec0`](#insn-00b6eec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eed4`](#insn-00b6eed4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eedc`](#insn-00b6eedc) → [`00b6efb8`](#insn-00b6efb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eee4`](#insn-00b6eee4) → [`00b6efb8`](#insn-00b6efb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eef8`](#insn-00b6eef8) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef08`](#insn-00b6ef08) → `00c1b868`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b6ef08`](#insn-00b6ef08) → [`00ae3dc8`](../00ae3/00ae3dc8.md) · `PARAM` · `ANALYSIS` · 関数 `00ae3dc8` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv` · 推定型 `None`
- [`00b6ef1c`](#insn-00b6ef1c) → [`00bddf70`](../00bdd/00bddf70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf70` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef28`](#insn-00b6ef28) → [`00bddf30`](../00bdd/00bddf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf30` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef30`](#insn-00b6ef30) → [`00bddbf0`](../00bdd/00bddbf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbf0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef3c`](#insn-00b6ef3c) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef50`](#insn-00b6ef50) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef60`](#insn-00b6ef60) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef6c`](#insn-00b6ef6c) → `010a19f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6ef7c`](#insn-00b6ef7c) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef90`](#insn-00b6ef90) → [`00be0e60`](../00be0/00be0e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0e60` · 推定シンボル `None` · 推定型 `None`
- [`00b6ef94`](#insn-00b6ef94) → [`00b6efdc`](#insn-00b6efdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6efa4`](#insn-00b6efa4) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00b6efb0`](#insn-00b6efb0) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00b6efb4`](#insn-00b6efb4) → [`00b6f064`](#insn-00b6f064) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6efc0`](#insn-00b6efc0) → [`00bdddc0`](../00bdd/00bdddc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddc0` · 推定シンボル `None` · 推定型 `None`
- [`00b6efd4`](#insn-00b6efd4) → [`00bddd30`](../00bdd/00bddd30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd30` · 推定シンボル `None` · 推定型 `None`
- [`00b6efd8`](#insn-00b6efd8) → [`00b6f07c`](#insn-00b6f07c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6efe4`](#insn-00b6efe4) → [`00bddf30`](../00bdd/00bddf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf30` · 推定シンボル `None` · 推定型 `None`
- [`00b6eff0`](#insn-00b6eff0) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6effc`](#insn-00b6effc) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00b6f008`](#insn-00b6f008) → [`00bddf30`](../00bdd/00bddf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf30` · 推定シンボル `None` · 推定型 `None`
- [`00b6f010`](#insn-00b6f010) → `00c1bbd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b6f014`](#insn-00b6f014) → [`00b6ed38`](00b6ed38.md) · `DATA` · `ANALYSIS` · 関数 `00b6ed38` · 推定シンボル `_ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEEbPv` · 推定型 `None`
- [`00b6f01c`](#insn-00b6f01c) → [`00b6f02c`](#insn-00b6f02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f028`](#insn-00b6f028) → [`00b6f030`](#insn-00b6f030) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f034`](#insn-00b6f034) → `00c1bbd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b6f034`](#insn-00b6f034) → [`00b71a48`](../00b71/00b71a48.md) · `PARAM` · `ANALYSIS` · 関数 `00b71a48` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00b6f044`](#insn-00b6f044) → [`00bde070`](../00bde/00bde070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde070` · 推定シンボル `None` · 推定型 `None`
- [`00b6f04c`](#insn-00b6f04c) → [`00bddbf0`](../00bdd/00bddbf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbf0` · 推定シンボル `None` · 推定型 `None`
- [`00b6f070`](#insn-00b6f070) → [`00bddef0`](../00bdd/00bddef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddef0` · 推定シンボル `None` · 推定型 `None`
- [`00b6f078`](#insn-00b6f078) → [`00bddbf0`](../00bdd/00bddbf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbf0` · 推定シンボル `None` · 推定型 `None`
- [`00b6f080`](#insn-00b6f080) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f088`](#insn-00b6f088) → [`00b6f0a8`](#insn-00b6f0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f08c`](#insn-00b6f08c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f090`](#insn-00b6f090) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f094`](#insn-00b6f094) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f098`](#insn-00b6f098) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f09c`](#insn-00b6f09c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f0a8`](#insn-00b6f0a8) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6eeb0`](#insn-00b6eeb0)

~~~json
{
  "source": "00b6eeb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eeb4`](#insn-00b6eeb4)

~~~json
{
  "source": "00b6eeb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eeb8`](#insn-00b6eeb8)

~~~json
{
  "source": "00b6eeb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eebc`](#insn-00b6eebc)

~~~json
{
  "source": "00b6eebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eec0`](#insn-00b6eec0)

~~~json
{
  "source": "00b6eec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eed4`](#insn-00b6eed4)

~~~json
{
  "source": "00b6eed4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eedc`](#insn-00b6eedc)

~~~json
{
  "source": "00b6eedc",
  "target": "00b6efb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eee4`](#insn-00b6eee4)

~~~json
{
  "source": "00b6eee4",
  "target": "00b6efb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eef8`](#insn-00b6eef8)

~~~json
{
  "source": "00b6eef8",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef08`](#insn-00b6ef08)

~~~json
{
  "source": "00b6ef08",
  "target": "00c1b868",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b868",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b6ef08`](#insn-00b6ef08)

~~~json
{
  "source": "00b6ef08",
  "target": "00ae3dc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef1c`](#insn-00b6ef1c)

~~~json
{
  "source": "00b6ef1c",
  "target": "00bddf70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef28`](#insn-00b6ef28)

~~~json
{
  "source": "00b6ef28",
  "target": "00bddf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef30`](#insn-00b6ef30)

~~~json
{
  "source": "00b6ef30",
  "target": "00bddbf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef3c`](#insn-00b6ef3c)

~~~json
{
  "source": "00b6ef3c",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef50`](#insn-00b6ef50)

~~~json
{
  "source": "00b6ef50",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef60`](#insn-00b6ef60)

~~~json
{
  "source": "00b6ef60",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef6c`](#insn-00b6ef6c)

~~~json
{
  "source": "00b6ef6c",
  "target": "010a19f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a19f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6ef7c`](#insn-00b6ef7c)

~~~json
{
  "source": "00b6ef7c",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef90`](#insn-00b6ef90)

~~~json
{
  "source": "00b6ef90",
  "target": "00be0e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ef94`](#insn-00b6ef94)

~~~json
{
  "source": "00b6ef94",
  "target": "00b6efdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6efa4`](#insn-00b6efa4)

~~~json
{
  "source": "00b6efa4",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6efb0`](#insn-00b6efb0)

~~~json
{
  "source": "00b6efb0",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6efb4`](#insn-00b6efb4)

~~~json
{
  "source": "00b6efb4",
  "target": "00b6f064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6efc0`](#insn-00b6efc0)

~~~json
{
  "source": "00b6efc0",
  "target": "00bdddc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6efd4`](#insn-00b6efd4)

~~~json
{
  "source": "00b6efd4",
  "target": "00bddd30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6efd8`](#insn-00b6efd8)

~~~json
{
  "source": "00b6efd8",
  "target": "00b6f07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6efe4`](#insn-00b6efe4)

~~~json
{
  "source": "00b6efe4",
  "target": "00bddf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6eff0`](#insn-00b6eff0)

~~~json
{
  "source": "00b6eff0",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6effc`](#insn-00b6effc)

~~~json
{
  "source": "00b6effc",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f008`](#insn-00b6f008)

~~~json
{
  "source": "00b6f008",
  "target": "00bddf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f010`](#insn-00b6f010)

~~~json
{
  "source": "00b6f010",
  "target": "00c1bbd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bbd8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b6f014`](#insn-00b6f014)

~~~json
{
  "source": "00b6f014",
  "target": "00b6ed38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f01c`](#insn-00b6f01c)

~~~json
{
  "source": "00b6f01c",
  "target": "00b6f02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f028`](#insn-00b6f028)

~~~json
{
  "source": "00b6f028",
  "target": "00b6f030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f034`](#insn-00b6f034)

~~~json
{
  "source": "00b6f034",
  "target": "00c1bbd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bbd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b6f034`](#insn-00b6f034)

~~~json
{
  "source": "00b6f034",
  "target": "00b71a48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f044`](#insn-00b6f044)

~~~json
{
  "source": "00b6f044",
  "target": "00bde070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f04c`](#insn-00b6f04c)

~~~json
{
  "source": "00b6f04c",
  "target": "00bddbf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f070`](#insn-00b6f070)

~~~json
{
  "source": "00b6f070",
  "target": "00bddef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f078`](#insn-00b6f078)

~~~json
{
  "source": "00b6f078",
  "target": "00bddbf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f080`](#insn-00b6f080)

~~~json
{
  "source": "00b6f080",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f088`](#insn-00b6f088)

~~~json
{
  "source": "00b6f088",
  "target": "00b6f0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f08c`](#insn-00b6f08c)

~~~json
{
  "source": "00b6f08c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f090`](#insn-00b6f090)

~~~json
{
  "source": "00b6f090",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f094`](#insn-00b6f094)

~~~json
{
  "source": "00b6f094",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f098`](#insn-00b6f098)

~~~json
{
  "source": "00b6f098",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f09c`](#insn-00b6f09c)

~~~json
{
  "source": "00b6f09c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f0a8`](#insn-00b6f0a8)

~~~json
{
  "source": "00b6f0a8",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
