# 00acabc8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acab00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acab00.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-98fa0979f91d416e8141256e8e116073)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acac0c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acac0c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-b9f3d5a7fd7c7691b5bd272247144c45)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acabc8",
  "name": "FUN_00acabc8",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cbf5375189537341c74eb5ffc1547e923419cdb5b1dc0b79d793b3329b139605",
  "source_text_sha256": "cbf5375189537341c74eb5ffc1547e923419cdb5b1dc0b79d793b3329b139605",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acabc8",
        "00acacbb"
      ]
    ],
    "bytes_sha256": "e48934b6fc085e1b6ca97b397feb2b482bb94225df710948e4bb13e1a6234d66",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aca940](../00aca/00aca940.md)

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1829 bytes

~~~c

void FUN_00acabc8(undefined8 param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4)

{
  undefined1 uVar1;
  void *__ptr;
  undefined8 *puVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  puVar2 = param_2;
  if (param_2 != param_3) {
    do {
      uVar1 = *(undefined1 *)(puVar2 + 2);
      uVar4 = puVar2[1];
      uVar3 = *puVar2;
      param_4[4] = 0;
      param_4[5] = 0;
      param_4[3] = 0;
      *(undefined1 *)(param_4 + 2) = uVar1;
      param_4[1] = uVar4;
      *param_4 = uVar3;
      uVar3 = puVar2[3];
      param_4[4] = puVar2[4];
      param_4[3] = uVar3;
      param_4[5] = puVar2[5];
      uVar4 = puVar2[7];
      uVar3 = puVar2[6];
      puVar2[3] = 0;
      puVar2[4] = 0;
      puVar2[5] = 0;
      param_4[8] = puVar2[8];
      param_4[7] = uVar4;
      param_4[6] = uVar3;
      uVar4 = puVar2[10];
      uVar3 = puVar2[9];
      puVar2[7] = 0;
      puVar2[8] = 0;
      puVar2[6] = 0;
      param_4[0xb] = puVar2[0xb];
      param_4[10] = uVar4;
      param_4[9] = uVar3;
      param_4 = param_4 + 0xc;
      puVar2[10] = 0;
      puVar2[0xb] = 0;
      puVar2[9] = 0;
      puVar2 = puVar2 + 0xc;
    } while (puVar2 != param_3);
    for (; param_2 != param_3; param_2 = param_2 + 0xc) {
      if ((*(byte *)(param_2 + 9) & 1) == 0) {
        if ((*(byte *)(param_2 + 6) & 1) == 0) goto LAB_00acac78;
LAB_00acac94:
        _ZdlPv((void *)param_2[8]);
        __ptr = (void *)param_2[3];
      }
      else {
        _ZdlPv((void *)param_2[0xb]);
        if ((*(byte *)(param_2 + 6) & 1) != 0) goto LAB_00acac94;
LAB_00acac78:
        __ptr = (void *)param_2[3];
      }
      if (__ptr != (void *)0x0) {
                    /* try { // try from 00acaca4 to 00bcacaf has its CatchHandler @ 00acd6cc */
        param_2[4] = __ptr;
        _ZdlPv(__ptr);
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acabc8"></a> `00acabc8` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00acabcc"></a> `00acabcc` | `60 07 00 54` | b.eq 0x00acacb8 | `CONDITIONAL_JUMP`
<a id="insn-00acabd0"></a> `00acabd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acabd4"></a> `00acabd4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acabd8"></a> `00acabd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acabdc"></a> `00acabdc` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00acabe0"></a> `00acabe0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00acabe4"></a> `00acabe4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acabe8"></a> `00acabe8` | `09 41 40 39` | ldrb w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acabec"></a> `00acabec` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00acabf0"></a> `00acabf0` | `7f 7c 02 a9` | stp xzr,xzr,[x3, #0x20] | `FALL_THROUGH`
<a id="insn-00acabf4"></a> `00acabf4` | `7f 0c 00 f9` | str xzr,[x3, #0x18] | `FALL_THROUGH`
<a id="insn-00acabf8"></a> `00acabf8` | `69 40 00 39` | strb w9,[x3, #0x10] | `FALL_THROUGH`
<a id="insn-00acabfc"></a> `00acabfc` | `60 00 80 3d` | str q0,[x3] | `FALL_THROUGH`
<a id="insn-00acac00"></a> `00acac00` | `00 81 c1 3c` | ldur q0,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acac04"></a> `00acac04` | `60 80 81 3c` | stur q0,[x3, #0x18] | `FALL_THROUGH`
<a id="insn-00acac08"></a> `00acac08` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00acac0c"></a> `00acac0c` | `69 14 00 f9` | str x9,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00acac10"></a> `00acac10` | `09 21 40 f9` | ldr x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00acac14"></a> `00acac14` | `00 0d c0 3d` | ldr q0,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00acac18"></a> `00acac18` | `1f fd 01 a9` | stp xzr,xzr,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acac1c"></a> `00acac1c` | `1f 15 00 f9` | str xzr,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00acac20"></a> `00acac20` | `69 20 00 f9` | str x9,[x3, #0x40] | `FALL_THROUGH`
<a id="insn-00acac24"></a> `00acac24` | `60 0c 80 3d` | str q0,[x3, #0x30] | `FALL_THROUGH`
<a id="insn-00acac28"></a> `00acac28` | `09 2d 40 f9` | ldr x9,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00acac2c"></a> `00acac2c` | `00 81 c4 3c` | ldur q0,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00acac30"></a> `00acac30` | `1f fd 03 a9` | stp xzr,xzr,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00acac34"></a> `00acac34` | `1f 19 00 f9` | str xzr,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00acac38"></a> `00acac38` | `69 2c 00 f9` | str x9,[x3, #0x58] | `FALL_THROUGH`
<a id="insn-00acac3c"></a> `00acac3c` | `60 80 84 3c` | stur q0,[x3, #0x48] | `FALL_THROUGH`
<a id="insn-00acac40"></a> `00acac40` | `63 80 01 91` | add x3,x3,#0x60 | `FALL_THROUGH`
<a id="insn-00acac44"></a> `00acac44` | `1f 7d 05 a9` | stp xzr,xzr,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00acac48"></a> `00acac48` | `1f 25 00 f9` | str xzr,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00acac4c"></a> `00acac4c` | `08 81 01 91` | add x8,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00acac50"></a> `00acac50` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00acac54"></a> `00acac54` | `a1 fc ff 54` | b.ne 0x00acabe8 | `CONDITIONAL_JUMP`
<a id="insn-00acac58"></a> `00acac58` | `02 00 00 14` | b 0x00acac60 | `UNCONDITIONAL_JUMP`
<a id="insn-00acac5c"></a> `00acac5c` | `94 82 01 91` | add x20,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00acac60"></a> `00acac60` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00acac64"></a> `00acac64` | `60 02 00 54` | b.eq 0x00acacb0 | `CONDITIONAL_JUMP`
<a id="insn-00acac68"></a> `00acac68` | `88 22 41 39` | ldrb w8,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00acac6c"></a> `00acac6c` | `c8 00 00 37` | tbnz w8,#0x0,0x00acac84 | `CONDITIONAL_JUMP`
<a id="insn-00acac70"></a> `00acac70` | `88 c2 40 39` | ldrb w8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00acac74"></a> `00acac74` | `08 01 00 37` | tbnz w8,#0x0,0x00acac94 | `CONDITIONAL_JUMP`
<a id="insn-00acac78"></a> `00acac78` | `80 0e 40 f9` | ldr x0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00acac7c"></a> `00acac7c` | `40 01 00 b5` | cbnz x0,0x00acaca4 | `CONDITIONAL_JUMP`
<a id="insn-00acac80"></a> `00acac80` | `f7 ff ff 17` | b 0x00acac5c | `UNCONDITIONAL_JUMP`
<a id="insn-00acac84"></a> `00acac84` | `80 2e 40 f9` | ldr x0,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00acac88"></a> `00acac88` | `e2 40 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acac8c"></a> `00acac8c` | `88 c2 40 39` | ldrb w8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00acac90"></a> `00acac90` | `48 ff 07 36` | tbz w8,#0x0,0x00acac78 | `CONDITIONAL_JUMP`
<a id="insn-00acac94"></a> `00acac94` | `80 22 40 f9` | ldr x0,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00acac98"></a> `00acac98` | `de 40 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acac9c"></a> `00acac9c` | `80 0e 40 f9` | ldr x0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00acaca0"></a> `00acaca0` | `e0 fd ff b4` | cbz x0,0x00acac5c | `CONDITIONAL_JUMP`
<a id="insn-00acaca4"></a> `00acaca4` | `80 12 00 f9` | str x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaca8"></a> `00acaca8` | `da 40 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acacac"></a> `00acacac` | `ec ff ff 17` | b 0x00acac5c | `UNCONDITIONAL_JUMP`
<a id="insn-00acacb0"></a> `00acacb0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acacb4"></a> `00acacb4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acacb8"></a> `00acacb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acabc8`](#insn-00acabc8) 範囲 `[['00acabc8', '00acabcf']]`
  - `CONDITIONAL_JUMP` [`00acabcc`](#insn-00acabcc) → [`00acacb8`](#insn-00acacb8)
  - `FALL_THROUGH` [`00acabcc`](#insn-00acabcc) → [`00acabd0`](#insn-00acabd0)
- ブロック [`00acabd0`](#insn-00acabd0) 範囲 `[['00acabd0', '00acabe7']]`
  - `FALL_THROUGH` [`00acabe4`](#insn-00acabe4) → [`00acabe8`](#insn-00acabe8)
- ブロック [`00acabe8`](#insn-00acabe8) 範囲 `[['00acabe8', '00acac57']]`
  - `CONDITIONAL_JUMP` [`00acac54`](#insn-00acac54) → [`00acabe8`](#insn-00acabe8)
  - `FALL_THROUGH` [`00acac54`](#insn-00acac54) → [`00acac58`](#insn-00acac58)
- ブロック [`00acac58`](#insn-00acac58) 範囲 `[['00acac58', '00acac5b']]`
  - `UNCONDITIONAL_JUMP` [`00acac58`](#insn-00acac58) → [`00acac60`](#insn-00acac60)
- ブロック [`00acac5c`](#insn-00acac5c) 範囲 `[['00acac5c', '00acac5f']]`
  - `FALL_THROUGH` [`00acac5c`](#insn-00acac5c) → [`00acac60`](#insn-00acac60)
- ブロック [`00acac60`](#insn-00acac60) 範囲 `[['00acac60', '00acac67']]`
  - `CONDITIONAL_JUMP` [`00acac64`](#insn-00acac64) → [`00acacb0`](#insn-00acacb0)
  - `FALL_THROUGH` [`00acac64`](#insn-00acac64) → [`00acac68`](#insn-00acac68)
- ブロック [`00acac68`](#insn-00acac68) 範囲 `[['00acac68', '00acac6f']]`
  - `CONDITIONAL_JUMP` [`00acac6c`](#insn-00acac6c) → [`00acac84`](#insn-00acac84)
  - `FALL_THROUGH` [`00acac6c`](#insn-00acac6c) → [`00acac70`](#insn-00acac70)
- ブロック [`00acac70`](#insn-00acac70) 範囲 `[['00acac70', '00acac77']]`
  - `CONDITIONAL_JUMP` [`00acac74`](#insn-00acac74) → [`00acac94`](#insn-00acac94)
  - `FALL_THROUGH` [`00acac74`](#insn-00acac74) → [`00acac78`](#insn-00acac78)
- ブロック [`00acac78`](#insn-00acac78) 範囲 `[['00acac78', '00acac7f']]`
  - `CONDITIONAL_JUMP` [`00acac7c`](#insn-00acac7c) → [`00acaca4`](#insn-00acaca4)
  - `FALL_THROUGH` [`00acac7c`](#insn-00acac7c) → [`00acac80`](#insn-00acac80)
- ブロック [`00acac80`](#insn-00acac80) 範囲 `[['00acac80', '00acac83']]`
  - `UNCONDITIONAL_JUMP` [`00acac80`](#insn-00acac80) → [`00acac5c`](#insn-00acac5c)
- ブロック [`00acac84`](#insn-00acac84) 範囲 `[['00acac84', '00acac93']]`
  - `CONDITIONAL_JUMP` [`00acac90`](#insn-00acac90) → [`00acac78`](#insn-00acac78)
  - `FALL_THROUGH` [`00acac90`](#insn-00acac90) → [`00acac94`](#insn-00acac94)
- ブロック [`00acac94`](#insn-00acac94) 範囲 `[['00acac94', '00acaca3']]`
  - `CONDITIONAL_JUMP` [`00acaca0`](#insn-00acaca0) → [`00acac5c`](#insn-00acac5c)
  - `FALL_THROUGH` [`00acaca0`](#insn-00acaca0) → [`00acaca4`](#insn-00acaca4)
- ブロック [`00acaca4`](#insn-00acaca4) 範囲 `[['00acaca4', '00acacaf']]`
  - `UNCONDITIONAL_JUMP` [`00acacac`](#insn-00acacac) → [`00acac5c`](#insn-00acac5c)
- ブロック [`00acacb0`](#insn-00acacb0) 範囲 `[['00acacb0', '00acacb7']]`
  - `FALL_THROUGH` [`00acacb4`](#insn-00acacb4) → [`00acacb8`](#insn-00acacb8)
- ブロック [`00acacb8`](#insn-00acacb8) 範囲 `[['00acacb8', '00acacbb']]`

## 命令位置別の参照

- [`00acabcc`](#insn-00acabcc) → [`00acacb8`](#insn-00acacb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabd0`](#insn-00acabd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabd4`](#insn-00acabd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac54`](#insn-00acac54) → [`00acabe8`](#insn-00acabe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac58`](#insn-00acac58) → [`00acac60`](#insn-00acac60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac64`](#insn-00acac64) → [`00acacb0`](#insn-00acacb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac6c`](#insn-00acac6c) → [`00acac84`](#insn-00acac84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac74`](#insn-00acac74) → [`00acac94`](#insn-00acac94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac7c`](#insn-00acac7c) → [`00acaca4`](#insn-00acaca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac80`](#insn-00acac80) → [`00acac5c`](#insn-00acac5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac88`](#insn-00acac88) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acac90`](#insn-00acac90) → [`00acac78`](#insn-00acac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac98`](#insn-00acac98) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acaca0`](#insn-00acaca0) → [`00acac5c`](#insn-00acac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaca8`](#insn-00acaca8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acacac`](#insn-00acacac) → [`00acac5c`](#insn-00acac5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacb0`](#insn-00acacb0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacb4`](#insn-00acacb4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acabcc`](#insn-00acabcc)

~~~json
{
  "source": "00acabcc",
  "target": "00acacb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabd0`](#insn-00acabd0)

~~~json
{
  "source": "00acabd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabd4`](#insn-00acabd4)

~~~json
{
  "source": "00acabd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac54`](#insn-00acac54)

~~~json
{
  "source": "00acac54",
  "target": "00acabe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac58`](#insn-00acac58)

~~~json
{
  "source": "00acac58",
  "target": "00acac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac64`](#insn-00acac64)

~~~json
{
  "source": "00acac64",
  "target": "00acacb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac6c`](#insn-00acac6c)

~~~json
{
  "source": "00acac6c",
  "target": "00acac84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac74`](#insn-00acac74)

~~~json
{
  "source": "00acac74",
  "target": "00acac94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac7c`](#insn-00acac7c)

~~~json
{
  "source": "00acac7c",
  "target": "00acaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac80`](#insn-00acac80)

~~~json
{
  "source": "00acac80",
  "target": "00acac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac88`](#insn-00acac88)

~~~json
{
  "source": "00acac88",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac90`](#insn-00acac90)

~~~json
{
  "source": "00acac90",
  "target": "00acac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac98`](#insn-00acac98)

~~~json
{
  "source": "00acac98",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaca0`](#insn-00acaca0)

~~~json
{
  "source": "00acaca0",
  "target": "00acac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaca8`](#insn-00acaca8)

~~~json
{
  "source": "00acaca8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acacac`](#insn-00acacac)

~~~json
{
  "source": "00acacac",
  "target": "00acac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacb0`](#insn-00acacb0)

~~~json
{
  "source": "00acacb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacb4`](#insn-00acacb4)

~~~json
{
  "source": "00acacb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
