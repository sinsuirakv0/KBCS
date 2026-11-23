# 00b7dddc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7dea4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dea4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0004.md#compare-6aadf55b8fc9a4b4e61480b0323de9ad)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7dddc",
  "name": "_ZNSt6__ndk113random_deviceD2Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e62a244198d58329791df076882efe4b1e9a2d4fd9d89499753a099b8e5417e2",
  "source_text_sha256": "e62a244198d58329791df076882efe4b1e9a2d4fd9d89499753a099b8e5417e2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7dddc",
        "00b7ddfb"
      ]
    ],
    "bytes_sha256": "9c7bb2dbfe0f5b5f75f180b552fc0175e2ee9b563f89fec7f0eff98396c7d477",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdb480](../00bdb/00bdb480.md)

## 呼び出し先

- [00bdc880](../00bdc/00bdc880.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 116 bytes

~~~c

int _ZNSt6__ndk113random_deviceD2Ev(int *param_1)

{
  int iVar1;
  
  iVar1 = close(*param_1);
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7dddc"></a> `00b7dddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7dde0"></a> `00b7dde0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00b7dde4"></a> `00b7dde4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b7dde8"></a> `00b7dde8` | `00 00 40 b9` | ldr w0,[x0] | `FALL_THROUGH`
<a id="insn-00b7ddec"></a> `00b7ddec` | `a5 7a 01 94` | bl 0x00bdc880 | `UNCONDITIONAL_CALL`
<a id="insn-00b7ddf0"></a> `00b7ddf0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00b7ddf4"></a> `00b7ddf4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7ddf8"></a> `00b7ddf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7dddc`](#insn-00b7dddc) 範囲 `[['00b7dddc', '00b7ddfb']]`

## 命令位置別の参照

- [`00b7dde0`](#insn-00b7dde0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ddec`](#insn-00b7ddec) → [`00bdc880`](../00bdc/00bdc880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdc880` · 推定シンボル `None` · 推定型 `None`
- [`00b7ddf0`](#insn-00b7ddf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7dde0`](#insn-00b7dde0)

~~~json
{
  "source": "00b7dde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ddec`](#insn-00b7ddec)

~~~json
{
  "source": "00b7ddec",
  "target": "00bdc880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7ddf0`](#insn-00b7ddf0)

~~~json
{
  "source": "00b7ddf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
