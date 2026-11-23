# 00a3bddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a3bddc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3b/00a3bddc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0040.md#compare-5313d271479e581393ca6ee577a7c0c2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a3be20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3be20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0002.md#compare-5b7eefa3f297c9be60250c8b5a456a07)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3bddc",
  "name": "FUN_00a3bddc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4f63d3d92b2d7da3765b5aa8405437a901c5e308177673d2e77e15faae6f5db",
  "source_text_sha256": "e4f63d3d92b2d7da3765b5aa8405437a901c5e308177673d2e77e15faae6f5db",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3bddc",
        "00a3be8b"
      ]
    ],
    "bytes_sha256": "d5d4979aac623c7824013bac651e2659713f936b52d8f6aac7d35d037f008fff",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1044 bytes

~~~c

void FUN_00a3bddc(long param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  
  puVar2 = *(undefined8 **)(param_1 + 0x28);
  if (puVar2 != (undefined8 *)0x0) {
    puVar3 = *(undefined8 **)(param_1 + 0x30);
    puVar1 = puVar2;
    if (puVar3 != puVar2) {
      do {
        puVar3 = puVar3 + -3;
        if ((void *)*puVar3 != (void *)0x0) {
          _ZdlPv((void *)*puVar3);
        }
      } while (puVar3 != puVar2);
      puVar1 = *(undefined8 **)(param_1 + 0x28);
    }
    *(undefined8 **)(param_1 + 0x30) = puVar2;
    _ZdlPv(puVar1);
  }
  puVar2 = *(undefined8 **)(param_1 + 0x10);
  if (puVar2 == (undefined8 *)0x0) {
    return;
  }
  puVar3 = *(undefined8 **)(param_1 + 0x18);
  puVar1 = puVar2;
  if (puVar3 != puVar2) {
    do {
      puVar3 = puVar3 + -3;
      if ((void *)*puVar3 != (void *)0x0) {
        _ZdlPv((void *)*puVar3);
      }
    } while (puVar3 != puVar2);
    puVar1 = *(undefined8 **)(param_1 + 0x10);
  }
  *(undefined8 **)(param_1 + 0x18) = puVar2;
  _ZdlPv(puVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3bddc"></a> `00a3bddc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a3bde0"></a> `00a3bde0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3bde4"></a> `00a3bde4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3bde8"></a> `00a3bde8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3bdec"></a> `00a3bdec` | `14 14 40 f9` | ldr x20,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00a3bdf0"></a> `00a3bdf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a3bdf4"></a> `00a3bdf4` | `f4 01 00 b4` | cbz x20,0x00a3be30 | `CONDITIONAL_JUMP`
<a id="insn-00a3bdf8"></a> `00a3bdf8` | `75 1a 40 f9` | ldr x21,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00a3bdfc"></a> `00a3bdfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a3be00"></a> `00a3be00` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00a3be04"></a> `00a3be04` | `81 00 00 54` | b.ne 0x00a3be14 | `CONDITIONAL_JUMP`
<a id="insn-00a3be08"></a> `00a3be08` | `08 00 00 14` | b 0x00a3be28 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3be0c"></a> `00a3be0c` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00a3be10"></a> `00a3be10` | `a0 00 00 54` | b.eq 0x00a3be24 | `CONDITIONAL_JUMP`
<a id="insn-00a3be14"></a> `00a3be14` | `a0 8e 5e f8` | ldr x0,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00a3be18"></a> `00a3be18` | `a0 ff ff b4` | cbz x0,0x00a3be0c | `CONDITIONAL_JUMP`
<a id="insn-00a3be1c"></a> `00a3be1c` | `7d 7c 06 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00a3be20"></a> `00a3be20` | `fb ff ff 17` | b 0x00a3be0c | `UNCONDITIONAL_JUMP`
<a id="insn-00a3be24"></a> `00a3be24` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00a3be28"></a> `00a3be28` | `74 1a 00 f9` | str x20,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00a3be2c"></a> `00a3be2c` | `79 7c 06 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00a3be30"></a> `00a3be30` | `74 0a 40 f9` | ldr x20,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a3be34"></a> `00a3be34` | `54 02 00 b4` | cbz x20,0x00a3be7c | `CONDITIONAL_JUMP`
<a id="insn-00a3be38"></a> `00a3be38` | `75 0e 40 f9` | ldr x21,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a3be3c"></a> `00a3be3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a3be40"></a> `00a3be40` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00a3be44"></a> `00a3be44` | `81 00 00 54` | b.ne 0x00a3be54 | `CONDITIONAL_JUMP`
<a id="insn-00a3be48"></a> `00a3be48` | `08 00 00 14` | b 0x00a3be68 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3be4c"></a> `00a3be4c` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00a3be50"></a> `00a3be50` | `a0 00 00 54` | b.eq 0x00a3be64 | `CONDITIONAL_JUMP`
<a id="insn-00a3be54"></a> `00a3be54` | `a0 8e 5e f8` | ldr x0,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00a3be58"></a> `00a3be58` | `a0 ff ff b4` | cbz x0,0x00a3be4c | `CONDITIONAL_JUMP`
<a id="insn-00a3be5c"></a> `00a3be5c` | `6d 7c 06 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00a3be60"></a> `00a3be60` | `fb ff ff 17` | b 0x00a3be4c | `UNCONDITIONAL_JUMP`
<a id="insn-00a3be64"></a> `00a3be64` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a3be68"></a> `00a3be68` | `74 0e 00 f9` | str x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a3be6c"></a> `00a3be6c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3be70"></a> `00a3be70` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3be74"></a> `00a3be74` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a3be78"></a> `00a3be78` | `66 7c 06 14` | b 0x00bdb010 | `CALL_TERMINATOR`
<a id="insn-00a3be7c"></a> `00a3be7c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3be80"></a> `00a3be80` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3be84"></a> `00a3be84` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a3be88"></a> `00a3be88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3bddc`](#insn-00a3bddc) 範囲 `[['00a3bddc', '00a3bdf7']]`
  - `CONDITIONAL_JUMP` [`00a3bdf4`](#insn-00a3bdf4) → [`00a3be30`](#insn-00a3be30)
  - `FALL_THROUGH` [`00a3bdf4`](#insn-00a3bdf4) → [`00a3bdf8`](#insn-00a3bdf8)
- ブロック [`00a3bdf8`](#insn-00a3bdf8) 範囲 `[['00a3bdf8', '00a3be07']]`
  - `CONDITIONAL_JUMP` [`00a3be04`](#insn-00a3be04) → [`00a3be14`](#insn-00a3be14)
  - `FALL_THROUGH` [`00a3be04`](#insn-00a3be04) → [`00a3be08`](#insn-00a3be08)
- ブロック [`00a3be08`](#insn-00a3be08) 範囲 `[['00a3be08', '00a3be0b']]`
  - `UNCONDITIONAL_JUMP` [`00a3be08`](#insn-00a3be08) → [`00a3be28`](#insn-00a3be28)
- ブロック [`00a3be0c`](#insn-00a3be0c) 範囲 `[['00a3be0c', '00a3be13']]`
  - `CONDITIONAL_JUMP` [`00a3be10`](#insn-00a3be10) → [`00a3be24`](#insn-00a3be24)
  - `FALL_THROUGH` [`00a3be10`](#insn-00a3be10) → [`00a3be14`](#insn-00a3be14)
- ブロック [`00a3be14`](#insn-00a3be14) 範囲 `[['00a3be14', '00a3be1b']]`
  - `CONDITIONAL_JUMP` [`00a3be18`](#insn-00a3be18) → [`00a3be0c`](#insn-00a3be0c)
  - `FALL_THROUGH` [`00a3be18`](#insn-00a3be18) → [`00a3be1c`](#insn-00a3be1c)
- ブロック [`00a3be1c`](#insn-00a3be1c) 範囲 `[['00a3be1c', '00a3be23']]`
  - `UNCONDITIONAL_JUMP` [`00a3be20`](#insn-00a3be20) → [`00a3be0c`](#insn-00a3be0c)
- ブロック [`00a3be24`](#insn-00a3be24) 範囲 `[['00a3be24', '00a3be27']]`
  - `FALL_THROUGH` [`00a3be24`](#insn-00a3be24) → [`00a3be28`](#insn-00a3be28)
- ブロック [`00a3be28`](#insn-00a3be28) 範囲 `[['00a3be28', '00a3be2f']]`
  - `FALL_THROUGH` [`00a3be2c`](#insn-00a3be2c) → [`00a3be30`](#insn-00a3be30)
- ブロック [`00a3be30`](#insn-00a3be30) 範囲 `[['00a3be30', '00a3be37']]`
  - `CONDITIONAL_JUMP` [`00a3be34`](#insn-00a3be34) → [`00a3be7c`](#insn-00a3be7c)
  - `FALL_THROUGH` [`00a3be34`](#insn-00a3be34) → [`00a3be38`](#insn-00a3be38)
- ブロック [`00a3be38`](#insn-00a3be38) 範囲 `[['00a3be38', '00a3be47']]`
  - `CONDITIONAL_JUMP` [`00a3be44`](#insn-00a3be44) → [`00a3be54`](#insn-00a3be54)
  - `FALL_THROUGH` [`00a3be44`](#insn-00a3be44) → [`00a3be48`](#insn-00a3be48)
- ブロック [`00a3be48`](#insn-00a3be48) 範囲 `[['00a3be48', '00a3be4b']]`
  - `UNCONDITIONAL_JUMP` [`00a3be48`](#insn-00a3be48) → [`00a3be68`](#insn-00a3be68)
- ブロック [`00a3be4c`](#insn-00a3be4c) 範囲 `[['00a3be4c', '00a3be53']]`
  - `CONDITIONAL_JUMP` [`00a3be50`](#insn-00a3be50) → [`00a3be64`](#insn-00a3be64)
  - `FALL_THROUGH` [`00a3be50`](#insn-00a3be50) → [`00a3be54`](#insn-00a3be54)
- ブロック [`00a3be54`](#insn-00a3be54) 範囲 `[['00a3be54', '00a3be5b']]`
  - `CONDITIONAL_JUMP` [`00a3be58`](#insn-00a3be58) → [`00a3be4c`](#insn-00a3be4c)
  - `FALL_THROUGH` [`00a3be58`](#insn-00a3be58) → [`00a3be5c`](#insn-00a3be5c)
- ブロック [`00a3be5c`](#insn-00a3be5c) 範囲 `[['00a3be5c', '00a3be63']]`
  - `UNCONDITIONAL_JUMP` [`00a3be60`](#insn-00a3be60) → [`00a3be4c`](#insn-00a3be4c)
- ブロック [`00a3be64`](#insn-00a3be64) 範囲 `[['00a3be64', '00a3be67']]`
  - `FALL_THROUGH` [`00a3be64`](#insn-00a3be64) → [`00a3be68`](#insn-00a3be68)
- ブロック [`00a3be68`](#insn-00a3be68) 範囲 `[['00a3be68', '00a3be7b']]`
- ブロック [`00a3be7c`](#insn-00a3be7c) 範囲 `[['00a3be7c', '00a3be8b']]`

## 命令位置別の参照

- [`00a3bddc`](#insn-00a3bddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bde0`](#insn-00a3bde0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bde4`](#insn-00a3bde4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bdf4`](#insn-00a3bdf4) → [`00a3be30`](#insn-00a3be30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be04`](#insn-00a3be04) → [`00a3be14`](#insn-00a3be14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be08`](#insn-00a3be08) → [`00a3be28`](#insn-00a3be28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be10`](#insn-00a3be10) → [`00a3be24`](#insn-00a3be24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be18`](#insn-00a3be18) → [`00a3be0c`](#insn-00a3be0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be1c`](#insn-00a3be1c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00a3be20`](#insn-00a3be20) → [`00a3be0c`](#insn-00a3be0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be2c`](#insn-00a3be2c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00a3be34`](#insn-00a3be34) → [`00a3be7c`](#insn-00a3be7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be44`](#insn-00a3be44) → [`00a3be54`](#insn-00a3be54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be48`](#insn-00a3be48) → [`00a3be68`](#insn-00a3be68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be50`](#insn-00a3be50) → [`00a3be64`](#insn-00a3be64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be58`](#insn-00a3be58) → [`00a3be4c`](#insn-00a3be4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be5c`](#insn-00a3be5c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00a3be60`](#insn-00a3be60) → [`00a3be4c`](#insn-00a3be4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be6c`](#insn-00a3be6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be70`](#insn-00a3be70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be74`](#insn-00a3be74) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be78`](#insn-00a3be78) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00a3be7c`](#insn-00a3be7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be80`](#insn-00a3be80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3be84`](#insn-00a3be84) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3bddc`](#insn-00a3bddc)

~~~json
{
  "source": "00a3bddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bde0`](#insn-00a3bde0)

~~~json
{
  "source": "00a3bde0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bde4`](#insn-00a3bde4)

~~~json
{
  "source": "00a3bde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bdf4`](#insn-00a3bdf4)

~~~json
{
  "source": "00a3bdf4",
  "target": "00a3be30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be04`](#insn-00a3be04)

~~~json
{
  "source": "00a3be04",
  "target": "00a3be14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be08`](#insn-00a3be08)

~~~json
{
  "source": "00a3be08",
  "target": "00a3be28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be10`](#insn-00a3be10)

~~~json
{
  "source": "00a3be10",
  "target": "00a3be24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be18`](#insn-00a3be18)

~~~json
{
  "source": "00a3be18",
  "target": "00a3be0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be1c`](#insn-00a3be1c)

~~~json
{
  "source": "00a3be1c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3be20`](#insn-00a3be20)

~~~json
{
  "source": "00a3be20",
  "target": "00a3be0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be2c`](#insn-00a3be2c)

~~~json
{
  "source": "00a3be2c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3be34`](#insn-00a3be34)

~~~json
{
  "source": "00a3be34",
  "target": "00a3be7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be44`](#insn-00a3be44)

~~~json
{
  "source": "00a3be44",
  "target": "00a3be54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be48`](#insn-00a3be48)

~~~json
{
  "source": "00a3be48",
  "target": "00a3be68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be50`](#insn-00a3be50)

~~~json
{
  "source": "00a3be50",
  "target": "00a3be64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be58`](#insn-00a3be58)

~~~json
{
  "source": "00a3be58",
  "target": "00a3be4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be5c`](#insn-00a3be5c)

~~~json
{
  "source": "00a3be5c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3be60`](#insn-00a3be60)

~~~json
{
  "source": "00a3be60",
  "target": "00a3be4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be6c`](#insn-00a3be6c)

~~~json
{
  "source": "00a3be6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be70`](#insn-00a3be70)

~~~json
{
  "source": "00a3be70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be74`](#insn-00a3be74)

~~~json
{
  "source": "00a3be74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be78`](#insn-00a3be78)

~~~json
{
  "source": "00a3be78",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3be7c`](#insn-00a3be7c)

~~~json
{
  "source": "00a3be7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be80`](#insn-00a3be80)

~~~json
{
  "source": "00a3be80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3be84`](#insn-00a3be84)

~~~json
{
  "source": "00a3be84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
