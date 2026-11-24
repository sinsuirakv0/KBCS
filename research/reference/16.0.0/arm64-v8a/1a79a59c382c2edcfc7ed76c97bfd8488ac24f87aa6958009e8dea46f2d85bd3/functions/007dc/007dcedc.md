# 007dcedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `007aae6c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007aa/007aae6c.md) · 移動量 `+0x32070`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0009.md#compare-189042dd4533023782187984d9a35664)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007dcf1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0010.md#compare-17ba933d09baf8eaebb054737e8a8d14)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007dcedc",
  "name": "FUN_007dcedc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "927b43fe6e528fb0f142b6b0df7c32d49246d04398eb0868fb7bce39565baddd",
  "source_text_sha256": "927b43fe6e528fb0f142b6b0df7c32d49246d04398eb0868fb7bce39565baddd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007dcedc",
        "007dcef7"
      ]
    ],
    "bytes_sha256": "9acde36c18984908cd22a7daf69f397c25f1e3f060db1ccedd956bfa48528ddc",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007cceac](../007cc/007cceac.md)
- [0089e838](../0089e/0089e838.md)
- [00bf85ec](../00bf8/00bf85ec.md)

## 呼び出し先

- [00c57b80](../00c57/00c57b80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 389 bytes

~~~c

void FUN_007dcedc(undefined8 param_1,byte *param_2)

{
  ulong uVar1;
  byte *pbVar2;
  
  uVar1 = *(ulong *)(param_2 + 8);
  pbVar2 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar2 = param_2 + 1;
    uVar1 = (ulong)(*param_2 >> 1);
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (param_1,pbVar2,uVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007dcedc"></a> `007dcedc` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-007dcee0"></a> `007dcee0` | `2a a4 40 a9` | ldp x10,x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-007dcee4"></a> `007dcee4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-007dcee8"></a> `007dcee8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-007dceec"></a> `007dceec` | `21 15 81 9a` | csinc x1,x9,x1,ne | `FALL_THROUGH`
<a id="insn-007dcef0"></a> `007dcef0` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-007dcef4"></a> `007dcef4` | `23 eb 11 14` | b 0x00c57b80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007dcedc`](#insn-007dcedc) 範囲 `[['007dcedc', '007dcef7']]`

## 命令位置別の参照

- [`007dcef4`](#insn-007dcef4) → [`00c57b80`](../00c57/00c57b80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007dcef4`](#insn-007dcef4)

~~~json
{
  "source": "007dcef4",
  "target": "00c57b80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
