# 00bdcdc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcd70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-f139f03ae0baabd11a4eb6565adcd79c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59810`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59810.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0021.md#compare-0970bc984078accd7cdbc51041490086)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdc0",
  "name": "_ZNK5Botan16X509_Certificate23load_subject_public_keyEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e61f413f441edf365fe23104b6bdd5bed014a21f28c1bc499411cb45a856552",
  "source_text_sha256": "1e61f413f441edf365fe23104b6bdd5bed014a21f28c1bc499411cb45a856552",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdc0",
        "00bdcdcf"
      ]
    ],
    "bytes_sha256": "143eb5c5027d1584737f5a7ed6f0c56f6f1e83ac7b7c48cbc3e765ee6a1547b9",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e85ec](../004e8/004e85ec.md)
- [00501b08](../00501/00501b08.md)
- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)

## 呼び出し先

- [00500f10](../00500/00500f10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 266 bytes

~~~c

void _ZNK5Botan16X509_Certificate23load_subject_public_keyEv(void)

{
                    /* try { // try from 00bdcdcc to 00cdced3 has its CatchHandler @ 00bdccd8 */
  (*(code *)PTR__ZNK5Botan16X509_Certificate23load_subject_public_keyEv_00c1cf98)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdc0"></a> `00bdcdc0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcdc4"></a> `00bdcdc4` | `11 ce 47 f9` | ldr x17,[x16, #0xf98] | `FALL_THROUGH`
<a id="insn-00bdcdc8"></a> `00bdcdc8` | `10 62 3e 91` | add x16,x16,#0xf98 | `FALL_THROUGH`
<a id="insn-00bdcdcc"></a> `00bdcdcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdc0`](#insn-00bdcdc0) 範囲 `[['00bdcdc0', '00bdcdcb']]`
  - `FALL_THROUGH` [`00bdcdc8`](#insn-00bdcdc8) → [`00bdcdcc`](#insn-00bdcdcc)
- ブロック [`00bdcdcc`](#insn-00bdcdcc) 範囲 `[['00bdcdcc', '00bdcdcf']]`

## 命令位置別の参照

- [`00bdcdc4`](#insn-00bdcdc4) → `00c1cf98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdcc`](#insn-00bdcdcc) → [`00500f10`](../00500/00500f10.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00500f10` · 推定シンボル `_ZNK5Botan16X509_Certificate23load_subject_public_keyEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdc4`](#insn-00bdcdc4)

~~~json
{
  "source": "00bdcdc4",
  "target": "00c1cf98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcdcc`](#insn-00bdcdcc)

~~~json
{
  "source": "00bdcdcc",
  "target": "00500f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
