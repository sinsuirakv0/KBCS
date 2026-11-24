# 00bdecc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdec70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-fc1e08f01470eddb9d1fee28e374a079)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5b780`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b780.md) · 移動量 `+0x7cac0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0014.md#compare-20551a67b0e49f68fff591234b8ad671)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdecc0",
  "name": "<EXTERNAL>::sem_post",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5beec4a18e7ae7eecb227ceae947bbc613852ab6b8b7f82c11149f7779d10e37",
  "source_text_sha256": "5beec4a18e7ae7eecb227ceae947bbc613852ab6b8b7f82c11149f7779d10e37",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdecc0",
        "00bdeccf"
      ]
    ],
    "bytes_sha256": "f2484f571e95d58a63178f1095f5fdf2bc91fe2c35844e78ba7237d91f97cc34",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afc3b8](../00afc/00afc3b8.md)
- [00afc40c](../00afc/00afc40c.md)

## 呼び出し先

- [010a55e0](../010a5/010a55e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 200 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_post(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_post_00c1df18)((int)__sem);
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdecc0"></a> `00bdecc0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdecc4"></a> `00bdecc4` | `11 8e 47 f9` | ldr x17,[x16, #0xf18] | `FALL_THROUGH`
<a id="insn-00bdecc8"></a> `00bdecc8` | `10 62 3c 91` | add x16,x16,#0xf18 | `FALL_THROUGH`
<a id="insn-00bdeccc"></a> `00bdeccc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdecc0`](#insn-00bdecc0) 範囲 `[['00bdecc0', '00bdeccf']]`

## 命令位置別の参照

- [`00bdecc4`](#insn-00bdecc4) → `00c1df18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeccc`](#insn-00bdeccc) → [`010a55e0`](../010a5/010a55e0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a55e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdecc4`](#insn-00bdecc4)

~~~json
{
  "source": "00bdecc4",
  "target": "00c1df18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeccc`](#insn-00bdeccc)

~~~json
{
  "source": "00bdeccc",
  "target": "010a55e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
