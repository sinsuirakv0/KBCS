# 00a6beec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a0e0d4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e0d4.md) · 移動量 `+0x5de18`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0015.md#compare-a91ec7fa1955f3060d32f975c9904499)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a6c0e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c0e4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0019.md#compare-25145188c9b15de1c7c5fbe3fe6e332f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6beec",
  "name": "FUN_00a6beec",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ecd41032274546acef0255d0390cce71921150d0da6e21c420d9701b5696d81e",
  "source_text_sha256": "ecd41032274546acef0255d0390cce71921150d0da6e21c420d9701b5696d81e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6beec",
        "00a6bf17"
      ]
    ],
    "bytes_sha256": "35f064b8f0df4483dc46cf7047e98cf06104873a7446f40bfe82bd64d3ddeb9b",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a6a8d4](../00a6a/00a6a8d4.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 443 bytes

~~~c

void FUN_00a6beec(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*(byte *)(param_2 + 8) & 1) == 0) {
    uVar2 = *(undefined8 *)(param_2 + 8);
    uVar1 = *(undefined8 *)(param_2 + 0x18);
    param_1[1] = *(undefined8 *)(param_2 + 0x10);
    *param_1 = uVar2;
    param_1[2] = uVar1;
    return;
  }
  FUN_0043bae0(param_1,*(undefined8 *)(param_2 + 0x18),*(undefined8 *)(param_2 + 0x10));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a6beec"></a> `00a6beec` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00a6bef0"></a> `00a6bef0` | `2a 8d 40 38` | ldrb w10,[x9, #0x8]! | `FALL_THROUGH`
<a id="insn-00a6bef4"></a> `00a6bef4` | `ca 00 00 37` | tbnz w10,#0x0,0x00a6bf0c | `CONDITIONAL_JUMP`
<a id="insn-00a6bef8"></a> `00a6bef8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a6befc"></a> `00a6befc` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00a6bf00"></a> `00a6bf00` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00a6bf04"></a> `00a6bf04` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6bf08"></a> `00a6bf08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6bf0c"></a> `00a6bf0c` | `02 04 41 a9` | ldp x2,x1,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a6bf10"></a> `00a6bf10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00a6bf14"></a> `00a6bf14` | `f3 3e e7 17` | b 0x0043bae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6beec`](#insn-00a6beec) 範囲 `[['00a6beec', '00a6bef7']]`
  - `CONDITIONAL_JUMP` [`00a6bef4`](#insn-00a6bef4) → [`00a6bf0c`](#insn-00a6bf0c)
  - `FALL_THROUGH` [`00a6bef4`](#insn-00a6bef4) → [`00a6bef8`](#insn-00a6bef8)
- ブロック [`00a6bef8`](#insn-00a6bef8) 範囲 `[['00a6bef8', '00a6bf0b']]`
- ブロック [`00a6bf0c`](#insn-00a6bf0c) 範囲 `[['00a6bf0c', '00a6bf17']]`

## 命令位置別の参照

- [`00a6bef4`](#insn-00a6bef4) → [`00a6bf0c`](#insn-00a6bf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6bf14`](#insn-00a6bf14) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6bef4`](#insn-00a6bef4)

~~~json
{
  "source": "00a6bef4",
  "target": "00a6bf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6bf14`](#insn-00a6bf14)

~~~json
{
  "source": "00a6bf14",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
