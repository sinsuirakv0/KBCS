# 00aeffb8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0083.md#review-fdca792e7fc43d52827a0649478d2cac)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0042.md#review-fdca792e7fc43d52827a0649478d2cac)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeffb8",
  "name": "FUN_00aeffb8",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ce40332259742261bd83f9a41173a093d9a37cacb821ceb343201a6e057d41c",
  "source_text_sha256": "9ce40332259742261bd83f9a41173a093d9a37cacb821ceb343201a6e057d41c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeffb8",
        "00aeffcf"
      ]
    ],
    "bytes_sha256": "2ab6a4a010084987ac44fd2cdb5e9a07bfe5cecffa0e96d45f313917d687074d",
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

void FUN_00aeffb8(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  *param_2 = &PTR_FUN_00c8e278;
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
<a id="insn-00aeffb8"></a> `00aeffb8` | `e8 0c 00 f0` | adrp x8,0xc8e000 | `FALL_THROUGH`
<a id="insn-00aeffbc"></a> `00aeffbc` | `08 e1 09 91` | add x8,x8,#0x278 | `FALL_THROUGH`
<a id="insn-00aeffc0"></a> `00aeffc0` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00aeffc4"></a> `00aeffc4` | `00 80 c0 3c` | ldur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeffc8"></a> `00aeffc8` | `20 80 80 3c` | stur q0,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00aeffcc"></a> `00aeffcc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeffb8`](#insn-00aeffb8) 範囲 `[['00aeffb8', '00aeffcf']]`

## 命令位置別の参照

- [`00aeffc0`](#insn-00aeffc0) → `00c8e278`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeffc0`](#insn-00aeffc0)

~~~json
{
  "source": "00aeffc0",
  "target": "00c8e278",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e278",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
