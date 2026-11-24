# 00bf9aac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf9a10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9a10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-8bddcb0b2f8db2f602d36a3608f0ab25)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfaaa0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfaaa0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-43f74062764d7bc20437fd90b0ee5a1a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf9aac",
  "name": "_ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5cac8a2745ea7a00e46c3c8060bca9e60be786e48a4e49c1f283941c0870eb0",
  "source_text_sha256": "e5cac8a2745ea7a00e46c3c8060bca9e60be786e48a4e49c1f283941c0870eb0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf9aac",
        "00bf9b3b"
      ]
    ],
    "bytes_sha256": "24f068e6c576bb76ebefe4a704074746f2a17148ae216576e12637b1b710e2f4",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c58570](../00c58/00c58570.md)

## 呼び出し先

- [00c581c0](../00c58/00c581c0.md)
- [00c581f0](../00c58/00c581f0.md)
- [00c58550](../00c58/00c58550.md)

## 関連文字列（未確認候補）

~~~text
"unique_lock::unlock: not locked"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1079 bytes

~~~c

void _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE
               (long *param_1,undefined8 *param_2)

{
  uint uVar1;
  byte bVar2;
  long lVar3;
  
  uVar1 = *(uint *)(param_1 + 0xe);
  if ((uVar1 >> 2 & 1) == 0) {
    if ((uVar1 >> 3 & 1) != 0) {
      bVar2 = *(byte *)(param_2 + 1);
      *(uint *)(param_1 + 0xe) = uVar1 & 0xfffffff3;
      if ((bVar2 & 1) != 0) {
        _ZNSt6__ndk15mutex6unlockEv(*param_2);
        lVar3 = *param_1;
        *(undefined1 *)(param_2 + 1) = 0;
                    /* WARNING: Could not recover jumptable at 0x00bf9b28. Too many branches */
                    /* WARNING: Treating indirect jump as call */
        (**(code **)(lVar3 + 0x18))(param_1);
        return;
      }
                    /* WARNING: Subroutine does not return */
      _ZNSt6__ndk120__throw_system_errorEiPKc(1,"unique_lock::unlock: not locked");
    }
    do {
      _ZNSt6__ndk118condition_variable4waitERNS_11unique_lockINS_5mutexEEE(param_1 + 8,param_2);
    } while ((*(byte *)(param_1 + 0xe) >> 2 & 1) == 0);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf9aac"></a> `00bf9aac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf9ab0"></a> `00bf9ab0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bf9ab4"></a> `00bf9ab4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9ab8"></a> `00bf9ab8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf9abc"></a> `00bf9abc` | `08 70 40 b9` | ldr w8,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00bf9ac0"></a> `00bf9ac0` | `28 01 10 37` | tbnz w8,#0x2,0x00bf9ae4 | `CONDITIONAL_JUMP`
<a id="insn-00bf9ac4"></a> `00bf9ac4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf9ac8"></a> `00bf9ac8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bf9acc"></a> `00bf9acc` | `48 01 18 37` | tbnz w8,#0x3,0x00bf9af4 | `CONDITIONAL_JUMP`
<a id="insn-00bf9ad0"></a> `00bf9ad0` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00bf9ad4"></a> `00bf9ad4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bf9ad8"></a> `00bf9ad8` | `9e 7a 01 94` | bl 0x00c58550 | `UNCONDITIONAL_CALL`
<a id="insn-00bf9adc"></a> `00bf9adc` | `68 c2 41 39` | ldrb w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bf9ae0"></a> `00bf9ae0` | `88 ff 17 36` | tbz w8,#0x2,0x00bf9ad0 | `CONDITIONAL_JUMP`
<a id="insn-00bf9ae4"></a> `00bf9ae4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9ae8"></a> `00bf9ae8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bf9aec"></a> `00bf9aec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf9af0"></a> `00bf9af0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf9af4"></a> `00bf9af4` | `89 22 40 39` | ldrb w9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bf9af8"></a> `00bf9af8` | `08 75 1c 12` | and w8,w8,#0xfffffff3 | `FALL_THROUGH`
<a id="insn-00bf9afc"></a> `00bf9afc` | `68 72 00 b9` | str w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bf9b00"></a> `00bf9b00` | `69 01 00 36` | tbz w9,#0x0,0x00bf9b2c | `CONDITIONAL_JUMP`
<a id="insn-00bf9b04"></a> `00bf9b04` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-00bf9b08"></a> `00bf9b08` | `ae 79 01 94` | bl 0x00c581c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf9b0c"></a> `00bf9b0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf9b10"></a> `00bf9b10` | `9f 22 00 39` | strb wzr,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bf9b14"></a> `00bf9b14` | `10 0d 40 f9` | ldr x16,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bf9b18"></a> `00bf9b18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf9b1c"></a> `00bf9b1c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9b20"></a> `00bf9b20` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bf9b24"></a> `00bf9b24` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf9b28"></a> `00bf9b28` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bf9b2c"></a> `00bf9b2c` | `21 b6 ff b0` | adrp x1,0x2be000 | `FALL_THROUGH`
<a id="insn-00bf9b30"></a> `00bf9b30` | `21 1c 27 91` | add x1,x1,#0x9c7 | `FALL_THROUGH`
<a id="insn-00bf9b34"></a> `00bf9b34` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bf9b38"></a> `00bf9b38` | `ae 79 01 94` | bl 0x00c581f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf9aac`](#insn-00bf9aac) 範囲 `[['00bf9aac', '00bf9ac3']]`
  - `CONDITIONAL_JUMP` [`00bf9ac0`](#insn-00bf9ac0) → [`00bf9ae4`](#insn-00bf9ae4)
  - `FALL_THROUGH` [`00bf9ac0`](#insn-00bf9ac0) → [`00bf9ac4`](#insn-00bf9ac4)
- ブロック [`00bf9ac4`](#insn-00bf9ac4) 範囲 `[['00bf9ac4', '00bf9acf']]`
  - `CONDITIONAL_JUMP` [`00bf9acc`](#insn-00bf9acc) → [`00bf9af4`](#insn-00bf9af4)
  - `FALL_THROUGH` [`00bf9acc`](#insn-00bf9acc) → [`00bf9ad0`](#insn-00bf9ad0)
- ブロック [`00bf9ad0`](#insn-00bf9ad0) 範囲 `[['00bf9ad0', '00bf9ae3']]`
  - `CONDITIONAL_JUMP` [`00bf9ae0`](#insn-00bf9ae0) → [`00bf9ad0`](#insn-00bf9ad0)
  - `FALL_THROUGH` [`00bf9ae0`](#insn-00bf9ae0) → [`00bf9ae4`](#insn-00bf9ae4)
- ブロック [`00bf9ae4`](#insn-00bf9ae4) 範囲 `[['00bf9ae4', '00bf9af3']]`
- ブロック [`00bf9af4`](#insn-00bf9af4) 範囲 `[['00bf9af4', '00bf9b03']]`
  - `CONDITIONAL_JUMP` [`00bf9b00`](#insn-00bf9b00) → [`00bf9b2c`](#insn-00bf9b2c)
  - `FALL_THROUGH` [`00bf9b00`](#insn-00bf9b00) → [`00bf9b04`](#insn-00bf9b04)
- ブロック [`00bf9b04`](#insn-00bf9b04) 範囲 `[['00bf9b04', '00bf9b2b']]`
- ブロック [`00bf9b2c`](#insn-00bf9b2c) 範囲 `[['00bf9b2c', '00bf9b3b']]`

## 命令位置別の参照

- [`00bf9ab0`](#insn-00bf9ab0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9ab4`](#insn-00bf9ab4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9ac0`](#insn-00bf9ac0) → [`00bf9ae4`](#insn-00bf9ae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9acc`](#insn-00bf9acc) → [`00bf9af4`](#insn-00bf9af4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9ad8`](#insn-00bf9ad8) → [`00c58550`](../00c58/00c58550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58550` · 推定シンボル `None` · 推定型 `None`
- [`00bf9ae0`](#insn-00bf9ae0) → [`00bf9ad0`](#insn-00bf9ad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9ae4`](#insn-00bf9ae4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9ae8`](#insn-00bf9ae8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9b00`](#insn-00bf9b00) → [`00bf9b2c`](#insn-00bf9b2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9b08`](#insn-00bf9b08) → [`00c581c0`](../00c58/00c581c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581c0` · 推定シンボル `None` · 推定型 `None`
- [`00bf9b1c`](#insn-00bf9b1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9b20`](#insn-00bf9b20) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9b30`](#insn-00bf9b30) → `002be9c7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf9b38`](#insn-00bf9b38) → [`00c581f0`](../00c58/00c581f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf9ab0`](#insn-00bf9ab0)

~~~json
{
  "source": "00bf9ab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9ab4`](#insn-00bf9ab4)

~~~json
{
  "source": "00bf9ab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9ac0`](#insn-00bf9ac0)

~~~json
{
  "source": "00bf9ac0",
  "target": "00bf9ae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9acc`](#insn-00bf9acc)

~~~json
{
  "source": "00bf9acc",
  "target": "00bf9af4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9ad8`](#insn-00bf9ad8)

~~~json
{
  "source": "00bf9ad8",
  "target": "00c58550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf9ae0`](#insn-00bf9ae0)

~~~json
{
  "source": "00bf9ae0",
  "target": "00bf9ad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9ae4`](#insn-00bf9ae4)

~~~json
{
  "source": "00bf9ae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9ae8`](#insn-00bf9ae8)

~~~json
{
  "source": "00bf9ae8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9b00`](#insn-00bf9b00)

~~~json
{
  "source": "00bf9b00",
  "target": "00bf9b2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9b08`](#insn-00bf9b08)

~~~json
{
  "source": "00bf9b08",
  "target": "00c581c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf9b1c`](#insn-00bf9b1c)

~~~json
{
  "source": "00bf9b1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9b20`](#insn-00bf9b20)

~~~json
{
  "source": "00bf9b20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9b30`](#insn-00bf9b30)

~~~json
{
  "source": "00bf9b30",
  "target": "002be9c7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be9c7",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "756e697175655f6c6f636b3a3a756e6c6f636b3a206e6f74206c6f636b656400",
  "capture_start": "002be9c7",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf9b38`](#insn-00bf9b38)

~~~json
{
  "source": "00bf9b38",
  "target": "00c581f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
