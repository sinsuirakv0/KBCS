# 00bddba0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddb50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-3bd9c2f62e4fb0473602a5ea3335306c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-91e60a86a6f0b5a836e35146b8d16aae)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddba0",
  "name": "_ZN8firebase4auth10CredentialD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e40040619bd9a298e54e6ecc8044e96d467148848a35cd144966d7e65c5d549",
  "source_text_sha256": "3e40040619bd9a298e54e6ecc8044e96d467148848a35cd144966d7e65c5d549",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddba0",
        "00bddbaf"
      ]
    ],
    "bytes_sha256": "1780f617159fa6fd626a8b9be0b2b6101655c1096c035913e116a94cb6c837ad",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00847a5c](../00847/00847a5c.md)
- [00b603b0](../00b60/00b603b0.md)
- [00b64f04](../00b64/00b64f04.md)
- [00b650cc](../00b65/00b650cc.md)

## 呼び出し先

- [00b698c4](../00b69/00b698c4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 125 bytes

~~~c

void _ZN8firebase4auth10CredentialD1Ev(void)

{
  (*(code *)PTR__ZN8firebase4auth10CredentialD1Ev_00c1d688)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddba0"></a> `00bddba0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddba4"></a> `00bddba4` | `11 46 43 f9` | ldr x17,[x16, #0x688] | `FALL_THROUGH`
<a id="insn-00bddba8"></a> `00bddba8` | `10 22 1a 91` | add x16,x16,#0x688 | `FALL_THROUGH`
<a id="insn-00bddbac"></a> `00bddbac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddba0`](#insn-00bddba0) 範囲 `[['00bddba0', '00bddbaf']]`

## 命令位置別の参照

- [`00bddba4`](#insn-00bddba4) → `00c1d688`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbac`](#insn-00bddbac) → [`00b698c4`](../00b69/00b698c4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b698c4` · 推定シンボル `_ZN8firebase4auth10CredentialD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddba4`](#insn-00bddba4)

~~~json
{
  "source": "00bddba4",
  "target": "00c1d688",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d688",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbac`](#insn-00bddbac)

~~~json
{
  "source": "00bddbac",
  "target": "00b698c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
