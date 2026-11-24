# 00aadbe8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aadba4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-7d6ed14220a2a849a00331b42dd36d70)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0d678`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-8be935cae2bfc2b5b509a70e51ceefb5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadbe8",
  "name": "FUN_00aadbe8",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d8f7de860ff3c1075e08cd1f007ec58c566198abf60ee4d32cea2daf50fd37a",
  "source_text_sha256": "2d8f7de860ff3c1075e08cd1f007ec58c566198abf60ee4d32cea2daf50fd37a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadbe8",
        "00aadcbb"
      ]
    ],
    "bytes_sha256": "448aab9cea36b2848cb800c31bd7dedd6dc9a131a9709fe0a0ac003aaa1e61a4",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aac39c](../00aac/00aac39c.md)

## 呼び出し先

- [00471738](../00471/00471738.md)
- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1251 bytes

~~~c

undefined8 * FUN_00aadbe8(undefined8 *param_1,undefined8 *param_2)

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
<a id="insn-00aadbe8"></a> `00aadbe8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aadbec"></a> `00aadbec` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadbf0"></a> `00aadbf0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadbf4"></a> `00aadbf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aadbf8"></a> `00aadbf8` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00aadbfc"></a> `00aadbfc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00aadc00"></a> `00aadc00` | `a8 00 00 b4` | cbz x8,0x00aadc14 | `CONDITIONAL_JUMP`
<a id="insn-00aadc04"></a> `00aadc04` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aadc08"></a> `00aadc08` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aadc0c"></a> `00aadc0c` | `c8 ff ff b5` | cbnz x8,0x00aadc04 | `CONDITIONAL_JUMP`
<a id="insn-00aadc10"></a> `00aadc10` | `07 00 00 14` | b 0x00aadc2c | `UNCONDITIONAL_JUMP`
<a id="insn-00aadc14"></a> `00aadc14` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00aadc18"></a> `00aadc18` | `14 09 40 f9` | ldr x20,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aadc1c"></a> `00aadc1c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00aadc20"></a> `00aadc20` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00aadc24"></a> `00aadc24` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00aadc28"></a> `00aadc28` | `81 ff ff 54` | b.ne 0x00aadc18 | `CONDITIONAL_JUMP`
<a id="insn-00aadc2c"></a> `00aadc2c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aadc30"></a> `00aadc30` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00aadc34"></a> `00aadc34` | `41 00 00 54` | b.ne 0x00aadc3c | `CONDITIONAL_JUMP`
<a id="insn-00aadc38"></a> `00aadc38` | `14 00 00 f9` | str x20,[x0] | `FALL_THROUGH`
<a id="insn-00aadc3c"></a> `00aadc3c` | `08 a4 40 a9` | ldp x8,x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aadc40"></a> `00aadc40` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aadc44"></a> `00aadc44` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00aadc48"></a> `00aadc48` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aadc4c"></a> `00aadc4c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aadc50"></a> `00aadc50` | `ba 0e e7 97` | bl 0x00471738 | `UNCONDITIONAL_CALL`
<a id="insn-00aadc54"></a> `00aadc54` | `75 16 40 f9` | ldr x21,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aadc58"></a> `00aadc58` | `55 02 00 b4` | cbz x21,0x00aadca0 | `CONDITIONAL_JUMP`
<a id="insn-00aadc5c"></a> `00aadc5c` | `68 1a 40 f9` | ldr x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aadc60"></a> `00aadc60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aadc64"></a> `00aadc64` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00aadc68"></a> `00aadc68` | `80 01 00 54` | b.eq 0x00aadc98 | `CONDITIONAL_JUMP`
<a id="insn-00aadc6c"></a> `00aadc6c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00aadc70"></a> `00aadc70` | `04 00 00 14` | b 0x00aadc80 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadc74"></a> `00aadc74` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00aadc78"></a> `00aadc78` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00aadc7c"></a> `00aadc7c` | `c0 00 00 54` | b.eq 0x00aadc94 | `CONDITIONAL_JUMP`
<a id="insn-00aadc80"></a> `00aadc80` | `c0 8e 5e f8` | ldr x0,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00aadc84"></a> `00aadc84` | `80 ff ff b4` | cbz x0,0x00aadc74 | `CONDITIONAL_JUMP`
<a id="insn-00aadc88"></a> `00aadc88` | `00 01 1f f8` | stur x0,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-00aadc8c"></a> `00aadc8c` | `f5 b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadc90"></a> `00aadc90` | `f9 ff ff 17` | b 0x00aadc74 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadc94"></a> `00aadc94` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aadc98"></a> `00aadc98` | `75 1a 00 f9` | str x21,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aadc9c"></a> `00aadc9c` | `f1 b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadca0"></a> `00aadca0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadca4"></a> `00aadca4` | `ef b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadca8"></a> `00aadca8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aadcac"></a> `00aadcac` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadcb0"></a> `00aadcb0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadcb4"></a> `00aadcb4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aadcb8"></a> `00aadcb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadbe8`](#insn-00aadbe8) 範囲 `[['00aadbe8', '00aadc03']]`
  - `CONDITIONAL_JUMP` [`00aadc00`](#insn-00aadc00) → [`00aadc14`](#insn-00aadc14)
  - `FALL_THROUGH` [`00aadc00`](#insn-00aadc00) → [`00aadc04`](#insn-00aadc04)
- ブロック [`00aadc04`](#insn-00aadc04) 範囲 `[['00aadc04', '00aadc0f']]`
  - `CONDITIONAL_JUMP` [`00aadc0c`](#insn-00aadc0c) → [`00aadc04`](#insn-00aadc04)
  - `FALL_THROUGH` [`00aadc0c`](#insn-00aadc0c) → [`00aadc10`](#insn-00aadc10)
- ブロック [`00aadc10`](#insn-00aadc10) 範囲 `[['00aadc10', '00aadc13']]`
  - `UNCONDITIONAL_JUMP` [`00aadc10`](#insn-00aadc10) → [`00aadc2c`](#insn-00aadc2c)
- ブロック [`00aadc14`](#insn-00aadc14) 範囲 `[['00aadc14', '00aadc17']]`
  - `FALL_THROUGH` [`00aadc14`](#insn-00aadc14) → [`00aadc18`](#insn-00aadc18)
- ブロック [`00aadc18`](#insn-00aadc18) 範囲 `[['00aadc18', '00aadc2b']]`
  - `CONDITIONAL_JUMP` [`00aadc28`](#insn-00aadc28) → [`00aadc18`](#insn-00aadc18)
  - `FALL_THROUGH` [`00aadc28`](#insn-00aadc28) → [`00aadc2c`](#insn-00aadc2c)
- ブロック [`00aadc2c`](#insn-00aadc2c) 範囲 `[['00aadc2c', '00aadc37']]`
  - `CONDITIONAL_JUMP` [`00aadc34`](#insn-00aadc34) → [`00aadc3c`](#insn-00aadc3c)
  - `FALL_THROUGH` [`00aadc34`](#insn-00aadc34) → [`00aadc38`](#insn-00aadc38)
- ブロック [`00aadc38`](#insn-00aadc38) 範囲 `[['00aadc38', '00aadc3b']]`
  - `FALL_THROUGH` [`00aadc38`](#insn-00aadc38) → [`00aadc3c`](#insn-00aadc3c)
- ブロック [`00aadc3c`](#insn-00aadc3c) 範囲 `[['00aadc3c', '00aadc5b']]`
  - `CONDITIONAL_JUMP` [`00aadc58`](#insn-00aadc58) → [`00aadca0`](#insn-00aadca0)
  - `FALL_THROUGH` [`00aadc58`](#insn-00aadc58) → [`00aadc5c`](#insn-00aadc5c)
- ブロック [`00aadc5c`](#insn-00aadc5c) 範囲 `[['00aadc5c', '00aadc6b']]`
  - `CONDITIONAL_JUMP` [`00aadc68`](#insn-00aadc68) → [`00aadc98`](#insn-00aadc98)
  - `FALL_THROUGH` [`00aadc68`](#insn-00aadc68) → [`00aadc6c`](#insn-00aadc6c)
- ブロック [`00aadc6c`](#insn-00aadc6c) 範囲 `[['00aadc6c', '00aadc73']]`
  - `UNCONDITIONAL_JUMP` [`00aadc70`](#insn-00aadc70) → [`00aadc80`](#insn-00aadc80)
- ブロック [`00aadc74`](#insn-00aadc74) 範囲 `[['00aadc74', '00aadc7f']]`
  - `CONDITIONAL_JUMP` [`00aadc7c`](#insn-00aadc7c) → [`00aadc94`](#insn-00aadc94)
  - `FALL_THROUGH` [`00aadc7c`](#insn-00aadc7c) → [`00aadc80`](#insn-00aadc80)
- ブロック [`00aadc80`](#insn-00aadc80) 範囲 `[['00aadc80', '00aadc87']]`
  - `CONDITIONAL_JUMP` [`00aadc84`](#insn-00aadc84) → [`00aadc74`](#insn-00aadc74)
  - `FALL_THROUGH` [`00aadc84`](#insn-00aadc84) → [`00aadc88`](#insn-00aadc88)
- ブロック [`00aadc88`](#insn-00aadc88) 範囲 `[['00aadc88', '00aadc93']]`
  - `UNCONDITIONAL_JUMP` [`00aadc90`](#insn-00aadc90) → [`00aadc74`](#insn-00aadc74)
- ブロック [`00aadc94`](#insn-00aadc94) 範囲 `[['00aadc94', '00aadc97']]`
  - `FALL_THROUGH` [`00aadc94`](#insn-00aadc94) → [`00aadc98`](#insn-00aadc98)
- ブロック [`00aadc98`](#insn-00aadc98) 範囲 `[['00aadc98', '00aadc9f']]`
  - `FALL_THROUGH` [`00aadc9c`](#insn-00aadc9c) → [`00aadca0`](#insn-00aadca0)
- ブロック [`00aadca0`](#insn-00aadca0) 範囲 `[['00aadca0', '00aadcbb']]`

## 命令位置別の参照

- [`00aadbe8`](#insn-00aadbe8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbec`](#insn-00aadbec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbf0`](#insn-00aadbf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc00`](#insn-00aadc00) → [`00aadc14`](#insn-00aadc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc0c`](#insn-00aadc0c) → [`00aadc04`](#insn-00aadc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc10`](#insn-00aadc10) → [`00aadc2c`](#insn-00aadc2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc28`](#insn-00aadc28) → [`00aadc18`](#insn-00aadc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc34`](#insn-00aadc34) → [`00aadc3c`](#insn-00aadc3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc50`](#insn-00aadc50) → [`00471738`](../00471/00471738.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00471738` · 推定シンボル `None` · 推定型 `None`
- [`00aadc58`](#insn-00aadc58) → [`00aadca0`](#insn-00aadca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc68`](#insn-00aadc68) → [`00aadc98`](#insn-00aadc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc70`](#insn-00aadc70) → [`00aadc80`](#insn-00aadc80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc7c`](#insn-00aadc7c) → [`00aadc94`](#insn-00aadc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc84`](#insn-00aadc84) → [`00aadc74`](#insn-00aadc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc8c`](#insn-00aadc8c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadc90`](#insn-00aadc90) → [`00aadc74`](#insn-00aadc74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc9c`](#insn-00aadc9c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadca4`](#insn-00aadca4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadcac`](#insn-00aadcac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcb0`](#insn-00aadcb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcb4`](#insn-00aadcb4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadbe8`](#insn-00aadbe8)

~~~json
{
  "source": "00aadbe8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbec`](#insn-00aadbec)

~~~json
{
  "source": "00aadbec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbf0`](#insn-00aadbf0)

~~~json
{
  "source": "00aadbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc00`](#insn-00aadc00)

~~~json
{
  "source": "00aadc00",
  "target": "00aadc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc0c`](#insn-00aadc0c)

~~~json
{
  "source": "00aadc0c",
  "target": "00aadc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc10`](#insn-00aadc10)

~~~json
{
  "source": "00aadc10",
  "target": "00aadc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc28`](#insn-00aadc28)

~~~json
{
  "source": "00aadc28",
  "target": "00aadc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc34`](#insn-00aadc34)

~~~json
{
  "source": "00aadc34",
  "target": "00aadc3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc50`](#insn-00aadc50)

~~~json
{
  "source": "00aadc50",
  "target": "00471738",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadc58`](#insn-00aadc58)

~~~json
{
  "source": "00aadc58",
  "target": "00aadca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc68`](#insn-00aadc68)

~~~json
{
  "source": "00aadc68",
  "target": "00aadc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc70`](#insn-00aadc70)

~~~json
{
  "source": "00aadc70",
  "target": "00aadc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc7c`](#insn-00aadc7c)

~~~json
{
  "source": "00aadc7c",
  "target": "00aadc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc84`](#insn-00aadc84)

~~~json
{
  "source": "00aadc84",
  "target": "00aadc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc8c`](#insn-00aadc8c)

~~~json
{
  "source": "00aadc8c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadc90`](#insn-00aadc90)

~~~json
{
  "source": "00aadc90",
  "target": "00aadc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc9c`](#insn-00aadc9c)

~~~json
{
  "source": "00aadc9c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadca4`](#insn-00aadca4)

~~~json
{
  "source": "00aadca4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadcac`](#insn-00aadcac)

~~~json
{
  "source": "00aadcac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcb0`](#insn-00aadcb0)

~~~json
{
  "source": "00aadcb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcb4`](#insn-00aadcb4)

~~~json
{
  "source": "00aadcb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
