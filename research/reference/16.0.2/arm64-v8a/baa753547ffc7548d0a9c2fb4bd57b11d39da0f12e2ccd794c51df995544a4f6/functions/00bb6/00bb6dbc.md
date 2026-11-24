# 00bb6dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb6d20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6d20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0009.md#compare-7e20f9985ec6fbb4483f133e30175a51)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb7db0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7db0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-7f52fd7e5f292dc307137b467d99a986)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb6dbc",
  "name": "_ZN8firebase9messaging16PollableListenerC2Ev",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8671ffee3722dd7f2b13eb49dcac3ea5b81e9a2e701563500db93948506967c5",
  "source_text_sha256": "8671ffee3722dd7f2b13eb49dcac3ea5b81e9a2e701563500db93948506967c5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb6dbc",
        "00bb6e2b"
      ]
    ],
    "bytes_sha256": "be8aece06c2739e850975dc2872be02b747898f70f705d52036e8ae3fe4bafef",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c5ad50](../00c5a/00c5ad50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 829 bytes

~~~c

void _ZN8firebase9messaging16PollableListenerC2Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVN8firebase9messaging16PollableListenerE_00c9b9d0 + 0x10);
  lVar1 = _Znwm(0xa0);
  _ZN8firebase5MutexC1ENS0_4ModeE(lVar1,1);
  *(undefined8 *)(lVar1 + 0x98) = 0;
  *(undefined8 *)(lVar1 + 0x90) = 0;
  *(undefined8 *)(lVar1 + 0x88) = 0;
  *(undefined8 *)(lVar1 + 0x80) = 0;
  *(undefined8 *)(lVar1 + 0x78) = 0;
  *(undefined8 *)(lVar1 + 0x70) = 0;
  *(undefined8 *)(lVar1 + 0x68) = 0;
  *(undefined8 *)(lVar1 + 0x60) = 0;
  *(undefined8 *)(lVar1 + 0x58) = 0;
  *(undefined8 *)(lVar1 + 0x50) = 0;
  *(undefined8 *)(lVar1 + 0x48) = 0;
  *(undefined8 *)(lVar1 + 0x40) = 0;
  *(undefined8 *)(lVar1 + 0x38) = 0;
  *(undefined8 *)(lVar1 + 0x30) = 0;
  *(undefined8 *)(lVar1 + 0x28) = 0;
  param_1[1] = lVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb6dbc"></a> `00bb6dbc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bb6dc0"></a> `00bb6dc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6dc4"></a> `00bb6dc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb6dc8"></a> `00bb6dc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bb6dcc"></a> `00bb6dcc` | `28 07 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bb6dd0"></a> `00bb6dd0` | `08 e9 44 f9` | ldr x8,[x8, #0x9d0] | `FALL_THROUGH`
<a id="insn-00bb6dd4"></a> `00bb6dd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb6dd8"></a> `00bb6dd8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bb6ddc"></a> `00bb6ddc` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bb6de0"></a> `00bb6de0` | `00 14 80 52` | mov w0,#0xa0 | `FALL_THROUGH`
<a id="insn-00bb6de4"></a> `00bb6de4` | `5f 84 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6de8"></a> `00bb6de8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bb6dec"></a> `00bb6dec` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6df0"></a> `00bb6df0` | `d8 8f 02 94` | bl 0x00c5ad50 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6df4"></a> `00bb6df4` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bb6df8"></a> `00bb6df8` | `9f 4e 00 f9` | str xzr,[x20, #0x98] | `FALL_THROUGH`
<a id="insn-00bb6dfc"></a> `00bb6dfc` | `80 82 88 3c` | stur q0,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00bb6e00"></a> `00bb6e00` | `80 82 87 3c` | stur q0,[x20, #0x78] | `FALL_THROUGH`
<a id="insn-00bb6e04"></a> `00bb6e04` | `80 82 86 3c` | stur q0,[x20, #0x68] | `FALL_THROUGH`
<a id="insn-00bb6e08"></a> `00bb6e08` | `80 82 85 3c` | stur q0,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00bb6e0c"></a> `00bb6e0c` | `80 82 84 3c` | stur q0,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bb6e10"></a> `00bb6e10` | `80 82 83 3c` | stur q0,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bb6e14"></a> `00bb6e14` | `80 82 82 3c` | stur q0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bb6e18"></a> `00bb6e18` | `74 06 00 f9` | str x20,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bb6e1c"></a> `00bb6e1c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb6e20"></a> `00bb6e20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6e24"></a> `00bb6e24` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bb6e28"></a> `00bb6e28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb6dbc`](#insn-00bb6dbc) 範囲 `[['00bb6dbc', '00bb6e2b']]`

## 命令位置別の参照

- [`00bb6dbc`](#insn-00bb6dbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6dc0`](#insn-00bb6dc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6dc4`](#insn-00bb6dc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6dd0`](#insn-00bb6dd0) → `00c9b9d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb6ddc`](#insn-00bb6ddc) → `00c912f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[64]`
- [`00bb6de4`](#insn-00bb6de4) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bb6df0`](#insn-00bb6df0) → [`00c5ad50`](../00c5a/00c5ad50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad50` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e1c`](#insn-00bb6e1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e20`](#insn-00bb6e20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb6dbc`](#insn-00bb6dbc)

~~~json
{
  "source": "00bb6dbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6dc0`](#insn-00bb6dc0)

~~~json
{
  "source": "00bb6dc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6dc4`](#insn-00bb6dc4)

~~~json
{
  "source": "00bb6dc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6dd0`](#insn-00bb6dd0)

~~~json
{
  "source": "00bb6dd0",
  "target": "00c9b9d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb6ddc`](#insn-00bb6ddc)

~~~json
{
  "source": "00bb6ddc",
  "target": "00c912f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c912e8",
  "offset": 16,
  "size": 64,
  "datatype": "undefined1[64]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bb6de4`](#insn-00bb6de4)

~~~json
{
  "source": "00bb6de4",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6df0`](#insn-00bb6df0)

~~~json
{
  "source": "00bb6df0",
  "target": "00c5ad50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6e1c`](#insn-00bb6e1c)

~~~json
{
  "source": "00bb6e1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e20`](#insn-00bb6e20)

~~~json
{
  "source": "00bb6e20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
