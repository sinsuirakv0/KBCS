# 00bdcdf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcd40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-4983c4d9156275f5aa8874126f134034)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdce40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-d01c11d36b3e38c4044d1471a6032ae6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdf0",
  "name": "_ZNK5Botan14PKCS10_Request18subject_public_keyEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d55cea7e94b2c6a67e1302c7c6817493734b9fb089cbc46af5a41c8125d33e00",
  "source_text_sha256": "d55cea7e94b2c6a67e1302c7c6817493734b9fb089cbc46af5a41c8125d33e00",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdf0",
        "00bdcdff"
      ]
    ],
    "bytes_sha256": "99394148ae289f9a10deb292693924bca27ece508106db9c7c22c6dbe49fe81e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004eb16c](../004eb/004eb16c.md)
- [004ede80](../004ed/004ede80.md)

## 呼び出し先

- [004ec0b4](../004ec/004ec0b4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void _ZNK5Botan14PKCS10_Request18subject_public_keyEv(void)

{
  (*(code *)PTR__ZNK5Botan14PKCS10_Request18subject_public_keyEv_00c1cf88)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdf0"></a> `00bdcdf0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcdf4"></a> `00bdcdf4` | `11 c6 47 f9` | ldr x17,[x16, #0xf88] | `FALL_THROUGH`
<a id="insn-00bdcdf8"></a> `00bdcdf8` | `10 22 3e 91` | add x16,x16,#0xf88 | `FALL_THROUGH`
<a id="insn-00bdcdfc"></a> `00bdcdfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdf0`](#insn-00bdcdf0) 範囲 `[['00bdcdf0', '00bdcdff']]`

## 命令位置別の参照

- [`00bdcdf4`](#insn-00bdcdf4) → `00c1cf88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdfc`](#insn-00bdcdfc) → [`004ec0b4`](../004ec/004ec0b4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ec0b4` · 推定シンボル `_ZNK5Botan14PKCS10_Request18subject_public_keyEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdf4`](#insn-00bdcdf4)

~~~json
{
  "source": "00bdcdf4",
  "target": "00c1cf88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcdfc`](#insn-00bdcdfc)

~~~json
{
  "source": "00bdcdfc",
  "target": "004ec0b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
