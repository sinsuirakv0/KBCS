# 00bddbe0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddb90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-12207f0cff4b18ae72413d75d3e942f7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-f0c227cd34b1219e4b758b9891ab4008)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbe0",
  "name": "_ZN8firebase4auth4UserD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f0de2a015dde2dd1f8a0da80aa9592af90470b978989c383062708214836fd95",
  "source_text_sha256": "f0de2a015dde2dd1f8a0da80aa9592af90470b978989c383062708214836fd95",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbe0",
        "00bddbef"
      ]
    ],
    "bytes_sha256": "70d74a5aae53e15b2c74e15a7d7f6bd99d449647ac2c98d2f7ea40aad83905c6",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008480ec](../00848/008480ec.md)
- [0084859c](../00848/0084859c.md)
- [0084914c](../00849/0084914c.md)
- [00ad5038](../00ad5/00ad5038.md)
- [00b5b370](../00b5b/00b5b370.md)
- [00b603b0](../00b60/00b603b0.md)
- [00b64f04](../00b64/00b64f04.md)
- [00b65314](../00b65/00b65314.md)
- [00b6bf6c](../00b6b/00b6bf6c.md)
- [00b6c550](../00b6c/00b6c550.md)
- [00b6c828](../00b6c/00b6c828.md)

## 呼び出し先

- [00b6e934](../00b6e/00b6e934.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 111 bytes

~~~c

void _ZN8firebase4auth4UserD1Ev(void)

{
  (*(code *)PTR__ZN8firebase4auth4UserD1Ev_00c1d6a8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbe0"></a> `00bddbe0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddbe4"></a> `00bddbe4` | `11 56 43 f9` | ldr x17,[x16, #0x6a8] | `FALL_THROUGH`
<a id="insn-00bddbe8"></a> `00bddbe8` | `10 a2 1a 91` | add x16,x16,#0x6a8 | `FALL_THROUGH`
<a id="insn-00bddbec"></a> `00bddbec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbe0`](#insn-00bddbe0) 範囲 `[['00bddbe0', '00bddbef']]`

## 命令位置別の参照

- [`00bddbe4`](#insn-00bddbe4) → `00c1d6a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbec`](#insn-00bddbec) → [`00b6e934`](../00b6e/00b6e934.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b6e934` · 推定シンボル `_ZN8firebase4auth4UserD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbe4`](#insn-00bddbe4)

~~~json
{
  "source": "00bddbe4",
  "target": "00c1d6a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d6a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbec`](#insn-00bddbec)

~~~json
{
  "source": "00bddbec",
  "target": "00b6e934",
  "target_space": "ram",
  "resolution": "function"
}
~~~
