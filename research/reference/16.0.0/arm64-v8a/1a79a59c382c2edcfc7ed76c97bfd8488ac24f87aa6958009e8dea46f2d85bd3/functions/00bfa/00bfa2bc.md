# 00bfa2bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7d874`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d874.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0020.md#compare-a5b60ffbe170ba9dff013543ae9bf93f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfa6e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa6e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-ba2ef230421d536f253296d8429b98d1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa2bc",
  "name": "_ZNSt6__ndk16threadD2Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4a0dbf2c6ca2e59794e120809d6f08ac0e148e1fbe43a79561a00908594a160",
  "source_text_sha256": "f4a0dbf2c6ca2e59794e120809d6f08ac0e148e1fbe43a79561a00908594a160",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa2bc",
        "00bfa2db"
      ]
    ],
    "bytes_sha256": "69dbe87b01d1af96fef8762c13305e31dc8cdc5017d7f8964c25b71cc4f06f9a",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c57d80](../00c57/00c57d80.md)

## 呼び出し先

- [00c57c20](../00c57/00c57c20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 173 bytes

~~~c

void _ZNSt6__ndk16threadD2Ev(long *param_1)

{
  if (*param_1 == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa2bc"></a> `00bfa2bc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfa2c0"></a> `00bfa2c0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfa2c4"></a> `00bfa2c4` | `48 00 00 b5` | cbnz x8,0x00bfa2cc | `CONDITIONAL_JUMP`
<a id="insn-00bfa2c8"></a> `00bfa2c8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfa2cc"></a> `00bfa2cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa2d0"></a> `00bfa2d0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfa2d4"></a> `00bfa2d4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa2d8"></a> `00bfa2d8` | `52 76 01 94` | bl 0x00c57c20 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa2bc`](#insn-00bfa2bc) 範囲 `[['00bfa2bc', '00bfa2c7']]`
  - `CONDITIONAL_JUMP` [`00bfa2c4`](#insn-00bfa2c4) → [`00bfa2cc`](#insn-00bfa2cc)
  - `FALL_THROUGH` [`00bfa2c4`](#insn-00bfa2c4) → [`00bfa2c8`](#insn-00bfa2c8)
- ブロック [`00bfa2c8`](#insn-00bfa2c8) 範囲 `[['00bfa2c8', '00bfa2cb']]`
- ブロック [`00bfa2cc`](#insn-00bfa2cc) 範囲 `[['00bfa2cc', '00bfa2db']]`

## 命令位置別の参照

- [`00bfa2c4`](#insn-00bfa2c4) → [`00bfa2cc`](#insn-00bfa2cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa2d0`](#insn-00bfa2d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa2d8`](#insn-00bfa2d8) → [`00c57c20`](../00c57/00c57c20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c20` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa2c4`](#insn-00bfa2c4)

~~~json
{
  "source": "00bfa2c4",
  "target": "00bfa2cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa2d0`](#insn-00bfa2d0)

~~~json
{
  "source": "00bfa2d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa2d8`](#insn-00bfa2d8)

~~~json
{
  "source": "00bfa2d8",
  "target": "00c57c20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
