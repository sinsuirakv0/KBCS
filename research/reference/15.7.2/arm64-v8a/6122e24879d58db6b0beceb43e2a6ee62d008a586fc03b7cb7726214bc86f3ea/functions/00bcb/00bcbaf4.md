# 00bcbaf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcbbbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbbbc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-5ead316249c4ff943142e91a70242bdd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbaf4",
  "name": "FUN_00bcbaf4",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c10c9b88fd117873dfc27d0076e89579124495c854852e58b7873da86ae95bb",
  "source_text_sha256": "7c10c9b88fd117873dfc27d0076e89579124495c854852e58b7873da86ae95bb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbaf4",
        "00bcbc07"
      ]
    ],
    "bytes_sha256": "fdff7f22cc2fd8c0856f66b82892f57142c7b96d5e95eef30853989238cbb8b7",
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

- [00bc81c8](../00bc8/00bc81c8.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 関連文字列（未確認候補）

~~~text
"> typename "
"template<"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1980 bytes

~~~c

void FUN_00bcbaf4(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char *pcVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  void *pvVar5;
  long lVar6;
  size_t sVar7;
  
  lVar6 = param_2[1];
  pvVar5 = (void *)*param_2;
  uVar3 = *(undefined4 *)(param_2 + 4);
  *(undefined4 *)(param_2 + 4) = 0;
  if ((ulong)param_2[2] < lVar6 + 9U) {
    sVar7 = param_2[2] * 2;
    uVar1 = lVar6 + 0x3e9;
                    /* try { // try from 00bcbb38 to 00ccbb43 has its CatchHandler @ 00bcbba0 */
    if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
      sVar7 = uVar1;
    }
    param_2[2] = sVar7;
    pvVar5 = realloc(pvVar5,sVar7);
                    /* try { // try from 00bcbb44 to 00ccbc07 has its CatchHandler @ 00bcb930 */
    *param_2 = pvVar5;
    if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar6 = param_2[1];
  }
  uVar4 = s_template<_002ae6c0._0_8_;
  ((char *)((long)pvVar5 + lVar6))[8] = '<';
  *(undefined8 *)((long)pvVar5 + lVar6) = uVar4;
  param_2[1] = param_2[1] + 9;
  FUN_00bc81c8(param_1 + 0x18,param_2);
  lVar6 = param_2[1];
  pvVar5 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar6 + 0xbU) {
    sVar7 = param_2[2] * 2;
    uVar1 = lVar6 + 0x3eb;
                    /* catch() { ... } // from try @ 00bcbb38 with catch @ 00bcbba0 */
    if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
      sVar7 = uVar1;
    }
    param_2[2] = sVar7;
    pvVar5 = realloc(pvVar5,sVar7);
    *param_2 = pvVar5;
    if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar6 = param_2[1];
  }
                    /* catch() { ... } // from try @ 00bcba08 with catch @ 00bcbbbc */
  pcVar2 = (char *)((long)pvVar5 + lVar6);
  *(undefined8 *)pcVar2 = s_>_typename_002a0244._0_8_;
  pcVar2[7] = 'a';
  pcVar2[8] = 'm';
  pcVar2[9] = 'e';
  pcVar2[10] = ' ';
  param_2[1] = param_2[1] + 0xb;
  *(undefined4 *)(param_2 + 4) = uVar3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbaf4"></a> `00bcbaf4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbaf8"></a> `00bcbaf8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbafc"></a> `00bcbafc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbb00"></a> `00bcbb00` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbb04"></a> `00bcbb04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbb08"></a> `00bcbb08` | `28 a4 40 a9` | ldp x8,x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb0c"></a> `00bcbb0c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbb10"></a> `00bcbb10` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00bcbb14"></a> `00bcbb14` | `35 20 40 b9` | ldr w21,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbb18"></a> `00bcbb18` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbb1c"></a> `00bcbb1c` | `3f 20 00 b9` | str wzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbb20"></a> `00bcbb20` | `0a 25 00 91` | add x10,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bcbb24"></a> `00bcbb24` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbb28"></a> `00bcbb28` | `49 01 00 54` | b.ls 0x00bcbb50 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb2c"></a> `00bcbb2c` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbb30"></a> `00bcbb30` | `08 a5 0f 91` | add x8,x8,#0x3e9 | `FALL_THROUGH`
