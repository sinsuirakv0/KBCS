# 00bd4efc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bd4e34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4e34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-34c91ebcab3f5ef70ccb87e605c4a4eb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bd4f40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0019.md#compare-18c392e10fcae497982b888156d525a5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd4efc",
  "name": "_ZnwmSt11align_val_tRKSt9nothrow_t",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8d4e7301e9c88401d8a65b607cf522202632400493ae7804a7408133ae60a60",
  "source_text_sha256": "c8d4e7301e9c88401d8a65b607cf522202632400493ae7804a7408133ae60a60",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd4efc",
        "00bd4f17"
      ]
    ],
    "bytes_sha256": "b4c886e4c163f4fdf2ac2c08a389c663e0c29904c7f8c7fea25218f78a05c34f",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1eb0](../00be1/00be1eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 89 bytes

~~~c

void _ZnwmSt11align_val_tRKSt9nothrow_t(void)

{
  _ZnwmSt11align_val_t();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd4efc"></a> `00bd4efc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd4f00"></a> `00bd4f00` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bd4f04"></a> `00bd4f04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd4f08"></a> `00bd4f08` | `ea 33 00 94` | bl 0x00be1eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd4f0c"></a> `00bd4f0c` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bd4f10"></a> `00bd4f10` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd4f14"></a> `00bd4f14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd4efc`](#insn-00bd4efc) 範囲 `[['00bd4efc', '00bd4f17']]`

## 命令位置別の参照

- [`00bd4f00`](#insn-00bd4f00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f08`](#insn-00bd4f08) → [`00be1eb0`](../00be1/00be1eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f0c`](#insn-00bd4f0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd4f00`](#insn-00bd4f00)

~~~json
{
  "source": "00bd4f00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4f08`](#insn-00bd4f08)

~~~json
{
  "source": "00bd4f08",
  "target": "00be1eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4f0c`](#insn-00bd4f0c)

~~~json
{
  "source": "00bd4f0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
