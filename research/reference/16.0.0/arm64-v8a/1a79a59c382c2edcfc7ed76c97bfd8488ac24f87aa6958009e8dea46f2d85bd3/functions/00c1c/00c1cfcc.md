# 00c1cfcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ba0584`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0584.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-3f580f89e167ad899de117dc44bf50d2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c1d3f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d3f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0023.md#compare-5ea7fbaaa3b38a9d75b4f43a7640aeb5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c1cfcc",
  "name": "_ZNKSt6__ndk18messagesIwE6do_getEliiRKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEE",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0243bb9b82b2378afc8cb768053bbcc768d509aacbac7ed9358ae0a7660a3849",
  "source_text_sha256": "0243bb9b82b2378afc8cb768053bbcc768d509aacbac7ed9358ae0a7660a3849",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c1cfcc",
        "00c1cff7"
      ]
    ],
    "bytes_sha256": "89b8c401fd1dad30ef186e7b328dae82ee1706a9ad1a96d0a7b45d5b4b730360",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006d76a4](../006d7/006d76a4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 701 bytes

~~~c

void _ZNKSt6__ndk18messagesIwE6do_getEliiRKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEE
               (undefined8 *param_1)

{
  byte *in_x4;
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*in_x4 & 1) == 0) {
    uVar2 = *(undefined8 *)in_x4;
    uVar1 = *(undefined8 *)(in_x4 + 0x10);
    param_1[1] = *(undefined8 *)(in_x4 + 8);
    *param_1 = uVar2;
                    /* try { // try from 00c1cfe4 to 00d1cfef has its CatchHandler @ 00c1dc18 */
    param_1[2] = uVar1;
    return;
  }
                    /* try { // try from 00c1cff0 to 00d1d033 has its CatchHandler @ 00c1dc24 */
  FUN_006d76a4(param_1,*(undefined8 *)(in_x4 + 0x10),*(undefined8 *)(in_x4 + 8));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c1cfcc"></a> `00c1cfcc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c1cfd0"></a> `00c1cfd0` | `89 00 40 39` | ldrb w9,[x4] | `FALL_THROUGH`
<a id="insn-00c1cfd4"></a> `00c1cfd4` | `c9 00 00 37` | tbnz w9,#0x0,0x00c1cfec | `CONDITIONAL_JUMP`
<a id="insn-00c1cfd8"></a> `00c1cfd8` | `80 00 c0 3d` | ldr q0,[x4] | `FALL_THROUGH`
<a id="insn-00c1cfdc"></a> `00c1cfdc` | `89 08 40 f9` | ldr x9,[x4, #0x10] | `FALL_THROUGH`
<a id="insn-00c1cfe0"></a> `00c1cfe0` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00c1cfe4"></a> `00c1cfe4` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00c1cfe8"></a> `00c1cfe8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c1cfec"></a> `00c1cfec` | `82 84 40 a9` | ldp x2,x1,[x4, #0x8] | `FALL_THROUGH`
<a id="insn-00c1cff0"></a> `00c1cff0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00c1cff4"></a> `00c1cff4` | `ac e9 ea 17` | b 0x006d76a4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c1cfcc`](#insn-00c1cfcc) 範囲 `[['00c1cfcc', '00c1cfd7']]`
  - `CONDITIONAL_JUMP` [`00c1cfd4`](#insn-00c1cfd4) → [`00c1cfec`](#insn-00c1cfec)
  - `FALL_THROUGH` [`00c1cfd4`](#insn-00c1cfd4) → [`00c1cfd8`](#insn-00c1cfd8)
- ブロック [`00c1cfd8`](#insn-00c1cfd8) 範囲 `[['00c1cfd8', '00c1cfe3']]`
  - `FALL_THROUGH` [`00c1cfe0`](#insn-00c1cfe0) → [`00c1cfe4`](#insn-00c1cfe4)
- ブロック [`00c1cfe4`](#insn-00c1cfe4) 範囲 `[['00c1cfe4', '00c1cfeb']]`
- ブロック [`00c1cfec`](#insn-00c1cfec) 範囲 `[['00c1cfec', '00c1cfef']]`
  - `FALL_THROUGH` [`00c1cfec`](#insn-00c1cfec) → [`00c1cff0`](#insn-00c1cff0)
- ブロック [`00c1cff0`](#insn-00c1cff0) 範囲 `[['00c1cff0', '00c1cff7']]`

## 命令位置別の参照

- [`00c1cfd4`](#insn-00c1cfd4) → [`00c1cfec`](#insn-00c1cfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cff4`](#insn-00c1cff4) → [`006d76a4`](../006d7/006d76a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d76a4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c1cfd4`](#insn-00c1cfd4)

~~~json
{
  "source": "00c1cfd4",
  "target": "00c1cfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cff4`](#insn-00c1cff4)

~~~json
{
  "source": "00c1cff4",
  "target": "006d76a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
