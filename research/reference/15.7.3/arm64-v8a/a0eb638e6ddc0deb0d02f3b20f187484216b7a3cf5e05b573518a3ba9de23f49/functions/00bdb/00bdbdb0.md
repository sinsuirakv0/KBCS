# 00bdbdb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbd00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbd00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-e10aabc9e226efc1038e8b78d23d37b5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbe00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-5bb50ea9c98bfec72b7ed513f074e61c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdb0",
  "name": "_ZN5BotanmlERKNS_6BigIntES2_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f6dc6896eaf03d42ae53b8bc011952256d7c1fdb8051118e31f88ed887d3d33",
  "source_text_sha256": "9f6dc6896eaf03d42ae53b8bc011952256d7c1fdb8051118e31f88ed887d3d33",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdb0",
        "00bdbdbf"
      ]
    ],
    "bytes_sha256": "5f1299ecd8f882e30651b2466cb3d05e84e4b731358ebff65d49edd6498c6833",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00493850](../00493/00493850.md)
- [004b5004](../004b5/004b5004.md)
- [004b8d44](../004b8/004b8d44.md)
- [004bc070](../004bc/004bc070.md)
- [004bc440](../004bc/004bc440.md)
- [004be0f4](../004be/004be0f4.md)
- [004c4ce8](../004c4/004c4ce8.md)
- [004c5180](../004c5/004c5180.md)
- [004c5f28](../004c5/004c5f28.md)
- [004cfcb0](../004cf/004cfcb0.md)
- [004d04c0](../004d0/004d04c0.md)
- [004d0c9c](../004d0/004d0c9c.md)
- [004d1904](../004d1/004d1904.md)

## 呼び出し先

- [0049731c](../00497/0049731c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 115 bytes

~~~c

void _ZN5BotanmlERKNS_6BigIntES2_(void)

{
  (*(code *)PTR__ZN5BotanmlERKNS_6BigIntES2__00c1c768)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdb0"></a> `00bdbdb0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdb4"></a> `00bdbdb4` | `11 b6 43 f9` | ldr x17,[x16, #0x768] | `FALL_THROUGH`
<a id="insn-00bdbdb8"></a> `00bdbdb8` | `10 a2 1d 91` | add x16,x16,#0x768 | `FALL_THROUGH`
<a id="insn-00bdbdbc"></a> `00bdbdbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdb0`](#insn-00bdbdb0) 範囲 `[['00bdbdb0', '00bdbdbf']]`

## 命令位置別の参照

- [`00bdbdb4`](#insn-00bdbdb4) → `00c1c768`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdbc`](#insn-00bdbdbc) → [`0049731c`](../00497/0049731c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0049731c` · 推定シンボル `_ZN5BotanmlERKNS_6BigIntES2_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdb4`](#insn-00bdbdb4)

~~~json
{
  "source": "00bdbdb4",
  "target": "00c1c768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c768",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdbc`](#insn-00bdbdbc)

~~~json
{
  "source": "00bdbdbc",
  "target": "0049731c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
