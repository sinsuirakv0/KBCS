# 00aadba4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aadadc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aadadc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-887fcd8fc55585724330c43ed19c6195)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aadbe8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadbe8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-7d6ed14220a2a849a00331b42dd36d70)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadba4",
  "name": "FUN_00aadba4",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04c9925987a712cc17d08fb1a44789bcd8a741cb1a1d23efdd1474a9e73cbea5",
  "source_text_sha256": "04c9925987a712cc17d08fb1a44789bcd8a741cb1a1d23efdd1474a9e73cbea5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadba4",
        "00aadc77"
      ]
    ],
    "bytes_sha256": "0ac2bfc9dc4e04796b6443221e0b7bfed522196999a7ef84a2d00799e6644f50",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aac358](../00aac/00aac358.md)

## 呼び出し先

- [00471738](../00471/00471738.md)
- [00bdb010](../00bdb/00bdb010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1251 bytes

~~~c

undefined8 * FUN_00aadba4(undefined8 *param_1,undefined8 *param_2)

{
  bool bVar1;
  void *__ptr;
  undefined8 *puVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  
  puVar5 = param_2;
  puVar2 = (undefined8 *)param_2[1];
  if ((undefined8 *)param_2[1] == (undefined8 *)0x0) {
    do {
      puVar4 = (undefined8 *)puVar5[2];
      bVar1 = (undefined8 *)*puVar4 != puVar5;
      puVar5 = puVar4;
    } while (bVar1);
  }
  else {
    do {
      puVar4 = puVar2;
      puVar2 = (undefined8 *)*puVar4;
    } while ((undefined8 *)*puVar4 != (undefined8 *)0x0);
  }
  if ((void *)*param_1 == param_2) {
    *param_1 = puVar4;
  }
  param_1[2] = param_1[2] + -1;
  FUN_00471738(param_1[1],param_2);
  puVar5 = (undefined8 *)param_2[5];
  if (puVar5 != (undefined8 *)0x0) {
    puVar3 = (undefined8 *)param_2[6];
    puVar2 = puVar5;
    if (puVar3 != puVar5) {
      do {
        puVar2 = puVar3 + -3;
        __ptr = (void *)*puVar2;
        if (__ptr != (void *)0x0) {
          puVar3[-2] = __ptr;
          _ZdlPv(__ptr);
        }
        puVar3 = puVar2;
      } while (puVar2 != puVar5);
      puVar2 = (undefined8 *)param_2[5];
    }
    param_2[6] = puVar5;
    _ZdlPv(puVar2);
  }
  _ZdlPv(param_2);
  return puVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aadba4"></a> `00aadba4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aadba8"></a> `00aadba8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadbac"></a> `00aadbac` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadbb0"></a> `00aadbb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aadbb4"></a> `00aadbb4` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00aadbb8"></a> `00aadbb8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00aadbbc"></a> `00aadbbc` | `a8 00 00 b4` | cbz x8,0x00aadbd0 | `CONDITIONAL_JUMP`
<a id="insn-00aadbc0"></a> `00aadbc0` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aadbc4"></a> `00aadbc4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aadbc8"></a> `00aadbc8` | `c8 ff ff b5` | cbnz x8,0x00aadbc0 | `CONDITIONAL_JUMP`
<a id="insn-00aadbcc"></a> `00aadbcc` | `07 00 00 14` | b 0x00aadbe8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadbd0"></a> `00aadbd0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00aadbd4"></a> `00aadbd4` | `14 09 40 f9` | ldr x20,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aadbd8"></a> `00aadbd8` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00aadbdc"></a> `00aadbdc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00aadbe0"></a> `00aadbe0` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00aadbe4"></a> `00aadbe4` | `81 ff ff 54` | b.ne 0x00aadbd4 | `CONDITIONAL_JUMP`
<a id="insn-00aadbe8"></a> `00aadbe8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aadbec"></a> `00aadbec` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00aadbf0"></a> `00aadbf0` | `41 00 00 54` | b.ne 0x00aadbf8 | `CONDITIONAL_JUMP`
<a id="insn-00aadbf4"></a> `00aadbf4` | `14 00 00 f9` | str x20,[x0] | `FALL_THROUGH`
<a id="insn-00aadbf8"></a> `00aadbf8` | `08 a4 40 a9` | ldp x8,x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aadbfc"></a> `00aadbfc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aadc00"></a> `00aadc00` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00aadc04"></a> `00aadc04` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aadc08"></a> `00aadc08` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aadc0c"></a> `00aadc0c` | `cb 0e e7 97` | bl 0x00471738 | `UNCONDITIONAL_CALL`
<a id="insn-00aadc10"></a> `00aadc10` | `75 16 40 f9` | ldr x21,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aadc14"></a> `00aadc14` | `55 02 00 b4` | cbz x21,0x00aadc5c | `CONDITIONAL_JUMP`
<a id="insn-00aadc18"></a> `00aadc18` | `68 1a 40 f9` | ldr x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aadc1c"></a> `00aadc1c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aadc20"></a> `00aadc20` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00aadc24"></a> `00aadc24` | `80 01 00 54` | b.eq 0x00aadc54 | `CONDITIONAL_JUMP`
<a id="insn-00aadc28"></a> `00aadc28` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00aadc2c"></a> `00aadc2c` | `04 00 00 14` | b 0x00aadc3c | `UNCONDITIONAL_JUMP`
<a id="insn-00aadc30"></a> `00aadc30` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00aadc34"></a> `00aadc34` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00aadc38"></a> `00aadc38` | `c0 00 00 54` | b.eq 0x00aadc50 | `CONDITIONAL_JUMP`
<a id="insn-00aadc3c"></a> `00aadc3c` | `c0 8e 5e f8` | ldr x0,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00aadc40"></a> `00aadc40` | `80 ff ff b4` | cbz x0,0x00aadc30 | `CONDITIONAL_JUMP`
<a id="insn-00aadc44"></a> `00aadc44` | `00 01 1f f8` | stur x0,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-00aadc48"></a> `00aadc48` | `f2 b4 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aadc4c"></a> `00aadc4c` | `f9 ff ff 17` | b 0x00aadc30 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadc50"></a> `00aadc50` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aadc54"></a> `00aadc54` | `75 1a 00 f9` | str x21,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aadc58"></a> `00aadc58` | `ee b4 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aadc5c"></a> `00aadc5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadc60"></a> `00aadc60` | `ec b4 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aadc64"></a> `00aadc64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aadc68"></a> `00aadc68` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadc6c"></a> `00aadc6c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadc70"></a> `00aadc70` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aadc74"></a> `00aadc74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadba4`](#insn-00aadba4) 範囲 `[['00aadba4', '00aadbbf']]`
  - `CONDITIONAL_JUMP` [`00aadbbc`](#insn-00aadbbc) → [`00aadbd0`](#insn-00aadbd0)
  - `FALL_THROUGH` [`00aadbbc`](#insn-00aadbbc) → [`00aadbc0`](#insn-00aadbc0)
- ブロック [`00aadbc0`](#insn-00aadbc0) 範囲 `[['00aadbc0', '00aadbcb']]`
  - `CONDITIONAL_JUMP` [`00aadbc8`](#insn-00aadbc8) → [`00aadbc0`](#insn-00aadbc0)
  - `FALL_THROUGH` [`00aadbc8`](#insn-00aadbc8) → [`00aadbcc`](#insn-00aadbcc)
- ブロック [`00aadbcc`](#insn-00aadbcc) 範囲 `[['00aadbcc', '00aadbcf']]`
  - `UNCONDITIONAL_JUMP` [`00aadbcc`](#insn-00aadbcc) → [`00aadbe8`](#insn-00aadbe8)
- ブロック [`00aadbd0`](#insn-00aadbd0) 範囲 `[['00aadbd0', '00aadbd3']]`
  - `FALL_THROUGH` [`00aadbd0`](#insn-00aadbd0) → [`00aadbd4`](#insn-00aadbd4)
- ブロック [`00aadbd4`](#insn-00aadbd4) 範囲 `[['00aadbd4', '00aadbe7']]`
  - `CONDITIONAL_JUMP` [`00aadbe4`](#insn-00aadbe4) → [`00aadbd4`](#insn-00aadbd4)
  - `FALL_THROUGH` [`00aadbe4`](#insn-00aadbe4) → [`00aadbe8`](#insn-00aadbe8)
- ブロック [`00aadbe8`](#insn-00aadbe8) 範囲 `[['00aadbe8', '00aadbf3']]`
  - `CONDITIONAL_JUMP` [`00aadbf0`](#insn-00aadbf0) → [`00aadbf8`](#insn-00aadbf8)
  - `FALL_THROUGH` [`00aadbf0`](#insn-00aadbf0) → [`00aadbf4`](#insn-00aadbf4)
- ブロック [`00aadbf4`](#insn-00aadbf4) 範囲 `[['00aadbf4', '00aadbf7']]`
  - `FALL_THROUGH` [`00aadbf4`](#insn-00aadbf4) → [`00aadbf8`](#insn-00aadbf8)
- ブロック [`00aadbf8`](#insn-00aadbf8) 範囲 `[['00aadbf8', '00aadc17']]`
  - `CONDITIONAL_JUMP` [`00aadc14`](#insn-00aadc14) → [`00aadc5c`](#insn-00aadc5c)
  - `FALL_THROUGH` [`00aadc14`](#insn-00aadc14) → [`00aadc18`](#insn-00aadc18)
- ブロック [`00aadc18`](#insn-00aadc18) 範囲 `[['00aadc18', '00aadc27']]`
  - `CONDITIONAL_JUMP` [`00aadc24`](#insn-00aadc24) → [`00aadc54`](#insn-00aadc54)
  - `FALL_THROUGH` [`00aadc24`](#insn-00aadc24) → [`00aadc28`](#insn-00aadc28)
- ブロック [`00aadc28`](#insn-00aadc28) 範囲 `[['00aadc28', '00aadc2f']]`
  - `UNCONDITIONAL_JUMP` [`00aadc2c`](#insn-00aadc2c) → [`00aadc3c`](#insn-00aadc3c)
- ブロック [`00aadc30`](#insn-00aadc30) 範囲 `[['00aadc30', '00aadc3b']]`
  - `CONDITIONAL_JUMP` [`00aadc38`](#insn-00aadc38) → [`00aadc50`](#insn-00aadc50)
  - `FALL_THROUGH` [`00aadc38`](#insn-00aadc38) → [`00aadc3c`](#insn-00aadc3c)
- ブロック [`00aadc3c`](#insn-00aadc3c) 範囲 `[['00aadc3c', '00aadc43']]`
  - `CONDITIONAL_JUMP` [`00aadc40`](#insn-00aadc40) → [`00aadc30`](#insn-00aadc30)
  - `FALL_THROUGH` [`00aadc40`](#insn-00aadc40) → [`00aadc44`](#insn-00aadc44)
- ブロック [`00aadc44`](#insn-00aadc44) 範囲 `[['00aadc44', '00aadc4f']]`
  - `UNCONDITIONAL_JUMP` [`00aadc4c`](#insn-00aadc4c) → [`00aadc30`](#insn-00aadc30)
- ブロック [`00aadc50`](#insn-00aadc50) 範囲 `[['00aadc50', '00aadc53']]`
  - `FALL_THROUGH` [`00aadc50`](#insn-00aadc50) → [`00aadc54`](#insn-00aadc54)
- ブロック [`00aadc54`](#insn-00aadc54) 範囲 `[['00aadc54', '00aadc5b']]`
  - `FALL_THROUGH` [`00aadc58`](#insn-00aadc58) → [`00aadc5c`](#insn-00aadc5c)
- ブロック [`00aadc5c`](#insn-00aadc5c) 範囲 `[['00aadc5c', '00aadc77']]`

## 命令位置別の参照

- [`00aadba4`](#insn-00aadba4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadba8`](#insn-00aadba8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbac`](#insn-00aadbac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbbc`](#insn-00aadbbc) → [`00aadbd0`](#insn-00aadbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbc8`](#insn-00aadbc8) → [`00aadbc0`](#insn-00aadbc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbcc`](#insn-00aadbcc) → [`00aadbe8`](#insn-00aadbe8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbe4`](#insn-00aadbe4) → [`00aadbd4`](#insn-00aadbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbf0`](#insn-00aadbf0) → [`00aadbf8`](#insn-00aadbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc0c`](#insn-00aadc0c) → [`00471738`](../00471/00471738.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00471738` · 推定シンボル `None` · 推定型 `None`
- [`00aadc14`](#insn-00aadc14) → [`00aadc5c`](#insn-00aadc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc24`](#insn-00aadc24) → [`00aadc54`](#insn-00aadc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc2c`](#insn-00aadc2c) → [`00aadc3c`](#insn-00aadc3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc38`](#insn-00aadc38) → [`00aadc50`](#insn-00aadc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc40`](#insn-00aadc40) → [`00aadc30`](#insn-00aadc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc48`](#insn-00aadc48) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aadc4c`](#insn-00aadc4c) → [`00aadc30`](#insn-00aadc30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc58`](#insn-00aadc58) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aadc60`](#insn-00aadc60) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aadc68`](#insn-00aadc68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc6c`](#insn-00aadc6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc70`](#insn-00aadc70) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadba4`](#insn-00aadba4)

~~~json
{
  "source": "00aadba4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadba8`](#insn-00aadba8)

~~~json
{
  "source": "00aadba8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbac`](#insn-00aadbac)

~~~json
{
  "source": "00aadbac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbbc`](#insn-00aadbbc)

~~~json
{
  "source": "00aadbbc",
  "target": "00aadbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbc8`](#insn-00aadbc8)

~~~json
{
  "source": "00aadbc8",
  "target": "00aadbc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbcc`](#insn-00aadbcc)

~~~json
{
  "source": "00aadbcc",
  "target": "00aadbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbe4`](#insn-00aadbe4)

~~~json
{
  "source": "00aadbe4",
  "target": "00aadbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbf0`](#insn-00aadbf0)

~~~json
{
  "source": "00aadbf0",
  "target": "00aadbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc0c`](#insn-00aadc0c)

~~~json
{
  "source": "00aadc0c",
  "target": "00471738",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadc14`](#insn-00aadc14)

~~~json
{
  "source": "00aadc14",
  "target": "00aadc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc24`](#insn-00aadc24)

~~~json
{
  "source": "00aadc24",
  "target": "00aadc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc2c`](#insn-00aadc2c)

~~~json
{
  "source": "00aadc2c",
  "target": "00aadc3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc38`](#insn-00aadc38)

~~~json
{
  "source": "00aadc38",
  "target": "00aadc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc40`](#insn-00aadc40)

~~~json
{
  "source": "00aadc40",
  "target": "00aadc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc48`](#insn-00aadc48)

~~~json
{
  "source": "00aadc48",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadc4c`](#insn-00aadc4c)

~~~json
{
  "source": "00aadc4c",
  "target": "00aadc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc58`](#insn-00aadc58)

~~~json
{
  "source": "00aadc58",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadc60`](#insn-00aadc60)

~~~json
{
  "source": "00aadc60",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadc68`](#insn-00aadc68)

~~~json
{
  "source": "00aadc68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc6c`](#insn-00aadc6c)

~~~json
{
  "source": "00aadc6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc70`](#insn-00aadc70)

~~~json
{
  "source": "00aadc70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
