# 00bddfe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bde090`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-f5d863eecb13f43d117873d243191cbd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfe0",
  "name": "_ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "736190b46552d0a8421ff858b9e2e5480824599ebba4fe9d943748de5db072a1",
  "source_text_sha256": "736190b46552d0a8421ff858b9e2e5480824599ebba4fe9d943748de5db072a1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfe0",
        "00bddfef"
      ]
    ],
    "bytes_sha256": "45271d3d958400bfc8434e24288674ab32237de8f14779278bdc4c5d043092ce",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae05e4](../00ae0/00ae05e4.md)
- [00ae0650](../00ae0/00ae0650.md)
- [00ae092c](../00ae0/00ae092c.md)
- [00ae0998](../00ae0/00ae0998.md)
- [00ae0c74](../00ae0/00ae0c74.md)
- [00ae0ce0](../00ae0/00ae0ce0.md)
- [00ae0ea8](../00ae0/00ae0ea8.md)
- [00ae124c](../00ae1/00ae124c.md)
- [00ae13c4](../00ae1/00ae13c4.md)
- [00ae1428](../00ae1/00ae1428.md)
- [00ae17c8](../00ae1/00ae17c8.md)
- [00ae186c](../00ae1/00ae186c.md)
- [00ae18ec](../00ae1/00ae18ec.md)
- [00ae1964](../00ae1/00ae1964.md)
- [00ae19dc](../00ae1/00ae19dc.md)
- [00ae1a54](../00ae1/00ae1a54.md)
- [00ae1b58](../00ae1/00ae1b58.md)
- [00ae1d14](../00ae1/00ae1d14.md)
- [00ae2044](../00ae2/00ae2044.md)
- [00ae21c8](../00ae2/00ae21c8.md)
- [00ae2320](../00ae2/00ae2320.md)
- [00ae248c](../00ae2/00ae248c.md)
- [00ae2614](../00ae2/00ae2614.md)
- [00ae2858](../00ae2/00ae2858.md)
- [00ae295c](../00ae2/00ae295c.md)
- [00ae2a30](../00ae2/00ae2a30.md)
- [00ae2a94](../00ae2/00ae2a94.md)
- [00ae3940](../00ae3/00ae3940.md)
- [00b05518](../00b05/00b05518.md)
- [00b05584](../00b05/00b05584.md)
- [00b05860](../00b05/00b05860.md)
- [00b058cc](../00b05/00b058cc.md)
- [00b05ba8](../00b05/00b05ba8.md)
- [00b05c14](../00b05/00b05c14.md)
- [00b05ef0](../00b05/00b05ef0.md)
- [00b05f5c](../00b05/00b05f5c.md)
- [00b06124](../00b06/00b06124.md)
- [00b064b0](../00b06/00b064b0.md)
- [00b068bc](../00b06/00b068bc.md)
- [00b06c18](../00b06/00b06c18.md)
- [00b07ebc](../00b07/00b07ebc.md)
- [00b07fd0](../00b07/00b07fd0.md)
- [00b08044](../00b08/00b08044.md)
- [00b0d678](../00b0d/00b0d678.md)
- [00b0da84](../00b0d/00b0da84.md)
- [00b0dba8](../00b0d/00b0dba8.md)
- [00b0dcf4](../00b0d/00b0dcf4.md)
- [00b0de68](../00b0d/00b0de68.md)
- [00b4ab1c](../00b4a/00b4ab1c.md)
- [00b4ab88](../00b4a/00b4ab88.md)
- [00b4ae64](../00b4a/00b4ae64.md)
- [00b4aed0](../00b4a/00b4aed0.md)
- [00b4b1ac](../00b4b/00b4b1ac.md)
- [00b4b218](../00b4b/00b4b218.md)
- [00b4b7bc](../00b4b/00b4b7bc.md)
- [00b4c8e0](../00b4c/00b4c8e0.md)
- [00b4d40c](../00b4d/00b4d40c.md)
- [00b4d9b0](../00b4d/00b4d9b0.md)
- [00b4dd3c](../00b4d/00b4dd3c.md)
- [00b4e378](../00b4e/00b4e378.md)
- [00b52db0](../00b52/00b52db0.md)
- [00b52e1c](../00b52/00b52e1c.md)
- [00b530f8](../00b53/00b530f8.md)
- [00b53164](../00b53/00b53164.md)
- [00b53440](../00b53/00b53440.md)
- [00b534ac](../00b53/00b534ac.md)
- [00b53788](../00b53/00b53788.md)
- [00b537f4](../00b53/00b537f4.md)
- [00b53ad0](../00b53/00b53ad0.md)
- [00b53b3c](../00b53/00b53b3c.md)
- [00b53e18](../00b53/00b53e18.md)
- [00b53e84](../00b53/00b53e84.md)
- [00b54160](../00b54/00b54160.md)
- [00b541cc](../00b54/00b541cc.md)
- [00b544a8](../00b54/00b544a8.md)
- [00b54514](../00b54/00b54514.md)
- [00b547f0](../00b54/00b547f0.md)
- [00b5485c](../00b54/00b5485c.md)
- [00b54a2c](../00b54/00b54a2c.md)
- [00b5589c](../00b55/00b5589c.md)
- [00b55d70](../00b55/00b55d70.md)
- [00b563e8](../00b56/00b563e8.md)
- [00b56714](../00b56/00b56714.md)
- [00b56a40](../00b56/00b56a40.md)
- [00b56d6c](../00b56/00b56d6c.md)
- [00b57094](../00b57/00b57094.md)
- [00b5732c](../00b57/00b5732c.md)
- [00b57a40](../00b57/00b57a40.md)
- [00b57ffc](../00b57/00b57ffc.md)
- [00b58450](../00b58/00b58450.md)
- [00b5862c](../00b58/00b5862c.md)
- [00b589d8](../00b58/00b589d8.md)
- [00b58b48](../00b58/00b58b48.md)
- [00b58cb8](../00b58/00b58cb8.md)
- [00b58fa4](../00b58/00b58fa4.md)
- [00b59740](../00b59/00b59740.md)
- [00b597c0](../00b59/00b597c0.md)
- [00b59a5c](../00b59/00b59a5c.md)
- [00b5a5a4](../00b5a/00b5a5a4.md)
- [00b5c9ec](../00b5c/00b5c9ec.md)
- [00b5ca58](../00b5c/00b5ca58.md)
- [00b5cd34](../00b5c/00b5cd34.md)
- [00b5cda0](../00b5c/00b5cda0.md)
- [00b5d07c](../00b5d/00b5d07c.md)
- [00b5d0e8](../00b5d/00b5d0e8.md)
- [00b5d3c4](../00b5d/00b5d3c4.md)
- [00b5d430](../00b5d/00b5d430.md)
- [00b5d5f8](../00b5d/00b5d5f8.md)
- [00b5d828](../00b5d/00b5d828.md)
- [00b5d97c](../00b5d/00b5d97c.md)
- [00b5da38](../00b5d/00b5da38.md)
- [00b5dab8](../00b5d/00b5dab8.md)
- [00b5dc20](../00b5d/00b5dc20.md)
- [00b5e080](../00b5e/00b5e080.md)
- [00b5e480](../00b5e/00b5e480.md)
- [00b5f868](../00b5f/00b5f868.md)
- [00b5f8f0](../00b5f/00b5f8f0.md)
- [00b5f990](../00b5f/00b5f990.md)
- [00b5f9e4](../00b5f/00b5f9e4.md)
- [00b5fdcc](../00b5f/00b5fdcc.md)
- [00b60dac](../00b60/00b60dac.md)
- [00b60e18](../00b60/00b60e18.md)
- [00b610f4](../00b61/00b610f4.md)
- [00b61160](../00b61/00b61160.md)
- [00b6143c](../00b61/00b6143c.md)
- [00b614a8](../00b61/00b614a8.md)
- [00b61784](../00b61/00b61784.md)
- [00b617f0](../00b61/00b617f0.md)
- [00b61acc](../00b61/00b61acc.md)
- [00b61b38](../00b61/00b61b38.md)
- [00b61e14](../00b61/00b61e14.md)
- [00b61e80](../00b61/00b61e80.md)
- [00b6215c](../00b62/00b6215c.md)
- [00b621c8](../00b62/00b621c8.md)
- [00b624a4](../00b62/00b624a4.md)
- [00b62510](../00b62/00b62510.md)
- [00b627ec](../00b62/00b627ec.md)
- [00b62858](../00b62/00b62858.md)
- [00b62b34](../00b62/00b62b34.md)
- [00b62ba0](../00b62/00b62ba0.md)
- [00b62e7c](../00b62/00b62e7c.md)
- [00b62ee8](../00b62/00b62ee8.md)
- [00b631c4](../00b63/00b631c4.md)
- [00b63230](../00b63/00b63230.md)
- [00b6350c](../00b63/00b6350c.md)
- [00b63578](../00b63/00b63578.md)
- [00b63854](../00b63/00b63854.md)
- [00b638c0](../00b63/00b638c0.md)
- [00b63b9c](../00b63/00b63b9c.md)
- [00b63c08](../00b63/00b63c08.md)
- [00b6432c](../00b64/00b6432c.md)
- [00b647c4](../00b64/00b647c4.md)
- [00b64df8](../00b64/00b64df8.md)
- [00b64fc0](../00b64/00b64fc0.md)
- [00b65208](../00b65/00b65208.md)
- [00b65560](../00b65/00b65560.md)
- [00b655cc](../00b65/00b655cc.md)
- [00b658a8](../00b65/00b658a8.md)
- [00b65914](../00b65/00b65914.md)
- [00b65bf0](../00b65/00b65bf0.md)
- [00b65c5c](../00b65/00b65c5c.md)
- [00b65f38](../00b65/00b65f38.md)
- [00b65fa4](../00b65/00b65fa4.md)
- [00b66280](../00b66/00b66280.md)
- [00b662ec](../00b66/00b662ec.md)
- [00b665c8](../00b66/00b665c8.md)
- [00b66634](../00b66/00b66634.md)
- [00b66910](../00b66/00b66910.md)
- [00b6697c](../00b66/00b6697c.md)
- [00b66c58](../00b66/00b66c58.md)
- [00b66cc4](../00b66/00b66cc4.md)
- [00b66fa0](../00b66/00b66fa0.md)
- [00b6700c](../00b67/00b6700c.md)
- [00b672e8](../00b67/00b672e8.md)
- [00b67354](../00b67/00b67354.md)
- [00b67630](../00b67/00b67630.md)
- [00b6769c](../00b67/00b6769c.md)
- [00b67978](../00b67/00b67978.md)
- [00b679e4](../00b67/00b679e4.md)
- [00b67cc0](../00b67/00b67cc0.md)
- [00b67d2c](../00b67/00b67d2c.md)
- [00b68008](../00b68/00b68008.md)
- [00b68074](../00b68/00b68074.md)
- [00b68350](../00b68/00b68350.md)
- [00b683bc](../00b68/00b683bc.md)
- [00b68698](../00b68/00b68698.md)
- [00b68704](../00b68/00b68704.md)
- [00b689e0](../00b68/00b689e0.md)
- [00b68a4c](../00b68/00b68a4c.md)
- [00b68c14](../00b68/00b68c14.md)
- [00b69280](../00b69/00b69280.md)
- [00b699f0](../00b69/00b699f0.md)
- [00b69e4c](../00b69/00b69e4c.md)
- [00b6a008](../00b6a/00b6a008.md)
- [00b6a0e4](../00b6a/00b6a0e4.md)
- [00b6a288](../00b6a/00b6a288.md)
- [00b6a3d4](../00b6a/00b6a3d4.md)
- [00b6a558](../00b6a/00b6a558.md)
- [00b6a71c](../00b6a/00b6a71c.md)
- [00b6b064](../00b6b/00b6b064.md)
- [00b6b584](../00b6b/00b6b584.md)
- [00b6d4f8](../00b6d/00b6d4f8.md)
- [00b6d564](../00b6d/00b6d564.md)
- [00b6d840](../00b6d/00b6d840.md)
- [00b6d8ac](../00b6d/00b6d8ac.md)
- [00b6db88](../00b6d/00b6db88.md)
- [00b6dbf4](../00b6d/00b6dbf4.md)
- [00b6ded0](../00b6d/00b6ded0.md)
- [00b6df3c](../00b6d/00b6df3c.md)
- [00b6e218](../00b6e/00b6e218.md)
- [00b6e284](../00b6e/00b6e284.md)
- [00b6e638](../00b6e/00b6e638.md)
- [00b6e898](../00b6e/00b6e898.md)
- [00b6e93c](../00b6e/00b6e93c.md)
- [00b6e9e0](../00b6e/00b6e9e0.md)
- [00b6ea84](../00b6e/00b6ea84.md)
- [00b6eb28](../00b6e/00b6eb28.md)
- [00b6ebcc](../00b6e/00b6ebcc.md)
- [00b6f148](../00b6f/00b6f148.md)
- [00b6f9a0](../00b6f/00b6f9a0.md)
- [00b6fa24](../00b6f/00b6fa24.md)
- [00b6faa8](../00b6f/00b6faa8.md)
- [00b6fb2c](../00b6f/00b6fb2c.md)
- [00b6fbb0](../00b6f/00b6fbb0.md)
- [00b6fc34](../00b6f/00b6fc34.md)
- [00b71670](../00b71/00b71670.md)
- [00b7172c](../00b71/00b7172c.md)
- [00b71794](../00b71/00b71794.md)

## 呼び出し先

- [00ae4920](../00ae4/00ae4920.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 169 bytes

~~~c

void _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(void)

{
  (*(code *)PTR__ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv_00c1d828)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfe0"></a> `00bddfe0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfe4"></a> `00bddfe4` | `11 16 44 f9` | ldr x17,[x16, #0x828] | `FALL_THROUGH`
<a id="insn-00bddfe8"></a> `00bddfe8` | `10 a2 20 91` | add x16,x16,#0x828 | `FALL_THROUGH`
<a id="insn-00bddfec"></a> `00bddfec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfe0`](#insn-00bddfe0) 範囲 `[['00bddfe0', '00bddfef']]`

## 命令位置別の参照

- [`00bddfe4`](#insn-00bddfe4) → `00c1d828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfec`](#insn-00bddfec) → [`00ae4920`](../00ae4/00ae4920.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae4920` · 推定シンボル `_ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfe4`](#insn-00bddfe4)

~~~json
{
  "source": "00bddfe4",
  "target": "00c1d828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d828",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfec`](#insn-00bddfec)

~~~json
{
  "source": "00bddfec",
  "target": "00ae4920",
  "target_space": "ram",
  "resolution": "function"
}
~~~
