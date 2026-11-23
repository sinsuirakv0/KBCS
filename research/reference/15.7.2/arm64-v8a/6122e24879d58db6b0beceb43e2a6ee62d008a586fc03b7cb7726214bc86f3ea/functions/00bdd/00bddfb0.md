# 00bddfb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bde060`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-fa1116fbb7081a3fc7ca85811002ef70)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfb0",
  "name": "_ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1903677513068047a8602ec9a9f8ffe12e15495708264de8ffb91ac4145eb9c3",
  "source_text_sha256": "1903677513068047a8602ec9a9f8ffe12e15495708264de8ffb91ac4145eb9c3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfb0",
        "00bddfbf"
      ]
    ],
    "bytes_sha256": "2bd5ff8891bc94512e766e93acd2f5766bdcc74d46b6f9a1da2bd01d8fb67f69",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae06c0](../00ae0/00ae06c0.md)
- [00ae0a08](../00ae0/00ae0a08.md)
- [00ae0d50](../00ae0/00ae0d50.md)
- [00ae0ea8](../00ae0/00ae0ea8.md)
- [00ae4a1c](../00ae4/00ae4a1c.md)
- [00ae529c](../00ae5/00ae529c.md)
- [00ae5644](../00ae5/00ae5644.md)
- [00ae59ec](../00ae5/00ae59ec.md)
- [00ae5d94](../00ae5/00ae5d94.md)
- [00ae613c](../00ae6/00ae613c.md)
- [00ae64e4](../00ae6/00ae64e4.md)
- [00ae688c](../00ae6/00ae688c.md)
- [00ae6c34](../00ae6/00ae6c34.md)
- [00ae6fdc](../00ae6/00ae6fdc.md)
- [00ae7384](../00ae7/00ae7384.md)
- [00ae772c](../00ae7/00ae772c.md)
- [00ae7ad4](../00ae7/00ae7ad4.md)
- [00ae7e7c](../00ae7/00ae7e7c.md)
- [00ae8224](../00ae8/00ae8224.md)
- [00ae85cc](../00ae8/00ae85cc.md)
- [00ae8974](../00ae8/00ae8974.md)
- [00ae8d1c](../00ae8/00ae8d1c.md)
- [00ae90c4](../00ae9/00ae90c4.md)
- [00ae946c](../00ae9/00ae946c.md)
- [00ae9814](../00ae9/00ae9814.md)
- [00ae9bbc](../00ae9/00ae9bbc.md)
- [00ae9f64](../00ae9/00ae9f64.md)
- [00aea30c](../00aea/00aea30c.md)
- [00aea6b4](../00aea/00aea6b4.md)
- [00aeaa5c](../00aea/00aeaa5c.md)
- [00aeae04](../00aea/00aeae04.md)
- [00aeb1ac](../00aeb/00aeb1ac.md)
- [00aeb554](../00aeb/00aeb554.md)
- [00aeb8fc](../00aeb/00aeb8fc.md)
- [00aebca4](../00aeb/00aebca4.md)
- [00aec04c](../00aec/00aec04c.md)
- [00aec3f4](../00aec/00aec3f4.md)
- [00aec79c](../00aec/00aec79c.md)
- [00aecb44](../00aec/00aecb44.md)
- [00aeceec](../00aec/00aeceec.md)
- [00aed294](../00aed/00aed294.md)
- [00aed63c](../00aed/00aed63c.md)
- [00aed9e4](../00aed/00aed9e4.md)
- [00aedd8c](../00aed/00aedd8c.md)
- [00aee134](../00aee/00aee134.md)
- [00aee28c](../00aee/00aee28c.md)
- [00aee884](../00aee/00aee884.md)
- [00af10e4](../00af1/00af10e4.md)
- [00b055f4](../00b05/00b055f4.md)
- [00b0593c](../00b05/00b0593c.md)
- [00b05c84](../00b05/00b05c84.md)
- [00b05fcc](../00b05/00b05fcc.md)
- [00b062c8](../00b06/00b062c8.md)
- [00b0d678](../00b0d/00b0d678.md)
- [00b4abf8](../00b4a/00b4abf8.md)
- [00b4af40](../00b4a/00b4af40.md)
- [00b4b288](../00b4b/00b4b288.md)
- [00b4c3b8](../00b4c/00b4c3b8.md)
- [00b52e8c](../00b52/00b52e8c.md)
- [00b531d4](../00b53/00b531d4.md)
- [00b5351c](../00b53/00b5351c.md)
- [00b53864](../00b53/00b53864.md)
- [00b53bac](../00b53/00b53bac.md)
- [00b53ef4](../00b53/00b53ef4.md)
- [00b5423c](../00b54/00b5423c.md)
- [00b54584](../00b54/00b54584.md)
- [00b548cc](../00b54/00b548cc.md)
- [00b54a2c](../00b54/00b54a2c.md)
- [00b5cac8](../00b5c/00b5cac8.md)
- [00b5ce10](../00b5c/00b5ce10.md)
- [00b5d158](../00b5d/00b5d158.md)
- [00b5d4a0](../00b5d/00b5d4a0.md)
- [00b5d5f8](../00b5d/00b5d5f8.md)
- [00b60e88](../00b60/00b60e88.md)
- [00b611d0](../00b61/00b611d0.md)
- [00b61518](../00b61/00b61518.md)
- [00b61860](../00b61/00b61860.md)
- [00b61ba8](../00b61/00b61ba8.md)
- [00b61ef0](../00b61/00b61ef0.md)
- [00b62238](../00b62/00b62238.md)
- [00b62580](../00b62/00b62580.md)
- [00b628c8](../00b62/00b628c8.md)
- [00b62c10](../00b62/00b62c10.md)
- [00b62f58](../00b62/00b62f58.md)
- [00b632a0](../00b63/00b632a0.md)
- [00b635e8](../00b63/00b635e8.md)
- [00b63930](../00b63/00b63930.md)
- [00b63c78](../00b63/00b63c78.md)
- [00b63dd0](../00b63/00b63dd0.md)
- [00b6563c](../00b65/00b6563c.md)
- [00b65984](../00b65/00b65984.md)
- [00b65ccc](../00b65/00b65ccc.md)
- [00b66014](../00b66/00b66014.md)
- [00b6635c](../00b66/00b6635c.md)
- [00b666a4](../00b66/00b666a4.md)
- [00b669ec](../00b66/00b669ec.md)
- [00b66d34](../00b66/00b66d34.md)
- [00b6707c](../00b67/00b6707c.md)
- [00b673c4](../00b67/00b673c4.md)
- [00b6770c](../00b67/00b6770c.md)
- [00b67a54](../00b67/00b67a54.md)
- [00b67d9c](../00b67/00b67d9c.md)
- [00b680e4](../00b68/00b680e4.md)
- [00b6842c](../00b68/00b6842c.md)
- [00b68774](../00b68/00b68774.md)
- [00b68abc](../00b68/00b68abc.md)
- [00b68c14](../00b68/00b68c14.md)
- [00b6d5d4](../00b6d/00b6d5d4.md)
- [00b6d91c](../00b6d/00b6d91c.md)
- [00b6dc64](../00b6d/00b6dc64.md)
- [00b6dfac](../00b6d/00b6dfac.md)
- [00b6e2f4](../00b6e/00b6e2f4.md)
- [00b6e44c](../00b6e/00b6e44c.md)

## 呼び出し先

- [00ae4a8c](../00ae4/00ae4a8c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 281 bytes

~~~c

void _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
               (void)

{
  (*(code *)
    PTR__ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc_00c1d810
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfb0"></a> `00bddfb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfb4"></a> `00bddfb4` | `11 0a 44 f9` | ldr x17,[x16, #0x810] | `FALL_THROUGH`
<a id="insn-00bddfb8"></a> `00bddfb8` | `10 42 20 91` | add x16,x16,#0x810 | `FALL_THROUGH`
<a id="insn-00bddfbc"></a> `00bddfbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfb0`](#insn-00bddfb0) 範囲 `[['00bddfb0', '00bddfbf']]`

## 命令位置別の参照

- [`00bddfb4`](#insn-00bddfb4) → `00c1d810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfbc`](#insn-00bddfbc) → [`00ae4a8c`](../00ae4/00ae4a8c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae4a8c` · 推定シンボル `_ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfb4`](#insn-00bddfb4)

~~~json
{
  "source": "00bddfb4",
  "target": "00c1d810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d810",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfbc`](#insn-00bddfbc)

~~~json
{
  "source": "00bddfbc",
  "target": "00ae4a8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
