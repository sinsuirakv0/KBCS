# 007ceacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `007ceacc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007ceacc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0027.md#compare-8f83ac011d85995cb549680b46477c16)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ceacc",
  "name": "FUN_007ceacc",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "86c77a6940e05451867f9ac4c8b3d853c70371f069af5115c9399b4e0ef3f53f",
  "source_text_sha256": "86c77a6940e05451867f9ac4c8b3d853c70371f069af5115c9399b4e0ef3f53f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ceacc",
        "007cebc7"
      ]
    ],
    "bytes_sha256": "a42259478a2854307070b415039e32e1c04b3dee4b2ca3f06406ba36d011719f",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0073fa38](../0073f/0073fa38.md)
- [00749514](../00749/00749514.md)
- [0075bc70](../0075b/0075bc70.md)
- [007e9118](../007e9/007e9118.md)
- [007ef4ec](../007ef/007ef4ec.md)
- [0083f65c](../0083f/0083f65c.md)
- [0086b704](../0086b/0086b704.md)
- [00a52458](../00a52/00a52458.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [00bdaf40](../00bda/00bdaf40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1576 bytes

~~~c

undefined4 FUN_007ceacc(long param_1,int param_2)

{
  undefined8 *puVar1;
  long *plVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  
  puVar1 = *(undefined8 **)(param_1 + 0x20);
  puVar3 = puVar1;
  if (puVar1 == (undefined8 *)0x0) {
    return 0;
  }
  do {
    if (*(int *)((long)puVar3 + 0x1c) <= param_2) {
      if (param_2 <= *(int *)((long)puVar3 + 0x1c)) break;
      puVar3 = puVar3 + 1;
    }
    puVar3 = (undefined8 *)*puVar3;
    if (puVar3 == (undefined8 *)0x0) {
      return 0;
    }
  } while( true );
LAB_007ceb18:
  puVar3 = puVar1;
  if (*(int *)((long)puVar3 + 0x1c) <= param_2) {
    if (param_2 <= *(int *)((long)puVar3 + 0x1c)) goto LAB_007cebb0;
    puVar1 = (undefined8 *)puVar3[1];
    if ((undefined8 *)puVar3[1] == (undefined8 *)0x0) {
      puVar4 = puVar3 + 1;
      goto LAB_007ceb60;
    }
    goto LAB_007ceb18;
  }
  puVar1 = (undefined8 *)*puVar3;
  puVar4 = puVar3;
  if ((undefined8 *)*puVar3 == (undefined8 *)0x0) {
LAB_007ceb60:
    puVar1 = (undefined8 *)_Znwm(0x28);
    *puVar1 = 0;
    puVar1[1] = 0;
    puVar1[2] = puVar3;
    *puVar4 = puVar1;
    plVar2 = *(long **)(param_1 + 0x18);
    *(int *)((long)puVar1 + 0x1c) = param_2;
    *(undefined4 *)(puVar1 + 4) = 0;
    puVar3 = puVar1;
    if (*plVar2 != 0) {
      *(long *)(param_1 + 0x18) = *plVar2;
      puVar3 = (undefined8 *)*puVar4;
    }
    FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar3);
    *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
    puVar3 = puVar1;
LAB_007cebb0:
    return *(undefined4 *)(puVar3 + 4);
  }
  goto LAB_007ceb18;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007ceacc"></a> `007ceacc` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-007cead0"></a> `007cead0` | `e8 03 00 b4` | cbz x8,0x007ceb4c | `CONDITIONAL_JUMP`
<a id="insn-007cead4"></a> `007cead4` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-007cead8"></a> `007cead8` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ceadc"></a> `007ceadc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ceae0"></a> `007ceae0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007ceae4"></a> `007ceae4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007ceae8"></a> `007ceae8` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-007ceaec"></a> `007ceaec` | `03 00 00 14` | b 0x007ceaf8 | `UNCONDITIONAL_JUMP`
<a id="insn-007ceaf0"></a> `007ceaf0` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-007ceaf4"></a> `007ceaf4` | `89 02 00 b4` | cbz x9,0x007ceb44 | `CONDITIONAL_JUMP`
<a id="insn-007ceaf8"></a> `007ceaf8` | `2a 1d 40 b9` | ldr w10,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-007ceafc"></a> `007ceafc` | `5f 01 01 6b` | cmp w10,w1 | `FALL_THROUGH`
<a id="insn-007ceb00"></a> `007ceb00` | `8c ff ff 54` | b.gt 0x007ceaf0 | `CONDITIONAL_JUMP`
<a id="insn-007ceb04"></a> `007ceb04` | `aa 00 00 54` | b.ge 0x007ceb18 | `CONDITIONAL_JUMP`
<a id="insn-007ceb08"></a> `007ceb08` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-007ceb0c"></a> `007ceb0c` | `f9 ff ff 17` | b 0x007ceaf0 | `UNCONDITIONAL_JUMP`
<a id="insn-007ceb10"></a> `007ceb10` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-007ceb14"></a> `007ceb14` | `08 02 00 b4` | cbz x8,0x007ceb54 | `CONDITIONAL_JUMP`
<a id="insn-007ceb18"></a> `007ceb18` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-007ceb1c"></a> `007ceb1c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-007ceb20"></a> `007ceb20` | `1f 01 01 6b` | cmp w8,w1 | `FALL_THROUGH`
<a id="insn-007ceb24"></a> `007ceb24` | `6c ff ff 54` | b.gt 0x007ceb10 | `CONDITIONAL_JUMP`
<a id="insn-007ceb28"></a> `007ceb28` | `2a 04 00 54` | b.ge 0x007cebac | `CONDITIONAL_JUMP`
<a id="insn-007ceb2c"></a> `007ceb2c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-007ceb30"></a> `007ceb30` | `48 ff ff b5` | cbnz x8,0x007ceb18 | `CONDITIONAL_JUMP`
<a id="insn-007ceb34"></a> `007ceb34` | `f6 03 01 2a` | mov w22,w1 | `FALL_THROUGH`
<a id="insn-007ceb38"></a> `007ceb38` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-007ceb3c"></a> `007ceb3c` | `95 22 00 91` | add x21,x20,#0x8 | `FALL_THROUGH`
<a id="insn-007ceb40"></a> `007ceb40` | `08 00 00 14` | b 0x007ceb60 | `UNCONDITIONAL_JUMP`
<a id="insn-007ceb44"></a> `007ceb44` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-007ceb48"></a> `007ceb48` | `1b 00 00 14` | b 0x007cebb4 | `UNCONDITIONAL_JUMP`
<a id="insn-007ceb4c"></a> `007ceb4c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-007ceb50"></a> `007ceb50` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007ceb54"></a> `007ceb54` | `f6 03 01 2a` | mov w22,w1 | `FALL_THROUGH`
<a id="insn-007ceb58"></a> `007ceb58` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-007ceb5c"></a> `007ceb5c` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-007ceb60"></a> `007ceb60` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-007ceb64"></a> `007ceb64` | `f7 30 10 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-007ceb68"></a> `007ceb68` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-007ceb6c"></a> `007ceb6c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007ceb70"></a> `007ceb70` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-007ceb74"></a> `007ceb74` | `14 08 00 f9` | str x20,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007ceb78"></a> `007ceb78` | `a0 02 00 f9` | str x0,[x21] | `FALL_THROUGH`
<a id="insn-007ceb7c"></a> `007ceb7c` | `e8 0e 40 f9` | ldr x8,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-007ceb80"></a> `007ceb80` | `16 fc 03 29` | stp w22,wzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-007ceb84"></a> `007ceb84` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-007ceb88"></a> `007ceb88` | `68 00 00 b4` | cbz x8,0x007ceb94 | `CONDITIONAL_JUMP`
<a id="insn-007ceb8c"></a> `007ceb8c` | `e8 0e 00 f9` | str x8,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-007ceb90"></a> `007ceb90` | `a1 02 40 f9` | ldr x1,[x21] | `FALL_THROUGH`
<a id="insn-007ceb94"></a> `007ceb94` | `e0 12 40 f9` | ldr x0,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-007ceb98"></a> `007ceb98` | `33 29 f1 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-007ceb9c"></a> `007ceb9c` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-007ceba0"></a> `007ceba0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-007ceba4"></a> `007ceba4` | `e8 16 00 f9` | str x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-007ceba8"></a> `007ceba8` | `02 00 00 14` | b 0x007cebb0 | `UNCONDITIONAL_JUMP`
<a id="insn-007cebac"></a> `007cebac` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-007cebb0"></a> `007cebb0` | `60 22 40 b9` | ldr w0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-007cebb4"></a> `007cebb4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007cebb8"></a> `007cebb8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007cebbc"></a> `007cebbc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007cebc0"></a> `007cebc0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-007cebc4"></a> `007cebc4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007ceacc`](#insn-007ceacc) 範囲 `[['007ceacc', '007cead3']]`
  - `CONDITIONAL_JUMP` [`007cead0`](#insn-007cead0) → [`007ceb4c`](#insn-007ceb4c)
  - `FALL_THROUGH` [`007cead0`](#insn-007cead0) → [`007cead4`](#insn-007cead4)
- ブロック [`007cead4`](#insn-007cead4) 範囲 `[['007cead4', '007ceaef']]`
  - `UNCONDITIONAL_JUMP` [`007ceaec`](#insn-007ceaec) → [`007ceaf8`](#insn-007ceaf8)
- ブロック [`007ceaf0`](#insn-007ceaf0) 範囲 `[['007ceaf0', '007ceaf7']]`
  - `CONDITIONAL_JUMP` [`007ceaf4`](#insn-007ceaf4) → [`007ceb44`](#insn-007ceb44)
  - `FALL_THROUGH` [`007ceaf4`](#insn-007ceaf4) → [`007ceaf8`](#insn-007ceaf8)
- ブロック [`007ceaf8`](#insn-007ceaf8) 範囲 `[['007ceaf8', '007ceb03']]`
  - `CONDITIONAL_JUMP` [`007ceb00`](#insn-007ceb00) → [`007ceaf0`](#insn-007ceaf0)
  - `FALL_THROUGH` [`007ceb00`](#insn-007ceb00) → [`007ceb04`](#insn-007ceb04)
- ブロック [`007ceb04`](#insn-007ceb04) 範囲 `[['007ceb04', '007ceb07']]`
  - `CONDITIONAL_JUMP` [`007ceb04`](#insn-007ceb04) → [`007ceb18`](#insn-007ceb18)
  - `FALL_THROUGH` [`007ceb04`](#insn-007ceb04) → [`007ceb08`](#insn-007ceb08)
- ブロック [`007ceb08`](#insn-007ceb08) 範囲 `[['007ceb08', '007ceb0f']]`
  - `UNCONDITIONAL_JUMP` [`007ceb0c`](#insn-007ceb0c) → [`007ceaf0`](#insn-007ceaf0)
- ブロック [`007ceb10`](#insn-007ceb10) 範囲 `[['007ceb10', '007ceb17']]`
  - `CONDITIONAL_JUMP` [`007ceb14`](#insn-007ceb14) → [`007ceb54`](#insn-007ceb54)
  - `FALL_THROUGH` [`007ceb14`](#insn-007ceb14) → [`007ceb18`](#insn-007ceb18)
- ブロック [`007ceb18`](#insn-007ceb18) 範囲 `[['007ceb18', '007ceb27']]`
  - `CONDITIONAL_JUMP` [`007ceb24`](#insn-007ceb24) → [`007ceb10`](#insn-007ceb10)
  - `FALL_THROUGH` [`007ceb24`](#insn-007ceb24) → [`007ceb28`](#insn-007ceb28)
- ブロック [`007ceb28`](#insn-007ceb28) 範囲 `[['007ceb28', '007ceb2b']]`
  - `CONDITIONAL_JUMP` [`007ceb28`](#insn-007ceb28) → [`007cebac`](#insn-007cebac)
  - `FALL_THROUGH` [`007ceb28`](#insn-007ceb28) → [`007ceb2c`](#insn-007ceb2c)
- ブロック [`007ceb2c`](#insn-007ceb2c) 範囲 `[['007ceb2c', '007ceb33']]`
  - `CONDITIONAL_JUMP` [`007ceb30`](#insn-007ceb30) → [`007ceb18`](#insn-007ceb18)
  - `FALL_THROUGH` [`007ceb30`](#insn-007ceb30) → [`007ceb34`](#insn-007ceb34)
- ブロック [`007ceb34`](#insn-007ceb34) 範囲 `[['007ceb34', '007ceb43']]`
  - `UNCONDITIONAL_JUMP` [`007ceb40`](#insn-007ceb40) → [`007ceb60`](#insn-007ceb60)
- ブロック [`007ceb44`](#insn-007ceb44) 範囲 `[['007ceb44', '007ceb4b']]`
  - `UNCONDITIONAL_JUMP` [`007ceb48`](#insn-007ceb48) → [`007cebb4`](#insn-007cebb4)
- ブロック [`007ceb4c`](#insn-007ceb4c) 範囲 `[['007ceb4c', '007ceb53']]`
- ブロック [`007ceb54`](#insn-007ceb54) 範囲 `[['007ceb54', '007ceb5f']]`
  - `FALL_THROUGH` [`007ceb5c`](#insn-007ceb5c) → [`007ceb60`](#insn-007ceb60)
- ブロック [`007ceb60`](#insn-007ceb60) 範囲 `[['007ceb60', '007ceb8b']]`
  - `CONDITIONAL_JUMP` [`007ceb88`](#insn-007ceb88) → [`007ceb94`](#insn-007ceb94)
  - `FALL_THROUGH` [`007ceb88`](#insn-007ceb88) → [`007ceb8c`](#insn-007ceb8c)
- ブロック [`007ceb8c`](#insn-007ceb8c) 範囲 `[['007ceb8c', '007ceb93']]`
  - `FALL_THROUGH` [`007ceb90`](#insn-007ceb90) → [`007ceb94`](#insn-007ceb94)
- ブロック [`007ceb94`](#insn-007ceb94) 範囲 `[['007ceb94', '007cebab']]`
  - `UNCONDITIONAL_JUMP` [`007ceba8`](#insn-007ceba8) → [`007cebb0`](#insn-007cebb0)
- ブロック [`007cebac`](#insn-007cebac) 範囲 `[['007cebac', '007cebaf']]`
  - `FALL_THROUGH` [`007cebac`](#insn-007cebac) → [`007cebb0`](#insn-007cebb0)
- ブロック [`007cebb0`](#insn-007cebb0) 範囲 `[['007cebb0', '007cebb3']]`
  - `FALL_THROUGH` [`007cebb0`](#insn-007cebb0) → [`007cebb4`](#insn-007cebb4)
- ブロック [`007cebb4`](#insn-007cebb4) 範囲 `[['007cebb4', '007cebc7']]`

## 命令位置別の参照

- [`007cead0`](#insn-007cead0) → [`007ceb4c`](#insn-007ceb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cead4`](#insn-007cead4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cead8`](#insn-007cead8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceadc`](#insn-007ceadc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceae0`](#insn-007ceae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceaec`](#insn-007ceaec) → [`007ceaf8`](#insn-007ceaf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceaf4`](#insn-007ceaf4) → [`007ceb44`](#insn-007ceb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb00`](#insn-007ceb00) → [`007ceaf0`](#insn-007ceaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb04`](#insn-007ceb04) → [`007ceb18`](#insn-007ceb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb0c`](#insn-007ceb0c) → [`007ceaf0`](#insn-007ceaf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb14`](#insn-007ceb14) → [`007ceb54`](#insn-007ceb54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb24`](#insn-007ceb24) → [`007ceb10`](#insn-007ceb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb28`](#insn-007ceb28) → [`007cebac`](#insn-007cebac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb30`](#insn-007ceb30) → [`007ceb18`](#insn-007ceb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb40`](#insn-007ceb40) → [`007ceb60`](#insn-007ceb60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb48`](#insn-007ceb48) → [`007cebb4`](#insn-007cebb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb64`](#insn-007ceb64) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`007ceb88`](#insn-007ceb88) → [`007ceb94`](#insn-007ceb94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ceb98`](#insn-007ceb98) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`007ceba8`](#insn-007ceba8) → [`007cebb0`](#insn-007cebb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cebb4`](#insn-007cebb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cebb8`](#insn-007cebb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cebbc`](#insn-007cebbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cebc0`](#insn-007cebc0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007cead0`](#insn-007cead0)

~~~json
{
  "source": "007cead0",
  "target": "007ceb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cead4`](#insn-007cead4)

~~~json
{
  "source": "007cead4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cead8`](#insn-007cead8)

~~~json
{
  "source": "007cead8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceadc`](#insn-007ceadc)

~~~json
{
  "source": "007ceadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceae0`](#insn-007ceae0)

~~~json
{
  "source": "007ceae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceaec`](#insn-007ceaec)

~~~json
{
  "source": "007ceaec",
  "target": "007ceaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceaf4`](#insn-007ceaf4)

~~~json
{
  "source": "007ceaf4",
  "target": "007ceb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb00`](#insn-007ceb00)

~~~json
{
  "source": "007ceb00",
  "target": "007ceaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb04`](#insn-007ceb04)

~~~json
{
  "source": "007ceb04",
  "target": "007ceb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb0c`](#insn-007ceb0c)

~~~json
{
  "source": "007ceb0c",
  "target": "007ceaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb14`](#insn-007ceb14)

~~~json
{
  "source": "007ceb14",
  "target": "007ceb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb24`](#insn-007ceb24)

~~~json
{
  "source": "007ceb24",
  "target": "007ceb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb28`](#insn-007ceb28)

~~~json
{
  "source": "007ceb28",
  "target": "007cebac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb30`](#insn-007ceb30)

~~~json
{
  "source": "007ceb30",
  "target": "007ceb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb40`](#insn-007ceb40)

~~~json
{
  "source": "007ceb40",
  "target": "007ceb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb48`](#insn-007ceb48)

~~~json
{
  "source": "007ceb48",
  "target": "007cebb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb64`](#insn-007ceb64)

~~~json
{
  "source": "007ceb64",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ceb88`](#insn-007ceb88)

~~~json
{
  "source": "007ceb88",
  "target": "007ceb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ceb98`](#insn-007ceb98)

~~~json
{
  "source": "007ceb98",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ceba8`](#insn-007ceba8)

~~~json
{
  "source": "007ceba8",
  "target": "007cebb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cebb4`](#insn-007cebb4)

~~~json
{
  "source": "007cebb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cebb8`](#insn-007cebb8)

~~~json
{
  "source": "007cebb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cebbc`](#insn-007cebbc)

~~~json
{
  "source": "007cebbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cebc0`](#insn-007cebc0)

~~~json
{
  "source": "007cebc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
