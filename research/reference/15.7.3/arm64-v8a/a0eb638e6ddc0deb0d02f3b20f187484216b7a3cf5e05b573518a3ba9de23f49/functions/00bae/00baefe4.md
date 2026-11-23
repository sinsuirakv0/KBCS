# 00baefe4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baef1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baef1c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-14d07852d06e763fa0478f0bbe72669d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00baf028`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf028.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-a34e262436695063f9535ac47354a5b8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baefe4",
  "name": "_ZNSt6__ndk18numpunctIwEC2Em",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a9cbf042b9bcd6035f61e0017617699c16fc76875a2775e6593f0b0519c2afb",
  "source_text_sha256": "8a9cbf042b9bcd6035f61e0017617699c16fc76875a2775e6593f0b0519c2afb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baefe4",
        "00baf013"
      ]
    ],
    "bytes_sha256": "2d0b313eb544af65558439517a7e7abca10261f8fbf656170244ae890aadf5ee",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be17d0](../00be1/00be17d0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt6__ndk18numpunctIwEC2Em(long *param_1,long param_2)

{
  long lVar1;
  undefined *puVar2;
  
  puVar2 = PTR__ZTVNSt6__ndk18numpunctIwEE_00c1bf70;
  lVar1 = DAT_002b2b98;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  param_1[2] = lVar1;
  *param_1 = (long)(puVar2 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baefe4"></a> `00baefe4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baefe8"></a> `00baefe8` | `69 03 00 b0` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00baefec"></a> `00baefec` | `28 b8 ff 90` | adrp x8,0x2b2000 | `FALL_THROUGH`
<a id="insn-00baeff0"></a> `00baeff0` | `2a 04 00 d1` | sub x10,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00baeff4"></a> `00baeff4` | `29 b9 47 f9` | ldr x9,[x9, #0xf70] | `FALL_THROUGH`
<a id="insn-00baeff8"></a> `00baeff8` | `00 cd 45 fd` | ldr d0,[x8, #0xb98] | `FALL_THROUGH`
<a id="insn-00baeffc"></a> `00baeffc` | `1f 7c 02 a9` | stp xzr,xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00baf000"></a> `00baf000` | `1f 0c 00 f9` | str xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baf004"></a> `00baf004` | `28 41 00 91` | add x8,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00baf008"></a> `00baf008` | `00 08 00 fd` | str d0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baf00c"></a> `00baf00c` | `08 28 00 a9` | stp x8,x10,[x0] | `FALL_THROUGH`
<a id="insn-00baf010"></a> `00baf010` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baefe4`](#insn-00baefe4) 範囲 `[['00baefe4', '00baf013']]`

## 命令位置別の参照

- [`00baeff4`](#insn-00baeff4) → `00c1bf70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baeff8`](#insn-00baeff8) → `002b2b98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baf00c`](#insn-00baf00c) → `00c13b78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeff4`](#insn-00baeff4)

~~~json
{
  "source": "00baeff4",
  "target": "00c1bf70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baeff8`](#insn-00baeff8)

~~~json
{
  "source": "00baeff8",
  "target": "002b2b98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2b98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "2e0000002c000000",
  "capture_start": "002b2b98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baf00c`](#insn-00baf00c)

~~~json
{
  "source": "00baf00c",
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
