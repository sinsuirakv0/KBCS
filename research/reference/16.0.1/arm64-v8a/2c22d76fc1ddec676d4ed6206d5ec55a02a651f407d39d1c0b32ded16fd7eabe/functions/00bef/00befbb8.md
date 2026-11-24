# 00befbb8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef790`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef790.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-f4bb7e0acae5931d948ec6149bccc45c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00befc54`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc54.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-2f8cc74a56811c539f79cf0da0a33b18)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befbb8",
  "name": "_ZNKSt16nested_exception14rethrow_nestedEv",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae78c5395c275261242cb3a96b766f35a0ee62dea1d5fbdd1d73fc1f1c79f502",
  "source_text_sha256": "ae78c5395c275261242cb3a96b766f35a0ee62dea1d5fbdd1d73fc1f1c79f502",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befbb8",
        "00befc0f"
      ]
    ],
    "bytes_sha256": "012019dbef36c4e71e311b0b71927799fdbd13feb7f62c12ffbd0b0c18c3511a",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53f5c](../00c53/00c53f5c.md)
- [00c58020](../00c58/00c58020.md)
- [00c582f0](../00c58/00c582f0.md)
- [00c584b0](../00c58/00c584b0.md)
- [00c584c0](../00c58/00c584c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 610 bytes

~~~c

void _ZNKSt16nested_exception14rethrow_nestedEv(long param_1)

{
  undefined8 uVar1;
  long lVar2;
  undefined1 auStack_30 [8];
  undefined8 local_28;
  
  local_28 = 0;
  lVar2 = *(long *)(param_1 + 8);
  _ZNSt13exception_ptrD1Ev(&local_28);
  if (lVar2 == 0) {
                    /* WARNING: Subroutine does not return */
    _ZSt9terminatev();
  }
  _ZNSt13exception_ptrC1ERKS_(auStack_30,(long *)(param_1 + 8));
  uVar1 = _ZSt17rethrow_exceptionSt13exception_ptr(auStack_30);
  _ZNSt13exception_ptrD1Ev(auStack_30);
                    /* WARNING: Subroutine does not return */
  FUN_00c53f5c(uVar1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befbb8"></a> `00befbb8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befbbc"></a> `00befbbc` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00befbc0"></a> `00befbc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befbc4"></a> `00befbc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00befbc8"></a> `00befbc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00befbcc"></a> `00befbcc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00befbd0"></a> `00befbd0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00befbd4"></a> `00befbd4` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00befbd8"></a> `00befbd8` | `74 8e 40 f8` | ldr x20,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00befbdc"></a> `00befbdc` | `c5 a1 01 94` | bl 0x00c582f0 | `UNCONDITIONAL_CALL`
<a id="insn-00befbe0"></a> `00befbe0` | `54 00 00 b5` | cbnz x20,0x00befbe8 | `CONDITIONAL_JUMP`
<a id="insn-00befbe4"></a> `00befbe4` | `0f a1 01 94` | bl 0x00c58020 | `CALL_TERMINATOR`
<a id="insn-00befbe8"></a> `00befbe8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00befbec"></a> `00befbec` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00befbf0"></a> `00befbf0` | `30 a2 01 94` | bl 0x00c584b0 | `UNCONDITIONAL_CALL`
<a id="insn-00befbf4"></a> `00befbf4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00befbf8"></a> `00befbf8` | `32 a2 01 94` | bl 0x00c584c0 | `UNCONDITIONAL_CALL`
<a id="insn-00befbfc"></a> `00befbfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00befc00"></a> `00befc00` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00befc04"></a> `00befc04` | `bb a1 01 94` | bl 0x00c582f0 | `UNCONDITIONAL_CALL`
<a id="insn-00befc08"></a> `00befc08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00befc0c"></a> `00befc0c` | `d4 90 01 94` | bl 0x00c53f5c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befbb8`](#insn-00befbb8) 範囲 `[['00befbb8', '00befbe3']]`
  - `CONDITIONAL_JUMP` [`00befbe0`](#insn-00befbe0) → [`00befbe8`](#insn-00befbe8)
  - `FALL_THROUGH` [`00befbe0`](#insn-00befbe0) → [`00befbe4`](#insn-00befbe4)
- ブロック [`00befbe4`](#insn-00befbe4) 範囲 `[['00befbe4', '00befbe7']]`
- ブロック [`00befbe8`](#insn-00befbe8) 範囲 `[['00befbe8', '00befc0f']]`

## 命令位置別の参照

- [`00befbc0`](#insn-00befbc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbc4`](#insn-00befbc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbd4`](#insn-00befbd4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbdc`](#insn-00befbdc) → [`00c582f0`](../00c58/00c582f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582f0` · 推定シンボル `None` · 推定型 `None`
- [`00befbe0`](#insn-00befbe0) → [`00befbe8`](#insn-00befbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbe4`](#insn-00befbe4) → [`00c58020`](../00c58/00c58020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58020` · 推定シンボル `None` · 推定型 `None`
- [`00befbf0`](#insn-00befbf0) → [`00c584b0`](../00c58/00c584b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c584b0` · 推定シンボル `None` · 推定型 `None`
- [`00befbf8`](#insn-00befbf8) → [`00c584c0`](../00c58/00c584c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c584c0` · 推定シンボル `None` · 推定型 `None`
- [`00befc04`](#insn-00befc04) → [`00c582f0`](../00c58/00c582f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582f0` · 推定シンボル `None` · 推定型 `None`
- [`00befc0c`](#insn-00befc0c) → [`00c53f5c`](../00c53/00c53f5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53f5c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befbc0`](#insn-00befbc0)

~~~json
{
  "source": "00befbc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbc4`](#insn-00befbc4)

~~~json
{
  "source": "00befbc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbd4`](#insn-00befbd4)

~~~json
{
  "source": "00befbd4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbdc`](#insn-00befbdc)

~~~json
{
  "source": "00befbdc",
  "target": "00c582f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befbe0`](#insn-00befbe0)

~~~json
{
  "source": "00befbe0",
  "target": "00befbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbe4`](#insn-00befbe4)

~~~json
{
  "source": "00befbe4",
  "target": "00c58020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befbf0`](#insn-00befbf0)

~~~json
{
  "source": "00befbf0",
  "target": "00c584b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befbf8`](#insn-00befbf8)

~~~json
{
  "source": "00befbf8",
  "target": "00c584c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befc04`](#insn-00befc04)

~~~json
{
  "source": "00befc04",
  "target": "00c582f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befc0c`](#insn-00befc0c)

~~~json
{
  "source": "00befc0c",
  "target": "00c53f5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
