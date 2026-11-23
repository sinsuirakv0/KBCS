# 00aadabc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aad9f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad9f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-65e2af3d2d2ccdbc2fcecafa14157aae)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aadb00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-91667cd1a58ee911ae537db645a8132a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadabc",
  "name": "FUN_00aadabc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d36487850e611cc8e3138088b67957da068882c4cbb259035f0835049716184c",
  "source_text_sha256": "d36487850e611cc8e3138088b67957da068882c4cbb259035f0835049716184c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadabc",
        "00aadad3"
      ]
    ],
    "bytes_sha256": "e5db9f09b4edee3cb1d30e9b3119ea8021d229c66d7a70f74c569ae0b57929da",
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

void FUN_00aadabc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  *param_2 = &PTR_FUN_00c0f588;
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
<a id="insn-00aadabc"></a> `00aadabc` | `08 0b 00 d0` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00aadac0"></a> `00aadac0` | `08 21 16 91` | add x8,x8,#0x588 | `FALL_THROUGH`
<a id="insn-00aadac4"></a> `00aadac4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00aadac8"></a> `00aadac8` | `00 80 c0 3c` | ldur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aadacc"></a> `00aadacc` | `20 80 80 3c` | stur q0,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00aadad0"></a> `00aadad0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadabc`](#insn-00aadabc) 範囲 `[['00aadabc', '00aadad3']]`

## 命令位置別の参照

- [`00aadac4`](#insn-00aadac4) → `00c0f588`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadac4`](#insn-00aadac4)

~~~json
{
  "source": "00aadac4",
  "target": "00c0f588",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f588",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
