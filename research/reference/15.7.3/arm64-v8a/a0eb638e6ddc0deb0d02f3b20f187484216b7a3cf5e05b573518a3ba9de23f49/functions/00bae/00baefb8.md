# 00baefb8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baeef0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baeef0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-13f503b96f9a6f65ff90ffece5b7255a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00baeffc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baeffc.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-d3101185221a776be419fa4e7c59febb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baefb8",
  "name": "_ZNSt6__ndk18numpunctIcEC2Em",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3032ad56f224226dfbd56808b5df5a76aeea44422952bb5fda9bb32b9d0991d5",
  "source_text_sha256": "3032ad56f224226dfbd56808b5df5a76aeea44422952bb5fda9bb32b9d0991d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baefb8",
        "00baefe3"
      ]
    ],
    "bytes_sha256": "7dd7182b82c37a0b584f49c7fb7da9f802f9ea8b18f299a8ec4b27ceb7a4ec3f",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be17c0](../00be1/00be17c0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 316 bytes

~~~c

void _ZNSt6__ndk18numpunctIcEC2Em(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk18numpunctIcEE_00c1bf68;
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
<a id="insn-00baefb8"></a> `00baefb8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baefbc"></a> `00baefbc` | `69 03 00 b0` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00baefc0"></a> `00baefc0` | `c8 85 85 52` | mov w8,#0x2c2e | `FALL_THROUGH`
<a id="insn-00baefc4"></a> `00baefc4` | `29 b5 47 f9` | ldr x9,[x9, #0xf68] | `FALL_THROUGH`
<a id="insn-00baefc8"></a> `00baefc8` | `08 20 00 79` | strh w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baefcc"></a> `00baefcc` | `28 04 00 d1` | sub x8,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00baefd0"></a> `00baefd0` | `1f 7c 02 a9` | stp xzr,xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00baefd4"></a> `00baefd4` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00baefd8"></a> `00baefd8` | `1f 0c 00 f9` | str xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baefdc"></a> `00baefdc` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00baefe0"></a> `00baefe0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baefb8`](#insn-00baefb8) 範囲 `[['00baefb8', '00baefe3']]`

## 命令位置別の参照

- [`00baefc4`](#insn-00baefc4) → `00c1bf68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baefdc`](#insn-00baefdc) → `00c13b28`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baefc4`](#insn-00baefc4)

~~~json
{
  "source": "00baefc4",
  "target": "00c1bf68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baefdc`](#insn-00baefdc)

~~~json
{
  "source": "00baefdc",
  "target": "00c13b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13b18",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
