# 00bdfbd4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b706d4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b706d4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-657562f1d61f15942d202464fd058d89)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdfffc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfffc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-5081d77257dae35f12dbba92d775797a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfbd4",
  "name": "_ZN8firebase4auth4User6UnlinkEPKc",
  "size": 440,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6c76afe4e8f3d0e732125a21420b187e6692f8df60dec08cc068c05513cda00",
  "source_text_sha256": "d6c76afe4e8f3d0e732125a21420b187e6692f8df60dec08cc068c05513cda00",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfbd4",
        "00bdfd8b"
      ]
    ],
    "bytes_sha256": "f0d53b27ec0d2a0628f6bc936b0740c9add72679b926d40c63c49477850222e0",
    "instruction_count": 110,
    "instruction_bytes": 440,
    "body_bytes": 440,
    "indirect": 3,
    "unresolved": 3
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
- [00c5d800](../00c5d/00c5d800.md)
- [00c5d8d0](../00c5d/00c5d8d0.md)
- [00c5d930](../00c5d/00c5d930.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3186 bytes

~~~c

void _ZN8firebase4auth4User6UnlinkEPKc(long param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  undefined *puVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00bdfbdc to 00cdfc0f has its CatchHandler @ 00be01dc */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
                    /* try { // try from 00bdfcf0 to 00cdfcf7 has its CatchHandler @ 00be02ac */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
              (auStack_68,lVar9,0x15);
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
                    /* try { // try from 00bdfc3c to 00cdfc47 has its CatchHandler @ 00be02ac */
    uVar4 = (**(code **)(*plVar3 + 0x538))(plVar3,param_3);
                    /* try { // try from 00bdfc54 to 00cdfc87 has its CatchHandler @ 00be01e0 */
    uVar5 = FUN_004977f4(plVar3,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126968,
                         uVar4);
    (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
    uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar3,lVar9,auStack_68);
    if ((uVar6 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      puVar10 = *(undefined8 **)(param_2 + 0x98);
      uVar4 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar7 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_78);
      puVar2 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9b620
      ;
      *(undefined8 **)(lVar7 + 0x10) = puVar10;
      *(undefined **)(lVar7 + 0x18) = puVar2;
      if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
        lVar8 = (long)puVar10 + 0x141;
      }
      else {
        lVar8 = puVar10[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar4,uVar5,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9b600
                 ,lVar7,lVar8);
      _ZN8firebase12FutureHandleD2Ev(auStack_78);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar5);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_68);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
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
<a id="insn-00bdfbd4"></a> `00bdfbd4` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdfbd8"></a> `00bdfbd8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfbdc"></a> `00bdfbdc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfbe0"></a> `00bdfbe0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfbe4"></a> `00bdfbe4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdfbe8"></a> `00bdfbe8` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdfbec"></a> `00bdfbec` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bdfbf0"></a> `00bdfbf0` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdfbf4"></a> `00bdfbf4` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfbf8"></a> `00bdfbf8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdfbfc"></a> `00bdfbfc` | `e9 17 00 f9` | str x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfc00"></a> `00bdfc00` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfc04"></a> `00bdfc04` | `29 07 00 b4` | cbz x9,0x00bdfce8 | `CONDITIONAL_JUMP`
<a id="insn-00bdfc08"></a> `00bdfc08` | `28 01 41 f9` | ldr x8,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfc0c"></a> `00bdfc0c` | `e8 06 00 b4` | cbz x8,0x00bdfce8 | `CONDITIONAL_JUMP`
<a id="insn-00bdfc10"></a> `00bdfc10` | `34 41 00 91` | add x20,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bdfc14"></a> `00bdfc14` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bdfc18"></a> `00bdfc18` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdfc1c"></a> `00bdfc1c` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfc20"></a> `00bdfc20` | `a1 02 80 52` | mov w1,#0x15 | `FALL_THROUGH`
<a id="insn-00bdfc24"></a> `00bdfc24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdfc28"></a> `00bdfc28` | `f6 f6 01 94` | bl 0x00c5d800 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfc2c"></a> `00bdfc2c` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfc30"></a> `00bdfc30` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdfc34"></a> `00bdfc34` | `13 ec 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfc38"></a> `00bdfc38` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdfc3c"></a> `00bdfc3c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdfc40"></a> `00bdfc40` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdfc44"></a> `00bdfc44` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdfc48"></a> `00bdfc48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdfc4c"></a> `00bdfc4c` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfc50"></a> `00bdfc50` | `29 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdfc54"></a> `00bdfc54` | `22 b5 44 f9` | ldr x2,[x9, #0x968] | `FALL_THROUGH`
<a id="insn-00bdfc58"></a> `00bdfc58` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bdfc5c"></a> `00bdfc5c` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfc60"></a> `00bdfc60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfc64"></a> `00bdfc64` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bdfc68"></a> `00bdfc68` | `e3 de e2 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfc6c"></a> `00bdfc6c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdfc70"></a> `00bdfc70` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdfc74"></a> `00bdfc74` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdfc78"></a> `00bdfc78` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfc7c"></a> `00bdfc7c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bdfc80"></a> `00bdfc80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdfc84"></a> `00bdfc84` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfc88"></a> `00bdfc88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfc8c"></a> `00bdfc8c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdfc90"></a> `00bdfc90` | `10 f7 01 94` | bl 0x00c5d8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfc94"></a> `00bdfc94` | `80 05 00 37` | tbnz w0,#0x0,0x00bdfd44 | `CONDITIONAL_JUMP`
<a id="insn-00bdfc98"></a> `00bdfc98` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfc9c"></a> `00bdfc9c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfca0"></a> `00bdfca0` | `58 eb 01 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfca4"></a> `00bdfca4` | `fa 4e 40 f9` | ldr x26,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfca8"></a> `00bdfca8` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bdfcac"></a> `00bdfcac` | `f5 eb 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfcb0"></a> `00bdfcb0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdfcb4"></a> `00bdfcb4` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bdfcb8"></a> `00bdfcb8` | `76 df 01 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfcbc"></a> `00bdfcbc` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bdfcc0"></a> `00bdfcc0` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfcc4"></a> `00bdfcc4` | `4f eb 01 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfcc8"></a> `00bdfcc8` | `e8 05 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdfccc"></a> `00bdfccc` | `08 11 43 f9` | ldr x8,[x8, #0x620] | `FALL_THROUGH`
<a id="insn-00bdfcd0"></a> `00bdfcd0` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfcd4"></a> `00bdfcd4` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bdfcd8"></a> `00bdfcd8` | `a8 01 00 37` | tbnz w8,#0x0,0x00bdfd0c | `CONDITIONAL_JUMP`
<a id="insn-00bdfcdc"></a> `00bdfcdc` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bdfce0"></a> `00bdfce0` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdfce4"></a> `00bdfce4` | `0b 00 00 14` | b 0x00bdfd10 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdfce8"></a> `00bdfce8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdfcec"></a> `00bdfcec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bdfcf0"></a> `00bdfcf0` | `e0 ea 01 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfcf4"></a> `00bdfcf4` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bdfcf8"></a> `00bdfcf8` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfcfc"></a> `00bdfcfc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bdfd00"></a> `00bdfd00` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdfd04"></a> `00bdfd04` | `b7 ea 01 94` | bl 0x00c5a7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfd08"></a> `00bdfd08` | `15 00 00 14` | b 0x00bdfd5c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdfd0c"></a> `00bdfd0c` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bdfd10"></a> `00bdfd10` | `e2 05 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdfd14"></a> `00bdfd14` | `42 00 43 f9` | ldr x2,[x2, #0x600] | `FALL_THROUGH`
<a id="insn-00bdfd18"></a> `00bdfd18` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bdfd1c"></a> `00bdfd1c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdfd20"></a> `00bdfd20` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bdfd24"></a> `00bdfd24` | `87 eb 01 94` | bl 0x00c5ab40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfd28"></a> `00bdfd28` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfd2c"></a> `00bdfd2c` | `59 ea 01 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfd30"></a> `00bdfd30` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdfd34"></a> `00bdfd34` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdfd38"></a> `00bdfd38` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdfd3c"></a> `00bdfd3c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdfd40"></a> `00bdfd40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdfd44"></a> `00bdfd44` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfd48"></a> `00bdfd48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdfd4c"></a> `00bdfd4c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdfd50"></a> `00bdfd50` | `f8 f6 01 94` | bl 0x00c5d930 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfd54"></a> `00bdfd54` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdfd58"></a> `00bdfd58` | `4e ea 01 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfd5c"></a> `00bdfd5c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfd60"></a> `00bdfd60` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfd64"></a> `00bdfd64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdfd68"></a> `00bdfd68` | `01 01 00 54` | b.ne 0x00bdfd88 | `CONDITIONAL_JUMP`
<a id="insn-00bdfd6c"></a> `00bdfd6c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdfd70"></a> `00bdfd70` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdfd74"></a> `00bdfd74` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfd78"></a> `00bdfd78` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfd7c"></a> `00bdfd7c` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfd80"></a> `00bdfd80` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdfd84"></a> `00bdfd84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdfd88"></a> `00bdfd88` | `56 df 01 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfbd4`](#insn-00bdfbd4) 範囲 `[['00bdfbd4', '00bdfbdb']]`
  - `FALL_THROUGH` [`00bdfbd8`](#insn-00bdfbd8) → [`00bdfbdc`](#insn-00bdfbdc)
- ブロック [`00bdfbdc`](#insn-00bdfbdc) 範囲 `[['00bdfbdc', '00bdfc07']]`
  - `CONDITIONAL_JUMP` [`00bdfc04`](#insn-00bdfc04) → [`00bdfce8`](#insn-00bdfce8)
  - `FALL_THROUGH` [`00bdfc04`](#insn-00bdfc04) → [`00bdfc08`](#insn-00bdfc08)
- ブロック [`00bdfc08`](#insn-00bdfc08) 範囲 `[['00bdfc08', '00bdfc0f']]`
  - `CONDITIONAL_JUMP` [`00bdfc0c`](#insn-00bdfc0c) → [`00bdfce8`](#insn-00bdfce8)
  - `FALL_THROUGH` [`00bdfc0c`](#insn-00bdfc0c) → [`00bdfc10`](#insn-00bdfc10)
- ブロック [`00bdfc10`](#insn-00bdfc10) 範囲 `[['00bdfc10', '00bdfc3b']]`
  - `FALL_THROUGH` [`00bdfc38`](#insn-00bdfc38) → [`00bdfc3c`](#insn-00bdfc3c)
- ブロック [`00bdfc3c`](#insn-00bdfc3c) 範囲 `[['00bdfc3c', '00bdfc53']]`
  - `FALL_THROUGH` [`00bdfc50`](#insn-00bdfc50) → [`00bdfc54`](#insn-00bdfc54)
- ブロック [`00bdfc54`](#insn-00bdfc54) 範囲 `[['00bdfc54', '00bdfc97']]`
  - `CONDITIONAL_JUMP` [`00bdfc94`](#insn-00bdfc94) → [`00bdfd44`](#insn-00bdfd44)
  - `FALL_THROUGH` [`00bdfc94`](#insn-00bdfc94) → [`00bdfc98`](#insn-00bdfc98)
- ブロック [`00bdfc98`](#insn-00bdfc98) 範囲 `[['00bdfc98', '00bdfcdb']]`
  - `CONDITIONAL_JUMP` [`00bdfcd8`](#insn-00bdfcd8) → [`00bdfd0c`](#insn-00bdfd0c)
  - `FALL_THROUGH` [`00bdfcd8`](#insn-00bdfcd8) → [`00bdfcdc`](#insn-00bdfcdc)
- ブロック [`00bdfcdc`](#insn-00bdfcdc) 範囲 `[['00bdfcdc', '00bdfce7']]`
  - `UNCONDITIONAL_JUMP` [`00bdfce4`](#insn-00bdfce4) → [`00bdfd10`](#insn-00bdfd10)
- ブロック [`00bdfce8`](#insn-00bdfce8) 範囲 `[['00bdfce8', '00bdfcef']]`
  - `FALL_THROUGH` [`00bdfcec`](#insn-00bdfcec) → [`00bdfcf0`](#insn-00bdfcf0)
- ブロック [`00bdfcf0`](#insn-00bdfcf0) 範囲 `[['00bdfcf0', '00bdfd0b']]`
  - `UNCONDITIONAL_JUMP` [`00bdfd08`](#insn-00bdfd08) → [`00bdfd5c`](#insn-00bdfd5c)
- ブロック [`00bdfd0c`](#insn-00bdfd0c) 範囲 `[['00bdfd0c', '00bdfd0f']]`
  - `FALL_THROUGH` [`00bdfd0c`](#insn-00bdfd0c) → [`00bdfd10`](#insn-00bdfd10)
- ブロック [`00bdfd10`](#insn-00bdfd10) 範囲 `[['00bdfd10', '00bdfd43']]`
  - `FALL_THROUGH` [`00bdfd40`](#insn-00bdfd40) → [`00bdfd44`](#insn-00bdfd44)
- ブロック [`00bdfd44`](#insn-00bdfd44) 範囲 `[['00bdfd44', '00bdfd5b']]`
  - `FALL_THROUGH` [`00bdfd58`](#insn-00bdfd58) → [`00bdfd5c`](#insn-00bdfd5c)
- ブロック [`00bdfd5c`](#insn-00bdfd5c) 範囲 `[['00bdfd5c', '00bdfd6b']]`
  - `CONDITIONAL_JUMP` [`00bdfd68`](#insn-00bdfd68) → [`00bdfd88`](#insn-00bdfd88)
  - `FALL_THROUGH` [`00bdfd68`](#insn-00bdfd68) → [`00bdfd6c`](#insn-00bdfd6c)
- ブロック [`00bdfd6c`](#insn-00bdfd6c) 範囲 `[['00bdfd6c', '00bdfd87']]`
- ブロック [`00bdfd88`](#insn-00bdfd88) 範囲 `[['00bdfd88', '00bdfd8b']]`

## 命令位置別の参照

- [`00bdfbd8`](#insn-00bdfbd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfbdc`](#insn-00bdfbdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfbe0`](#insn-00bdfbe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfbe4`](#insn-00bdfbe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfbe8`](#insn-00bdfbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfbfc`](#insn-00bdfbfc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc04`](#insn-00bdfc04) → [`00bdfce8`](#insn-00bdfce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc0c`](#insn-00bdfc0c) → [`00bdfce8`](#insn-00bdfce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc28`](#insn-00bdfc28) → [`00c5d800`](../00c5d/00c5d800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d800` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc34`](#insn-00bdfc34) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc54`](#insn-00bdfc54) → `01126968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdfc68`](#insn-00bdfc68) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc90`](#insn-00bdfc90) → [`00c5d8d0`](../00c5d/00c5d8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d8d0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc94`](#insn-00bdfc94) → [`00bdfd44`](#insn-00bdfd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfca0`](#insn-00bdfca0) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bdfcac`](#insn-00bdfcac) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdfcb8`](#insn-00bdfcb8) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bdfcc4`](#insn-00bdfcc4) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bdfccc`](#insn-00bdfccc) → `00c9b620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfcd0`](#insn-00bdfcd0) → [`00bd4404`](../00bd4/00bd4404.md) · `DATA` · `ANALYSIS` · 関数 `00bd4404` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bdfcd8`](#insn-00bdfcd8) → [`00bdfd0c`](#insn-00bdfd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfce4`](#insn-00bdfce4) → [`00bdfd10`](#insn-00bdfd10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfcf0`](#insn-00bdfcf0) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd04`](#insn-00bdfd04) → [`00c5a7e0`](../00c5a/00c5a7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7e0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd08`](#insn-00bdfd08) → [`00bdfd5c`](#insn-00bdfd5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd14`](#insn-00bdfd14) → `00c9b600`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfd14`](#insn-00bdfd14) → [`00bcf91c`](../00bcf/00bcf91c.md) · `PARAM` · `ANALYSIS` · 関数 `00bcf91c` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bdfd24`](#insn-00bdfd24) → [`00c5ab40`](../00c5a/00c5ab40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab40` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd2c`](#insn-00bdfd2c) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd50`](#insn-00bdfd50) → [`00c5d930`](../00c5d/00c5d930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d930` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd58`](#insn-00bdfd58) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd60`](#insn-00bdfd60) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd68`](#insn-00bdfd68) → [`00bdfd88`](#insn-00bdfd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd6c`](#insn-00bdfd6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd70`](#insn-00bdfd70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd74`](#insn-00bdfd74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd78`](#insn-00bdfd78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd7c`](#insn-00bdfd7c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd88`](#insn-00bdfd88) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfbd8`](#insn-00bdfbd8)

~~~json
{
  "source": "00bdfbd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfbdc`](#insn-00bdfbdc)

~~~json
{
  "source": "00bdfbdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfbe0`](#insn-00bdfbe0)

~~~json
{
  "source": "00bdfbe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfbe4`](#insn-00bdfbe4)

~~~json
{
  "source": "00bdfbe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfbe8`](#insn-00bdfbe8)

~~~json
{
  "source": "00bdfbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfbfc`](#insn-00bdfbfc)

~~~json
{
  "source": "00bdfbfc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc04`](#insn-00bdfc04)

~~~json
{
  "source": "00bdfc04",
  "target": "00bdfce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc0c`](#insn-00bdfc0c)

~~~json
{
  "source": "00bdfc0c",
  "target": "00bdfce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc28`](#insn-00bdfc28)

~~~json
{
  "source": "00bdfc28",
  "target": "00c5d800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfc34`](#insn-00bdfc34)

~~~json
{
  "source": "00bdfc34",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfc54`](#insn-00bdfc54)

~~~json
{
  "source": "00bdfc54",
  "target": "01126968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdfc68`](#insn-00bdfc68)

~~~json
{
  "source": "00bdfc68",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfc90`](#insn-00bdfc90)

~~~json
{
  "source": "00bdfc90",
  "target": "00c5d8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfc94`](#insn-00bdfc94)

~~~json
{
  "source": "00bdfc94",
  "target": "00bdfd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfca0`](#insn-00bdfca0)

~~~json
{
  "source": "00bdfca0",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfcac`](#insn-00bdfcac)

~~~json
{
  "source": "00bdfcac",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfcb8`](#insn-00bdfcb8)

~~~json
{
  "source": "00bdfcb8",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfcc4`](#insn-00bdfcc4)

~~~json
{
  "source": "00bdfcc4",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfccc`](#insn-00bdfccc)

~~~json
{
  "source": "00bdfccc",
  "target": "00c9b620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b620",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfcd0`](#insn-00bdfcd0)

~~~json
{
  "source": "00bdfcd0",
  "target": "00bd4404",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfcd8`](#insn-00bdfcd8)

~~~json
{
  "source": "00bdfcd8",
  "target": "00bdfd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfce4`](#insn-00bdfce4)

~~~json
{
  "source": "00bdfce4",
  "target": "00bdfd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfcf0`](#insn-00bdfcf0)

~~~json
{
  "source": "00bdfcf0",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd04`](#insn-00bdfd04)

~~~json
{
  "source": "00bdfd04",
  "target": "00c5a7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd08`](#insn-00bdfd08)

~~~json
{
  "source": "00bdfd08",
  "target": "00bdfd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd14`](#insn-00bdfd14)

~~~json
{
  "source": "00bdfd14",
  "target": "00c9b600",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b600",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfd14`](#insn-00bdfd14)

~~~json
{
  "source": "00bdfd14",
  "target": "00bcf91c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd24`](#insn-00bdfd24)

~~~json
{
  "source": "00bdfd24",
  "target": "00c5ab40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd2c`](#insn-00bdfd2c)

~~~json
{
  "source": "00bdfd2c",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd50`](#insn-00bdfd50)

~~~json
{
  "source": "00bdfd50",
  "target": "00c5d930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd58`](#insn-00bdfd58)

~~~json
{
  "source": "00bdfd58",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd60`](#insn-00bdfd60)

~~~json
{
  "source": "00bdfd60",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd68`](#insn-00bdfd68)

~~~json
{
  "source": "00bdfd68",
  "target": "00bdfd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd6c`](#insn-00bdfd6c)

~~~json
{
  "source": "00bdfd6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd70`](#insn-00bdfd70)

~~~json
{
  "source": "00bdfd70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd74`](#insn-00bdfd74)

~~~json
{
  "source": "00bdfd74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd78`](#insn-00bdfd78)

~~~json
{
  "source": "00bdfd78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd7c`](#insn-00bdfd7c)

~~~json
{
  "source": "00bdfd7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd88`](#insn-00bdfd88)

~~~json
{
  "source": "00bdfd88",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
