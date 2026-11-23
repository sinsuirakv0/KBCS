# 00bdbdf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbd40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbd40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-b7224845da0874ef616a12ad025172dd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbe40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-af3b1d1159edb513678d9dc45ab5957b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdf0",
  "name": "_ZN5BotandvERKNS_6BigIntES2_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f378bae64e8e60de8e626354358075c4563f93cb6e0a8f8aee91f3ac17c380b3",
  "source_text_sha256": "f378bae64e8e60de8e626354358075c4563f93cb6e0a8f8aee91f3ac17c380b3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdf0",
        "00bdbdff"
      ]
    ],
    "bytes_sha256": "f118bf6a6c7086d3fb2e96e9b086098ce5f2d0e3016c6fd91d6ab6b80e3b5d08",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004963cc](../00496/004963cc.md)
- [004b6640](../004b6/004b6640.md)
- [004b8d44](../004b8/004b8d44.md)
- [004bdd7c](../004bd/004bdd7c.md)

## 呼び出し先

- [00496604](../00496/00496604.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 115 bytes

~~~c

void _ZN5BotandvERKNS_6BigIntES2_(void)

{
  (*(code *)PTR__ZN5BotandvERKNS_6BigIntES2__00c1c788)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdf0"></a> `00bdbdf0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdf4"></a> `00bdbdf4` | `11 c6 43 f9` | ldr x17,[x16, #0x788] | `FALL_THROUGH`
<a id="insn-00bdbdf8"></a> `00bdbdf8` | `10 22 1e 91` | add x16,x16,#0x788 | `FALL_THROUGH`
<a id="insn-00bdbdfc"></a> `00bdbdfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdf0`](#insn-00bdbdf0) 範囲 `[['00bdbdf0', '00bdbdff']]`

## 命令位置別の参照

- [`00bdbdf4`](#insn-00bdbdf4) → `00c1c788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdfc`](#insn-00bdbdfc) → [`00496604`](../00496/00496604.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00496604` · 推定シンボル `_ZN5BotandvERKNS_6BigIntES2_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdf4`](#insn-00bdbdf4)

~~~json
{
  "source": "00bdbdf4",
  "target": "00c1c788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c788",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdfc`](#insn-00bdbdfc)

~~~json
{
  "source": "00bdbdfc",
  "target": "00496604",
  "target_space": "ram",
  "resolution": "function"
}
~~~
