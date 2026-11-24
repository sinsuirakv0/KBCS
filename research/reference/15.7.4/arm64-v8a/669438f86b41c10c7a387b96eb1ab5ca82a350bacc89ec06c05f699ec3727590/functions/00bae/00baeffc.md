# 00baeffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baefb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-d3101185221a776be419fa4e7c59febb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2ba44`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba44.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-581d56e2e0f4d46dd590994e54b91c77)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baeffc",
  "name": "_ZNSt6__ndk18numpunctIcEC2Em",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4050c51bece412fd7c60ff1def9d0c32140759c11c5fe670b0e0ab81ae8ca733",
  "source_text_sha256": "4050c51bece412fd7c60ff1def9d0c32140759c11c5fe670b0e0ab81ae8ca733",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baeffc",
        "00baf027"
      ]
    ],
    "bytes_sha256": "663c633ece04b92287001f89d19ec757592d35659803eb5f27358bf8965c939e",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1810](../00be1/00be1810.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 316 bytes

~~~c

void _ZNSt6__ndk18numpunctIcEC2Em(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk18numpunctIcEE_00c1bfb8;
  *(undefined2 *)(param_1 + 2) = 0x2c2e;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baeffc"></a> `00baeffc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baf000"></a> `00baf000` | `69 03 00 90` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00baf004"></a> `00baf004` | `c8 85 85 52` | mov w8,#0x2c2e | `FALL_THROUGH`
<a id="insn-00baf008"></a> `00baf008` | `29 dd 47 f9` | ldr x9,[x9, #0xfb8] | `FALL_THROUGH`
<a id="insn-00baf00c"></a> `00baf00c` | `08 20 00 79` | strh w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baf010"></a> `00baf010` | `28 04 00 d1` | sub x8,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00baf014"></a> `00baf014` | `1f 7c 02 a9` | stp xzr,xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00baf018"></a> `00baf018` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00baf01c"></a> `00baf01c` | `1f 0c 00 f9` | str xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baf020"></a> `00baf020` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00baf024"></a> `00baf024` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baeffc`](#insn-00baeffc) 範囲 `[['00baeffc', '00baf027']]`

## 命令位置別の参照

- [`00baf008`](#insn-00baf008) → `00c1bfb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baf020`](#insn-00baf020) → `00c13b78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baf008`](#insn-00baf008)

~~~json
{
  "source": "00baf008",
  "target": "00c1bfb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bfb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baf020`](#insn-00baf020)

~~~json
{
  "source": "00baf020",
  "target": "00c13b78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13b68",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
