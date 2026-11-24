# 00aeebd0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aeeb34`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeb34.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-7839b2623048cc0a5ebb54cbfb378bd7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aefbc4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefbc4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-2fd9276f0a604d1538f621c33361e8c6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeebd0",
  "name": "FUN_00aeebd0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "66e089b0e4bcc3d3f71d12def452fb47400d95ff55cae08b73572e11abb30880",
  "source_text_sha256": "66e089b0e4bcc3d3f71d12def452fb47400d95ff55cae08b73572e11abb30880",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeebd0",
        "00aeec0f"
      ]
    ],
    "bytes_sha256": "74cafb4f997766e4cc46489931aa49c609f563ded0c13e02f1ef587b5d32fdd1",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [008b91d0](../008b9/008b91d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 276 bytes

~~~c

void FUN_00aeebd0(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
    uVar2 = *param_2;
    uVar1 = FUN_0047ad34();
    FUN_0047ce14(uVar1,0xb,0);
    FUN_008b91d0(uVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeebd0"></a> `00aeebd0` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aeebd4"></a> `00aeebd4` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aeebd8"></a> `00aeebd8` | `a1 01 00 54` | b.ne 0x00aeec0c | `CONDITIONAL_JUMP`
<a id="insn-00aeebdc"></a> `00aeebdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeebe0"></a> `00aeebe0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeebe4"></a> `00aeebe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aeebe8"></a> `00aeebe8` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aeebec"></a> `00aeebec` | `52 30 e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00aeebf0"></a> `00aeebf0` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aeebf4"></a> `00aeebf4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeebf8"></a> `00aeebf8` | `87 38 e6 97` | bl 0x0047ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00aeebfc"></a> `00aeebfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeec00"></a> `00aeec00` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeec04"></a> `00aeec04` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeec08"></a> `00aeec08` | `72 29 f7 17` | b 0x008b91d0 | `CALL_TERMINATOR`
<a id="insn-00aeec0c"></a> `00aeec0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeebd0`](#insn-00aeebd0) 範囲 `[['00aeebd0', '00aeebdb']]`
  - `CONDITIONAL_JUMP` [`00aeebd8`](#insn-00aeebd8) → [`00aeec0c`](#insn-00aeec0c)
  - `FALL_THROUGH` [`00aeebd8`](#insn-00aeebd8) → [`00aeebdc`](#insn-00aeebdc)
- ブロック [`00aeebdc`](#insn-00aeebdc) 範囲 `[['00aeebdc', '00aeec0b']]`
- ブロック [`00aeec0c`](#insn-00aeec0c) 範囲 `[['00aeec0c', '00aeec0f']]`

## 命令位置別の参照

- [`00aeebd8`](#insn-00aeebd8) → [`00aeec0c`](#insn-00aeec0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeebdc`](#insn-00aeebdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeebe0`](#insn-00aeebe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeebec`](#insn-00aeebec) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00aeebf8`](#insn-00aeebf8) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`00aeec00`](#insn-00aeec00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec04`](#insn-00aeec04) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec08`](#insn-00aeec08) → [`008b91d0`](../008b9/008b91d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b91d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeebd8`](#insn-00aeebd8)

~~~json
{
  "source": "00aeebd8",
  "target": "00aeec0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeebdc`](#insn-00aeebdc)

~~~json
{
  "source": "00aeebdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeebe0`](#insn-00aeebe0)

~~~json
{
  "source": "00aeebe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeebec`](#insn-00aeebec)

~~~json
{
  "source": "00aeebec",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeebf8`](#insn-00aeebf8)

~~~json
{
  "source": "00aeebf8",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeec00`](#insn-00aeec00)

~~~json
{
  "source": "00aeec00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec04`](#insn-00aeec04)

~~~json
{
  "source": "00aeec04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec08`](#insn-00aeec08)

~~~json
{
  "source": "00aeec08",
  "target": "008b91d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
