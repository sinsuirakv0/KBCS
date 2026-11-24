# 00bcfcd8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcf8b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-1e713da92de405a214a90e18205d0aa0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcfd74`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfd74.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-67be0d56395de774b626285b05aa89aa)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfcd8",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95902d6af978300ab699da4482c5b836442deb89fcc13f69258ba4b59a1cd8bd",
  "source_text_sha256": "95902d6af978300ab699da4482c5b836442deb89fcc13f69258ba4b59a1cd8bd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfcd8",
        "00bcfd43"
      ]
    ],
    "bytes_sha256": "8e11220ac1682e73c22f02b78e282a522468a8da01e5ee2a7d56243af537817f",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5a9f0](../00c5a/00c5a9f0.md)
- [00c5aa50](../00c5a/00c5aa50.md)
- [00c5be20](../00c5b/00c5be20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 739 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv(byte *param_1)

{
  if (param_1 != (byte *)0x0) {
    _ZN8firebase4auth4UserD2Ev(param_1 + 0x98);
    _ZN8firebase4auth10CredentialD2Ev(param_1 + 0x70);
    _ZN8firebase4auth10CredentialD2Ev(param_1 + 0x48);
    _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
              (param_1 + 0x30,*(undefined8 *)(param_1 + 0x38));
    if ((param_1[0x18] & 1) != 0) {
      _ZdlPv(*(void **)(param_1 + 0x28));
    }
    if ((*param_1 & 1) != 0) {
      _ZdlPv(*(void **)(param_1 + 0x10));
    }
    _ZdlPv(param_1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfcd8"></a> `00bcfcd8` | `40 03 00 b4` | cbz x0,0x00bcfd40 | `CONDITIONAL_JUMP`
<a id="insn-00bcfcdc"></a> `00bcfcdc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcfce0"></a> `00bcfce0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfce4"></a> `00bcfce4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfce8"></a> `00bcfce8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcfcec"></a> `00bcfcec` | `00 60 02 91` | add x0,x0,#0x98 | `FALL_THROUGH`
<a id="insn-00bcfcf0"></a> `00bcfcf0` | `58 2b 02 94` | bl 0x00c5aa50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfcf4"></a> `00bcfcf4` | `60 c2 01 91` | add x0,x19,#0x70 | `FALL_THROUGH`
<a id="insn-00bcfcf8"></a> `00bcfcf8` | `3e 2b 02 94` | bl 0x00c5a9f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfcfc"></a> `00bcfcfc` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00bcfd00"></a> `00bcfd00` | `3c 2b 02 94` | bl 0x00c5a9f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd04"></a> `00bcfd04` | `61 1e 40 f9` | ldr x1,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfd08"></a> `00bcfd08` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcfd0c"></a> `00bcfd0c` | `45 30 02 94` | bl 0x00c5be20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd10"></a> `00bcfd10` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bcfd14"></a> `00bcfd14` | `68 00 00 36` | tbz w8,#0x0,0x00bcfd20 | `CONDITIONAL_JUMP`
<a id="insn-00bcfd18"></a> `00bcfd18` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfd1c"></a> `00bcfd1c` | `65 20 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd20"></a> `00bcfd20` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bcfd24"></a> `00bcfd24` | `68 00 00 36` | tbz w8,#0x0,0x00bcfd30 | `CONDITIONAL_JUMP`
<a id="insn-00bcfd28"></a> `00bcfd28` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfd2c"></a> `00bcfd2c` | `61 20 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd30"></a> `00bcfd30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfd34"></a> `00bcfd34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfd38"></a> `00bcfd38` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcfd3c"></a> `00bcfd3c` | `5d 20 02 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00bcfd40"></a> `00bcfd40` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfcd8`](#insn-00bcfcd8) 範囲 `[['00bcfcd8', '00bcfcdb']]`
  - `CONDITIONAL_JUMP` [`00bcfcd8`](#insn-00bcfcd8) → [`00bcfd40`](#insn-00bcfd40)
  - `FALL_THROUGH` [`00bcfcd8`](#insn-00bcfcd8) → [`00bcfcdc`](#insn-00bcfcdc)
- ブロック [`00bcfcdc`](#insn-00bcfcdc) 範囲 `[['00bcfcdc', '00bcfd17']]`
  - `CONDITIONAL_JUMP` [`00bcfd14`](#insn-00bcfd14) → [`00bcfd20`](#insn-00bcfd20)
  - `FALL_THROUGH` [`00bcfd14`](#insn-00bcfd14) → [`00bcfd18`](#insn-00bcfd18)
- ブロック [`00bcfd18`](#insn-00bcfd18) 範囲 `[['00bcfd18', '00bcfd1f']]`
  - `FALL_THROUGH` [`00bcfd1c`](#insn-00bcfd1c) → [`00bcfd20`](#insn-00bcfd20)
- ブロック [`00bcfd20`](#insn-00bcfd20) 範囲 `[['00bcfd20', '00bcfd27']]`
  - `CONDITIONAL_JUMP` [`00bcfd24`](#insn-00bcfd24) → [`00bcfd30`](#insn-00bcfd30)
  - `FALL_THROUGH` [`00bcfd24`](#insn-00bcfd24) → [`00bcfd28`](#insn-00bcfd28)
- ブロック [`00bcfd28`](#insn-00bcfd28) 範囲 `[['00bcfd28', '00bcfd2f']]`
  - `FALL_THROUGH` [`00bcfd2c`](#insn-00bcfd2c) → [`00bcfd30`](#insn-00bcfd30)
- ブロック [`00bcfd30`](#insn-00bcfd30) 範囲 `[['00bcfd30', '00bcfd3f']]`
- ブロック [`00bcfd40`](#insn-00bcfd40) 範囲 `[['00bcfd40', '00bcfd43']]`

## 命令位置別の参照

- [`00bcfcd8`](#insn-00bcfcd8) → [`00bcfd40`](#insn-00bcfd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcdc`](#insn-00bcfcdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfce0`](#insn-00bcfce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcf0`](#insn-00bcfcf0) → [`00c5aa50`](../00c5a/00c5aa50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa50` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcf8`](#insn-00bcfcf8) → [`00c5a9f0`](../00c5a/00c5a9f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a9f0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd00`](#insn-00bcfd00) → [`00c5a9f0`](../00c5a/00c5a9f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a9f0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd0c`](#insn-00bcfd0c) → [`00c5be20`](../00c5b/00c5be20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be20` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd14`](#insn-00bcfd14) → [`00bcfd20`](#insn-00bcfd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd1c`](#insn-00bcfd1c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd24`](#insn-00bcfd24) → [`00bcfd30`](#insn-00bcfd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd2c`](#insn-00bcfd2c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd30`](#insn-00bcfd30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd3c`](#insn-00bcfd3c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfcd8`](#insn-00bcfcd8)

~~~json
{
  "source": "00bcfcd8",
  "target": "00bcfd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcdc`](#insn-00bcfcdc)

~~~json
{
  "source": "00bcfcdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfce0`](#insn-00bcfce0)

~~~json
{
  "source": "00bcfce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcf0`](#insn-00bcfcf0)

~~~json
{
  "source": "00bcfcf0",
  "target": "00c5aa50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfcf8`](#insn-00bcfcf8)

~~~json
{
  "source": "00bcfcf8",
  "target": "00c5a9f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd00`](#insn-00bcfd00)

~~~json
{
  "source": "00bcfd00",
  "target": "00c5a9f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd0c`](#insn-00bcfd0c)

~~~json
{
  "source": "00bcfd0c",
  "target": "00c5be20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd14`](#insn-00bcfd14)

~~~json
{
  "source": "00bcfd14",
  "target": "00bcfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd1c`](#insn-00bcfd1c)

~~~json
{
  "source": "00bcfd1c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd24`](#insn-00bcfd24)

~~~json
{
  "source": "00bcfd24",
  "target": "00bcfd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd2c`](#insn-00bcfd2c)

~~~json
{
  "source": "00bcfd2c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd30`](#insn-00bcfd30)

~~~json
{
  "source": "00bcfd30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd3c`](#insn-00bcfd3c)

~~~json
{
  "source": "00bcfd3c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
