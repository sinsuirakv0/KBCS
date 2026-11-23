# 00ae3fbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae4084`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4084.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0008.md#compare-97710713051ebdf7481539e3b61e6895)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae3fbc",
  "name": "_ZN8firebase11LogGetLevelEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c22c5d9902073689b2bd52018e3e9223cb35e9aa64264cd35252c1c46c91d2c0",
  "source_text_sha256": "c22c5d9902073689b2bd52018e3e9223cb35e9aa64264cd35252c1c46c91d2c0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae3fbc",
        "00ae3fcb"
      ]
    ],
    "bytes_sha256": "38b900a7fcb24af883ca6d6f0ea12c474b4455695abdbd4d49cf65dbce9eda25",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 117 bytes

~~~c

undefined4 _ZN8firebase11LogGetLevelEv(void)

{
  return *(undefined4 *)PTR__ZN8firebase11g_log_levelE_00c1b7d0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae3fbc"></a> `00ae3fbc` | `c8 09 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ae3fc0"></a> `00ae3fc0` | `08 e9 43 f9` | ldr x8,[x8, #0x7d0] | `FALL_THROUGH`
<a id="insn-00ae3fc4"></a> `00ae3fc4` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00ae3fc8"></a> `00ae3fc8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae3fbc`](#insn-00ae3fbc) 範囲 `[['00ae3fbc', '00ae3fcb']]`

## 命令位置別の参照

- [`00ae3fc0`](#insn-00ae3fc0) → `00c1b7d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ae3fc4`](#insn-00ae3fc4) → `00c24658`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase11g_log_levelE` · 推定型 `undefined4`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae3fc0`](#insn-00ae3fc0)

~~~json
{
  "source": "00ae3fc0",
  "target": "00c1b7d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b7d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ae3fc4`](#insn-00ae3fc4)

~~~json
{
  "source": "00ae3fc4",
  "target": "00c24658",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24658",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
