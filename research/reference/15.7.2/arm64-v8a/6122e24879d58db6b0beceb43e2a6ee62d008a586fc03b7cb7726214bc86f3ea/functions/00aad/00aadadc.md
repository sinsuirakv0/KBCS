# 00aadadc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aadba4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-887fcd8fc55585724330c43ed19c6195)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadadc",
  "name": "FUN_00aadadc",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e0520f0ed24694dba4947e4de7c44a4919f746e1495f16d974f406c5079e1e7e",
  "source_text_sha256": "e0520f0ed24694dba4947e4de7c44a4919f746e1495f16d974f406c5079e1e7e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadadc",
        "00aadbaf"
      ]
    ],
    "bytes_sha256": "b122c70f9a4835ee79c70e65706019d328619985443e697d0ba706c92d72340f",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aac290](../00aac/00aac290.md)

## 呼び出し先

- [00471738](../00471/00471738.md)
- [00bdaf60](../00bda/00bdaf60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1251 bytes

~~~c

undefined8 * FUN_00aadadc(undefined8 *param_1,undefined8 *param_2)

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
<a id="insn-00aadadc"></a> `00aadadc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aadae0"></a> `00aadae0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadae4"></a> `00aadae4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadae8"></a> `00aadae8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aadaec"></a> `00aadaec` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00aadaf0"></a> `00aadaf0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00aadaf4"></a> `00aadaf4` | `a8 00 00 b4` | cbz x8,0x00aadb08 | `CONDITIONAL_JUMP`
<a id="insn-00aadaf8"></a> `00aadaf8` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aadafc"></a> `00aadafc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aadb00"></a> `00aadb00` | `c8 ff ff b5` | cbnz x8,0x00aadaf8 | `CONDITIONAL_JUMP`
<a id="insn-00aadb04"></a> `00aadb04` | `07 00 00 14` | b 0x00aadb20 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadb08"></a> `00aadb08` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00aadb0c"></a> `00aadb0c` | `14 09 40 f9` | ldr x20,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aadb10"></a> `00aadb10` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00aadb14"></a> `00aadb14` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00aadb18"></a> `00aadb18` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00aadb1c"></a> `00aadb1c` | `81 ff ff 54` | b.ne 0x00aadb0c | `CONDITIONAL_JUMP`
<a id="insn-00aadb20"></a> `00aadb20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aadb24"></a> `00aadb24` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00aadb28"></a> `00aadb28` | `41 00 00 54` | b.ne 0x00aadb30 | `CONDITIONAL_JUMP`
<a id="insn-00aadb2c"></a> `00aadb2c` | `14 00 00 f9` | str x20,[x0] | `FALL_THROUGH`
<a id="insn-00aadb30"></a> `00aadb30` | `08 a4 40 a9` | ldp x8,x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aadb34"></a> `00aadb34` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aadb38"></a> `00aadb38` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00aadb3c"></a> `00aadb3c` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aadb40"></a> `00aadb40` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aadb44"></a> `00aadb44` | `fd 0e e7 97` | bl 0x00471738 | `UNCONDITIONAL_CALL`
<a id="insn-00aadb48"></a> `00aadb48` | `75 16 40 f9` | ldr x21,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aadb4c"></a> `00aadb4c` | `55 02 00 b4` | cbz x21,0x00aadb94 | `CONDITIONAL_JUMP`
<a id="insn-00aadb50"></a> `00aadb50` | `68 1a 40 f9` | ldr x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aadb54"></a> `00aadb54` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aadb58"></a> `00aadb58` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00aadb5c"></a> `00aadb5c` | `80 01 00 54` | b.eq 0x00aadb8c | `CONDITIONAL_JUMP`
<a id="insn-00aadb60"></a> `00aadb60` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00aadb64"></a> `00aadb64` | `04 00 00 14` | b 0x00aadb74 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadb68"></a> `00aadb68` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00aadb6c"></a> `00aadb6c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00aadb70"></a> `00aadb70` | `c0 00 00 54` | b.eq 0x00aadb88 | `CONDITIONAL_JUMP`
<a id="insn-00aadb74"></a> `00aadb74` | `c0 8e 5e f8` | ldr x0,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00aadb78"></a> `00aadb78` | `80 ff ff b4` | cbz x0,0x00aadb68 | `CONDITIONAL_JUMP`
<a id="insn-00aadb7c"></a> `00aadb7c` | `00 01 1f f8` | stur x0,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-00aadb80"></a> `00aadb80` | `f8 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aadb84"></a> `00aadb84` | `f9 ff ff 17` | b 0x00aadb68 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadb88"></a> `00aadb88` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aadb8c"></a> `00aadb8c` | `75 1a 00 f9` | str x21,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aadb90"></a> `00aadb90` | `f4 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aadb94"></a> `00aadb94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadb98"></a> `00aadb98` | `f2 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aadb9c"></a> `00aadb9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aadba0"></a> `00aadba0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadba4"></a> `00aadba4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadba8"></a> `00aadba8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aadbac"></a> `00aadbac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadadc`](#insn-00aadadc) 範囲 `[['00aadadc', '00aadaf7']]`
  - `CONDITIONAL_JUMP` [`00aadaf4`](#insn-00aadaf4) → [`00aadb08`](#insn-00aadb08)
  - `FALL_THROUGH` [`00aadaf4`](#insn-00aadaf4) → [`00aadaf8`](#insn-00aadaf8)
- ブロック [`00aadaf8`](#insn-00aadaf8) 範囲 `[['00aadaf8', '00aadb03']]`
  - `CONDITIONAL_JUMP` [`00aadb00`](#insn-00aadb00) → [`00aadaf8`](#insn-00aadaf8)
  - `FALL_THROUGH` [`00aadb00`](#insn-00aadb00) → [`00aadb04`](#insn-00aadb04)
- ブロック [`00aadb04`](#insn-00aadb04) 範囲 `[['00aadb04', '00aadb07']]`
  - `UNCONDITIONAL_JUMP` [`00aadb04`](#insn-00aadb04) → [`00aadb20`](#insn-00aadb20)
- ブロック [`00aadb08`](#insn-00aadb08) 範囲 `[['00aadb08', '00aadb0b']]`
  - `FALL_THROUGH` [`00aadb08`](#insn-00aadb08) → [`00aadb0c`](#insn-00aadb0c)
- ブロック [`00aadb0c`](#insn-00aadb0c) 範囲 `[['00aadb0c', '00aadb1f']]`
  - `CONDITIONAL_JUMP` [`00aadb1c`](#insn-00aadb1c) → [`00aadb0c`](#insn-00aadb0c)
  - `FALL_THROUGH` [`00aadb1c`](#insn-00aadb1c) → [`00aadb20`](#insn-00aadb20)
- ブロック [`00aadb20`](#insn-00aadb20) 範囲 `[['00aadb20', '00aadb2b']]`
  - `CONDITIONAL_JUMP` [`00aadb28`](#insn-00aadb28) → [`00aadb30`](#insn-00aadb30)
  - `FALL_THROUGH` [`00aadb28`](#insn-00aadb28) → [`00aadb2c`](#insn-00aadb2c)
- ブロック [`00aadb2c`](#insn-00aadb2c) 範囲 `[['00aadb2c', '00aadb2f']]`
  - `FALL_THROUGH` [`00aadb2c`](#insn-00aadb2c) → [`00aadb30`](#insn-00aadb30)
- ブロック [`00aadb30`](#insn-00aadb30) 範囲 `[['00aadb30', '00aadb4f']]`
  - `CONDITIONAL_JUMP` [`00aadb4c`](#insn-00aadb4c) → [`00aadb94`](#insn-00aadb94)
  - `FALL_THROUGH` [`00aadb4c`](#insn-00aadb4c) → [`00aadb50`](#insn-00aadb50)
- ブロック [`00aadb50`](#insn-00aadb50) 範囲 `[['00aadb50', '00aadb5f']]`
  - `CONDITIONAL_JUMP` [`00aadb5c`](#insn-00aadb5c) → [`00aadb8c`](#insn-00aadb8c)
  - `FALL_THROUGH` [`00aadb5c`](#insn-00aadb5c) → [`00aadb60`](#insn-00aadb60)
- ブロック [`00aadb60`](#insn-00aadb60) 範囲 `[['00aadb60', '00aadb67']]`
  - `UNCONDITIONAL_JUMP` [`00aadb64`](#insn-00aadb64) → [`00aadb74`](#insn-00aadb74)
- ブロック [`00aadb68`](#insn-00aadb68) 範囲 `[['00aadb68', '00aadb73']]`
  - `CONDITIONAL_JUMP` [`00aadb70`](#insn-00aadb70) → [`00aadb88`](#insn-00aadb88)
  - `FALL_THROUGH` [`00aadb70`](#insn-00aadb70) → [`00aadb74`](#insn-00aadb74)
- ブロック [`00aadb74`](#insn-00aadb74) 範囲 `[['00aadb74', '00aadb7b']]`
  - `CONDITIONAL_JUMP` [`00aadb78`](#insn-00aadb78) → [`00aadb68`](#insn-00aadb68)
  - `FALL_THROUGH` [`00aadb78`](#insn-00aadb78) → [`00aadb7c`](#insn-00aadb7c)
- ブロック [`00aadb7c`](#insn-00aadb7c) 範囲 `[['00aadb7c', '00aadb87']]`
  - `UNCONDITIONAL_JUMP` [`00aadb84`](#insn-00aadb84) → [`00aadb68`](#insn-00aadb68)
- ブロック [`00aadb88`](#insn-00aadb88) 範囲 `[['00aadb88', '00aadb8b']]`
  - `FALL_THROUGH` [`00aadb88`](#insn-00aadb88) → [`00aadb8c`](#insn-00aadb8c)
- ブロック [`00aadb8c`](#insn-00aadb8c) 範囲 `[['00aadb8c', '00aadb93']]`
  - `FALL_THROUGH` [`00aadb90`](#insn-00aadb90) → [`00aadb94`](#insn-00aadb94)
- ブロック [`00aadb94`](#insn-00aadb94) 範囲 `[['00aadb94', '00aadbaf']]`

## 命令位置別の参照

- [`00aadadc`](#insn-00aadadc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadae0`](#insn-00aadae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadae4`](#insn-00aadae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadaf4`](#insn-00aadaf4) → [`00aadb08`](#insn-00aadb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb00`](#insn-00aadb00) → [`00aadaf8`](#insn-00aadaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb04`](#insn-00aadb04) → [`00aadb20`](#insn-00aadb20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb1c`](#insn-00aadb1c) → [`00aadb0c`](#insn-00aadb0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb28`](#insn-00aadb28) → [`00aadb30`](#insn-00aadb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb44`](#insn-00aadb44) → [`00471738`](../00471/00471738.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00471738` · 推定シンボル `None` · 推定型 `None`
- [`00aadb4c`](#insn-00aadb4c) → [`00aadb94`](#insn-00aadb94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb5c`](#insn-00aadb5c) → [`00aadb8c`](#insn-00aadb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb64`](#insn-00aadb64) → [`00aadb74`](#insn-00aadb74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb70`](#insn-00aadb70) → [`00aadb88`](#insn-00aadb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb78`](#insn-00aadb78) → [`00aadb68`](#insn-00aadb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb80`](#insn-00aadb80) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aadb84`](#insn-00aadb84) → [`00aadb68`](#insn-00aadb68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb90`](#insn-00aadb90) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aadb98`](#insn-00aadb98) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aadba0`](#insn-00aadba0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadba4`](#insn-00aadba4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadba8`](#insn-00aadba8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadadc`](#insn-00aadadc)

~~~json
{
  "source": "00aadadc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadae0`](#insn-00aadae0)

~~~json
{
  "source": "00aadae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadae4`](#insn-00aadae4)

~~~json
{
  "source": "00aadae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadaf4`](#insn-00aadaf4)

~~~json
{
  "source": "00aadaf4",
  "target": "00aadb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb00`](#insn-00aadb00)

~~~json
{
  "source": "00aadb00",
  "target": "00aadaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb04`](#insn-00aadb04)

~~~json
{
  "source": "00aadb04",
  "target": "00aadb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb1c`](#insn-00aadb1c)

~~~json
{
  "source": "00aadb1c",
  "target": "00aadb0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb28`](#insn-00aadb28)

~~~json
{
  "source": "00aadb28",
  "target": "00aadb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb44`](#insn-00aadb44)

~~~json
{
  "source": "00aadb44",
  "target": "00471738",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadb4c`](#insn-00aadb4c)

~~~json
{
  "source": "00aadb4c",
  "target": "00aadb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb5c`](#insn-00aadb5c)

~~~json
{
  "source": "00aadb5c",
  "target": "00aadb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb64`](#insn-00aadb64)

~~~json
{
  "source": "00aadb64",
  "target": "00aadb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb70`](#insn-00aadb70)

~~~json
{
  "source": "00aadb70",
  "target": "00aadb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb78`](#insn-00aadb78)

~~~json
{
  "source": "00aadb78",
  "target": "00aadb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb80`](#insn-00aadb80)

~~~json
{
  "source": "00aadb80",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadb84`](#insn-00aadb84)

~~~json
{
  "source": "00aadb84",
  "target": "00aadb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb90`](#insn-00aadb90)

~~~json
{
  "source": "00aadb90",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadb98`](#insn-00aadb98)

~~~json
{
  "source": "00aadb98",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadba0`](#insn-00aadba0)

~~~json
{
  "source": "00aadba0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadba4`](#insn-00aadba4)

~~~json
{
  "source": "00aadba4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadba8`](#insn-00aadba8)

~~~json
{
  "source": "00aadba8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
