# 00bfb1ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfa1f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-e0c9ec7e4c79bb22d3d33fac40d8b0fc)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb1ec",
  "name": "_ZNSt6__ndk15mutex8try_lockEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28c84b37fcdb121278cca28c03496ef0e38461d2bd1f4c6f61aca3bffb58de6a",
  "source_text_sha256": "28c84b37fcdb121278cca28c03496ef0e38461d2bd1f4c6f61aca3bffb58de6a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb1ec",
        "00bfb20f"
      ]
    ],
    "bytes_sha256": "ef5c327fc1881a9d742cfc2a4312c709c5f0c0ed0d056bb928eeb31c9d9b0ea6",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5f310](../00c5f/00c5f310.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 147 bytes

~~~c

bool _ZNSt6__ndk15mutex8try_lockEv(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_trylock(param_1);
  return iVar1 == 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb1ec"></a> `00bfb1ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb1f0"></a> `00bfb1f0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfb1f4"></a> `00bfb1f4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb1f8"></a> `00bfb1f8` | `46 90 01 94` | bl 0x00c5f310 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb1fc"></a> `00bfb1fc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bfb200"></a> `00bfb200` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bfb204"></a> `00bfb204` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bfb208"></a> `00bfb208` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb20c"></a> `00bfb20c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfb1ec`](#insn-00bfb1ec) 範囲 `[['00bfb1ec', '00bfb20f']]`

## 命令位置別の参照

- [`00bfb1f0`](#insn-00bfb1f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb1f8`](#insn-00bfb1f8) → [`00c5f310`](../00c5f/00c5f310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f310` · 推定シンボル `None` · 推定型 `None`
- [`00bfb204`](#insn-00bfb204) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb1f0`](#insn-00bfb1f0)

~~~json
{
  "source": "00bfb1f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb1f8`](#insn-00bfb1f8)

~~~json
{
  "source": "00bfb1f8",
  "target": "00c5f310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb204`](#insn-00bfb204)

~~~json
{
  "source": "00bfb204",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
