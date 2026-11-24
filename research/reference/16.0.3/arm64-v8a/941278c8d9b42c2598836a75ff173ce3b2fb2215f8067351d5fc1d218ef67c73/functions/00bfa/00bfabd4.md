# 00bfabd4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf9be0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9be0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-60a43e82cfcb92ca0a2f8d9585f94cfb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfabd4",
  "name": "_ZNSt6__ndk117__assoc_sub_state9__executeEv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6a9b415ef6486db342ec3e761cc70355b66b35192c45ff9dda0372402ef66c8d",
  "source_text_sha256": "6a9b415ef6486db342ec3e761cc70355b66b35192c45ff9dda0372402ef66c8d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfabd4",
        "00bfabe7"
      ]
    ],
    "bytes_sha256": "b6cfd93dee2b2950da3d680250ec0d49f83ced00f741747f3d074fbc4fbc96dc",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 143 bytes

~~~c

void _ZNSt6__ndk117__assoc_sub_state9__executeEv(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_0045aa34(3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfabd4"></a> `00bfabd4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfabd8"></a> `00bfabd8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfabdc"></a> `00bfabdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfabe0"></a> `00bfabe0` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00bfabe4"></a> `00bfabe4` | `94 7f e1 97` | bl 0x0045aa34 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfabd4`](#insn-00bfabd4) 範囲 `[['00bfabd4', '00bfabe7']]`

## 命令位置別の参照

- [`00bfabd8`](#insn-00bfabd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabe4`](#insn-00bfabe4) → [`0045aa34`](../0045a/0045aa34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045aa34` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfabd8`](#insn-00bfabd8)

~~~json
{
  "source": "00bfabd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabe4`](#insn-00bfabe4)

~~~json
{
  "source": "00bfabe4",
  "target": "0045aa34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
