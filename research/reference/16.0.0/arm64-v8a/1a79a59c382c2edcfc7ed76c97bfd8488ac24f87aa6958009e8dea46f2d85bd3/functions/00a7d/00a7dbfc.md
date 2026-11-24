# 00a7dbfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0159.md#review-006c3e55ac9fde9a93bc10c950adac5d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a7ddf4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7ddf4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0061.md#compare-804abf97c9d48b21cdae408941e4244b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7dbfc",
  "name": "FUN_00a7dbfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f948d5c802d98bce49deedef76e0f97ddec7d586985e74771eac4c63a3a91033",
  "source_text_sha256": "f948d5c802d98bce49deedef76e0f97ddec7d586985e74771eac4c63a3a91033",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7dbfc",
        "00a7dc0f"
      ]
    ],
    "bytes_sha256": "d527c4170d392af30d6878cc7c710a1e22b22fb5d8fe40ce960bc684fd14e73f",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
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

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00a7dbfc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c8b9a0;
  param_2[1] = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7dbfc"></a> `00a7dbfc` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a7dc00"></a> `00a7dc00` | `69 10 00 d0` | adrp x9,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a7dc04"></a> `00a7dc04` | `29 81 26 91` | add x9,x9,#0x9a0 | `FALL_THROUGH`
<a id="insn-00a7dc08"></a> `00a7dc08` | `29 20 00 a9` | stp x9,x8,[x1] | `FALL_THROUGH`
<a id="insn-00a7dc0c"></a> `00a7dc0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7dbfc`](#insn-00a7dbfc) 範囲 `[['00a7dbfc', '00a7dc0f']]`

## 命令位置別の参照

- [`00a7dc08`](#insn-00a7dc08) → `00c8b9a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7dc08`](#insn-00a7dc08)

~~~json
{
  "source": "00a7dc08",
  "target": "00c8b9a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b9a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
