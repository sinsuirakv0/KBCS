# 00b2cfec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acd534`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd534.md) · 移動量 `+0x5fab8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-1a7ae287dc005eaa3b646de5dee58fad)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b2d414`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d414.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-796c29c4fe1cb15c46a054d0bbf3c58a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2cfec",
  "name": "FUN_00b2cfec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8aa327de5cee3db40fd2650442c5986724d249ed07c3f4123e317def98d446a",
  "source_text_sha256": "c8aa327de5cee3db40fd2650442c5986724d249ed07c3f4123e317def98d446a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2cfec",
        "00b2d007"
      ]
    ],
    "bytes_sha256": "ccf8b738f206f4ae6cafb59a52d035f598194ab47a0cab71c97200390c019d92",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 292 bytes

~~~c

void FUN_00b2cfec(void)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_008514b8();
                    /* WARNING: Could not recover jumptable at 0x00b2d004. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + 0x38))();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2cfec"></a> `00b2cfec` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00b2cff0"></a> `00b2cff0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b2cff4"></a> `00b2cff4` | `31 91 f4 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00b2cff8"></a> `00b2cff8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b2cffc"></a> `00b2cffc` | `01 1d 40 f9` | ldr x1,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00b2d000"></a> `00b2d000` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00b2d004"></a> `00b2d004` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b2cfec`](#insn-00b2cfec) 範囲 `[['00b2cfec', '00b2d007']]`

## 命令位置別の参照

- [`00b2cfec`](#insn-00b2cfec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cff4`](#insn-00b2cff4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00b2d000`](#insn-00b2d000) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2cfec`](#insn-00b2cfec)

~~~json
{
  "source": "00b2cfec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cff4`](#insn-00b2cff4)

~~~json
{
  "source": "00b2cff4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2d000`](#insn-00b2d000)

~~~json
{
  "source": "00b2d000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