<a id="insn-00bcbb34"></a> `00bcbb34` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbb38"></a> `00bcbb38` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbb3c"></a> `00bcbb3c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbb40"></a> `00bcbb40` | `84 45 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb44"></a> `00bcbb44` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbb48"></a> `00bcbb48` | `c0 05 00 b4` | cbz x0,0x00bcbc00 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb4c"></a> `00bcbb4c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb50"></a> `00bcbb50` | `09 b7 ff f0` | adrp x9,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bcbb54"></a> `00bcbb54` | `29 01 1b 91` | add x9,x9,#0x6c0 | `FALL_THROUGH`
<a id="insn-00bcbb58"></a> `00bcbb58` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbb5c"></a> `00bcbb5c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcbb60"></a> `00bcbb60` | `8a 07 80 52` | mov w10,#0x3c | `FALL_THROUGH`
<a id="insn-00bcbb64"></a> `00bcbb64` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb68"></a> `00bcbb68` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bcbb6c"></a> `00bcbb6c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb70"></a> `00bcbb70` | `08 25 00 91` | add x8,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bcbb74"></a> `00bcbb74` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb78"></a> `00bcbb78` | `80 62 00 91` | add x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bcbb7c"></a> `00bcbb7c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbb80"></a> `00bcbb80` | `92 f1 ff 97` | bl 0x00bc81c8 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb84"></a> `00bcbb84` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb88"></a> `00bcbb88` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbb8c"></a> `00bcbb8c` | `0a 2d 00 91` | add x10,x8,#0xb | `FALL_THROUGH`
<a id="insn-00bcbb90"></a> `00bcbb90` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbb94"></a> `00bcbb94` | `49 01 00 54` | b.ls 0x00bcbbbc | `CONDITIONAL_JUMP`
<a id="insn-00bcbb98"></a> `00bcbb98` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbb9c"></a> `00bcbb9c` | `08 ad 0f 91` | add x8,x8,#0x3eb | `FALL_THROUGH`
<a id="insn-00bcbba0"></a> `00bcbba0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbba4"></a> `00bcbba4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbba8"></a> `00bcbba8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbbac"></a> `00bcbbac` | `69 45 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbbb0"></a> `00bcbbb0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbbb4"></a> `00bcbbb4` | `80 02 00 b4` | cbz x0,0x00bcbc04 | `CONDITIONAL_JUMP`
<a id="insn-00bcbbb8"></a> `00bcbbb8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbbbc"></a> `00bcbbbc` | `a9 b6 ff b0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bcbbc0"></a> `00bcbbc0` | `29 11 09 91` | add x9,x9,#0x244 | `FALL_THROUGH`
<a id="insn-00bcbbc4"></a> `00bcbbc4` | `2a ac 8d 52` | mov w10,#0x6d61 | `FALL_THROUGH`
<a id="insn-00bcbbc8"></a> `00bcbbc8` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcbbcc"></a> `00bcbbcc` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbbd0"></a> `00bcbbd0` | `aa 0c a4 72` | movk w10,#0x2065, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbbd4"></a> `00bcbbd4` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bcbbd8"></a> `00bcbbd8` | `0a 71 00 b8` | stur w10,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00bcbbdc"></a> `00bcbbdc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbbe0"></a> `00bcbbe0` | `08 2d 00 91` | add x8,x8,#0xb | `FALL_THROUGH`
<a id="insn-00bcbbe4"></a> `00bcbbe4` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbbe8"></a> `00bcbbe8` | `75 22 00 b9` | str w21,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbec"></a> `00bcbbec` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbf0"></a> `00bcbbf0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbbf4"></a> `00bcbbf4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbbf8"></a> `00bcbbf8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbbfc"></a> `00bcbbfc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbc00"></a> `00bcbc00` | `70 49 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bcbc04"></a> `00bcbc04` | `6f 49 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbaf4`](#insn-00bcbaf4) 範囲 `[['00bcbaf4', '00bcbb2b']]`
  - `CONDITIONAL_JUMP` [`00bcbb28`](#insn-00bcbb28) → [`00bcbb50`](#insn-00bcbb50)
  - `FALL_THROUGH` [`00bcbb28`](#insn-00bcbb28) → [`00bcbb2c`](#insn-00bcbb2c)
- ブロック [`00bcbb2c`](#insn-00bcbb2c) 範囲 `[['00bcbb2c', '00bcbb37']]`
  - `FALL_THROUGH` [`00bcbb34`](#insn-00bcbb34) → [`00bcbb38`](#insn-00bcbb38)
- ブロック [`00bcbb38`](#insn-00bcbb38) 範囲 `[['00bcbb38', '00bcbb43']]`
  - `FALL_THROUGH` [`00bcbb40`](#insn-00bcbb40) → [`00bcbb44`](#insn-00bcbb44)
- ブロック [`00bcbb44`](#insn-00bcbb44) 範囲 `[['00bcbb44', '00bcbb4b']]`
  - `CONDITIONAL_JUMP` [`00bcbb48`](#insn-00bcbb48) → [`00bcbc00`](#insn-00bcbc00)
  - `FALL_THROUGH` [`00bcbb48`](#insn-00bcbb48) → [`00bcbb4c`](#insn-00bcbb4c)
- ブロック [`00bcbb4c`](#insn-00bcbb4c) 範囲 `[['00bcbb4c', '00bcbb4f']]`
  - `FALL_THROUGH` [`00bcbb4c`](#insn-00bcbb4c) → [`00bcbb50`](#insn-00bcbb50)
- ブロック [`00bcbb50`](#insn-00bcbb50) 範囲 `[['00bcbb50', '00bcbb97']]`
  - `CONDITIONAL_JUMP` [`00bcbb94`](#insn-00bcbb94) → [`00bcbbbc`](#insn-00bcbbbc)
  - `FALL_THROUGH` [`00bcbb94`](#insn-00bcbb94) → [`00bcbb98`](#insn-00bcbb98)
- ブロック [`00bcbb98`](#insn-00bcbb98) 範囲 `[['00bcbb98', '00bcbb9f']]`
  - `FALL_THROUGH` [`00bcbb9c`](#insn-00bcbb9c) → [`00bcbba0`](#insn-00bcbba0)
- ブロック [`00bcbba0`](#insn-00bcbba0) 範囲 `[['00bcbba0', '00bcbbb7']]`
  - `CONDITIONAL_JUMP` [`00bcbbb4`](#insn-00bcbbb4) → [`00bcbc04`](#insn-00bcbc04)
  - `FALL_THROUGH` [`00bcbbb4`](#insn-00bcbbb4) → [`00bcbbb8`](#insn-00bcbbb8)
- ブロック [`00bcbbb8`](#insn-00bcbbb8) 範囲 `[['00bcbbb8', '00bcbbbb']]`
  - `FALL_THROUGH` [`00bcbbb8`](#insn-00bcbbb8) → [`00bcbbbc`](#insn-00bcbbbc)
- ブロック [`00bcbbbc`](#insn-00bcbbbc) 範囲 `[['00bcbbbc', '00bcbbff']]`
- ブロック [`00bcbc00`](#insn-00bcbc00) 範囲 `[['00bcbc00', '00bcbc03']]`
- ブロック [`00bcbc04`](#insn-00bcbc04) 範囲 `[['00bcbc04', '00bcbc07']]`

## 命令位置別の参照

- [`00bcbaf8`](#insn-00bcbaf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbafc`](#insn-00bcbafc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb00`](#insn-00bcbb00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb28`](#insn-00bcbb28) → [`00bcbb50`](#insn-00bcbb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb40`](#insn-00bcbb40) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb48`](#insn-00bcbb48) → [`00bcbc00`](#insn-00bcbc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb5c`](#insn-00bcbb5c) → `002ae6c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbb80`](#insn-00bcbb80) → [`00bc81c8`](../00bc8/00bc81c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc81c8` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb94`](#insn-00bcbb94) → [`00bcbbbc`](#insn-00bcbbbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbac`](#insn-00bcbbac) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbb4`](#insn-00bcbbb4) → [`00bcbc04`](#insn-00bcbc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbc8`](#insn-00bcbbc8) → `002a0244`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbbec`](#insn-00bcbbec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf0`](#insn-00bcbbf0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf4`](#insn-00bcbbf4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc00`](#insn-00bcbc00) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc04`](#insn-00bcbc04) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbaf8`](#insn-00bcbaf8)

~~~json
{
  "source": "00bcbaf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbafc`](#insn-00bcbafc)

~~~json
{
  "source": "00bcbafc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb00`](#insn-00bcbb00)

~~~json
{
  "source": "00bcbb00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb28`](#insn-00bcbb28)

~~~json
{
  "source": "00bcbb28",
  "target": "00bcbb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb40`](#insn-00bcbb40)

~~~json
{
  "source": "00bcbb40",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb48`](#insn-00bcbb48)

~~~json
{
  "source": "00bcbb48",
  "target": "00bcbc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb5c`](#insn-00bcbb5c)

~~~json
{
  "source": "00bcbb5c",
  "target": "002ae6c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae6c0",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "74656d706c6174653c00",
  "capture_start": "002ae6c0",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbb80`](#insn-00bcbb80)

~~~json
{
  "source": "00bcbb80",
  "target": "00bc81c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb94`](#insn-00bcbb94)

~~~json
{
  "source": "00bcbb94",
  "target": "00bcbbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbac`](#insn-00bcbbac)

~~~json
{
  "source": "00bcbbac",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbbb4`](#insn-00bcbbb4)

~~~json
{
  "source": "00bcbbb4",
  "target": "00bcbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbc8`](#insn-00bcbbc8)

~~~json
{
  "source": "00bcbbc8",
  "target": "002a0244",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0244",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "3e20747970656e616d652000",
  "capture_start": "002a0244",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbbec`](#insn-00bcbbec)

~~~json
{
  "source": "00bcbbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf0`](#insn-00bcbbf0)

~~~json
{
  "source": "00bcbbf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf4`](#insn-00bcbbf4)

~~~json
{
  "source": "00bcbbf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc00`](#insn-00bcbc00)

~~~json
{
  "source": "00bcbc00",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc04`](#insn-00bcbc04)

~~~json
{
  "source": "00bcbc04",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
