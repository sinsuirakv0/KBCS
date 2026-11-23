# 00bdbae0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbb90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-6b2585ce842292e8baecb3bc071d1a33)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbae0",
  "name": "<EXTERNAL>::calloc",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "577cc9bd50c0b20c2fb6b941a8ff6c3ebd3147d9d34d84528c186e0f36f41dd5",
  "source_text_sha256": "577cc9bd50c0b20c2fb6b941a8ff6c3ebd3147d9d34d84528c186e0f36f41dd5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbae0",
        "00bdbaef"
      ]
    ],
    "bytes_sha256": "dfd98deb96a7236143827412c259c6cd8a41bbe1e3b6dc338ff6d7626c2fd2da",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048cd38](../0048c/0048cd38.md)
- [0048df5c](../0048d/0048df5c.md)
- [00490630](../00490/00490630.md)
- [00495978](../00495/00495978.md)
- [004a1040](../004a1/004a1040.md)
- [004a1190](../004a1/004a1190.md)
- [004a1328](../004a1/004a1328.md)
- [004a15d0](../004a1/004a15d0.md)
- [004a5bdc](../004a5/004a5bdc.md)
- [004a6378](../004a6/004a6378.md)
- [004a6590](../004a6/004a6590.md)
- [004a6c9c](../004a6/004a6c9c.md)
- [004a710c](../004a7/004a710c.md)
- [004a728c](../004a7/004a728c.md)
- [004a7444](../004a7/004a7444.md)
- [004a76c0](../004a7/004a76c0.md)
- [004a8854](../004a8/004a8854.md)
- [004a8a10](../004a8/004a8a10.md)
- [004a8bc4](../004a8/004a8bc4.md)
- [004a8d78](../004a8/004a8d78.md)
- [004b76d8](../004b7/004b76d8.md)
- [004bf57c](../004bf/004bf57c.md)
- [004d989c](../004d9/004d989c.md)
- [005132d4](../00513/005132d4.md)
- [00513e2c](../00513/00513e2c.md)
- [0051d3cc](../0051d/0051d3cc.md)
- [0051d4f0](../0051d/0051d4f0.md)
- [0051d614](../0051d/0051d614.md)
- [0051da48](../0051d/0051da48.md)
- [0051dbb0](../0051d/0051dbb0.md)
- [0051dca0](../0051d/0051dca0.md)
- [0051e054](../0051e/0051e054.md)
- [0051e2cc](../0051e/0051e2cc.md)
- [005204e8](../00520/005204e8.md)
- [00520804](../00520/00520804.md)
- [00520980](../00520/00520980.md)
- [00520afc](../00520/00520afc.md)
- [00521e04](../00521/00521e04.md)

## 呼び出し先

- [010a5118](../010a5/010a5118.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 218 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * calloc(size_t __nmemb,size_t __size)

{
  void *pvVar1;
  
  pvVar1 = (void *)(*(code *)PTR_calloc_00c1c5a8)();
  return pvVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbae0"></a> `00bdbae0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbae4"></a> `00bdbae4` | `11 d6 42 f9` | ldr x17,[x16, #0x5a8] | `FALL_THROUGH`
<a id="insn-00bdbae8"></a> `00bdbae8` | `10 a2 16 91` | add x16,x16,#0x5a8 | `FALL_THROUGH`
<a id="insn-00bdbaec"></a> `00bdbaec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbae0`](#insn-00bdbae0) 範囲 `[['00bdbae0', '00bdbaef']]`

## 命令位置別の参照

- [`00bdbae4`](#insn-00bdbae4) → `00c1c5a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbaec`](#insn-00bdbaec) → [`010a5118`](../010a5/010a5118.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5118` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbae4`](#insn-00bdbae4)

~~~json
{
  "source": "00bdbae4",
  "target": "00c1c5a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c5a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbaec`](#insn-00bdbaec)

~~~json
{
  "source": "00bdbaec",
  "target": "010a5118",
  "target_space": "ram",
  "resolution": "function"
}
~~~
