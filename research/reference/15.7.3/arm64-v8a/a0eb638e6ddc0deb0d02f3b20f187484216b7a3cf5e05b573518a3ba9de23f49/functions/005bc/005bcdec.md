# 005bcdec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `005bcdec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bc/005bcdec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0004.md#compare-29ac60e1dbbd6df38e60ca140d761378)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `005bcdec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcdec.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0004.md#compare-ff1577116ccc668330a3995ef5ee52f5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005bcdec",
  "name": "FUN_005bcdec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d5aaa47432c3d651ab9917043ad384985d81d7dca96828ca01ecc03b7379758",
  "source_text_sha256": "9d5aaa47432c3d651ab9917043ad384985d81d7dca96828ca01ecc03b7379758",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005bcdec",
        "005bce07"
      ]
    ],
    "bytes_sha256": "1735a747ef2d78a761d73f4dd32f305d9fbc92acacb667d263f75c4bc106048c",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006ee6c8](../006ee/006ee6c8.md)
- [009f4a74](../009f4/009f4a74.md)
- [009f560c](../009f5/009f560c.md)

## 呼び出し先

- [005bc280](../005bc/005bc280.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 95 bytes

~~~c

bool FUN_005bcdec(void)

{
  int iVar1;
  
  iVar1 = FUN_005bc280();
  return iVar1 != -1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005bcdec"></a> `005bcdec` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-005bcdf0"></a> `005bcdf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005bcdf4"></a> `005bcdf4` | `23 fd ff 97` | bl 0x005bc280 | `UNCONDITIONAL_CALL`
<a id="insn-005bcdf8"></a> `005bcdf8` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-005bcdfc"></a> `005bcdfc` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-005bce00"></a> `005bce00` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-005bce04"></a> `005bce04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005bcdec`](#insn-005bcdec) 範囲 `[['005bcdec', '005bce07']]`

## 命令位置別の参照

- [`005bcdec`](#insn-005bcdec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bcdf4`](#insn-005bcdf4) → [`005bc280`](005bc280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bc280` · 推定シンボル `None` · 推定型 `None`
- [`005bce00`](#insn-005bce00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005bcdec`](#insn-005bcdec)

~~~json
{
  "source": "005bcdec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bcdf4`](#insn-005bcdf4)

~~~json
{
  "source": "005bcdf4",
  "target": "005bc280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bce00`](#insn-005bce00)

~~~json
{
  "source": "005bce00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
