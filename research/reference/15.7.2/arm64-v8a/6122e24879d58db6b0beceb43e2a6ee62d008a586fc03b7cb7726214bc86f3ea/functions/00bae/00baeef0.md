# 00baeef0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baefb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefb8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-13f503b96f9a6f65ff90ffece5b7255a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baeef0",
  "name": "_ZNSt6__ndk18numpunctIcEC2Em",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09b384e18a6609c00cca071b8e35e0a93c16a6eb388a516e91789b0591b160d7",
  "source_text_sha256": "09b384e18a6609c00cca071b8e35e0a93c16a6eb388a516e91789b0591b160d7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baeef0",
        "00baef1b"
      ]
    ],
    "bytes_sha256": "1596e96db6ec3a37ad7b920ef03eeac907550d6dd4ecde967000e69be1565d55",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1710](../00be1/00be1710.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 316 bytes

~~~c

void _ZNSt6__ndk18numpunctIcEC2Em(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk18numpunctIcEE_00c1beb8;
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
<a id="insn-00baeef0"></a> `00baeef0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baeef4"></a> `00baeef4` | `69 03 00 b0` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00baeef8"></a> `00baeef8` | `c8 85 85 52` | mov w8,#0x2c2e | `FALL_THROUGH`
<a id="insn-00baeefc"></a> `00baeefc` | `29 5d 47 f9` | ldr x9,[x9, #0xeb8] | `FALL_THROUGH`
<a id="insn-00baef00"></a> `00baef00` | `08 20 00 79` | strh w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baef04"></a> `00baef04` | `28 04 00 d1` | sub x8,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00baef08"></a> `00baef08` | `1f 7c 02 a9` | stp xzr,xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00baef0c"></a> `00baef0c` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00baef10"></a> `00baef10` | `1f 0c 00 f9` | str xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baef14"></a> `00baef14` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00baef18"></a> `00baef18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baeef0`](#insn-00baeef0) 範囲 `[['00baeef0', '00baef1b']]`

## 命令位置別の参照

- [`00baeefc`](#insn-00baeefc) → `00c1beb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baef14`](#insn-00baef14) → `00c13a78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeefc`](#insn-00baeefc)

~~~json
{
  "source": "00baeefc",
  "target": "00c1beb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1beb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baef14`](#insn-00baef14)

~~~json
{
  "source": "00baef14",
  "target": "00c13a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13a68",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
