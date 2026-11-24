# 00bf2fdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf1fe8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1fe8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-c0e3a5bc9d5d5a6bb863ec1c638b116c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf2fdc",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3ad2ad9d947e837a354e464be79b1e31cb85228cf5358ae89dc6923fdad6f6ba",
  "source_text_sha256": "3ad2ad9d947e837a354e464be79b1e31cb85228cf5358ae89dc6923fdad6f6ba",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf2fdc",
        "00bf301f"
      ]
    ],
    "bytes_sha256": "def3bebce0239910cecf1c1c4aae1f153025f6556c2bb23fbaea0c25b20680e8",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442c7c](../00442/00442c7c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 540 bytes

~~~c

byte * _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm
                 (byte *param_1,ulong param_2)

{
  ulong uVar1;
  byte bVar2;
  byte *pbVar3;
  
  bVar2 = *param_1;
  uVar1 = (ulong)(bVar2 >> 1);
  if ((bVar2 & 1) != 0) {
    uVar1 = *(ulong *)(param_1 + 8);
  }
  if (param_2 < uVar1) {
    pbVar3 = *(byte **)(param_1 + 0x10);
    if ((bVar2 & 1) == 0) {
      pbVar3 = param_1 + 1;
    }
    return pbVar3 + param_2;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00442c7c();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf2fdc"></a> `00bf2fdc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bf2fe0"></a> `00bf2fe0` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bf2fe4"></a> `00bf2fe4` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bf2fe8"></a> `00bf2fe8` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2fec"></a> `00bf2fec` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2ff0"></a> `00bf2ff0` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bf2ff4"></a> `00bf2ff4` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bf2ff8"></a> `00bf2ff8` | `c9 00 00 54` | b.ls 0x00bf3010 | `CONDITIONAL_JUMP`
<a id="insn-00bf2ffc"></a> `00bf2ffc` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf3000"></a> `00bf3000` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf3004"></a> `00bf3004` | `28 15 80 9a` | csinc x8,x9,x0,ne | `FALL_THROUGH`
<a id="insn-00bf3008"></a> `00bf3008` | `00 01 01 8b` | add x0,x8,x1 | `FALL_THROUGH`
<a id="insn-00bf300c"></a> `00bf300c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf3010"></a> `00bf3010` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf3014"></a> `00bf3014` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bf3018"></a> `00bf3018` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf301c"></a> `00bf301c` | `18 3f e1 97` | bl 0x00442c7c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf2fdc`](#insn-00bf2fdc) 範囲 `[['00bf2fdc', '00bf2ffb']]`
  - `CONDITIONAL_JUMP` [`00bf2ff8`](#insn-00bf2ff8) → [`00bf3010`](#insn-00bf3010)
  - `FALL_THROUGH` [`00bf2ff8`](#insn-00bf2ff8) → [`00bf2ffc`](#insn-00bf2ffc)
- ブロック [`00bf2ffc`](#insn-00bf2ffc) 範囲 `[['00bf2ffc', '00bf300f']]`
- ブロック [`00bf3010`](#insn-00bf3010) 範囲 `[['00bf3010', '00bf301f']]`

## 命令位置別の参照

- [`00bf2ff8`](#insn-00bf2ff8) → [`00bf3010`](#insn-00bf3010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf3014`](#insn-00bf3014) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf301c`](#insn-00bf301c) → [`00442c7c`](../00442/00442c7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442c7c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf2ff8`](#insn-00bf2ff8)

~~~json
{
  "source": "00bf2ff8",
  "target": "00bf3010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf3014`](#insn-00bf3014)

~~~json
{
  "source": "00bf3014",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf301c`](#insn-00bf301c)

~~~json
{
  "source": "00bf301c",
  "target": "00442c7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
