# 00bdcbc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcb70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-6f077cacdb7ab5bc763513241d990b34)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59610`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59610.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-a4712632749fac6dbc2c632ac7e0da81)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbc0",
  "name": "_ZN5BotaneqERKNS_7X509_DNES2_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd6cdf34e40421615a69fccf017a9247dc03119a2382140486def4e328f263ad",
  "source_text_sha256": "fd6cdf34e40421615a69fccf017a9247dc03119a2382140486def4e328f263ad",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbc0",
        "00bdcbcf"
      ]
    ],
    "bytes_sha256": "663ec6fd4f02ab237f08f19a81d43c7530fdeec958e610e635114330152543d5",
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
  (*(code *)PTR__ZN5BotaneqERKNS_7X509_DNES2__00c1ce98)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbc0"></a> `00bdcbc0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcbc4"></a> `00bdcbc4` | `11 4e 47 f9` | ldr x17,[x16, #0xe98] | `FALL_THROUGH`
<a id="insn-00bdcbc8"></a> `00bdcbc8` | `10 62 3a 91` | add x16,x16,#0xe98 | `FALL_THROUGH`
<a id="insn-00bdcbcc"></a> `00bdcbcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbc0`](#insn-00bdcbc0) 範囲 `[['00bdcbc0', '00bdcbcf']]`

## 命令位置別の参照

- [`00bdcbc4`](#insn-00bdcbc4) → `00c1ce98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbcc`](#insn-00bdcbcc) → [`004deb5c`](../004de/004deb5c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004deb5c` · 推定シンボル `_ZN5BotaneqERKNS_7X509_DNES2_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbc4`](#insn-00bdcbc4)

~~~json
{
  "source": "00bdcbc4",
  "target": "00c1ce98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbcc`](#insn-00bdcbcc)

~~~json
{
  "source": "00bdcbcc",
  "target": "004deb5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
