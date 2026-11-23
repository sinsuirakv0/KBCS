# 00bdddf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddea0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-3301a2380ed39c108a3fb701bdcd15c8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddf0",
  "name": "_ZN8firebase10FutureBaseaSERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "38d3e939a9ca21bb749b2e513ea39ec735a94fe39064b09e9f77d842b3e15bff",
  "source_text_sha256": "38d3e939a9ca21bb749b2e513ea39ec735a94fe39064b09e9f77d842b3e15bff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddf0",
        "00bdddff"
      ]
    ],
    "bytes_sha256": "4e6b19e5d364e7a4f3863f30c6240fb063cfed452d038afb83a01e080cbaa97e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae2d54](../00ae2/00ae2d54.md)
- [00ae3190](../00ae3/00ae3190.md)
- [00b00570](../00b00/00b00570.md)
- [00b01454](../00b01/00b01454.md)
- [00b017e4](../00b01/00b017e4.md)
- [00b0e08c](../00b0e/00b0e08c.md)
- [00b4b6e8](../00b4b/00b4b6e8.md)
- [00b4d608](../00b4d/00b4d608.md)
- [00b4dbac](../00b4d/00b4dbac.md)
- [00b4e2a0](../00b4e/00b4e2a0.md)
- [00b4e6f8](../00b4e/00b4e6f8.md)
- [00b56684](../00b56/00b56684.md)
- [00b569b0](../00b56/00b569b0.md)
- [00b56cdc](../00b56/00b56cdc.md)
- [00b57004](../00b57/00b57004.md)
- [00b57f6c](../00b57/00b57f6c.md)
- [00b583c0](../00b58/00b583c0.md)
- [00b5bf70](../00b5b/00b5bf70.md)
- [00b5c000](../00b5c/00b5c000.md)
- [00b5c090](../00b5c/00b5c090.md)
- [00b5c120](../00b5c/00b5c120.md)
- [00b5c1b0](../00b5c/00b5c1b0.md)
- [00b5c240](../00b5c/00b5c240.md)
- [00b5c2d0](../00b5c/00b5c2d0.md)
- [00b6ab00](../00b6a/00b6ab00.md)
- [00b71ea4](../00b71/00b71ea4.md)
- [00b71f34](../00b71/00b71f34.md)
- [00b71fc4](../00b71/00b71fc4.md)
- [00b72054](../00b72/00b72054.md)
- [00b720e4](../00b72/00b720e4.md)
- [00b72174](../00b72/00b72174.md)
- [00b72204](../00b72/00b72204.md)
- [00b72294](../00b72/00b72294.md)
- [00b72324](../00b72/00b72324.md)
- [00b723b4](../00b72/00b723b4.md)
- [00b72444](../00b72/00b72444.md)
- [00b724d4](../00b72/00b724d4.md)
- [00b72564](../00b72/00b72564.md)

## 呼び出し先

- [00ae37cc](../00ae3/00ae37cc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZN8firebase10FutureBaseaSERKS0_(void)

{
  (*(code *)PTR__ZN8firebase10FutureBaseaSERKS0__00c1d730)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddf0"></a> `00bdddf0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdddf4"></a> `00bdddf4` | `11 9a 43 f9` | ldr x17,[x16, #0x730] | `FALL_THROUGH`
<a id="insn-00bdddf8"></a> `00bdddf8` | `10 c2 1c 91` | add x16,x16,#0x730 | `FALL_THROUGH`
<a id="insn-00bdddfc"></a> `00bdddfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddf0`](#insn-00bdddf0) 範囲 `[['00bdddf0', '00bdddff']]`

## 命令位置別の参照

- [`00bdddf4`](#insn-00bdddf4) → `00c1d730`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddfc`](#insn-00bdddfc) → [`00ae37cc`](../00ae3/00ae37cc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae37cc` · 推定シンボル `_ZN8firebase10FutureBaseaSERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddf4`](#insn-00bdddf4)

~~~json
{
  "source": "00bdddf4",
  "target": "00c1d730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d730",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddfc`](#insn-00bdddfc)

~~~json
{
  "source": "00bdddfc",
  "target": "00ae37cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
