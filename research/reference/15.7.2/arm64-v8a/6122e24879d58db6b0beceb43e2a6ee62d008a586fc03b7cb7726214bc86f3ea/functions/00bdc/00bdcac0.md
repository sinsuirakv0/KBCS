# 00bdcac0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcb70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-518fc9c268cb60d4e642ab4f8f686224)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcac0",
  "name": "_ZN5BotaneqERKNS_7X509_DNES2_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c360301468064c80d9fff0aa0764f3a46b41fb9f2112e926ca99536f38975a6",
  "source_text_sha256": "2c360301468064c80d9fff0aa0764f3a46b41fb9f2112e926ca99536f38975a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcac0",
        "00bdcacf"
      ]
    ],
    "bytes_sha256": "e4d8748094911b72cd0548f247f5a7a949ab49f1a931bbc0ff15474325ddf7ce",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004de9a8](../004de/004de9a8.md)
- [004ded14](../004de/004ded14.md)
- [004df724](../004df/004df724.md)
- [004dfa64](../004df/004dfa64.md)
- [004e66d0](../004e6/004e66d0.md)
- [004e68c8](../004e6/004e68c8.md)
- [004e8a14](../004e8/004e8a14.md)
- [004f00b0](../004f0/004f00b0.md)
- [004fdfd8](../004fd/004fdfd8.md)
- [00503af8](../00503/00503af8.md)

## 呼び出し先

- [004deb5c](../004de/004deb5c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 117 bytes

~~~c

void _ZN5BotaneqERKNS_7X509_DNES2_(void)

{
  (*(code *)PTR__ZN5BotaneqERKNS_7X509_DNES2__00c1cd98)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcac0"></a> `00bdcac0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcac4"></a> `00bdcac4` | `11 ce 46 f9` | ldr x17,[x16, #0xd98] | `FALL_THROUGH`
<a id="insn-00bdcac8"></a> `00bdcac8` | `10 62 36 91` | add x16,x16,#0xd98 | `FALL_THROUGH`
<a id="insn-00bdcacc"></a> `00bdcacc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcac0`](#insn-00bdcac0) 範囲 `[['00bdcac0', '00bdcacf']]`

## 命令位置別の参照

- [`00bdcac4`](#insn-00bdcac4) → `00c1cd98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcacc`](#insn-00bdcacc) → [`004deb5c`](../004de/004deb5c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004deb5c` · 推定シンボル `_ZN5BotaneqERKNS_7X509_DNES2_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcac4`](#insn-00bdcac4)

~~~json
{
  "source": "00bdcac4",
  "target": "00c1cd98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cd98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcacc`](#insn-00bdcacc)

~~~json
{
  "source": "00bdcacc",
  "target": "004deb5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
