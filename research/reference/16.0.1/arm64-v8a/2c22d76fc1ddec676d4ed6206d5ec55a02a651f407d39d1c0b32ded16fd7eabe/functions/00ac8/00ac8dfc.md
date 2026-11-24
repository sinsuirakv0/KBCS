# 00ac8dfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac8c00`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c00.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-b70366f51c64078721b514a38384d998)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac8e6c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8e6c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0013.md#compare-0ebf2766199ccc59ce98d5df439082c1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8dfc",
  "name": "FUN_00ac8dfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56791046ae044d613b5ffc4e9046c995fdc495a36cf26e120260b1157c747b21",
  "source_text_sha256": "56791046ae044d613b5ffc4e9046c995fdc495a36cf26e120260b1157c747b21",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac8dfc",
        "00ac8e0f"
      ]
    ],
    "bytes_sha256": "24706ae4c6cd7c137afd8360622b8463633d1be48c6ca3b0a7f742c468d926e4",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00693458](../00693/00693458.md)
- [00788cac](../00788/00788cac.md)
- [0082cd18](../0082c/0082cd18.md)
- [008c385c](../008c3/008c385c.md)
- [008c5208](../008c5/008c5208.md)
- [00a6fd88](../00a6f/00a6fd88.md)
- [00a72594](../00a72/00a72594.md)
- [00a73530](../00a73/00a73530.md)
- [00a7c224](../00a7c/00a7c224.md)
- [00a7e564](../00a7e/00a7e564.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 236 bytes

~~~c

void FUN_00ac8dfc(long param_1,int param_2)

{
  int iVar1;
  
  *(int *)(param_1 + 0x60) = param_2;
  iVar1 = -(*(int *)(param_1 + 0x68) * param_2);
  *(int *)(param_1 + 0x4c) = iVar1;
  *(int *)(param_1 + 0x50) = iVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac8dfc"></a> `00ac8dfc` | `08 68 40 b9` | ldr w8,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00ac8e00"></a> `00ac8e00` | `01 60 00 b9` | str w1,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00ac8e04"></a> `00ac8e04` | `08 fd 01 1b` | mneg w8,w8,w1 | `FALL_THROUGH`
<a id="insn-00ac8e08"></a> `00ac8e08` | `08 a0 09 29` | stp w8,w8,[x0, #0x4c] | `FALL_THROUGH`
<a id="insn-00ac8e0c"></a> `00ac8e0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac8dfc`](#insn-00ac8dfc) 範囲 `[['00ac8dfc', '00ac8e0f']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

