# 00bdbcf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbca0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbca0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-cfb3c4399130bc8396521de38bd503f6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-0910589ab4a95343c77e02d9bf1ca135)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcf0",
  "name": "_ZN5Botan6BigIntC1ERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b6aeb5164ebb2fd7f5465de4f65dc3a0a7bf9b74e0818bab8686e6f75fe53d0",
  "source_text_sha256": "9b6aeb5164ebb2fd7f5465de4f65dc3a0a7bf9b74e0818bab8686e6f75fe53d0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcf0",
        "00bdbcff"
      ]
    ],
    "bytes_sha256": "fef40c1653cb4379fab650170177056cee81fc67f115301e30e6d79df8927d50",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00490728](../00490/00490728.md)
- [00493850](../00493/00493850.md)
- [00494d38](../00494/00494d38.md)
- [004967a4](../00496/004967a4.md)
- [00497724](../00497/00497724.md)
- [00497874](../00497/00497874.md)
- [00498754](../00498/00498754.md)
- [004987cc](../00498/004987cc.md)
- [004989ec](../00498/004989ec.md)
- [004b6640](../004b6/004b6640.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8aa0](../004b8/004b8aa0.md)
- [004b8bd8](../004b8/004b8bd8.md)
- [004b8e58](../004b8/004b8e58.md)
- [004b9948](../004b9/004b9948.md)
- [004ba430](../004ba/004ba430.md)
- [004bb1c0](../004bb/004bb1c0.md)
- [004bcf24](../004bc/004bcf24.md)
- [004bd550](../004bd/004bd550.md)
- [004bd8d4](../004bd/004bd8d4.md)
- [004be0f4](../004be/004be0f4.md)
- [004cfcb0](../004cf/004cfcb0.md)
- [004d04c0](../004d0/004d04c0.md)
- [0050fea8](../0050f/0050fea8.md)
- [005150ac](../00515/005150ac.md)
- [0051ce40](../0051c/0051ce40.md)
- [0051d0c8](../0051d/0051d0c8.md)
- [005221e4](../00522/005221e4.md)
- [00526bb4](../00526/00526bb4.md)

## 呼び出し先

- [00497dc8](../00497/00497dc8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void _ZN5Botan6BigIntC1ERKS0_(void)

{
  (*(code *)PTR__ZN5Botan6BigIntC1ERKS0__00c1c730)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbcf0"></a> `00bdbcf0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbcf4"></a> `00bdbcf4` | `11 9a 43 f9` | ldr x17,[x16, #0x730] | `FALL_THROUGH`
<a id="insn-00bdbcf8"></a> `00bdbcf8` | `10 c2 1c 91` | add x16,x16,#0x730 | `FALL_THROUGH`
<a id="insn-00bdbcfc"></a> `00bdbcfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcf0`](#insn-00bdbcf0) 範囲 `[['00bdbcf0', '00bdbcff']]`

## 命令位置別の参照

- [`00bdbcf4`](#insn-00bdbcf4) → `00c1c730`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcfc`](#insn-00bdbcfc) → [`00497dc8`](../00497/00497dc8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00497dc8` · 推定シンボル `_ZN5Botan6BigIntC1ERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcf4`](#insn-00bdbcf4)

~~~json
{
  "source": "00bdbcf4",
  "target": "00c1c730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c730",
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
  "target": "00497dc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
