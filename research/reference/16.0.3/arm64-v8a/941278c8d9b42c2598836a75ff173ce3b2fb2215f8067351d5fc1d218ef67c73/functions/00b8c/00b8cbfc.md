# 00b8cbfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b8bc08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bc08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0033.md#compare-8300fdcf81752e3faac5b33c6c77cceb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b8cbfc",
  "name": "_ZN11flatbuffers6Parser9ParseJsonEPKcS2_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b1bf799f9182e74f9225b118092238d4aaa23ca21d417ee77a0373d058baa623",
  "source_text_sha256": "b1bf799f9182e74f9225b118092238d4aaa23ca21d417ee77a0373d058baa623",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b8cbfc",
        "00b8cd0f"
      ]
    ],
    "bytes_sha256": "d629307aa01c56176ed967c592dbcc60d24b3a96e7302a599716356aa73939c5",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c5cab0](../00c5c/00c5cab0.md)
- [00c5d550](../00c5d/00c5d550.md)
- [00c5d650](../00c5d/00c5d650.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2028 bytes

~~~c

void _ZN11flatbuffers6Parser9ParseJsonEPKcS2_(long param_1,undefined8 param_2,undefined8 param_3)

{
  uint uVar1;
  long lVar2;
  bool bVar3;
  long lVar4;
  long lVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  char local_68 [8];
  char local_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  uVar1 = *(uint *)(param_1 + 0x1a8);
  lVar4 = *(long *)(param_1 + 400);
  *(undefined4 *)(param_1 + 0x1a8) = 0;
  *(undefined2 *)(param_1 + 0x1ac) = 0;
  *(ulong *)(param_1 + 0x1a0) = *(long *)(param_1 + 0x1a0) + (ulong)uVar1 * -8;
  if (lVar4 == 0) {
    lVar5 = 0;
    *(undefined8 *)(param_1 + 0x180) = 0;
  }
  else {
    lVar5 = lVar4 + *(long *)(param_1 + 0x180);
  }
  puVar6 = *(undefined8 **)(param_1 + 0x1d0);
  *(undefined4 *)(param_1 + 0x188) = 0;
  *(long *)(param_1 + 0x198) = lVar5;
  *(long *)(param_1 + 0x1a0) = lVar4;
  *(undefined2 *)(param_1 + 0x1b8) = 0;
  *(undefined8 *)(param_1 + 0x1c0) = 1;
  *(undefined8 *)(param_1 + 0x1b0) = 0;
  if (puVar6 != (undefined8 *)0x0) {
    puVar7 = puVar6 + 1;
    _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_21FlatBufferBuilderImplILb0EE19StringOffsetCompareENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
              (puVar6,*puVar7);
    *puVar6 = puVar7;
    puVar6[2] = 0;
    *puVar7 = 0;
  }
  _ZN11flatbuffers6Parser14StartParseFileEPKcS2_(local_60,param_1,param_2,param_3);
  local_60[1] = 1;
  if (local_60[0] == '\0') {
    _ZN11flatbuffers6Parser11DoParseJsonEv(local_68,param_1);
    bVar3 = local_68[0] == '\0';
  }
  else {
                    /* try { // try from 00b8ccc0 to 00c8cce7 has its CatchHandler @ 00b8eadc */
    bVar3 = false;
  }
  if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* try { // try from 00b8ccf4 to 00c8ccfb has its CatchHandler @ 00b8ead4 */
                    /* try { // try from 00b8cd00 to 00c8cd17 has its CatchHandler @ 00b8eacc */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(bVar3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b8cbfc"></a> `00b8cbfc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b8cc00"></a> `00b8cc00` | `f9 13 00 f9` | str x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b8cc04"></a> `00b8cc04` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b8cc08"></a> `00b8cc08` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b8cc0c"></a> `00b8cc0c` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b8cc10"></a> `00b8cc10` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b8cc14"></a> `00b8cc14` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b8cc18"></a> `00b8cc18` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b8cc1c"></a> `00b8cc1c` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b8cc20"></a> `00b8cc20` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00b8cc24"></a> `00b8cc24` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00b8cc28"></a> `00b8cc28` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b8cc2c"></a> `00b8cc2c` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b8cc30"></a> `00b8cc30` | `09 a8 41 b9` | ldr w9,[x0, #0x1a8] | `FALL_THROUGH`
<a id="insn-00b8cc34"></a> `00b8cc34` | `0a d0 40 f9` | ldr x10,[x0, #0x1a0] | `FALL_THROUGH`
<a id="insn-00b8cc38"></a> `00b8cc38` | `08 c8 40 f9` | ldr x8,[x0, #0x190] | `FALL_THROUGH`
<a id="insn-00b8cc3c"></a> `00b8cc3c` | `1f a8 01 b9` | str wzr,[x0, #0x1a8] | `FALL_THROUGH`
<a id="insn-00b8cc40"></a> `00b8cc40` | `1f 58 03 79` | strh wzr,[x0, #0x1ac] | `FALL_THROUGH`
<a id="insn-00b8cc44"></a> `00b8cc44` | `49 0d 09 cb` | sub x9,x10,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00b8cc48"></a> `00b8cc48` | `09 d0 00 f9` | str x9,[x0, #0x1a0] | `FALL_THROUGH`
<a id="insn-00b8cc4c"></a> `00b8cc4c` | `88 00 00 b4` | cbz x8,0x00b8cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b8cc50"></a> `00b8cc50` | `69 c2 40 f9` | ldr x9,[x19, #0x180] | `FALL_THROUGH`
<a id="insn-00b8cc54"></a> `00b8cc54` | `09 01 09 8b` | add x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00b8cc58"></a> `00b8cc58` | `03 00 00 14` | b 0x00b8cc64 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8cc5c"></a> `00b8cc5c` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00b8cc60"></a> `00b8cc60` | `7f c2 00 f9` | str xzr,[x19, #0x180] | `FALL_THROUGH`
<a id="insn-00b8cc64"></a> `00b8cc64` | `76 ea 40 f9` | ldr x22,[x19, #0x1d0] | `FALL_THROUGH`
<a id="insn-00b8cc68"></a> `00b8cc68` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00b8cc6c"></a> `00b8cc6c` | `7f 8a 01 b9` | str wzr,[x19, #0x188] | `FALL_THROUGH`
<a id="insn-00b8cc70"></a> `00b8cc70` | `69 a2 19 a9` | stp x9,x8,[x19, #0x198] | `FALL_THROUGH`
<a id="insn-00b8cc74"></a> `00b8cc74` | `7f 72 03 79` | strh wzr,[x19, #0x1b8] | `FALL_THROUGH`
<a id="insn-00b8cc78"></a> `00b8cc78` | `78 e2 00 f9` | str x24,[x19, #0x1c0] | `FALL_THROUGH`
<a id="insn-00b8cc7c"></a> `00b8cc7c` | `7f da 00 f9` | str xzr,[x19, #0x1b0] | `FALL_THROUGH`
<a id="insn-00b8cc80"></a> `00b8cc80` | `16 01 00 b4` | cbz x22,0x00b8cca0 | `CONDITIONAL_JUMP`
<a id="insn-00b8cc84"></a> `00b8cc84` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00b8cc88"></a> `00b8cc88` | `21 8f 40 f8` | ldr x1,[x25, #0x8]! | `FALL_THROUGH`
<a id="insn-00b8cc8c"></a> `00b8cc8c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b8cc90"></a> `00b8cc90` | `88 3f 03 94` | bl 0x00c5cab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b8cc94"></a> `00b8cc94` | `d9 02 00 f9` | str x25,[x22] | `FALL_THROUGH`
<a id="insn-00b8cc98"></a> `00b8cc98` | `df 0a 00 f9` | str xzr,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00b8cc9c"></a> `00b8cc9c` | `3f 03 00 f9` | str xzr,[x25] | `FALL_THROUGH`
<a id="insn-00b8cca0"></a> `00b8cca0` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b8cca4"></a> `00b8cca4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b8cca8"></a> `00b8cca8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b8ccac"></a> `00b8ccac` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00b8ccb0"></a> `00b8ccb0` | `68 42 03 94` | bl 0x00c5d650 | `UNCONDITIONAL_CALL`
<a id="insn-00b8ccb4"></a> `00b8ccb4` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b8ccb8"></a> `00b8ccb8` | `f8 47 00 39` | strb w24,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00b8ccbc"></a> `00b8ccbc` | `68 00 00 34` | cbz w8,0x00b8ccc8 | `CONDITIONAL_JUMP`
<a id="insn-00b8ccc0"></a> `00b8ccc0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b8ccc4"></a> `00b8ccc4` | `07 00 00 14` | b 0x00b8cce0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8ccc8"></a> `00b8ccc8` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b8cccc"></a> `00b8cccc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b8ccd0"></a> `00b8ccd0` | `20 42 03 94` | bl 0x00c5d550 | `UNCONDITIONAL_CALL`
<a id="insn-00b8ccd4"></a> `00b8ccd4` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b8ccd8"></a> `00b8ccd8` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00b8ccdc"></a> `00b8ccdc` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00b8cce0"></a> `00b8cce0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b8cce4"></a> `00b8cce4` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b8cce8"></a> `00b8cce8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8ccec"></a> `00b8ccec` | `01 01 00 54` | b.ne 0x00b8cd0c | `CONDITIONAL_JUMP`
<a id="insn-00b8ccf0"></a> `00b8ccf0` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b8ccf4"></a> `00b8ccf4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b8ccf8"></a> `00b8ccf8` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b8ccfc"></a> `00b8ccfc` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b8cd00"></a> `00b8cd00` | `f9 13 40 f9` | ldr x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b8cd04"></a> `00b8cd04` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b8cd08"></a> `00b8cd08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b8cd0c"></a> `00b8cd0c` | `9d 30 03 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b8cbfc`](#insn-00b8cbfc) 範囲 `[['00b8cbfc', '00b8cc4f']]`
  - `CONDITIONAL_JUMP` [`00b8cc4c`](#insn-00b8cc4c) → [`00b8cc5c`](#insn-00b8cc5c)
  - `FALL_THROUGH` [`00b8cc4c`](#insn-00b8cc4c) → [`00b8cc50`](#insn-00b8cc50)
- ブロック [`00b8cc50`](#insn-00b8cc50) 範囲 `[['00b8cc50', '00b8cc5b']]`
  - `UNCONDITIONAL_JUMP` [`00b8cc58`](#insn-00b8cc58) → [`00b8cc64`](#insn-00b8cc64)
- ブロック [`00b8cc5c`](#insn-00b8cc5c) 範囲 `[['00b8cc5c', '00b8cc63']]`
  - `FALL_THROUGH` [`00b8cc60`](#insn-00b8cc60) → [`00b8cc64`](#insn-00b8cc64)
- ブロック [`00b8cc64`](#insn-00b8cc64) 範囲 `[['00b8cc64', '00b8cc83']]`
  - `CONDITIONAL_JUMP` [`00b8cc80`](#insn-00b8cc80) → [`00b8cca0`](#insn-00b8cca0)
  - `FALL_THROUGH` [`00b8cc80`](#insn-00b8cc80) → [`00b8cc84`](#insn-00b8cc84)
- ブロック [`00b8cc84`](#insn-00b8cc84) 範囲 `[['00b8cc84', '00b8cc9f']]`
  - `FALL_THROUGH` [`00b8cc9c`](#insn-00b8cc9c) → [`00b8cca0`](#insn-00b8cca0)
- ブロック [`00b8cca0`](#insn-00b8cca0) 範囲 `[['00b8cca0', '00b8ccbf']]`
  - `CONDITIONAL_JUMP` [`00b8ccbc`](#insn-00b8ccbc) → [`00b8ccc8`](#insn-00b8ccc8)
  - `FALL_THROUGH` [`00b8ccbc`](#insn-00b8ccbc) → [`00b8ccc0`](#insn-00b8ccc0)
- ブロック [`00b8ccc0`](#insn-00b8ccc0) 範囲 `[['00b8ccc0', '00b8ccc7']]`
  - `UNCONDITIONAL_JUMP` [`00b8ccc4`](#insn-00b8ccc4) → [`00b8cce0`](#insn-00b8cce0)
- ブロック [`00b8ccc8`](#insn-00b8ccc8) 範囲 `[['00b8ccc8', '00b8ccdf']]`
  - `FALL_THROUGH` [`00b8ccdc`](#insn-00b8ccdc) → [`00b8cce0`](#insn-00b8cce0)
- ブロック [`00b8cce0`](#insn-00b8cce0) 範囲 `[['00b8cce0', '00b8ccef']]`
  - `CONDITIONAL_JUMP` [`00b8ccec`](#insn-00b8ccec) → [`00b8cd0c`](#insn-00b8cd0c)
  - `FALL_THROUGH` [`00b8ccec`](#insn-00b8ccec) → [`00b8ccf0`](#insn-00b8ccf0)
- ブロック [`00b8ccf0`](#insn-00b8ccf0) 範囲 `[['00b8ccf0', '00b8ccf3']]`
  - `FALL_THROUGH` [`00b8ccf0`](#insn-00b8ccf0) → [`00b8ccf4`](#insn-00b8ccf4)
- ブロック [`00b8ccf4`](#insn-00b8ccf4) 範囲 `[['00b8ccf4', '00b8ccff']]`
  - `FALL_THROUGH` [`00b8ccfc`](#insn-00b8ccfc) → [`00b8cd00`](#insn-00b8cd00)
- ブロック [`00b8cd00`](#insn-00b8cd00) 範囲 `[['00b8cd00', '00b8cd0b']]`
- ブロック [`00b8cd0c`](#insn-00b8cd0c) 範囲 `[['00b8cd0c', '00b8cd0f']]`

## 命令位置別の参照

- [`00b8cc00`](#insn-00b8cc00) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc04`](#insn-00b8cc04) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc08`](#insn-00b8cc08) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc0c`](#insn-00b8cc0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc10`](#insn-00b8cc10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc2c`](#insn-00b8cc2c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc4c`](#insn-00b8cc4c) → [`00b8cc5c`](#insn-00b8cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc58`](#insn-00b8cc58) → [`00b8cc64`](#insn-00b8cc64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc80`](#insn-00b8cc80) → [`00b8cca0`](#insn-00b8cca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cc90`](#insn-00b8cc90) → [`00c5cab0`](../00c5c/00c5cab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cab0` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccb0`](#insn-00b8ccb0) → [`00c5d650`](../00c5d/00c5d650.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d650` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccb4`](#insn-00b8ccb4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccb8`](#insn-00b8ccb8) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccbc`](#insn-00b8ccbc) → [`00b8ccc8`](#insn-00b8ccc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccc4`](#insn-00b8ccc4) → [`00b8cce0`](#insn-00b8cce0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccd0`](#insn-00b8ccd0) → [`00c5d550`](../00c5d/00c5d550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d550` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccd4`](#insn-00b8ccd4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cce4`](#insn-00b8cce4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccec`](#insn-00b8ccec) → [`00b8cd0c`](#insn-00b8cd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccf0`](#insn-00b8ccf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccf4`](#insn-00b8ccf4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccf8`](#insn-00b8ccf8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ccfc`](#insn-00b8ccfc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cd00`](#insn-00b8cd00) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8cd0c`](#insn-00b8cd0c) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b8cc00`](#insn-00b8cc00)

~~~json
{
  "source": "00b8cc00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc04`](#insn-00b8cc04)

~~~json
{
  "source": "00b8cc04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc08`](#insn-00b8cc08)

~~~json
{
  "source": "00b8cc08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc0c`](#insn-00b8cc0c)

~~~json
{
  "source": "00b8cc0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc10`](#insn-00b8cc10)

~~~json
{
  "source": "00b8cc10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc2c`](#insn-00b8cc2c)

~~~json
{
  "source": "00b8cc2c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc4c`](#insn-00b8cc4c)

~~~json
{
  "source": "00b8cc4c",
  "target": "00b8cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc58`](#insn-00b8cc58)

~~~json
{
  "source": "00b8cc58",
  "target": "00b8cc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc80`](#insn-00b8cc80)

~~~json
{
  "source": "00b8cc80",
  "target": "00b8cca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cc90`](#insn-00b8cc90)

~~~json
{
  "source": "00b8cc90",
  "target": "00c5cab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8ccb0`](#insn-00b8ccb0)

~~~json
{
  "source": "00b8ccb0",
  "target": "00c5d650",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8ccb4`](#insn-00b8ccb4)

~~~json
{
  "source": "00b8ccb4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccb8`](#insn-00b8ccb8)

~~~json
{
  "source": "00b8ccb8",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccbc`](#insn-00b8ccbc)

~~~json
{
  "source": "00b8ccbc",
  "target": "00b8ccc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccc4`](#insn-00b8ccc4)

~~~json
{
  "source": "00b8ccc4",
  "target": "00b8cce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccd0`](#insn-00b8ccd0)

~~~json
{
  "source": "00b8ccd0",
  "target": "00c5d550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8ccd4`](#insn-00b8ccd4)

~~~json
{
  "source": "00b8ccd4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cce4`](#insn-00b8cce4)

~~~json
{
  "source": "00b8cce4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccec`](#insn-00b8ccec)

~~~json
{
  "source": "00b8ccec",
  "target": "00b8cd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccf0`](#insn-00b8ccf0)

~~~json
{
  "source": "00b8ccf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccf4`](#insn-00b8ccf4)

~~~json
{
  "source": "00b8ccf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccf8`](#insn-00b8ccf8)

~~~json
{
  "source": "00b8ccf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ccfc`](#insn-00b8ccfc)

~~~json
{
  "source": "00b8ccfc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cd00`](#insn-00b8cd00)

~~~json
{
  "source": "00b8cd00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8cd0c`](#insn-00b8cd0c)

~~~json
{
  "source": "00b8cd0c",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
