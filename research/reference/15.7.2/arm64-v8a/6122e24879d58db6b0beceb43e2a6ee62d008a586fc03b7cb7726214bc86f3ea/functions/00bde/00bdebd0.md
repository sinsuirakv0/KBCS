# 00bdebd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdec80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-6bf29070da723d5b5cfab2ec25a278ad)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdebd0",
  "name": "<EXTERNAL>::sem_wait",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc6ecfab8a150ea8403b1c95f9f2ec8af2c0d2956dd4a328750c82b6974c9757",
  "source_text_sha256": "dc6ecfab8a150ea8403b1c95f9f2ec8af2c0d2956dd4a328750c82b6974c9757",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdebd0",
        "00bdebdf"
      ]
    ],
    "bytes_sha256": "939f034a5b6448f9b6edfd269c21a6a7fc45f3fcdd30f507cc17974bc5228492",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afbb64](../00afb/00afbb64.md)

## 呼び出し先

- [010a55e8](../010a5/010a55e8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 200 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_wait(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_wait_00c1de20)((int)__sem);
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdebd0"></a> `00bdebd0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdebd4"></a> `00bdebd4` | `11 12 47 f9` | ldr x17,[x16, #0xe20] | `FALL_THROUGH`
<a id="insn-00bdebd8"></a> `00bdebd8` | `10 82 38 91` | add x16,x16,#0xe20 | `FALL_THROUGH`
<a id="insn-00bdebdc"></a> `00bdebdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdebd0`](#insn-00bdebd0) 範囲 `[['00bdebd0', '00bdebdf']]`

## 命令位置別の参照

- [`00bdebd4`](#insn-00bdebd4) → `00c1de20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdebdc`](#insn-00bdebdc) → [`010a55e8`](../010a5/010a55e8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a55e8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdebd4`](#insn-00bdebd4)

~~~json
{
  "source": "00bdebd4",
  "target": "00c1de20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdebdc`](#insn-00bdebdc)

~~~json
{
  "source": "00bdebdc",
  "target": "010a55e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
