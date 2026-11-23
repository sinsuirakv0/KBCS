# 00bdefa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdeef0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeef0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-17c7ba65ab0e5417d2191fe4ad6d77ab)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdeff0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeff0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0021.md#compare-09d85e177ddafca99769528e7f5a9086)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdefa0",
  "name": "<EXTERNAL>::pthread_mutexattr_init",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1459ae1f0e236c49b4d0e26fb49fc98e9b7da4848dd2ff7798f2a28a6e47af54",
  "source_text_sha256": "1459ae1f0e236c49b4d0e26fb49fc98e9b7da4848dd2ff7798f2a28a6e47af54",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdefa0",
        "00bdefaf"
      ]
    ],
    "bytes_sha256": "a230921234ecb99c79750a7d50d6cf0f53e58e3f6326fcea5ce76264733be84e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b05390](../00b05/00b05390.md)
- [00b7d2f0](../00b7d/00b7d2f0.md)

## 呼び出し先

- [010a5620](../010a5/010a5620.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 244 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutexattr_init(pthread_mutexattr_t *__attr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutexattr_init_00c1e060)((int)__attr);
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdefa0"></a> `00bdefa0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdefa4"></a> `00bdefa4` | `11 32 40 f9` | ldr x17,[x16, #0x60] | `FALL_THROUGH`
<a id="insn-00bdefa8"></a> `00bdefa8` | `10 82 01 91` | add x16,x16,#0x60 | `FALL_THROUGH`
<a id="insn-00bdefac"></a> `00bdefac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdefa0`](#insn-00bdefa0) 範囲 `[['00bdefa0', '00bdefaf']]`

## 命令位置別の参照

- [`00bdefa4`](#insn-00bdefa4) → `00c1e060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdefac`](#insn-00bdefac) → [`010a5620`](../010a5/010a5620.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5620` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdefa4`](#insn-00bdefa4)

~~~json
{
  "source": "00bdefa4",
  "target": "00c1e060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdefac`](#insn-00bdefac)

~~~json
{
  "source": "00bdefac",
  "target": "010a5620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
