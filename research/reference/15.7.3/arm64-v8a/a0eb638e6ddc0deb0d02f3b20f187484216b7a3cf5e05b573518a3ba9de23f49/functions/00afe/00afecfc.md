# 00afecfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afec34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afec34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-470ecbac52cab4d4b02ae0119e56b1f3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afed40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afed40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-3bb24b50e7affa014a39901de3852461)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afecfc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E",
  "size": 796,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ddb6839f7b549f5204a6adf1cb82689c9dbe792e630e99143342e6c74f4b373f",
  "source_text_sha256": "ddb6839f7b549f5204a6adf1cb82689c9dbe792e630e99143342e6c74f4b373f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afecfc",
        "00aff017"
      ]
    ],
    "bytes_sha256": "d05a63eb77499e288639a7223816cf4214d3c571c4e55f0c91130b095aa66688",
    "instruction_count": 199,
    "instruction_bytes": 796,
    "body_bytes": 796,
    "indirect": 8,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

- [00bddf70](../00bdd/00bddf70.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddc00](../00bdd/00bddc00.md)
- [00bddd50](../00bdd/00bddd50.md)
- [00bddd60](../00bdd/00bddd60.md)
- [00bdddc0](../00bdd/00bdddc0.md)
- [00bde710](../00bde/00bde710.md)
- [00bded40](../00bde/00bded40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5780 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
               (ulong *param_1,long *param_2,int param_3,undefined8 param_4,undefined8 param_5)

{
  long lVar1;
  undefined4 *puVar2;
  undefined8 *puVar3;
  long lVar4;
  ulong uVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  long *plVar9;
  undefined1 auStack_a8 [40];
  long *local_80;
  ulong uStack_78;
  long *local_70;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
                    /* catch() { ... } // from try @ 00af6fa4 with catch @ 00afed38 */
  puVar2 = (undefined4 *)_Znwm(0x70);
  *(undefined8 *)(puVar2 + 10) = param_4;
  *(undefined8 *)(puVar2 + 0xc) = param_5;
                    /* catch() { ... } // from try @ 00af6f90 with catch @ 00afed58 */
  *(undefined8 *)(puVar2 + 0xe) = 0;
  *(undefined8 *)(puVar2 + 0x10) = 0;
  *(undefined8 *)(puVar2 + 0x18) = 0;
  *(undefined8 *)(puVar2 + 0x1a) = 0;
  *puVar2 = 1;
  *(undefined8 *)(puVar2 + 3) = 0;
  *(undefined8 *)(puVar2 + 1) = 0;
  *(undefined8 *)(puVar2 + 7) = 0;
  *(undefined8 *)(puVar2 + 5) = 0;
  *(undefined8 *)(puVar2 + 0x12) = 0;
  *(undefined4 **)(puVar2 + 0x14) = puVar2 + 0x14;
  *(undefined4 **)(puVar2 + 0x16) = puVar2 + 0x14;
  _ZN8firebase5Mutex7AcquireEv(param_2 + 1);
  plVar6 = param_2 + 7;
  plVar7 = (long *)*plVar6;
  uVar5 = param_2[9];
  lVar4 = uVar5 + 1;
  if (uVar5 == 0xffffffffffffffff) {
    lVar4 = 1;
  }
  param_2[9] = lVar4;
  plVar9 = plVar6;
  if (plVar7 != (long *)0x0) {
    plVar6 = param_2 + 7;
    do {
      while (plVar8 = plVar7, plVar9 = plVar8, uVar5 < (ulong)plVar8[4]) {
        plVar6 = plVar8;
        plVar7 = (long *)*plVar8;
        if ((long *)*plVar8 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00af6cd0 with catch @ 00afee00 */
          lVar4 = *plVar8;
          goto joined_r0x00afede4;
        }
      }
      if (uVar5 <= (ulong)plVar8[4]) break;
      plVar6 = plVar8 + 1;
                    /* catch() { ... } // from try @ 00af6f38 with catch @ 00afedc8 */
      plVar7 = (long *)*plVar6;
    } while ((long *)*plVar6 != (long *)0x0);
  }
  lVar4 = *plVar6;
  plVar8 = plVar6;
joined_r0x00afede4:
  if (lVar4 == 0) {
                    /* catch() { ... } // from try @ 00af7c1c with catch @ 00afee10 */
    puVar3 = (undefined8 *)_Znwm(0x30);
                    /* catch() { ... } // from try @ 00af6a28 with catch @ 00afee14 */
    puVar3[4] = uVar5;
    puVar3[5] = puVar2;
    *puVar3 = 0;
    puVar3[1] = 0;
    puVar3[2] = plVar9;
    *plVar8 = (long)puVar3;
    if (*(long *)param_2[6] != 0) {
      param_2[6] = *(long *)param_2[6];
      puVar3 = (undefined8 *)*plVar8;
    }
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_2[7],puVar3)
    ;
    param_2[8] = param_2[8] + 1;
    *param_1 = uVar5;
    param_1[1] = (ulong)param_2;
  }
  else {
                    /* catch() { ... } // from try @ 00af6f18 with catch @ 00afedec */
    *param_1 = uVar5;
                    /* catch() { ... } // from try @ 00af6d7c with catch @ 00afedf0 */
    param_1[1] = (ulong)param_2;
    if (param_2 == (long *)0x0) goto joined_r0x00afee8c;
  }
                    /* catch() { ... } // from try @ 00af6a1c with catch @ 00afee70 */
  (**(code **)(*param_2 + 0x10))(param_2,param_1);
  _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E(param_1[1] + 200,param_1,FUN_00b00cbc);
joined_r0x00afee8c:
                    /* catch() { ... } // from try @ 00af6a08 with catch @ 00afee90 */
  if ((-1 < param_3) && (param_3 < (int)((ulong)(param_2[0xb] - param_2[10]) >> 6))) {
    _ZN8firebase5MutexC2ENS0_4ModeE(auStack_a8,0);
    uStack_78 = *param_1;
    local_70 = (long *)param_1[1];
    local_80 = param_2;
    if (local_70 != (long *)0x0) {
      (**(code **)(*local_70 + 0x10))(local_70,&uStack_78);
                    /* catch() { ... } // from try @ 00af69fc with catch @ 00afeef0 */
      _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E
                (local_70 + 0x19,&uStack_78,FUN_00b00cbc);
    }
                    /* catch() { ... } // from try @ 00af69b0 with catch @ 00afef00 */
    (**(code **)(*local_80 + 0x10))(local_80,&uStack_78);
                    /* catch() { ... } // from try @ 00af699c with catch @ 00afef10 */
    if (local_70 != (long *)0x0) {
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(local_70 + 0x19,&uStack_78);
                    /* catch() { ... } // from try @ 00af6990 with catch @ 00afef24 */
                    /* catch() { ... } // from try @ 00af6dc8 with catch @ 00afef28 */
      (**(code **)(*local_70 + 0x18))(local_70,&uStack_78);
      local_70 = (long *)0x0;
    }
    if (local_80 != (long *)0x0) {
      (**(code **)(*local_80 + 0x58))(local_80,auStack_a8);
    }
    _ZN8firebase10FutureBaseaSEOS0_(param_2[10] + (long)param_3 * 0x40,auStack_a8);
    _ZN8firebase5Mutex7AcquireEv(auStack_a8);
    if (local_80 != (long *)0x0) {
      (**(code **)(*local_80 + 0x60))(local_80,auStack_a8);
      (**(code **)(*local_80 + 0x18))(local_80,&uStack_78);
      local_80 = (long *)0x0;
    }
                    /* catch() { ... } // from try @ 00af6dbc with catch @ 00afefa4 */
    _ZN8firebase5Mutex7ReleaseEv(auStack_a8);
    if (local_70 != (long *)0x0) {
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(local_70 + 0x19,&uStack_78);
      plVar6 = local_70;
      local_70 = (long *)0x0;
                    /* catch() { ... } // from try @ 00af6da0 with catch @ 00afefc4 */
      (**(code **)(*plVar6 + 0x18))(plVar6,&uStack_78);
    }
    _ZN8firebase5MutexD1Ev(auStack_a8);
  }
  _ZN8firebase5Mutex7ReleaseEv(param_2 + 1);
  if (*(long *)(lVar1 + 0x28) == local_68) {
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
<a id="insn-00afecfc"></a> `00afecfc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00afed00"></a> `00afed00` | `fb 2b 00 f9` | str x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afed04"></a> `00afed04` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afed08"></a> `00afed08` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afed0c"></a> `00afed0c` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afed10"></a> `00afed10` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afed14"></a> `00afed14` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afed18"></a> `00afed18` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00afed1c"></a> `00afed1c` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afed20"></a> `00afed20` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00afed24"></a> `00afed24` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00afed28"></a> `00afed28` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afed2c"></a> `00afed2c` | `00 0e 80 52` | mov w0,#0x70 | `FALL_THROUGH`
<a id="insn-00afed30"></a> `00afed30` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00afed34"></a> `00afed34` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00afed38"></a> `00afed38` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afed3c"></a> `00afed3c` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00afed40"></a> `00afed40` | `ac 70 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afed44"></a> `00afed44` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afed48"></a> `00afed48` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00afed4c"></a> `00afed4c` | `18 cc 02 a9` | stp x24,x19,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00afed50"></a> `00afed50` | `09 40 01 91` | add x9,x0,#0x50 | `FALL_THROUGH`
<a id="insn-00afed54"></a> `00afed54` | `b3 22 00 91` | add x19,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afed58"></a> `00afed58` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00afed5c"></a> `00afed5c` | `1f fc 03 a9` | stp xzr,xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00afed60"></a> `00afed60` | `1f 7c 06 a9` | stp xzr,xzr,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00afed64"></a> `00afed64` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00afed68"></a> `00afed68` | `00 40 80 3c` | stur q0,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00afed6c"></a> `00afed6c` | `00 40 81 3c` | stur q0,[x0, #0x14] | `FALL_THROUGH`
<a id="insn-00afed70"></a> `00afed70` | `1f a4 04 a9` | stp xzr,x9,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00afed74"></a> `00afed74` | `09 2c 00 f9` | str x9,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00afed78"></a> `00afed78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afed7c"></a> `00afed7c` | `95 7b 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afed80"></a> `00afed80` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00afed84"></a> `00afed84` | `5b 8f 43 f8` | ldr x27,[x26, #0x38]! | `FALL_THROUGH`
<a id="insn-00afed88"></a> `00afed88` | `58 0b 40 f9` | ldr x24,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00afed8c"></a> `00afed8c` | `08 07 00 b1` | adds x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00afed90"></a> `00afed90` | `08 35 9f 9a` | csinc x8,x8,xzr,cc | `FALL_THROUGH`
<a id="insn-00afed94"></a> `00afed94` | `48 0b 00 f9` | str x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00afed98"></a> `00afed98` | `3b 02 00 b4` | cbz x27,0x00afeddc | `CONDITIONAL_JUMP`
<a id="insn-00afed9c"></a> `00afed9c` | `ba e2 00 91` | add x26,x21,#0x38 | `FALL_THROUGH`
<a id="insn-00afeda0"></a> `00afeda0` | `68 13 40 f9` | ldr x8,[x27, #0x20] | `FALL_THROUGH`
<a id="insn-00afeda4"></a> `00afeda4` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00afeda8"></a> `00afeda8` | `c2 00 00 54` | b.cs 0x00afedc0 | `CONDITIONAL_JUMP`
<a id="insn-00afedac"></a> `00afedac` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00afedb0"></a> `00afedb0` | `88 02 00 b4` | cbz x8,0x00afee00 | `CONDITIONAL_JUMP`
<a id="insn-00afedb4"></a> `00afedb4` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00afedb8"></a> `00afedb8` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00afedbc"></a> `00afedbc` | `f9 ff ff 17` | b 0x00afeda0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afedc0"></a> `00afedc0` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00afedc4"></a> `00afedc4` | `e2 00 00 54` | b.cs 0x00afede0 | `CONDITIONAL_JUMP`
<a id="insn-00afedc8"></a> `00afedc8` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00afedcc"></a> `00afedcc` | `48 8f 40 f8` | ldr x8,[x26, #0x8]! | `FALL_THROUGH`
<a id="insn-00afedd0"></a> `00afedd0` | `88 00 00 b4` | cbz x8,0x00afede0 | `CONDITIONAL_JUMP`
<a id="insn-00afedd4"></a> `00afedd4` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00afedd8"></a> `00afedd8` | `f2 ff ff 17` | b 0x00afeda0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afeddc"></a> `00afeddc` | `fb 03 1a aa` | mov x27,x26 | `FALL_THROUGH`
<a id="insn-00afede0"></a> `00afede0` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00afede4"></a> `00afede4` | `48 01 00 b4` | cbz x8,0x00afee0c | `CONDITIONAL_JUMP`
<a id="insn-00afede8"></a> `00afede8` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00afedec"></a> `00afedec` | `d8 02 00 f9` | str x24,[x22] | `FALL_THROUGH`
<a id="insn-00afedf0"></a> `00afedf0` | `f5 8e 00 f8` | str x21,[x23, #0x8]! | `FALL_THROUGH`
<a id="insn-00afedf4"></a> `00afedf4` | `75 03 00 b5` | cbnz x21,0x00afee60 | `CONDITIONAL_JUMP`
<a id="insn-00afedf8"></a> `00afedf8` | `d4 04 f8 36` | tbz w20,#0x1f,0x00afee90 | `CONDITIONAL_JUMP`
<a id="insn-00afedfc"></a> `00afedfc` | `78 00 00 14` | b 0x00afefdc | `UNCONDITIONAL_JUMP`
<a id="insn-00afee00"></a> `00afee00` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00afee04"></a> `00afee04` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00afee08"></a> `00afee08` | `08 ff ff b5` | cbnz x8,0x00afede8 | `CONDITIONAL_JUMP`
<a id="insn-00afee0c"></a> `00afee0c` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00afee10"></a> `00afee10` | `78 70 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afee14"></a> `00afee14` | `18 5c 02 a9` | stp x24,x23,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00afee18"></a> `00afee18` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00afee1c"></a> `00afee1c` | `1b 08 00 f9` | str x27,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afee20"></a> `00afee20` | `40 03 00 f9` | str x0,[x26] | `FALL_THROUGH`
<a id="insn-00afee24"></a> `00afee24` | `a8 1a 40 f9` | ldr x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00afee28"></a> `00afee28` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afee2c"></a> `00afee2c` | `88 00 00 b4` | cbz x8,0x00afee3c | `CONDITIONAL_JUMP`
<a id="insn-00afee30"></a> `00afee30` | `a8 1a 00 f9` | str x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00afee34"></a> `00afee34` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00afee38"></a> `00afee38` | `02 00 00 14` | b 0x00afee40 | `UNCONDITIONAL_JUMP`
<a id="insn-00afee3c"></a> `00afee3c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00afee40"></a> `00afee40` | `a0 1e 40 f9` | ldr x0,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00afee44"></a> `00afee44` | `33 7e 03 94` | bl 0x00bde710 | `UNCONDITIONAL_CALL`
<a id="insn-00afee48"></a> `00afee48` | `a8 22 40 f9` | ldr x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00afee4c"></a> `00afee4c` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00afee50"></a> `00afee50` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afee54"></a> `00afee54` | `a8 22 00 f9` | str x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00afee58"></a> `00afee58` | `f8 86 00 f8` | str x24,[x23], #0x8 | `FALL_THROUGH`
<a id="insn-00afee5c"></a> `00afee5c` | `f5 02 00 f9` | str x21,[x23] | `FALL_THROUGH`
<a id="insn-00afee60"></a> `00afee60` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00afee64"></a> `00afee64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afee68"></a> `00afee68` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afee6c"></a> `00afee6c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afee70"></a> `00afee70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afee74"></a> `00afee74` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00afee78"></a> `00afee78` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00afee7c"></a> `00afee7c` | `02 f2 00 10` | adr x2,0xb00cbc | `FALL_THROUGH`
<a id="insn-00afee80"></a> `00afee80` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afee84"></a> `00afee84` | `00 21 03 91` | add x0,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00afee88"></a> `00afee88` | `b2 7b 03 94` | bl 0x00bddd50 | `UNCONDITIONAL_CALL`
<a id="insn-00afee8c"></a> `00afee8c` | `94 0a f8 37` | tbnz w20,#0x1f,0x00afefdc | `CONDITIONAL_JUMP`
<a id="insn-00afee90"></a> `00afee90` | `a8 26 45 a9` | ldp x8,x9,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00afee94"></a> `00afee94` | `28 01 08 cb` | sub x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00afee98"></a> `00afee98` | `08 fd 46 d3` | lsr x8,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00afee9c"></a> `00afee9c` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-00afeea0"></a> `00afeea0` | `ed 09 00 54` | b.le 0x00afefdc | `CONDITIONAL_JUMP`
<a id="insn-00afeea4"></a> `00afeea4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afeea8"></a> `00afeea8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00afeeac"></a> `00afeeac` | `f8 23 00 91` | add x24,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afeeb0"></a> `00afeeb0` | `c4 7b 03 94` | bl 0x00bdddc0 | `UNCONDITIONAL_CALL`
<a id="insn-00afeeb4"></a> `00afeeb4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afeeb8"></a> `00afeeb8` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00afeebc"></a> `00afeebc` | `16 c3 00 91` | add x22,x24,#0x30 | `FALL_THROUGH`
<a id="insn-00afeec0"></a> `00afeec0` | `f5 23 03 a9` | stp x21,x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afeec4"></a> `00afeec4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00afeec8"></a> `00afeec8` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afeecc"></a> `00afeecc` | `80 01 00 b4` | cbz x0,0x00afeefc | `CONDITIONAL_JUMP`
<a id="insn-00afeed0"></a> `00afeed0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afeed4"></a> `00afeed4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afeed8"></a> `00afeed8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afeedc"></a> `00afeedc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afeee0"></a> `00afeee0` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afeee4"></a> `00afeee4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00afeee8"></a> `00afeee8` | `a2 ee 00 10` | adr x2,0xb00cbc | `FALL_THROUGH`
<a id="insn-00afeeec"></a> `00afeeec` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afeef0"></a> `00afeef0` | `00 21 03 91` | add x0,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00afeef4"></a> `00afeef4` | `97 7b 03 94` | bl 0x00bddd50 | `UNCONDITIONAL_CALL`
<a id="insn-00afeef8"></a> `00afeef8` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afeefc"></a> `00afeefc` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afef00"></a> `00afef00` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00afef04"></a> `00afef04` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afef08"></a> `00afef08` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00afef0c"></a> `00afef0c` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00afef10"></a> `00afef10` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afef14"></a> `00afef14` | `48 01 00 b4` | cbz x8,0x00afef3c | `CONDITIONAL_JUMP`
<a id="insn-00afef18"></a> `00afef18` | `00 21 03 91` | add x0,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00afef1c"></a> `00afef1c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afef20"></a> `00afef20` | `90 7b 03 94` | bl 0x00bddd60 | `UNCONDITIONAL_CALL`
<a id="insn-00afef24"></a> `00afef24` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afef28"></a> `00afef28` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afef2c"></a> `00afef2c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afef30"></a> `00afef30` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afef34"></a> `00afef34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afef38"></a> `00afef38` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afef3c"></a> `00afef3c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afef40"></a> `00afef40` | `a0 00 00 b4` | cbz x0,0x00afef54 | `CONDITIONAL_JUMP`
<a id="insn-00afef44"></a> `00afef44` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afef48"></a> `00afef48` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afef4c"></a> `00afef4c` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00afef50"></a> `00afef50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afef54"></a> `00afef54` | `a8 2a 40 f9` | ldr x8,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00afef58"></a> `00afef58` | `89 7e 40 93` | sxtw x9,w20 | `FALL_THROUGH`
<a id="insn-00afef5c"></a> `00afef5c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afef60"></a> `00afef60` | `00 19 09 8b` | add x0,x8,x9, LSL #0x6 | `FALL_THROUGH`
<a id="insn-00afef64"></a> `00afef64` | `77 7f 03 94` | bl 0x00bded40 | `UNCONDITIONAL_CALL`
<a id="insn-00afef68"></a> `00afef68` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afef6c"></a> `00afef6c` | `19 7b 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afef70"></a> `00afef70` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afef74"></a> `00afef74` | `60 01 00 b4` | cbz x0,0x00afefa0 | `CONDITIONAL_JUMP`
<a id="insn-00afef78"></a> `00afef78` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afef7c"></a> `00afef7c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afef80"></a> `00afef80` | `08 31 40 f9` | ldr x8,[x8, #0x60] | `FALL_THROUGH`
<a id="insn-00afef84"></a> `00afef84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afef88"></a> `00afef88` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afef8c"></a> `00afef8c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afef90"></a> `00afef90` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afef94"></a> `00afef94` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afef98"></a> `00afef98` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afef9c"></a> `00afef9c` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afefa0"></a> `00afefa0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afefa4"></a> `00afefa4` | `0f 7b 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afefa8"></a> `00afefa8` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afefac"></a> `00afefac` | `48 01 00 b4` | cbz x8,0x00afefd4 | `CONDITIONAL_JUMP`
<a id="insn-00afefb0"></a> `00afefb0` | `00 21 03 91` | add x0,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00afefb4"></a> `00afefb4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afefb8"></a> `00afefb8` | `6a 7b 03 94` | bl 0x00bddd60 | `UNCONDITIONAL_CALL`
<a id="insn-00afefbc"></a> `00afefbc` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afefc0"></a> `00afefc0` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afefc4"></a> `00afefc4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afefc8"></a> `00afefc8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afefcc"></a> `00afefcc` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afefd0"></a> `00afefd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afefd4"></a> `00afefd4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afefd8"></a> `00afefd8` | `0a 7b 03 94` | bl 0x00bddc00 | `UNCONDITIONAL_CALL`
<a id="insn-00afefdc"></a> `00afefdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afefe0"></a> `00afefe0` | `00 7b 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afefe4"></a> `00afefe4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00afefe8"></a> `00afefe8` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00afefec"></a> `00afefec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afeff0"></a> `00afeff0` | `21 01 00 54` | b.ne 0x00aff014 | `CONDITIONAL_JUMP`
<a id="insn-00afeff4"></a> `00afeff4` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afeff8"></a> `00afeff8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afeffc"></a> `00afeffc` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aff000"></a> `00aff000` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aff004"></a> `00aff004` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aff008"></a> `00aff008` | `fb 2b 40 f9` | ldr x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aff00c"></a> `00aff00c` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00aff010"></a> `00aff010` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aff014"></a> `00aff014` | `0b 70 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afecfc`](#insn-00afecfc) 範囲 `[['00afecfc', '00afed37']]`
  - `FALL_THROUGH` [`00afed34`](#insn-00afed34) → [`00afed38`](#insn-00afed38)
- ブロック [`00afed38`](#insn-00afed38) 範囲 `[['00afed38', '00afed57']]`
  - `FALL_THROUGH` [`00afed54`](#insn-00afed54) → [`00afed58`](#insn-00afed58)
- ブロック [`00afed58`](#insn-00afed58) 範囲 `[['00afed58', '00afed9b']]`
  - `CONDITIONAL_JUMP` [`00afed98`](#insn-00afed98) → [`00afeddc`](#insn-00afeddc)
  - `FALL_THROUGH` [`00afed98`](#insn-00afed98) → [`00afed9c`](#insn-00afed9c)
- ブロック [`00afed9c`](#insn-00afed9c) 範囲 `[['00afed9c', '00afed9f']]`
  - `FALL_THROUGH` [`00afed9c`](#insn-00afed9c) → [`00afeda0`](#insn-00afeda0)
- ブロック [`00afeda0`](#insn-00afeda0) 範囲 `[['00afeda0', '00afedab']]`
  - `CONDITIONAL_JUMP` [`00afeda8`](#insn-00afeda8) → [`00afedc0`](#insn-00afedc0)
  - `FALL_THROUGH` [`00afeda8`](#insn-00afeda8) → [`00afedac`](#insn-00afedac)
- ブロック [`00afedac`](#insn-00afedac) 範囲 `[['00afedac', '00afedb3']]`
  - `CONDITIONAL_JUMP` [`00afedb0`](#insn-00afedb0) → [`00afee00`](#insn-00afee00)
  - `FALL_THROUGH` [`00afedb0`](#insn-00afedb0) → [`00afedb4`](#insn-00afedb4)
- ブロック [`00afedb4`](#insn-00afedb4) 範囲 `[['00afedb4', '00afedb7']]`
  - `FALL_THROUGH` [`00afedb4`](#insn-00afedb4) → [`00afedb8`](#insn-00afedb8)
- ブロック [`00afedb8`](#insn-00afedb8) 範囲 `[['00afedb8', '00afedbf']]`
  - `UNCONDITIONAL_JUMP` [`00afedbc`](#insn-00afedbc) → [`00afeda0`](#insn-00afeda0)
- ブロック [`00afedc0`](#insn-00afedc0) 範囲 `[['00afedc0', '00afedc7']]`
  - `CONDITIONAL_JUMP` [`00afedc4`](#insn-00afedc4) → [`00afede0`](#insn-00afede0)
  - `FALL_THROUGH` [`00afedc4`](#insn-00afedc4) → [`00afedc8`](#insn-00afedc8)
- ブロック [`00afedc8`](#insn-00afedc8) 範囲 `[['00afedc8', '00afedd3']]`
  - `CONDITIONAL_JUMP` [`00afedd0`](#insn-00afedd0) → [`00afede0`](#insn-00afede0)
  - `FALL_THROUGH` [`00afedd0`](#insn-00afedd0) → [`00afedd4`](#insn-00afedd4)
- ブロック [`00afedd4`](#insn-00afedd4) 範囲 `[['00afedd4', '00afedd7']]`
  - `FALL_THROUGH` [`00afedd4`](#insn-00afedd4) → [`00afedd8`](#insn-00afedd8)
- ブロック [`00afedd8`](#insn-00afedd8) 範囲 `[['00afedd8', '00afeddb']]`
  - `UNCONDITIONAL_JUMP` [`00afedd8`](#insn-00afedd8) → [`00afeda0`](#insn-00afeda0)
- ブロック [`00afeddc`](#insn-00afeddc) 範囲 `[['00afeddc', '00afeddf']]`
  - `FALL_THROUGH` [`00afeddc`](#insn-00afeddc) → [`00afede0`](#insn-00afede0)
- ブロック [`00afede0`](#insn-00afede0) 範囲 `[['00afede0', '00afede7']]`
  - `CONDITIONAL_JUMP` [`00afede4`](#insn-00afede4) → [`00afee0c`](#insn-00afee0c)
  - `FALL_THROUGH` [`00afede4`](#insn-00afede4) → [`00afede8`](#insn-00afede8)
- ブロック [`00afede8`](#insn-00afede8) 範囲 `[['00afede8', '00afedeb']]`
  - `FALL_THROUGH` [`00afede8`](#insn-00afede8) → [`00afedec`](#insn-00afedec)
- ブロック [`00afedec`](#insn-00afedec) 範囲 `[['00afedec', '00afedef']]`
  - `FALL_THROUGH` [`00afedec`](#insn-00afedec) → [`00afedf0`](#insn-00afedf0)
- ブロック [`00afedf0`](#insn-00afedf0) 範囲 `[['00afedf0', '00afedf7']]`
  - `CONDITIONAL_JUMP` [`00afedf4`](#insn-00afedf4) → [`00afee60`](#insn-00afee60)
  - `FALL_THROUGH` [`00afedf4`](#insn-00afedf4) → [`00afedf8`](#insn-00afedf8)
- ブロック [`00afedf8`](#insn-00afedf8) 範囲 `[['00afedf8', '00afedfb']]`
  - `CONDITIONAL_JUMP` [`00afedf8`](#insn-00afedf8) → [`00afee90`](#insn-00afee90)
  - `FALL_THROUGH` [`00afedf8`](#insn-00afedf8) → [`00afedfc`](#insn-00afedfc)
- ブロック [`00afedfc`](#insn-00afedfc) 範囲 `[['00afedfc', '00afedff']]`
  - `UNCONDITIONAL_JUMP` [`00afedfc`](#insn-00afedfc) → [`00afefdc`](#insn-00afefdc)
- ブロック [`00afee00`](#insn-00afee00) 範囲 `[['00afee00', '00afee0b']]`
  - `CONDITIONAL_JUMP` [`00afee08`](#insn-00afee08) → [`00afede8`](#insn-00afede8)
  - `FALL_THROUGH` [`00afee08`](#insn-00afee08) → [`00afee0c`](#insn-00afee0c)
- ブロック [`00afee0c`](#insn-00afee0c) 範囲 `[['00afee0c', '00afee0f']]`
  - `FALL_THROUGH` [`00afee0c`](#insn-00afee0c) → [`00afee10`](#insn-00afee10)
- ブロック [`00afee10`](#insn-00afee10) 範囲 `[['00afee10', '00afee13']]`
  - `FALL_THROUGH` [`00afee10`](#insn-00afee10) → [`00afee14`](#insn-00afee14)
- ブロック [`00afee14`](#insn-00afee14) 範囲 `[['00afee14', '00afee2f']]`
  - `CONDITIONAL_JUMP` [`00afee2c`](#insn-00afee2c) → [`00afee3c`](#insn-00afee3c)
  - `FALL_THROUGH` [`00afee2c`](#insn-00afee2c) → [`00afee30`](#insn-00afee30)
- ブロック [`00afee30`](#insn-00afee30) 範囲 `[['00afee30', '00afee3b']]`
  - `UNCONDITIONAL_JUMP` [`00afee38`](#insn-00afee38) → [`00afee40`](#insn-00afee40)
- ブロック [`00afee3c`](#insn-00afee3c) 範囲 `[['00afee3c', '00afee3f']]`
  - `FALL_THROUGH` [`00afee3c`](#insn-00afee3c) → [`00afee40`](#insn-00afee40)
- ブロック [`00afee40`](#insn-00afee40) 範囲 `[['00afee40', '00afee5f']]`
  - `FALL_THROUGH` [`00afee5c`](#insn-00afee5c) → [`00afee60`](#insn-00afee60)
- ブロック [`00afee60`](#insn-00afee60) 範囲 `[['00afee60', '00afee6f']]`
  - `FALL_THROUGH` [`00afee6c`](#insn-00afee6c) → [`00afee70`](#insn-00afee70)
- ブロック [`00afee70`](#insn-00afee70) 範囲 `[['00afee70', '00afee8f']]`
  - `CONDITIONAL_JUMP` [`00afee8c`](#insn-00afee8c) → [`00afefdc`](#insn-00afefdc)
  - `FALL_THROUGH` [`00afee8c`](#insn-00afee8c) → [`00afee90`](#insn-00afee90)
- ブロック [`00afee90`](#insn-00afee90) 範囲 `[['00afee90', '00afeea3']]`
  - `CONDITIONAL_JUMP` [`00afeea0`](#insn-00afeea0) → [`00afefdc`](#insn-00afefdc)
  - `FALL_THROUGH` [`00afeea0`](#insn-00afeea0) → [`00afeea4`](#insn-00afeea4)
- ブロック [`00afeea4`](#insn-00afeea4) 範囲 `[['00afeea4', '00afeecf']]`
  - `CONDITIONAL_JUMP` [`00afeecc`](#insn-00afeecc) → [`00afeefc`](#insn-00afeefc)
  - `FALL_THROUGH` [`00afeecc`](#insn-00afeecc) → [`00afeed0`](#insn-00afeed0)
- ブロック [`00afeed0`](#insn-00afeed0) 範囲 `[['00afeed0', '00afeeef']]`
  - `FALL_THROUGH` [`00afeeec`](#insn-00afeeec) → [`00afeef0`](#insn-00afeef0)
- ブロック [`00afeef0`](#insn-00afeef0) 範囲 `[['00afeef0', '00afeefb']]`
  - `FALL_THROUGH` [`00afeef8`](#insn-00afeef8) → [`00afeefc`](#insn-00afeefc)
- ブロック [`00afeefc`](#insn-00afeefc) 範囲 `[['00afeefc', '00afeeff']]`
  - `FALL_THROUGH` [`00afeefc`](#insn-00afeefc) → [`00afef00`](#insn-00afef00)
- ブロック [`00afef00`](#insn-00afef00) 範囲 `[['00afef00', '00afef0f']]`
  - `FALL_THROUGH` [`00afef0c`](#insn-00afef0c) → [`00afef10`](#insn-00afef10)
- ブロック [`00afef10`](#insn-00afef10) 範囲 `[['00afef10', '00afef17']]`
  - `CONDITIONAL_JUMP` [`00afef14`](#insn-00afef14) → [`00afef3c`](#insn-00afef3c)
  - `FALL_THROUGH` [`00afef14`](#insn-00afef14) → [`00afef18`](#insn-00afef18)
- ブロック [`00afef18`](#insn-00afef18) 範囲 `[['00afef18', '00afef23']]`
  - `FALL_THROUGH` [`00afef20`](#insn-00afef20) → [`00afef24`](#insn-00afef24)
- ブロック [`00afef24`](#insn-00afef24) 範囲 `[['00afef24', '00afef27']]`
  - `FALL_THROUGH` [`00afef24`](#insn-00afef24) → [`00afef28`](#insn-00afef28)
- ブロック [`00afef28`](#insn-00afef28) 範囲 `[['00afef28', '00afef3b']]`
  - `FALL_THROUGH` [`00afef38`](#insn-00afef38) → [`00afef3c`](#insn-00afef3c)
- ブロック [`00afef3c`](#insn-00afef3c) 範囲 `[['00afef3c', '00afef43']]`
  - `CONDITIONAL_JUMP` [`00afef40`](#insn-00afef40) → [`00afef54`](#insn-00afef54)
  - `FALL_THROUGH` [`00afef40`](#insn-00afef40) → [`00afef44`](#insn-00afef44)
- ブロック [`00afef44`](#insn-00afef44) 範囲 `[['00afef44', '00afef53']]`
  - `FALL_THROUGH` [`00afef50`](#insn-00afef50) → [`00afef54`](#insn-00afef54)
- ブロック [`00afef54`](#insn-00afef54) 範囲 `[['00afef54', '00afef77']]`
  - `CONDITIONAL_JUMP` [`00afef74`](#insn-00afef74) → [`00afefa0`](#insn-00afefa0)
  - `FALL_THROUGH` [`00afef74`](#insn-00afef74) → [`00afef78`](#insn-00afef78)
- ブロック [`00afef78`](#insn-00afef78) 範囲 `[['00afef78', '00afef9f']]`
  - `FALL_THROUGH` [`00afef9c`](#insn-00afef9c) → [`00afefa0`](#insn-00afefa0)
- ブロック [`00afefa0`](#insn-00afefa0) 範囲 `[['00afefa0', '00afefa3']]`
  - `FALL_THROUGH` [`00afefa0`](#insn-00afefa0) → [`00afefa4`](#insn-00afefa4)
- ブロック [`00afefa4`](#insn-00afefa4) 範囲 `[['00afefa4', '00afefaf']]`
  - `CONDITIONAL_JUMP` [`00afefac`](#insn-00afefac) → [`00afefd4`](#insn-00afefd4)
  - `FALL_THROUGH` [`00afefac`](#insn-00afefac) → [`00afefb0`](#insn-00afefb0)
- ブロック [`00afefb0`](#insn-00afefb0) 範囲 `[['00afefb0', '00afefc3']]`
  - `FALL_THROUGH` [`00afefc0`](#insn-00afefc0) → [`00afefc4`](#insn-00afefc4)
- ブロック [`00afefc4`](#insn-00afefc4) 範囲 `[['00afefc4', '00afefd3']]`
  - `FALL_THROUGH` [`00afefd0`](#insn-00afefd0) → [`00afefd4`](#insn-00afefd4)
- ブロック [`00afefd4`](#insn-00afefd4) 範囲 `[['00afefd4', '00afefdb']]`
  - `FALL_THROUGH` [`00afefd8`](#insn-00afefd8) → [`00afefdc`](#insn-00afefdc)
- ブロック [`00afefdc`](#insn-00afefdc) 範囲 `[['00afefdc', '00afeff3']]`
  - `CONDITIONAL_JUMP` [`00afeff0`](#insn-00afeff0) → [`00aff014`](#insn-00aff014)
  - `FALL_THROUGH` [`00afeff0`](#insn-00afeff0) → [`00afeff4`](#insn-00afeff4)
- ブロック [`00afeff4`](#insn-00afeff4) 範囲 `[['00afeff4', '00aff013']]`
- ブロック [`00aff014`](#insn-00aff014) 範囲 `[['00aff014', '00aff017']]`

## 命令位置別の参照

- [`00afed00`](#insn-00afed00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed04`](#insn-00afed04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed08`](#insn-00afed08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed0c`](#insn-00afed0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed10`](#insn-00afed10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed14`](#insn-00afed14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed3c`](#insn-00afed3c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed40`](#insn-00afed40) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afed7c`](#insn-00afed7c) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afed98`](#insn-00afed98) → [`00afeddc`](#insn-00afeddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeda8`](#insn-00afeda8) → [`00afedc0`](#insn-00afedc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedb0`](#insn-00afedb0) → [`00afee00`](#insn-00afee00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedbc`](#insn-00afedbc) → [`00afeda0`](#insn-00afeda0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedc4`](#insn-00afedc4) → [`00afede0`](#insn-00afede0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedd0`](#insn-00afedd0) → [`00afede0`](#insn-00afede0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedd8`](#insn-00afedd8) → [`00afeda0`](#insn-00afeda0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afede4`](#insn-00afede4) → [`00afee0c`](#insn-00afee0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedf4`](#insn-00afedf4) → [`00afee60`](#insn-00afee60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedf8`](#insn-00afedf8) → [`00afee90`](#insn-00afee90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedfc`](#insn-00afedfc) → [`00afefdc`](#insn-00afefdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee08`](#insn-00afee08) → [`00afede8`](#insn-00afede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee10`](#insn-00afee10) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afee2c`](#insn-00afee2c) → [`00afee3c`](#insn-00afee3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee38`](#insn-00afee38) → [`00afee40`](#insn-00afee40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee44`](#insn-00afee44) → [`00bde710`](../00bde/00bde710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde710` · 推定シンボル `None` · 推定型 `None`
- [`00afee7c`](#insn-00afee7c) → [`00b00cbc`](../00b00/00b00cbc.md) · `PARAM` · `ANALYSIS` · 関数 `00b00cbc` · 推定シンボル `None` · 推定型 `None`
- [`00afee88`](#insn-00afee88) → [`00bddd50`](../00bdd/00bddd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd50` · 推定シンボル `None` · 推定型 `None`
- [`00afee8c`](#insn-00afee8c) → [`00afefdc`](#insn-00afefdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeea0`](#insn-00afeea0) → [`00afefdc`](#insn-00afefdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeeb0`](#insn-00afeeb0) → [`00bdddc0`](../00bdd/00bdddc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddc0` · 推定シンボル `None` · 推定型 `None`
- [`00afeec0`](#insn-00afeec0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeec8`](#insn-00afeec8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeecc`](#insn-00afeecc) → [`00afeefc`](#insn-00afeefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeee0`](#insn-00afeee0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeee8`](#insn-00afeee8) → [`00b00cbc`](../00b00/00b00cbc.md) · `PARAM` · `ANALYSIS` · 関数 `00b00cbc` · 推定シンボル `None` · 推定型 `None`
- [`00afeef4`](#insn-00afeef4) → [`00bddd50`](../00bdd/00bddd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd50` · 推定シンボル `None` · 推定型 `None`
- [`00afeef8`](#insn-00afeef8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef10`](#insn-00afef10) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef14`](#insn-00afef14) → [`00afef3c`](#insn-00afef3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef20`](#insn-00afef20) → [`00bddd60`](../00bdd/00bddd60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd60` · 推定シンボル `None` · 推定型 `None`
- [`00afef24`](#insn-00afef24) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef38`](#insn-00afef38) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef3c`](#insn-00afef3c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef40`](#insn-00afef40) → [`00afef54`](#insn-00afef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef64`](#insn-00afef64) → [`00bded40`](../00bde/00bded40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded40` · 推定シンボル `None` · 推定型 `None`
- [`00afef6c`](#insn-00afef6c) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afef70`](#insn-00afef70) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef74`](#insn-00afef74) → [`00afefa0`](#insn-00afefa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef88`](#insn-00afef88) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef9c`](#insn-00afef9c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefa4`](#insn-00afefa4) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afefa8`](#insn-00afefa8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefac`](#insn-00afefac) → [`00afefd4`](#insn-00afefd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefb8`](#insn-00afefb8) → [`00bddd60`](../00bdd/00bddd60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd60` · 推定シンボル `None` · 推定型 `None`
- [`00afefbc`](#insn-00afefbc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefc0`](#insn-00afefc0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefd8`](#insn-00afefd8) → [`00bddc00`](../00bdd/00bddc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc00` · 推定シンボル `None` · 推定型 `None`
- [`00afefe0`](#insn-00afefe0) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afefe8`](#insn-00afefe8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeff0`](#insn-00afeff0) → [`00aff014`](#insn-00aff014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeff4`](#insn-00afeff4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeff8`](#insn-00afeff8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeffc`](#insn-00afeffc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff000`](#insn-00aff000) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff004`](#insn-00aff004) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff008`](#insn-00aff008) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff014`](#insn-00aff014) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afed00`](#insn-00afed00)

~~~json
{
  "source": "00afed00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed04`](#insn-00afed04)

~~~json
{
  "source": "00afed04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed08`](#insn-00afed08)

~~~json
{
  "source": "00afed08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed0c`](#insn-00afed0c)

~~~json
{
  "source": "00afed0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed10`](#insn-00afed10)

~~~json
{
  "source": "00afed10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed14`](#insn-00afed14)

~~~json
{
  "source": "00afed14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed3c`](#insn-00afed3c)

~~~json
{
  "source": "00afed3c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed40`](#insn-00afed40)

~~~json
{
  "source": "00afed40",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afed7c`](#insn-00afed7c)

~~~json
{
  "source": "00afed7c",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afed98`](#insn-00afed98)

~~~json
{
  "source": "00afed98",
  "target": "00afeddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeda8`](#insn-00afeda8)

~~~json
{
  "source": "00afeda8",
  "target": "00afedc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedb0`](#insn-00afedb0)

~~~json
{
  "source": "00afedb0",
  "target": "00afee00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedbc`](#insn-00afedbc)

~~~json
{
  "source": "00afedbc",
  "target": "00afeda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedc4`](#insn-00afedc4)

~~~json
{
  "source": "00afedc4",
  "target": "00afede0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedd0`](#insn-00afedd0)

~~~json
{
  "source": "00afedd0",
  "target": "00afede0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedd8`](#insn-00afedd8)

~~~json
{
  "source": "00afedd8",
  "target": "00afeda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afede4`](#insn-00afede4)

~~~json
{
  "source": "00afede4",
  "target": "00afee0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedf4`](#insn-00afedf4)

~~~json
{
  "source": "00afedf4",
  "target": "00afee60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedf8`](#insn-00afedf8)

~~~json
{
  "source": "00afedf8",
  "target": "00afee90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedfc`](#insn-00afedfc)

~~~json
{
  "source": "00afedfc",
  "target": "00afefdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee08`](#insn-00afee08)

~~~json
{
  "source": "00afee08",
  "target": "00afede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee10`](#insn-00afee10)

~~~json
{
  "source": "00afee10",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afee2c`](#insn-00afee2c)

~~~json
{
  "source": "00afee2c",
  "target": "00afee3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee38`](#insn-00afee38)

~~~json
{
  "source": "00afee38",
  "target": "00afee40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee44`](#insn-00afee44)

~~~json
{
  "source": "00afee44",
  "target": "00bde710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afee7c`](#insn-00afee7c)

~~~json
{
  "source": "00afee7c",
  "target": "00b00cbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afee88`](#insn-00afee88)

~~~json
{
  "source": "00afee88",
  "target": "00bddd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afee8c`](#insn-00afee8c)

~~~json
{
  "source": "00afee8c",
  "target": "00afefdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeea0`](#insn-00afeea0)

~~~json
{
  "source": "00afeea0",
  "target": "00afefdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeeb0`](#insn-00afeeb0)

~~~json
{
  "source": "00afeeb0",
  "target": "00bdddc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeec0`](#insn-00afeec0)

~~~json
{
  "source": "00afeec0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeec8`](#insn-00afeec8)

~~~json
{
  "source": "00afeec8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeecc`](#insn-00afeecc)

~~~json
{
  "source": "00afeecc",
  "target": "00afeefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeee0`](#insn-00afeee0)

~~~json
{
  "source": "00afeee0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeee8`](#insn-00afeee8)

~~~json
{
  "source": "00afeee8",
  "target": "00b00cbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeef4`](#insn-00afeef4)

~~~json
{
  "source": "00afeef4",
  "target": "00bddd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeef8`](#insn-00afeef8)

~~~json
{
  "source": "00afeef8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef10`](#insn-00afef10)

~~~json
{
  "source": "00afef10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef14`](#insn-00afef14)

~~~json
{
  "source": "00afef14",
  "target": "00afef3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef20`](#insn-00afef20)

~~~json
{
  "source": "00afef20",
  "target": "00bddd60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afef24`](#insn-00afef24)

~~~json
{
  "source": "00afef24",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef38`](#insn-00afef38)

~~~json
{
  "source": "00afef38",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef3c`](#insn-00afef3c)

~~~json
{
  "source": "00afef3c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef40`](#insn-00afef40)

~~~json
{
  "source": "00afef40",
  "target": "00afef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef64`](#insn-00afef64)

~~~json
{
  "source": "00afef64",
  "target": "00bded40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afef6c`](#insn-00afef6c)

~~~json
{
  "source": "00afef6c",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afef70`](#insn-00afef70)

~~~json
{
  "source": "00afef70",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef74`](#insn-00afef74)

~~~json
{
  "source": "00afef74",
  "target": "00afefa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef88`](#insn-00afef88)

~~~json
{
  "source": "00afef88",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef9c`](#insn-00afef9c)

~~~json
{
  "source": "00afef9c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefa4`](#insn-00afefa4)

~~~json
{
  "source": "00afefa4",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afefa8`](#insn-00afefa8)

~~~json
{
  "source": "00afefa8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefac`](#insn-00afefac)

~~~json
{
  "source": "00afefac",
  "target": "00afefd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefb8`](#insn-00afefb8)

~~~json
{
  "source": "00afefb8",
  "target": "00bddd60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afefbc`](#insn-00afefbc)

~~~json
{
  "source": "00afefbc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefc0`](#insn-00afefc0)

~~~json
{
  "source": "00afefc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefd8`](#insn-00afefd8)

~~~json
{
  "source": "00afefd8",
  "target": "00bddc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afefe0`](#insn-00afefe0)

~~~json
{
  "source": "00afefe0",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afefe8`](#insn-00afefe8)

~~~json
{
  "source": "00afefe8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeff0`](#insn-00afeff0)

~~~json
{
  "source": "00afeff0",
  "target": "00aff014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeff4`](#insn-00afeff4)

~~~json
{
  "source": "00afeff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeff8`](#insn-00afeff8)

~~~json
{
  "source": "00afeff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeffc`](#insn-00afeffc)

~~~json
{
  "source": "00afeffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff000`](#insn-00aff000)

~~~json
{
  "source": "00aff000",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff004`](#insn-00aff004)

~~~json
{
  "source": "00aff004",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff008`](#insn-00aff008)

~~~json
{
  "source": "00aff008",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff014`](#insn-00aff014)

~~~json
{
  "source": "00aff014",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
