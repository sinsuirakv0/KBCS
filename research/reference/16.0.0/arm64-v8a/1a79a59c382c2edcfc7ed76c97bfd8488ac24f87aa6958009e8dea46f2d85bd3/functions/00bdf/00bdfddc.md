# 00bdfddc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b708dc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b708dc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-c9239af8cd1a238ef081e19b93749f1a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00be0204`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0204.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-bf8457bfe448bae331e2f6f60d62c558)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfddc",
  "name": "_ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE",
  "size": 492,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07ca7934dfd2af7da302140af6ae02e7f0ca8c33320610869651fa37bd7e441e",
  "source_text_sha256": "07ca7934dfd2af7da302140af6ae02e7f0ca8c33320610869651fa37bd7e441e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfddc",
        "00bdffc7"
      ]
    ],
    "bytes_sha256": "2385588491da66cb4898d9bba3d08485b2089ec643c5a9b94faa6dc1b75e7ea8",
    "instruction_count": 123,
    "instruction_bytes": 492,
    "body_bytes": 492,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5a7e0](../00c5a/00c5a7e0.md)
- [00c5a870](../00c5a/00c5a870.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5ab40](../00c5a/00c5ab40.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d7e0](../00c5d/00c5d7e0.md)
- [00c5d810](../00c5d/00c5d810.md)
- [00c5d8f0](../00c5d/00c5d8f0.md)
- [00c5d950](../00c5d/00c5d950.md)
- [00c5da10](../00c5d/00c5da10.md)

## 関連文字列（未確認候補）

~~~text
"Credential is not a phone credential."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4190 bytes

~~~c

void _ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE
               (long param_1,long param_2,undefined8 *param_3)

