# 00a3abfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a3abfc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3abfc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0053.md#compare-4fd23ea481f9c8a6e13a0cf47a778803)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3abfc",
  "name": "FUN_00a3abfc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f30f26acd7b6f742f55d81a7a8cbf7c4ae4abb87c83d98756188d4a51dc1595",
  "source_text_sha256": "6f30f26acd7b6f742f55d81a7a8cbf7c4ae4abb87c83d98756188d4a51dc1595",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3abfc",
        "00a3ac13"
      ]
    ],
    "bytes_sha256": "976f0f549b02f8baa763114f3bcd28b3b5af37b7e10e6a73fbc454ed5eaca3ab",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 234 bytes

~~~c

void FUN_00a3abfc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  *param_2 = &PTR_FUN_00c0cab8;
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[2] = *(undefined8 *)(param_1 + 0x10);
  param_2[1] = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3abfc"></a> `00a3abfc` | `88 0e 00 d0` | adrp x8,0xc0c000 | `FALL_THROUGH`
<a id="insn-00a3ac00"></a> `00a3ac00` | `08 e1 2a 91` | add x8,x8,#0xab8 | `FALL_THROUGH`
<a id="insn-00a3ac04"></a> `00a3ac04` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00a3ac08"></a> `00a3ac08` | `00 80 c0 3c` | ldur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a3ac0c"></a> `00a3ac0c` | `20 80 80 3c` | stur q0,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00a3ac10"></a> `00a3ac10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3abfc`](#insn-00a3abfc) 範囲 `[['00a3abfc', '00a3ac13']]`

## 命令位置別の参照

- [`00a3ac04`](#insn-00a3ac04) → `00c0cab8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3ac04`](#insn-00a3ac04)

~~~json
{
  "source": "00a3ac04",
  "target": "00c0cab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0cab8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
