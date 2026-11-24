# 00acac0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acabc8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-b9f3d5a7fd7c7691b5bd272247144c45)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2a69c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a69c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0054.md#compare-e76d0d34e064285f3ef14fe94651577d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acac0c",
  "name": "FUN_00acac0c",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f66f8c502ba04a4bfa4a7ff743ebc796731b8525eac42ce4fc20f591744f9a8c",
  "source_text_sha256": "f66f8c502ba04a4bfa4a7ff743ebc796731b8525eac42ce4fc20f591744f9a8c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acac0c",
        "00acacff"
      ]
    ],
    "bytes_sha256": "57c188600db5213c3912b7d18ce7bd80a35925073852ec012a85ca57b975ce62",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aca984](../00aca/00aca984.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1926 bytes

~~~c

void FUN_00acac0c(undefined8 param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4)

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
                    /* try { // try from 00acacb0 to 00bcacbb has its CatchHandler @ 00acd710 */
      if ((*(byte *)(param_2 + 9) & 1) == 0) {
        if ((*(byte *)(param_2 + 6) & 1) == 0) goto LAB_00acacbc;
LAB_00acacd8:
        _ZdlPv((void *)param_2[8]);
        __ptr = (void *)param_2[3];
      }
      else {
        _ZdlPv((void *)param_2[0xb]);
        if ((*(byte *)(param_2 + 6) & 1) != 0) goto LAB_00acacd8;
LAB_00acacbc:
                    /* try { // try from 00acacbc to 00bcc0ab has its CatchHandler @ 00ac9134 */
        __ptr = (void *)param_2[3];
      }
      if (__ptr != (void *)0x0) {
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
<a id="insn-00acac0c"></a> `00acac0c` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00acac10"></a> `00acac10` | `60 07 00 54` | b.eq 0x00acacfc | `CONDITIONAL_JUMP`
<a id="insn-00acac14"></a> `00acac14` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acac18"></a> `00acac18` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acac1c"></a> `00acac1c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acac20"></a> `00acac20` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00acac24"></a> `00acac24` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00acac28"></a> `00acac28` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acac2c"></a> `00acac2c` | `09 41 40 39` | ldrb w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acac30"></a> `00acac30` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00acac34"></a> `00acac34` | `7f 7c 02 a9` | stp xzr,xzr,[x3, #0x20] | `FALL_THROUGH`
<a id="insn-00acac38"></a> `00acac38` | `7f 0c 00 f9` | str xzr,[x3, #0x18] | `FALL_THROUGH`
<a id="insn-00acac3c"></a> `00acac3c` | `69 40 00 39` | strb w9,[x3, #0x10] | `FALL_THROUGH`
<a id="insn-00acac40"></a> `00acac40` | `60 00 80 3d` | str q0,[x3] | `FALL_THROUGH`
<a id="insn-00acac44"></a> `00acac44` | `00 81 c1 3c` | ldur q0,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acac48"></a> `00acac48` | `60 80 81 3c` | stur q0,[x3, #0x18] | `FALL_THROUGH`
<a id="insn-00acac4c"></a> `00acac4c` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00acac50"></a> `00acac50` | `69 14 00 f9` | str x9,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00acac54"></a> `00acac54` | `09 21 40 f9` | ldr x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00acac58"></a> `00acac58` | `00 0d c0 3d` | ldr q0,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00acac5c"></a> `00acac5c` | `1f fd 01 a9` | stp xzr,xzr,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acac60"></a> `00acac60` | `1f 15 00 f9` | str xzr,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00acac64"></a> `00acac64` | `69 20 00 f9` | str x9,[x3, #0x40] | `FALL_THROUGH`
<a id="insn-00acac68"></a> `00acac68` | `60 0c 80 3d` | str q0,[x3, #0x30] | `FALL_THROUGH`
<a id="insn-00acac6c"></a> `00acac6c` | `09 2d 40 f9` | ldr x9,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00acac70"></a> `00acac70` | `00 81 c4 3c` | ldur q0,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00acac74"></a> `00acac74` | `1f fd 03 a9` | stp xzr,xzr,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00acac78"></a> `00acac78` | `1f 19 00 f9` | str xzr,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00acac7c"></a> `00acac7c` | `69 2c 00 f9` | str x9,[x3, #0x58] | `FALL_THROUGH`
<a id="insn-00acac80"></a> `00acac80` | `60 80 84 3c` | stur q0,[x3, #0x48] | `FALL_THROUGH`
<a id="insn-00acac84"></a> `00acac84` | `63 80 01 91` | add x3,x3,#0x60 | `FALL_THROUGH`
<a id="insn-00acac88"></a> `00acac88` | `1f 7d 05 a9` | stp xzr,xzr,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00acac8c"></a> `00acac8c` | `1f 25 00 f9` | str xzr,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00acac90"></a> `00acac90` | `08 81 01 91` | add x8,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00acac94"></a> `00acac94` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00acac98"></a> `00acac98` | `a1 fc ff 54` | b.ne 0x00acac2c | `CONDITIONAL_JUMP`
<a id="insn-00acac9c"></a> `00acac9c` | `02 00 00 14` | b 0x00acaca4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acaca0"></a> `00acaca0` | `94 82 01 91` | add x20,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00acaca4"></a> `00acaca4` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00acaca8"></a> `00acaca8` | `60 02 00 54` | b.eq 0x00acacf4 | `CONDITIONAL_JUMP`
<a id="insn-00acacac"></a> `00acacac` | `88 22 41 39` | ldrb w8,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00acacb0"></a> `00acacb0` | `c8 00 00 37` | tbnz w8,#0x0,0x00acacc8 | `CONDITIONAL_JUMP`
<a id="insn-00acacb4"></a> `00acacb4` | `88 c2 40 39` | ldrb w8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00acacb8"></a> `00acacb8` | `08 01 00 37` | tbnz w8,#0x0,0x00acacd8 | `CONDITIONAL_JUMP`
<a id="insn-00acacbc"></a> `00acacbc` | `80 0e 40 f9` | ldr x0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00acacc0"></a> `00acacc0` | `40 01 00 b5` | cbnz x0,0x00acace8 | `CONDITIONAL_JUMP`
<a id="insn-00acacc4"></a> `00acacc4` | `f7 ff ff 17` | b 0x00acaca0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acacc8"></a> `00acacc8` | `80 2e 40 f9` | ldr x0,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00acaccc"></a> `00acaccc` | `e5 40 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acacd0"></a> `00acacd0` | `88 c2 40 39` | ldrb w8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00acacd4"></a> `00acacd4` | `48 ff 07 36` | tbz w8,#0x0,0x00acacbc | `CONDITIONAL_JUMP`
<a id="insn-00acacd8"></a> `00acacd8` | `80 22 40 f9` | ldr x0,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00acacdc"></a> `00acacdc` | `e1 40 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acace0"></a> `00acace0` | `80 0e 40 f9` | ldr x0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00acace4"></a> `00acace4` | `e0 fd ff b4` | cbz x0,0x00acaca0 | `CONDITIONAL_JUMP`
<a id="insn-00acace8"></a> `00acace8` | `80 12 00 f9` | str x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acacec"></a> `00acacec` | `dd 40 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acacf0"></a> `00acacf0` | `ec ff ff 17` | b 0x00acaca0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acacf4"></a> `00acacf4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acacf8"></a> `00acacf8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acacfc"></a> `00acacfc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acac0c`](#insn-00acac0c) 範囲 `[['00acac0c', '00acac13']]`
  - `CONDITIONAL_JUMP` [`00acac10`](#insn-00acac10) → [`00acacfc`](#insn-00acacfc)
  - `FALL_THROUGH` [`00acac10`](#insn-00acac10) → [`00acac14`](#insn-00acac14)
- ブロック [`00acac14`](#insn-00acac14) 範囲 `[['00acac14', '00acac2b']]`
  - `FALL_THROUGH` [`00acac28`](#insn-00acac28) → [`00acac2c`](#insn-00acac2c)
- ブロック [`00acac2c`](#insn-00acac2c) 範囲 `[['00acac2c', '00acac9b']]`
  - `CONDITIONAL_JUMP` [`00acac98`](#insn-00acac98) → [`00acac2c`](#insn-00acac2c)
  - `FALL_THROUGH` [`00acac98`](#insn-00acac98) → [`00acac9c`](#insn-00acac9c)
- ブロック [`00acac9c`](#insn-00acac9c) 範囲 `[['00acac9c', '00acac9f']]`
  - `UNCONDITIONAL_JUMP` [`00acac9c`](#insn-00acac9c) → [`00acaca4`](#insn-00acaca4)
- ブロック [`00acaca0`](#insn-00acaca0) 範囲 `[['00acaca0', '00acaca3']]`
  - `FALL_THROUGH` [`00acaca0`](#insn-00acaca0) → [`00acaca4`](#insn-00acaca4)
- ブロック [`00acaca4`](#insn-00acaca4) 範囲 `[['00acaca4', '00acacab']]`
  - `CONDITIONAL_JUMP` [`00acaca8`](#insn-00acaca8) → [`00acacf4`](#insn-00acacf4)
  - `FALL_THROUGH` [`00acaca8`](#insn-00acaca8) → [`00acacac`](#insn-00acacac)
- ブロック [`00acacac`](#insn-00acacac) 範囲 `[['00acacac', '00acacaf']]`
  - `FALL_THROUGH` [`00acacac`](#insn-00acacac) → [`00acacb0`](#insn-00acacb0)
- ブロック [`00acacb0`](#insn-00acacb0) 範囲 `[['00acacb0', '00acacb3']]`
  - `CONDITIONAL_JUMP` [`00acacb0`](#insn-00acacb0) → [`00acacc8`](#insn-00acacc8)
  - `FALL_THROUGH` [`00acacb0`](#insn-00acacb0) → [`00acacb4`](#insn-00acacb4)
- ブロック [`00acacb4`](#insn-00acacb4) 範囲 `[['00acacb4', '00acacbb']]`
  - `CONDITIONAL_JUMP` [`00acacb8`](#insn-00acacb8) → [`00acacd8`](#insn-00acacd8)
  - `FALL_THROUGH` [`00acacb8`](#insn-00acacb8) → [`00acacbc`](#insn-00acacbc)
- ブロック [`00acacbc`](#insn-00acacbc) 範囲 `[['00acacbc', '00acacc3']]`
  - `CONDITIONAL_JUMP` [`00acacc0`](#insn-00acacc0) → [`00acace8`](#insn-00acace8)
  - `FALL_THROUGH` [`00acacc0`](#insn-00acacc0) → [`00acacc4`](#insn-00acacc4)
- ブロック [`00acacc4`](#insn-00acacc4) 範囲 `[['00acacc4', '00acacc7']]`
  - `UNCONDITIONAL_JUMP` [`00acacc4`](#insn-00acacc4) → [`00acaca0`](#insn-00acaca0)
- ブロック [`00acacc8`](#insn-00acacc8) 範囲 `[['00acacc8', '00acacd7']]`
  - `CONDITIONAL_JUMP` [`00acacd4`](#insn-00acacd4) → [`00acacbc`](#insn-00acacbc)
  - `FALL_THROUGH` [`00acacd4`](#insn-00acacd4) → [`00acacd8`](#insn-00acacd8)
- ブロック [`00acacd8`](#insn-00acacd8) 範囲 `[['00acacd8', '00acace7']]`
  - `CONDITIONAL_JUMP` [`00acace4`](#insn-00acace4) → [`00acaca0`](#insn-00acaca0)
  - `FALL_THROUGH` [`00acace4`](#insn-00acace4) → [`00acace8`](#insn-00acace8)
- ブロック [`00acace8`](#insn-00acace8) 範囲 `[['00acace8', '00acacf3']]`
  - `UNCONDITIONAL_JUMP` [`00acacf0`](#insn-00acacf0) → [`00acaca0`](#insn-00acaca0)
- ブロック [`00acacf4`](#insn-00acacf4) 範囲 `[['00acacf4', '00acacfb']]`
  - `FALL_THROUGH` [`00acacf8`](#insn-00acacf8) → [`00acacfc`](#insn-00acacfc)
- ブロック [`00acacfc`](#insn-00acacfc) 範囲 `[['00acacfc', '00acacff']]`

## 命令位置別の参照

- [`00acac10`](#insn-00acac10) → [`00acacfc`](#insn-00acacfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac14`](#insn-00acac14) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac18`](#insn-00acac18) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac98`](#insn-00acac98) → [`00acac2c`](#insn-00acac2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac9c`](#insn-00acac9c) → [`00acaca4`](#insn-00acaca4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaca8`](#insn-00acaca8) → [`00acacf4`](#insn-00acacf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacb0`](#insn-00acacb0) → [`00acacc8`](#insn-00acacc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacb8`](#insn-00acacb8) → [`00acacd8`](#insn-00acacd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacc0`](#insn-00acacc0) → [`00acace8`](#insn-00acace8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacc4`](#insn-00acacc4) → [`00acaca0`](#insn-00acaca0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaccc`](#insn-00acaccc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acacd4`](#insn-00acacd4) → [`00acacbc`](#insn-00acacbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacdc`](#insn-00acacdc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acace4`](#insn-00acace4) → [`00acaca0`](#insn-00acaca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacec`](#insn-00acacec) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acacf0`](#insn-00acacf0) → [`00acaca0`](#insn-00acaca0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacf4`](#insn-00acacf4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacf8`](#insn-00acacf8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acac10`](#insn-00acac10)

~~~json
{
  "source": "00acac10",
  "target": "00acacfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac14`](#insn-00acac14)

~~~json
{
  "source": "00acac14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac18`](#insn-00acac18)

~~~json
{
  "source": "00acac18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac98`](#insn-00acac98)

~~~json
{
  "source": "00acac98",
  "target": "00acac2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac9c`](#insn-00acac9c)

~~~json
{
  "source": "00acac9c",
  "target": "00acaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaca8`](#insn-00acaca8)

~~~json
{
  "source": "00acaca8",
  "target": "00acacf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacb0`](#insn-00acacb0)

~~~json
{
  "source": "00acacb0",
  "target": "00acacc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacb8`](#insn-00acacb8)

~~~json
{
  "source": "00acacb8",
  "target": "00acacd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacc0`](#insn-00acacc0)

~~~json
{
  "source": "00acacc0",
  "target": "00acace8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacc4`](#insn-00acacc4)

~~~json
{
  "source": "00acacc4",
  "target": "00acaca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaccc`](#insn-00acaccc)

~~~json
{
  "source": "00acaccc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acacd4`](#insn-00acacd4)

~~~json
{
  "source": "00acacd4",
  "target": "00acacbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacdc`](#insn-00acacdc)

~~~json
{
  "source": "00acacdc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acace4`](#insn-00acace4)

~~~json
{
  "source": "00acace4",
  "target": "00acaca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacec`](#insn-00acacec)

~~~json
{
  "source": "00acacec",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acacf0`](#insn-00acacf0)

~~~json
{
  "source": "00acacf0",
  "target": "00acaca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacf4`](#insn-00acacf4)

~~~json
{
  "source": "00acacf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacf8`](#insn-00acacf8)

~~~json
{
  "source": "00acacf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
