# 00acf8cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acf804`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf804.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-974abce9a1344e1ced6bd465efebc3fb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acf910`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf910.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-bdb0ae57dce34b8263b4ad5832435c2e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acf8cc",
  "name": "FUN_00acf8cc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "61796864e70a63628a6cf55c3b7ddf5559f4e0bc6258f5e99a12260b198a32e9",
  "source_text_sha256": "61796864e70a63628a6cf55c3b7ddf5559f4e0bc6258f5e99a12260b198a32e9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acf8cc",
        "00acf8ef"
      ]
    ],
    "bytes_sha256": "d3fa8716cd060f35253f630977a19cac7b094b16f205bd00bf674317090bad10",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005e53dc](../005e5/005e53dc.md)
- [0063e818](../0063e/0063e818.md)
- [0063e8b4](../0063e/0063e8b4.md)
- [0063ea04](../0063e/0063ea04.md)
- [006e34b0](../006e3/006e34b0.md)
- [006fd890](../006fd/006fd890.md)
- [00733374](../00733/00733374.md)
- [0073a8e0](../0073a/0073a8e0.md)
- [008e0bc0](../008e0/008e0bc0.md)
- [008e68f8](../008e6/008e68f8.md)
- [0092bc08](../0092b/0092bc08.md)
- [00934148](../00934/00934148.md)
- [00947d70](../00947/00947d70.md)
- [0094847c](../00948/0094847c.md)
- [00965df0](../00965/00965df0.md)
- [00999d28](../00999/00999d28.md)
- [009f4a74](../009f4/009f4a74.md)
- [00a82394](../00a82/00a82394.md)

## 呼び出し先

- [00adc050](../00adc/00adc050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 140 bytes

~~~c

ushort FUN_00acf8cc(void)

{
  ushort uVar1;
  
  uVar1 = FUN_00adc050();
  if (49999 < uVar1) {
    uVar1 = 50000;
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acf8cc"></a> `00acf8cc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00acf8d0"></a> `00acf8d0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acf8d4"></a> `00acf8d4` | `df 31 00 94` | bl 0x00adc050 | `UNCONDITIONAL_CALL`
<a id="insn-00acf8d8"></a> `00acf8d8` | `08 6a 98 52` | mov w8,#0xc350 | `FALL_THROUGH`
<a id="insn-00acf8dc"></a> `00acf8dc` | `09 3c 00 12` | and w9,w0,#0xffff | `FALL_THROUGH`
<a id="insn-00acf8e0"></a> `00acf8e0` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00acf8e4"></a> `00acf8e4` | `20 31 88 1a` | csel w0,w9,w8,cc | `FALL_THROUGH`
<a id="insn-00acf8e8"></a> `00acf8e8` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00acf8ec"></a> `00acf8ec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acf8cc`](#insn-00acf8cc) 範囲 `[['00acf8cc', '00acf8ef']]`

## 命令位置別の参照

- [`00acf8cc`](#insn-00acf8cc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf8d4`](#insn-00acf8d4) → [`00adc050`](../00adc/00adc050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adc050` · 推定シンボル `None` · 推定型 `None`
- [`00acf8e8`](#insn-00acf8e8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acf8cc`](#insn-00acf8cc)

~~~json
{
  "source": "00acf8cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf8d4`](#insn-00acf8d4)

~~~json
{
  "source": "00acf8d4",
  "target": "00adc050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf8e8`](#insn-00acf8e8)

~~~json
{
  "source": "00acf8e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
