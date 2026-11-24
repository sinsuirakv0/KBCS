# 00bdbdf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbda0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbda0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-0515eb5ec5c10021d393c775a2e4eff4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58840`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58840.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-b7a12212fd708e41ff3b8332c8a941cd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdf0",
  "name": "_ZN5Botan6BigIntmIERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f464095e15d7872b3c4f7dd662756fc398ac1d13b24fa9b078d67c5f304a68d",
  "source_text_sha256": "6f464095e15d7872b3c4f7dd662756fc398ac1d13b24fa9b078d67c5f304a68d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdf0",
        "00bdbdff"
      ]
    ],
    "bytes_sha256": "db85d7d493e2d63cbedba75ec036a06817444d839c33d338e0bd823e8a7a63e3",
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
- [004989ec](../00498/004989ec.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8aa0](../004b8/004b8aa0.md)
- [004b8bd8](../004b8/004b8bd8.md)
- [004b8e58](../004b8/004b8e58.md)
- [004ba430](../004ba/004ba430.md)
- [004bcf24](../004bc/004bcf24.md)
- [004be0f4](../004be/004be0f4.md)

## 呼び出し先

- [00495e3c](../00495/00495e3c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void _ZN5Botan6BigIntmIERKS0_(void)

{
  (*(code *)PTR__ZN5Botan6BigIntmIERKS0__00c1c7b0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdf0"></a> `00bdbdf0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdf4"></a> `00bdbdf4` | `11 da 43 f9` | ldr x17,[x16, #0x7b0] | `FALL_THROUGH`
<a id="insn-00bdbdf8"></a> `00bdbdf8` | `10 c2 1e 91` | add x16,x16,#0x7b0 | `FALL_THROUGH`
<a id="insn-00bdbdfc"></a> `00bdbdfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdf0`](#insn-00bdbdf0) 範囲 `[['00bdbdf0', '00bdbdff']]`

## 命令位置別の参照

- [`00bdbdf4`](#insn-00bdbdf4) → `00c1c7b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdfc`](#insn-00bdbdfc) → [`00495e3c`](../00495/00495e3c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00495e3c` · 推定シンボル `_ZN5Botan6BigIntmIERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdf4`](#insn-00bdbdf4)

~~~json
{
  "source": "00bdbdf4",
  "target": "00c1c7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c7b0",
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
  "target": "00495e3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
