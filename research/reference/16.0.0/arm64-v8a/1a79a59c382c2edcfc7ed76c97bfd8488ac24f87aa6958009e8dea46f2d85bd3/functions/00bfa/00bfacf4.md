# 00bfacf4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e2ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0018.md#compare-1d8097c0ec3ff3ad63871429065e2a90)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb11c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb11c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-ba981ce36db9966105080696433cc489)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfacf4",
  "name": "_ZNSt6__ndk18ios_base5iwordEi",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e408280b8d352835bdc831544d40be3d6a79780796579cf85f02c41b3625965",
  "source_text_sha256": "4e408280b8d352835bdc831544d40be3d6a79780796579cf85f02c41b3625965",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfacf4",
        "00bfae07"
      ]
    ],
    "bytes_sha256": "ceac4ee8f9477fb0e1238f48d6dfc3532350afa6d6b924f805c118ab9017a75a",
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

- [00bfb11c](../00bfb/00bfb11c.md)
- [00c57c90](../00c57/00c57c90.md)
- [00c59ca0](../00c59/00c59ca0.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1570 bytes

~~~c

undefined8 * _ZNSt6__ndk18ios_base5iwordEi(long param_1,int param_2)

{
  ulong uVar1;
  void *pvVar2;
  void *pvVar3;
  void *__s;
  uint uVar4;
  void *pvVar5;
  ulong uVar6;
  ulong uVar7;
  
  uVar1 = (long)param_2 + 1;
  if (*(ulong *)(param_1 + 0x68) < uVar1) {
    uVar6 = *(ulong *)(param_1 + 0x68) * 2;
    if (uVar6 < uVar1 || uVar6 - uVar1 == 0) {
      uVar6 = uVar1;
    }
    if (0xffffffffffffffe < uVar1) {
      uVar6 = 0x1fffffffffffffff;
    }
    pvVar5 = realloc(*(void **)(param_1 + 0x58),uVar6 * 8);
    if (pvVar5 == (void *)0x0) {
      uVar4 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar4;
      if ((*(uint *)(param_1 + 0x24) & uVar4) == 0) {
        DAT_01126fa0 = 0;
        return &DAT_01126fa0;
      }
                    /* WARNING: Subroutine does not return */
      FUN_00bfb11c("ios_base::clear");
    }
    uVar7 = *(ulong *)(param_1 + 0x60);
    *(void **)(param_1 + 0x58) = pvVar5;
    if ((long)uVar7 < (long)uVar6) {
      pvVar3 = (void *)(uVar6 * 8 + (long)pvVar5);
      __s = (void *)((long)pvVar5 + uVar7 * 8);
      pvVar2 = (void *)((long)__s + 8);
      if (pvVar2 <= pvVar3) {
        pvVar2 = pvVar3;
      }
      memset(__s,0,((long)pvVar2 + uVar7 * -8 + ~(ulong)pvVar5 & 0xfffffffffffffff8) + 8);
    }
    *(ulong *)(param_1 + 0x68) = uVar6;
  }
  else {
    pvVar5 = *(void **)(param_1 + 0x58);
    uVar7 = *(ulong *)(param_1 + 0x60);
  }
  if (uVar7 <= uVar1) {
    uVar7 = uVar1;
  }
  *(ulong *)(param_1 + 0x60) = uVar7;
  return (undefined8 *)((long)pvVar5 + (long)param_2 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfacf4"></a> `00bfacf4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfacf8"></a> `00bfacf8` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfacfc"></a> `00bfacfc` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfad00"></a> `00bfad00` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfad04"></a> `00bfad04` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfad08"></a> `00bfad08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfad0c"></a> `00bfad0c` | `35 7c 40 93` | sxtw x21,w1 | `FALL_THROUGH`
<a id="insn-00bfad10"></a> `00bfad10` | `08 34 40 f9` | ldr x8,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00bfad14"></a> `00bfad14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfad18"></a> `00bfad18` | `b6 06 00 91` | add x22,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfad1c"></a> `00bfad1c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bfad20"></a> `00bfad20` | `69 04 00 54` | b.ls 0x00bfadac | `CONDITIONAL_JUMP`
<a id="insn-00bfad24"></a> `00bfad24` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfad28"></a> `00bfad28` | `09 00 fe 92` | mov x9,#0xfffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfad2c"></a> `00bfad2c` | `60 2e 40 f9` | ldr x0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfad30"></a> `00bfad30` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bfad34"></a> `00bfad34` | `08 81 96 9a` | csel x8,x8,x22,hi | `FALL_THROUGH`
<a id="insn-00bfad38"></a> `00bfad38` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bfad3c"></a> `00bfad3c` | `09 00 fc 92` | mov x9,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfad40"></a> `00bfad40` | `17 31 89 9a` | csel x23,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bfad44"></a> `00bfad44` | `f4 f2 7d d3` | lsl x20,x23,#0x3 | `FALL_THROUGH`
<a id="insn-00bfad48"></a> `00bfad48` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfad4c"></a> `00bfad4c` | `d5 7b 01 94` | bl 0x00c59ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfad50"></a> `00bfad50` | `40 04 00 b4` | cbz x0,0x00bfadd8 | `CONDITIONAL_JUMP`
<a id="insn-00bfad54"></a> `00bfad54` | `78 32 40 f9` | ldr x24,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00bfad58"></a> `00bfad58` | `60 2e 00 f9` | str x0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfad5c"></a> `00bfad5c` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00bfad60"></a> `00bfad60` | `2a 02 00 54` | b.ge 0x00bfada4 | `CONDITIONAL_JUMP`
<a id="insn-00bfad64"></a> `00bfad64` | `09 f3 7d d3` | lsl x9,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00bfad68"></a> `00bfad68` | `8b 02 00 8b` | add x11,x20,x0 | `FALL_THROUGH`
<a id="insn-00bfad6c"></a> `00bfad6c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfad70"></a> `00bfad70` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bfad74"></a> `00bfad74` | `08 00 09 8b` | add x8,x0,x9 | `FALL_THROUGH`
<a id="insn-00bfad78"></a> `00bfad78` | `0a 21 00 91` | add x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bfad7c"></a> `00bfad7c` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bfad80"></a> `00bfad80` | `4a 81 8b 9a` | csel x10,x10,x11,hi | `FALL_THROUGH`
<a id="insn-00bfad84"></a> `00bfad84` | `eb 03 20 aa` | mvn x11,x0 | `FALL_THROUGH`
<a id="insn-00bfad88"></a> `00bfad88` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bfad8c"></a> `00bfad8c` | `4a 01 0b 8b` | add x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bfad90"></a> `00bfad90` | `49 01 09 cb` | sub x9,x10,x9 | `FALL_THROUGH`
<a id="insn-00bfad94"></a> `00bfad94` | `29 f1 7d 92` | and x9,x9,#-0x8 | `FALL_THROUGH`
<a id="insn-00bfad98"></a> `00bfad98` | `22 21 00 91` | add x2,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bfad9c"></a> `00bfad9c` | `bd 73 01 94` | bl 0x00c57c90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfada0"></a> `00bfada0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfada4"></a> `00bfada4` | `77 36 00 f9` | str x23,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bfada8"></a> `00bfada8` | `02 00 00 14` | b 0x00bfadb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfadac"></a> `00bfadac` | `60 e2 45 a9` | ldp x0,x24,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfadb0"></a> `00bfadb0` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bfadb4"></a> `00bfadb4` | `00 0c 15 8b` | add x0,x0,x21, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bfadb8"></a> `00bfadb8` | `08 83 96 9a` | csel x8,x24,x22,hi | `FALL_THROUGH`
<a id="insn-00bfadbc"></a> `00bfadbc` | `68 32 00 f9` | str x8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00bfadc0"></a> `00bfadc0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfadc4"></a> `00bfadc4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfadc8"></a> `00bfadc8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfadcc"></a> `00bfadcc` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfadd0"></a> `00bfadd0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfadd4"></a> `00bfadd4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfadd8"></a> `00bfadd8` | `68 26 44 29` | ldp w8,w9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfaddc"></a> `00bfaddc` | `08 01 00 32` | orr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfade0"></a> `00bfade0` | `3f 01 08 6a` | tst w9,w8 | `FALL_THROUGH`
<a id="insn-00bfade4"></a> `00bfade4` | `68 22 00 b9` | str w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfade8"></a> `00bfade8` | `a1 00 00 54` | b.ne 0x00bfadfc | `CONDITIONAL_JUMP`
<a id="insn-00bfadec"></a> `00bfadec` | `60 29 00 90` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bfadf0"></a> `00bfadf0` | `00 80 3e 91` | add x0,x0,#0xfa0 | `FALL_THROUGH`
<a id="insn-00bfadf4"></a> `00bfadf4` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bfadf8"></a> `00bfadf8` | `f2 ff ff 17` | b 0x00bfadc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfadfc"></a> `00bfadfc` | `60 b5 ff b0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bfae00"></a> `00bfae00` | `00 68 11 91` | add x0,x0,#0x45a | `FALL_THROUGH`
<a id="insn-00bfae04"></a> `00bfae04` | `c6 00 00 94` | bl 0x00bfb11c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfacf4`](#insn-00bfacf4) 範囲 `[['00bfacf4', '00bfad23']]`
  - `CONDITIONAL_JUMP` [`00bfad20`](#insn-00bfad20) → [`00bfadac`](#insn-00bfadac)
  - `FALL_THROUGH` [`00bfad20`](#insn-00bfad20) → [`00bfad24`](#insn-00bfad24)
- ブロック [`00bfad24`](#insn-00bfad24) 範囲 `[['00bfad24', '00bfad53']]`
  - `CONDITIONAL_JUMP` [`00bfad50`](#insn-00bfad50) → [`00bfadd8`](#insn-00bfadd8)
  - `FALL_THROUGH` [`00bfad50`](#insn-00bfad50) → [`00bfad54`](#insn-00bfad54)
- ブロック [`00bfad54`](#insn-00bfad54) 範囲 `[['00bfad54', '00bfad63']]`
  - `CONDITIONAL_JUMP` [`00bfad60`](#insn-00bfad60) → [`00bfada4`](#insn-00bfada4)
  - `FALL_THROUGH` [`00bfad60`](#insn-00bfad60) → [`00bfad64`](#insn-00bfad64)
- ブロック [`00bfad64`](#insn-00bfad64) 範囲 `[['00bfad64', '00bfada3']]`
  - `FALL_THROUGH` [`00bfada0`](#insn-00bfada0) → [`00bfada4`](#insn-00bfada4)
- ブロック [`00bfada4`](#insn-00bfada4) 範囲 `[['00bfada4', '00bfadab']]`
  - `UNCONDITIONAL_JUMP` [`00bfada8`](#insn-00bfada8) → [`00bfadb0`](#insn-00bfadb0)
- ブロック [`00bfadac`](#insn-00bfadac) 範囲 `[['00bfadac', '00bfadaf']]`
  - `FALL_THROUGH` [`00bfadac`](#insn-00bfadac) → [`00bfadb0`](#insn-00bfadb0)
- ブロック [`00bfadb0`](#insn-00bfadb0) 範囲 `[['00bfadb0', '00bfadbf']]`
  - `FALL_THROUGH` [`00bfadbc`](#insn-00bfadbc) → [`00bfadc0`](#insn-00bfadc0)
- ブロック [`00bfadc0`](#insn-00bfadc0) 範囲 `[['00bfadc0', '00bfadd7']]`
- ブロック [`00bfadd8`](#insn-00bfadd8) 範囲 `[['00bfadd8', '00bfadeb']]`
  - `CONDITIONAL_JUMP` [`00bfade8`](#insn-00bfade8) → [`00bfadfc`](#insn-00bfadfc)
  - `FALL_THROUGH` [`00bfade8`](#insn-00bfade8) → [`00bfadec`](#insn-00bfadec)
- ブロック [`00bfadec`](#insn-00bfadec) 範囲 `[['00bfadec', '00bfadfb']]`
  - `UNCONDITIONAL_JUMP` [`00bfadf8`](#insn-00bfadf8) → [`00bfadc0`](#insn-00bfadc0)
- ブロック [`00bfadfc`](#insn-00bfadfc) 範囲 `[['00bfadfc', '00bfae07']]`

## 命令位置別の参照

- [`00bfacf8`](#insn-00bfacf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacfc`](#insn-00bfacfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad00`](#insn-00bfad00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad04`](#insn-00bfad04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad20`](#insn-00bfad20) → [`00bfadac`](#insn-00bfadac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad4c`](#insn-00bfad4c) → [`00c59ca0`](../00c59/00c59ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ca0` · 推定シンボル `None` · 推定型 `None`
- [`00bfad50`](#insn-00bfad50) → [`00bfadd8`](#insn-00bfadd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad60`](#insn-00bfad60) → [`00bfada4`](#insn-00bfada4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfad9c`](#insn-00bfad9c) → [`00c57c90`](../00c57/00c57c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c90` · 推定シンボル `None` · 推定型 `None`
- [`00bfada8`](#insn-00bfada8) → [`00bfadb0`](#insn-00bfadb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadc0`](#insn-00bfadc0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadc4`](#insn-00bfadc4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadc8`](#insn-00bfadc8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadcc`](#insn-00bfadcc) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfade8`](#insn-00bfade8) → [`00bfadfc`](#insn-00bfadfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfadf0`](#insn-00bfadf0) → `01126fa0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bfadf4`](#insn-00bfadf4) → `01126fa0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bfadf8`](#insn-00bfadf8) → [`00bfadc0`](#insn-00bfadc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfae00`](#insn-00bfae00) → `002a745a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfae04`](#insn-00bfae04) → [`00bfb11c`](../00bfb/00bfb11c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfb11c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfacf8`](#insn-00bfacf8)

~~~json
{
  "source": "00bfacf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacfc`](#insn-00bfacfc)

~~~json
{
  "source": "00bfacfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad00`](#insn-00bfad00)

~~~json
{
  "source": "00bfad00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad04`](#insn-00bfad04)

~~~json
{
  "source": "00bfad04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad20`](#insn-00bfad20)

~~~json
{
  "source": "00bfad20",
  "target": "00bfadac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad4c`](#insn-00bfad4c)

~~~json
{
  "source": "00bfad4c",
  "target": "00c59ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfad50`](#insn-00bfad50)

~~~json
{
  "source": "00bfad50",
  "target": "00bfadd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad60`](#insn-00bfad60)

~~~json
{
  "source": "00bfad60",
  "target": "00bfada4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfad9c`](#insn-00bfad9c)

~~~json
{
  "source": "00bfad9c",
  "target": "00c57c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfada8`](#insn-00bfada8)

~~~json
{
  "source": "00bfada8",
  "target": "00bfadb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadc0`](#insn-00bfadc0)

~~~json
{
  "source": "00bfadc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadc4`](#insn-00bfadc4)

~~~json
{
  "source": "00bfadc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadc8`](#insn-00bfadc8)

~~~json
{
  "source": "00bfadc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadcc`](#insn-00bfadcc)

~~~json
{
  "source": "00bfadcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfade8`](#insn-00bfade8)

~~~json
{
  "source": "00bfade8",
  "target": "00bfadfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfadf0`](#insn-00bfadf0)

~~~json
{
  "source": "00bfadf0",
  "target": "01126fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126fa0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfadf4`](#insn-00bfadf4)

~~~json
{
  "source": "00bfadf4",
  "target": "01126fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126fa0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfadf8`](#insn-00bfadf8)

~~~json
{
  "source": "00bfadf8",
  "target": "00bfadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfae00`](#insn-00bfae00)

~~~json
{
  "source": "00bfae00",
  "target": "002a745a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a745a",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "696f735f626173653a3a636c65617200",
  "capture_start": "002a745a",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfae04`](#insn-00bfae04)

~~~json
{
  "source": "00bfae04",
  "target": "00bfb11c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
