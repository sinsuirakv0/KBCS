# 00bdbcf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbc40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbc40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-1f0905fc812d033224b7046f0a67536b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbd40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-888d642823003111e38e4aba4e2d8002)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcf0",
  "name": "_ZNK5Botan9SCAN_Name3argEm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "324eac85548a2412abb56369f6c196416f4b1e9d1b9dc9550d65b1181abd2a79",
  "source_text_sha256": "324eac85548a2412abb56369f6c196416f4b1e9d1b9dc9550d65b1181abd2a79",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcf0",
        "00bdbcff"
      ]
    ],
    "bytes_sha256": "5f728c6be1459a1ce0bf1813326cf3a09b23538cdb6611309fcc2fab9530fd77",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004a3d70](../004a3/004a3d70.md)
- [004ab3f4](../004ab/004ab3f4.md)
- [004c1804](../004c1/004c1804.md)
- [004c3c00](../004c3/004c3c00.md)
- [004c43dc](../004c4/004c43dc.md)
- [004c8d94](../004c8/004c8d94.md)

## 呼び出し先

- [00491be0](../00491/00491be0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 111 bytes

~~~c

void _ZNK5Botan9SCAN_Name3argEm(void)

{
  (*(code *)PTR__ZNK5Botan9SCAN_Name3argEm_00c1c708)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbcf0"></a> `00bdbcf0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbcf4"></a> `00bdbcf4` | `11 86 43 f9` | ldr x17,[x16, #0x708] | `FALL_THROUGH`
<a id="insn-00bdbcf8"></a> `00bdbcf8` | `10 22 1c 91` | add x16,x16,#0x708 | `FALL_THROUGH`
<a id="insn-00bdbcfc"></a> `00bdbcfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcf0`](#insn-00bdbcf0) 範囲 `[['00bdbcf0', '00bdbcff']]`

## 命令位置別の参照

- [`00bdbcf4`](#insn-00bdbcf4) → `00c1c708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcfc`](#insn-00bdbcfc) → [`00491be0`](../00491/00491be0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00491be0` · 推定シンボル `_ZNK5Botan9SCAN_Name3argEm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcf4`](#insn-00bdbcf4)

~~~json
{
  "source": "00bdbcf4",
  "target": "00c1c708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c708",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcfc`](#insn-00bdbcfc)

~~~json
{
  "source": "00bdbcfc",
  "target": "00491be0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
