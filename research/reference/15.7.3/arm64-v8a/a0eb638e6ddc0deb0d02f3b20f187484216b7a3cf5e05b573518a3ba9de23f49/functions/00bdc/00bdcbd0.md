# 00bdcbd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcb20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-c6e7cc88016377c410530219e72992bc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcc20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-4b8505150bc51387925fa8fdc07d74a1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbd0",
  "name": "_ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c9d921177bf915a88473ce86997b7b7ce010718eb7b755b4df379c38b2f4de1",
  "source_text_sha256": "7c9d921177bf915a88473ce86997b7b7ce010718eb7b755b4df379c38b2f4de1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbd0",
        "00bdcbdf"
      ]
    ],
    "bytes_sha256": "5f45b81a41445d728719f4eb1227331168eaaf0bfac942477ca34615a021b82b",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e0038](../004e0/004e0038.md)
- [004e9260](../004e9/004e9260.md)
- [004ef204](../004ef/004ef204.md)
- [005035d4](../00503/005035d4.md)
- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)

## 呼び出し先

- [0048ad44](../0048a/0048ad44.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 321 bytes

~~~c

void _ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE_00c1ce78
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbd0"></a> `00bdcbd0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcbd4"></a> `00bdcbd4` | `11 3e 47 f9` | ldr x17,[x16, #0xe78] | `FALL_THROUGH`
<a id="insn-00bdcbd8"></a> `00bdcbd8` | `10 e2 39 91` | add x16,x16,#0xe78 | `FALL_THROUGH`
<a id="insn-00bdcbdc"></a> `00bdcbdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbd0`](#insn-00bdcbd0) 範囲 `[['00bdcbd0', '00bdcbdf']]`

## 命令位置別の参照

- [`00bdcbd4`](#insn-00bdcbd4) → `00c1ce78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbdc`](#insn-00bdcbdc) → [`0048ad44`](../0048a/0048ad44.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048ad44` · 推定シンボル `_ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbd4`](#insn-00bdcbd4)

~~~json
{
  "source": "00bdcbd4",
  "target": "00c1ce78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce78",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbdc`](#insn-00bdcbdc)

~~~json
{
  "source": "00bdcbdc",
  "target": "0048ad44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
