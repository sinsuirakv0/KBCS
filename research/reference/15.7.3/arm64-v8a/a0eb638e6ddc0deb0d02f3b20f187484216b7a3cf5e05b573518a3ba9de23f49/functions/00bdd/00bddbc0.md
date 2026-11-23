# 00bddbc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddb10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-51ed16bea83c28c56d30b2d47bc35987)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddc10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-6321d23153159030fba6a771cdbc2499)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbc0",
  "name": "_ZN8firebase4auth4User6DeleteEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bf14bc542ff76dec7b287614c1adcaf702a86aa98c5228c63c70ad1d50164776",
  "source_text_sha256": "bf14bc542ff76dec7b287614c1adcaf702a86aa98c5228c63c70ad1d50164776",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbc0",
        "00bddbcf"
      ]
    ],
    "bytes_sha256": "49e320875acc0476627e40585dc399dda5fc9207d07e81280167821aa26bfb29",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084859c](../00848/0084859c.md)

## 呼び出し先

- [00b71540](../00b71/00b71540.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 121 bytes

~~~c

void _ZN8firebase4auth4User6DeleteEv(void)

{
  (*(code *)PTR__ZN8firebase4auth4User6DeleteEv_00c1d670)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbc0"></a> `00bddbc0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddbc4"></a> `00bddbc4` | `11 3a 43 f9` | ldr x17,[x16, #0x670] | `FALL_THROUGH`
<a id="insn-00bddbc8"></a> `00bddbc8` | `10 c2 19 91` | add x16,x16,#0x670 | `FALL_THROUGH`
<a id="insn-00bddbcc"></a> `00bddbcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbc0`](#insn-00bddbc0) 範囲 `[['00bddbc0', '00bddbcf']]`

## 命令位置別の参照

- [`00bddbc4`](#insn-00bddbc4) → `00c1d670`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbcc`](#insn-00bddbcc) → [`00b71540`](../00b71/00b71540.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b71540` · 推定シンボル `_ZN8firebase4auth4User6DeleteEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbc4`](#insn-00bddbc4)

~~~json
{
  "source": "00bddbc4",
  "target": "00c1d670",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d670",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbcc`](#insn-00bddbcc)

~~~json
{
  "source": "00bddbcc",
  "target": "00b71540",
  "target_space": "ram",
  "resolution": "function"
}
~~~