{
  long lVar1;
  undefined *puVar2;
  char cVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  undefined8 uVar10;
  undefined8 *puVar11;
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  undefined1 auStack_60 [8];
  long local_58;
  
                    /* try { // try from 00bdfdf0 to 00cdfdff has its CatchHandler @ 00be01e4 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
                    /* try { // try from 00bdfefc to 00cdff07 has its CatchHandler @ 00be02e8 */
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* try { // try from 00bdff08 to 00cdff3b has its CatchHandler @ 00be02f8 */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth4UserEEENS_16SafeFutureHandleIT_EEi
              (auStack_70,lVar9,0x16);
    plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar10 = *param_3;
    uVar5 = _ZN8firebase4auth15phonecredential8GetClassEv();
    cVar3 = (**(code **)(*plVar4 + 0x100))(plVar4,uVar10,uVar5);
    if (cVar3 == '\0') {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
                (lVar9,auStack_90,4,"Credential is not a phone credential.",auStack_60);
      _ZN8firebase12FutureHandleD2Ev(auStack_90);
    }
    else {
                    /* try { // try from 00bdfe74 to 00cdfe77 has its CatchHandler @ 00be0358 */
      uVar5 = FUN_004977f4(plVar4,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126970,
                           uVar10);
      uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                        (plVar4,lVar9,auStack_70);
      if ((uVar6 & 1) == 0) {
                    /* try { // try from 00bdfea8 to 00cdfeaf has its CatchHandler @ 00be0324 */
        _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
        puVar11 = *(undefined8 **)(param_2 + 0x98);
                    /* try { // try from 00bdfeb0 to 00cdfefb has its CatchHandler @ 00bdf01c */
        uVar10 = _ZNK8firebase3App9GetJNIEnvEv(*puVar11);
        lVar7 = _Znwm(0x20);
        _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_80);
        puVar2 = 
        PTR__ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv_00c9b628
        ;
        *(undefined8 **)(lVar7 + 0x10) = puVar11;
        *(undefined **)(lVar7 + 0x18) = puVar2;
        if ((*(byte *)(puVar11 + 0x28) & 1) == 0) {
          lVar8 = (long)puVar11 + 0x141;
        }
        else {
          lVar8 = puVar11[0x2a];
        }
        _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                  (uVar10,uVar5,
                   PTR__ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9b610
                   ,lVar7,lVar8);
        _ZN8firebase12FutureHandleD2Ev(auStack_80);
                    /* try { // try from 00bdff6c to 00cdff73 has its CatchHandler @ 00be02b4 */
        (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
      }
    }
    _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_70);
                    /* try { // try from 00bdff90 to 00cdffdb has its CatchHandler @ 00be0358 */
    _ZN8firebase12FutureHandleD2Ev(auStack_70);
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
<a id="insn-00bdfddc"></a> `00bdfddc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bdfde0"></a> `00bdfde0` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfde4"></a> `00bdfde4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfde8"></a> `00bdfde8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdfdec"></a> `00bdfdec` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdfdf0"></a> `00bdfdf0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdfdf4"></a> `00bdfdf4` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdfdf8"></a> `00bdfdf8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdfdfc"></a> `00bdfdfc` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfe00"></a> `00bdfe00` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdfe04"></a> `00bdfe04` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdfe08"></a> `00bdfe08` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfe0c"></a> `00bdfe0c` | `29 07 00 b4` | cbz x9,0x00bdfef0 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe10"></a> `00bdfe10` | `28 01 41 f9` | ldr x8,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfe14"></a> `00bdfe14` | `e8 06 00 b4` | cbz x8,0x00bdfef0 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe18"></a> `00bdfe18` | `34 41 00 91` | add x20,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bdfe1c"></a> `00bdfe1c` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bdfe20"></a> `00bdfe20` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdfe24"></a> `00bdfe24` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdfe28"></a> `00bdfe28` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00bdfe2c"></a> `00bdfe2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdfe30"></a> `00bdfe30` | `78 f6 01 94` | bl 0x00c5d810 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe34"></a> `00bdfe34` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfe38"></a> `00bdfe38` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdfe3c"></a> `00bdfe3c` | `91 eb 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe40"></a> `00bdfe40` | `d6 02 40 f9` | ldr x22,[x22] | `FALL_THROUGH`
<a id="insn-00bdfe44"></a> `00bdfe44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdfe48"></a> `00bdfe48` | `f2 f6 01 94` | bl 0x00c5da10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe4c"></a> `00bdfe4c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdfe50"></a> `00bdfe50` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bdfe54"></a> `00bdfe54` | `08 81 40 f9` | ldr x8,[x8, #0x100] | `FALL_THROUGH`
<a id="insn-00bdfe58"></a> `00bdfe58` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfe5c"></a> `00bdfe5c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdfe60"></a> `00bdfe60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdfe64"></a> `00bdfe64` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdfe68"></a> `00bdfe68` | `60 05 00 54` | b.eq 0x00bdff14 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe6c"></a> `00bdfe6c` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfe70"></a> `00bdfe70` | `29 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdfe74"></a> `00bdfe74` | `22 b9 44 f9` | ldr x2,[x9, #0x970] | `FALL_THROUGH`
<a id="insn-00bdfe78"></a> `00bdfe78` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfe7c"></a> `00bdfe7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfe80"></a> `00bdfe80` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bdfe84"></a> `00bdfe84` | `5c de e2 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe88"></a> `00bdfe88` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdfe8c"></a> `00bdfe8c` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdfe90"></a> `00bdfe90` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfe94"></a> `00bdfe94` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdfe98"></a> `00bdfe98` | `96 f6 01 94` | bl 0x00c5d8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe9c"></a> `00bdfe9c` | `20 07 00 37` | tbnz w0,#0x0,0x00bdff80 | `CONDITIONAL_JUMP`
<a id="insn-00bdfea0"></a> `00bdfea0` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdfea4"></a> `00bdfea4` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdfea8"></a> `00bdfea8` | `d6 ea 01 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfeac"></a> `00bdfeac` | `fa 4e 40 f9` | ldr x26,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfeb0"></a> `00bdfeb0` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bdfeb4"></a> `00bdfeb4` | `73 eb 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfeb8"></a> `00bdfeb8` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdfebc"></a> `00bdfebc` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bdfec0"></a> `00bdfec0` | `f4 de 01 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfec4"></a> `00bdfec4` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bdfec8"></a> `00bdfec8` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdfecc"></a> `00bdfecc` | `cd ea 01 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfed0"></a> `00bdfed0` | `e8 05 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdfed4"></a> `00bdfed4` | `08 15 43 f9` | ldr x8,[x8, #0x628] | `FALL_THROUGH`
<a id="insn-00bdfed8"></a> `00bdfed8` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfedc"></a> `00bdfedc` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bdfee0"></a> `00bdfee0` | `48 03 00 37` | tbnz w8,#0x0,0x00bdff48 | `CONDITIONAL_JUMP`
<a id="insn-00bdfee4"></a> `00bdfee4` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bdfee8"></a> `00bdfee8` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdfeec"></a> `00bdfeec` | `18 00 00 14` | b 0x00bdff4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdfef0"></a> `00bdfef0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdfef4"></a> `00bdfef4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bdfef8"></a> `00bdfef8` | `5e ea 01 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfefc"></a> `00bdfefc` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bdff00"></a> `00bdff00` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdff04"></a> `00bdff04` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bdff08"></a> `00bdff08` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdff0c"></a> `00bdff0c` | `35 ea 01 94` | bl 0x00c5a7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff10"></a> `00bdff10` | `22 00 00 14` | b 0x00bdff98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdff14"></a> `00bdff14` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bdff18"></a> `00bdff18` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdff1c"></a> `00bdff1c` | `b9 ea 01 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff20"></a> `00bdff20` | `83 b6 ff b0` | adrp x3,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bdff24"></a> `00bdff24` | `63 20 21 91` | add x3,x3,#0x848 | `FALL_THROUGH`
<a id="insn-00bdff28"></a> `00bdff28` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bdff2c"></a> `00bdff2c` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdff30"></a> `00bdff30` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00bdff34"></a> `00bdff34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdff38"></a> `00bdff38` | `2a f6 01 94` | bl 0x00c5d7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff3c"></a> `00bdff3c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bdff40"></a> `00bdff40` | `d4 e9 01 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff44"></a> `00bdff44` | `0f 00 00 14` | b 0x00bdff80 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdff48"></a> `00bdff48` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bdff4c"></a> `00bdff4c` | `e2 05 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdff50"></a> `00bdff50` | `42 08 43 f9` | ldr x2,[x2, #0x610] | `FALL_THROUGH`
<a id="insn-00bdff54"></a> `00bdff54` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bdff58"></a> `00bdff58` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdff5c"></a> `00bdff5c` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bdff60"></a> `00bdff60` | `f8 ea 01 94` | bl 0x00c5ab40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff64"></a> `00bdff64` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdff68"></a> `00bdff68` | `ca e9 01 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff6c"></a> `00bdff6c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdff70"></a> `00bdff70` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdff74"></a> `00bdff74` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdff78"></a> `00bdff78` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdff7c"></a> `00bdff7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdff80"></a> `00bdff80` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdff84"></a> `00bdff84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdff88"></a> `00bdff88` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdff8c"></a> `00bdff8c` | `71 f6 01 94` | bl 0x00c5d950 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff90"></a> `00bdff90` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdff94"></a> `00bdff94` | `bf e9 01 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff98"></a> `00bdff98` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdff9c"></a> `00bdff9c` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdffa0"></a> `00bdffa0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdffa4"></a> `00bdffa4` | `01 01 00 54` | b.ne 0x00bdffc4 | `CONDITIONAL_JUMP`
<a id="insn-00bdffa8"></a> `00bdffa8` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdffac"></a> `00bdffac` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdffb0"></a> `00bdffb0` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdffb4"></a> `00bdffb4` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdffb8"></a> `00bdffb8` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdffbc"></a> `00bdffbc` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bdffc0"></a> `00bdffc0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdffc4"></a> `00bdffc4` | `c7 de 01 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfddc`](#insn-00bdfddc) 範囲 `[['00bdfddc', '00bdfdef']]`
  - `FALL_THROUGH` [`00bdfdec`](#insn-00bdfdec) → [`00bdfdf0`](#insn-00bdfdf0)
- ブロック [`00bdfdf0`](#insn-00bdfdf0) 範囲 `[['00bdfdf0', '00bdfe0f']]`
  - `CONDITIONAL_JUMP` [`00bdfe0c`](#insn-00bdfe0c) → [`00bdfef0`](#insn-00bdfef0)
  - `FALL_THROUGH` [`00bdfe0c`](#insn-00bdfe0c) → [`00bdfe10`](#insn-00bdfe10)
- ブロック [`00bdfe10`](#insn-00bdfe10) 範囲 `[['00bdfe10', '00bdfe17']]`
  - `CONDITIONAL_JUMP` [`00bdfe14`](#insn-00bdfe14) → [`00bdfef0`](#insn-00bdfef0)
  - `FALL_THROUGH` [`00bdfe14`](#insn-00bdfe14) → [`00bdfe18`](#insn-00bdfe18)
- ブロック [`00bdfe18`](#insn-00bdfe18) 範囲 `[['00bdfe18', '00bdfe6b']]`
  - `CONDITIONAL_JUMP` [`00bdfe68`](#insn-00bdfe68) → [`00bdff14`](#insn-00bdff14)
  - `FALL_THROUGH` [`00bdfe68`](#insn-00bdfe68) → [`00bdfe6c`](#insn-00bdfe6c)
- ブロック [`00bdfe6c`](#insn-00bdfe6c) 範囲 `[['00bdfe6c', '00bdfe73']]`
  - `FALL_THROUGH` [`00bdfe70`](#insn-00bdfe70) → [`00bdfe74`](#insn-00bdfe74)
- ブロック [`00bdfe74`](#insn-00bdfe74) 範囲 `[['00bdfe74', '00bdfe9f']]`
  - `CONDITIONAL_JUMP` [`00bdfe9c`](#insn-00bdfe9c) → [`00bdff80`](#insn-00bdff80)
  - `FALL_THROUGH` [`00bdfe9c`](#insn-00bdfe9c) → [`00bdfea0`](#insn-00bdfea0)
- ブロック [`00bdfea0`](#insn-00bdfea0) 範囲 `[['00bdfea0', '00bdfea7']]`
  - `FALL_THROUGH` [`00bdfea4`](#insn-00bdfea4) → [`00bdfea8`](#insn-00bdfea8)
- ブロック [`00bdfea8`](#insn-00bdfea8) 範囲 `[['00bdfea8', '00bdfeaf']]`
  - `FALL_THROUGH` [`00bdfeac`](#insn-00bdfeac) → [`00bdfeb0`](#insn-00bdfeb0)
- ブロック [`00bdfeb0`](#insn-00bdfeb0) 範囲 `[['00bdfeb0', '00bdfee3']]`
  - `CONDITIONAL_JUMP` [`00bdfee0`](#insn-00bdfee0) → [`00bdff48`](#insn-00bdff48)
  - `FALL_THROUGH` [`00bdfee0`](#insn-00bdfee0) → [`00bdfee4`](#insn-00bdfee4)
- ブロック [`00bdfee4`](#insn-00bdfee4) 範囲 `[['00bdfee4', '00bdfeef']]`
  - `UNCONDITIONAL_JUMP` [`00bdfeec`](#insn-00bdfeec) → [`00bdff4c`](#insn-00bdff4c)
- ブロック [`00bdfef0`](#insn-00bdfef0) 範囲 `[['00bdfef0', '00bdfefb']]`
  - `FALL_THROUGH` [`00bdfef8`](#insn-00bdfef8) → [`00bdfefc`](#insn-00bdfefc)
- ブロック [`00bdfefc`](#insn-00bdfefc) 範囲 `[['00bdfefc', '00bdff07']]`
  - `FALL_THROUGH` [`00bdff04`](#insn-00bdff04) → [`00bdff08`](#insn-00bdff08)
- ブロック [`00bdff08`](#insn-00bdff08) 範囲 `[['00bdff08', '00bdff13']]`
  - `UNCONDITIONAL_JUMP` [`00bdff10`](#insn-00bdff10) → [`00bdff98`](#insn-00bdff98)
- ブロック [`00bdff14`](#insn-00bdff14) 範囲 `[['00bdff14', '00bdff47']]`
  - `UNCONDITIONAL_JUMP` [`00bdff44`](#insn-00bdff44) → [`00bdff80`](#insn-00bdff80)
- ブロック [`00bdff48`](#insn-00bdff48) 範囲 `[['00bdff48', '00bdff4b']]`
  - `FALL_THROUGH` [`00bdff48`](#insn-00bdff48) → [`00bdff4c`](#insn-00bdff4c)
- ブロック [`00bdff4c`](#insn-00bdff4c) 範囲 `[['00bdff4c', '00bdff6b']]`
  - `FALL_THROUGH` [`00bdff68`](#insn-00bdff68) → [`00bdff6c`](#insn-00bdff6c)
- ブロック [`00bdff6c`](#insn-00bdff6c) 範囲 `[['00bdff6c', '00bdff7f']]`
  - `FALL_THROUGH` [`00bdff7c`](#insn-00bdff7c) → [`00bdff80`](#insn-00bdff80)
- ブロック [`00bdff80`](#insn-00bdff80) 範囲 `[['00bdff80', '00bdff8f']]`
  - `FALL_THROUGH` [`00bdff8c`](#insn-00bdff8c) → [`00bdff90`](#insn-00bdff90)
- ブロック [`00bdff90`](#insn-00bdff90) 範囲 `[['00bdff90', '00bdff97']]`
  - `FALL_THROUGH` [`00bdff94`](#insn-00bdff94) → [`00bdff98`](#insn-00bdff98)
- ブロック [`00bdff98`](#insn-00bdff98) 範囲 `[['00bdff98', '00bdffa7']]`
  - `CONDITIONAL_JUMP` [`00bdffa4`](#insn-00bdffa4) → [`00bdffc4`](#insn-00bdffc4)
  - `FALL_THROUGH` [`00bdffa4`](#insn-00bdffa4) → [`00bdffa8`](#insn-00bdffa8)
- ブロック [`00bdffa8`](#insn-00bdffa8) 範囲 `[['00bdffa8', '00bdffc3']]`
- ブロック [`00bdffc4`](#insn-00bdffc4) 範囲 `[['00bdffc4', '00bdffc7']]`

## 命令位置別の参照

- [`00bdfde0`](#insn-00bdfde0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfde4`](#insn-00bdfde4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfde8`](#insn-00bdfde8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdec`](#insn-00bdfdec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdf0`](#insn-00bdfdf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe04`](#insn-00bdfe04) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe0c`](#insn-00bdfe0c) → [`00bdfef0`](#insn-00bdfef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe14`](#insn-00bdfe14) → [`00bdfef0`](#insn-00bdfef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe30`](#insn-00bdfe30) → [`00c5d810`](../00c5d/00c5d810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d810` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe3c`](#insn-00bdfe3c) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe48`](#insn-00bdfe48) → [`00c5da10`](../00c5d/00c5da10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da10` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe68`](#insn-00bdfe68) → [`00bdff14`](#insn-00bdff14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe74`](#insn-00bdfe74) → `01126970`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdfe84`](#insn-00bdfe84) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe98`](#insn-00bdfe98) → [`00c5d8f0`](../00c5d/00c5d8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d8f0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe9c`](#insn-00bdfe9c) → [`00bdff80`](#insn-00bdff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfea8`](#insn-00bdfea8) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bdfeb4`](#insn-00bdfeb4) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdfec0`](#insn-00bdfec0) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bdfecc`](#insn-00bdfecc) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bdfed4`](#insn-00bdfed4) → `00c9b628`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfed8`](#insn-00bdfed8) → [`00bd4814`](../00bd4/00bd4814.md) · `DATA` · `ANALYSIS` · 関数 `00bd4814` · 推定シンボル `_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv` · 推定型 `None`
- [`00bdfee0`](#insn-00bdfee0) → [`00bdff48`](#insn-00bdff48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfeec`](#insn-00bdfeec) → [`00bdff4c`](#insn-00bdff4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfef8`](#insn-00bdfef8) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bdff0c`](#insn-00bdff0c) → [`00c5a7e0`](../00c5a/00c5a7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7e0` · 推定シンボル `None` · 推定型 `None`
- [`00bdff10`](#insn-00bdff10) → [`00bdff98`](#insn-00bdff98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff1c`](#insn-00bdff1c) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bdff24`](#insn-00bdff24) → `002b0848`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdff38`](#insn-00bdff38) → [`00c5d7e0`](../00c5d/00c5d7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d7e0` · 推定シンボル `None` · 推定型 `None`
- [`00bdff40`](#insn-00bdff40) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bdff44`](#insn-00bdff44) → [`00bdff80`](#insn-00bdff80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff50`](#insn-00bdff50) → `00c9b610`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdff50`](#insn-00bdff50) → [`00bcfce4`](../00bcf/00bcfce4.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfce4` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bdff60`](#insn-00bdff60) → [`00c5ab40`](../00c5a/00c5ab40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab40` · 推定シンボル `None` · 推定型 `None`
- [`00bdff68`](#insn-00bdff68) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bdff8c`](#insn-00bdff8c) → [`00c5d950`](../00c5d/00c5d950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d950` · 推定シンボル `None` · 推定型 `None`
- [`00bdff94`](#insn-00bdff94) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bdff9c`](#insn-00bdff9c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffa4`](#insn-00bdffa4) → [`00bdffc4`](#insn-00bdffc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffa8`](#insn-00bdffa8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffac`](#insn-00bdffac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffb0`](#insn-00bdffb0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffb4`](#insn-00bdffb4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffb8`](#insn-00bdffb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffc4`](#insn-00bdffc4) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfde0`](#insn-00bdfde0)

~~~json
{
  "source": "00bdfde0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfde4`](#insn-00bdfde4)

~~~json
{
  "source": "00bdfde4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfde8`](#insn-00bdfde8)

~~~json
{
  "source": "00bdfde8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdec`](#insn-00bdfdec)

~~~json
{
  "source": "00bdfdec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdf0`](#insn-00bdfdf0)

~~~json
{
  "source": "00bdfdf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe04`](#insn-00bdfe04)

~~~json
{
  "source": "00bdfe04",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe0c`](#insn-00bdfe0c)

~~~json
{
  "source": "00bdfe0c",
  "target": "00bdfef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe14`](#insn-00bdfe14)

~~~json
{
  "source": "00bdfe14",
  "target": "00bdfef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe30`](#insn-00bdfe30)

~~~json
{
  "source": "00bdfe30",
  "target": "00c5d810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe3c`](#insn-00bdfe3c)

~~~json
{
  "source": "00bdfe3c",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe48`](#insn-00bdfe48)

~~~json
{
  "source": "00bdfe48",
  "target": "00c5da10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe68`](#insn-00bdfe68)

~~~json
{
  "source": "00bdfe68",
  "target": "00bdff14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe74`](#insn-00bdfe74)

~~~json
{
  "source": "00bdfe74",
  "target": "01126970",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126970",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdfe84`](#insn-00bdfe84)

~~~json
{
  "source": "00bdfe84",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe98`](#insn-00bdfe98)

~~~json
{
  "source": "00bdfe98",
  "target": "00c5d8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe9c`](#insn-00bdfe9c)

~~~json
{
  "source": "00bdfe9c",
  "target": "00bdff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfea8`](#insn-00bdfea8)

~~~json
{
  "source": "00bdfea8",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfeb4`](#insn-00bdfeb4)

~~~json
{
  "source": "00bdfeb4",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfec0`](#insn-00bdfec0)

~~~json
{
  "source": "00bdfec0",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfecc`](#insn-00bdfecc)

~~~json
{
  "source": "00bdfecc",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfed4`](#insn-00bdfed4)

~~~json
{
  "source": "00bdfed4",
  "target": "00c9b628",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b628",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfed8`](#insn-00bdfed8)

~~~json
{
  "source": "00bdfed8",
  "target": "00bd4814",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfee0`](#insn-00bdfee0)

~~~json
{
  "source": "00bdfee0",
  "target": "00bdff48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfeec`](#insn-00bdfeec)

~~~json
{
  "source": "00bdfeec",
  "target": "00bdff4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfef8`](#insn-00bdfef8)

~~~json
{
  "source": "00bdfef8",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff0c`](#insn-00bdff0c)

~~~json
{
  "source": "00bdff0c",
  "target": "00c5a7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff10`](#insn-00bdff10)

~~~json
{
  "source": "00bdff10",
  "target": "00bdff98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff1c`](#insn-00bdff1c)

~~~json
{
  "source": "00bdff1c",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff24`](#insn-00bdff24)

~~~json
{
  "source": "00bdff24",
  "target": "002b0848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0848",
  "offset": 0,
  "size": 38,
  "datatype": "string",
  "bytes": "43726564656e7469616c206973206e6f7420612070686f6e652063726564656e",
  "capture_start": "002b0848",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdff38`](#insn-00bdff38)

~~~json
{
  "source": "00bdff38",
  "target": "00c5d7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff40`](#insn-00bdff40)

~~~json
{
  "source": "00bdff40",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff44`](#insn-00bdff44)

~~~json
{
  "source": "00bdff44",
  "target": "00bdff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff50`](#insn-00bdff50)

~~~json
{
  "source": "00bdff50",
  "target": "00c9b610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b610",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdff50`](#insn-00bdff50)

~~~json
{
  "source": "00bdff50",
  "target": "00bcfce4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff60`](#insn-00bdff60)

~~~json
{
  "source": "00bdff60",
  "target": "00c5ab40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff68`](#insn-00bdff68)

~~~json
{
  "source": "00bdff68",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff8c`](#insn-00bdff8c)

~~~json
{
  "source": "00bdff8c",
  "target": "00c5d950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff94`](#insn-00bdff94)

~~~json
{
  "source": "00bdff94",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff9c`](#insn-00bdff9c)

~~~json
{
  "source": "00bdff9c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffa4`](#insn-00bdffa4)

~~~json
{
  "source": "00bdffa4",
  "target": "00bdffc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffa8`](#insn-00bdffa8)

~~~json
{
  "source": "00bdffa8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffac`](#insn-00bdffac)

~~~json
{
  "source": "00bdffac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffb0`](#insn-00bdffb0)

~~~json
{
  "source": "00bdffb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffb4`](#insn-00bdffb4)

~~~json
{
  "source": "00bdffb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffb8`](#insn-00bdffb8)

~~~json
{
  "source": "00bdffb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffc4`](#insn-00bdffc4)

~~~json
{
  "source": "00bdffc4",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
