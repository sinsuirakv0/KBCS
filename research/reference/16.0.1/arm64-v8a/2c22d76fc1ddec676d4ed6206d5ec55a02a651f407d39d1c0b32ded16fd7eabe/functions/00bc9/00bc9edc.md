# 00bc9edc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc9ab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-bdfee68838894840a4817ff5ee6ca0e4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc9f78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9f78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-e34126ebd15de82c8c72f33fac402dbd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc9edc",
  "name": "_ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "937f498659a3cb37972eb38c3a26728ebe04ab216c180ed323f2ddd460fdaa07",
  "source_text_sha256": "937f498659a3cb37972eb38c3a26728ebe04ab216c180ed323f2ddd460fdaa07",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc9edc",
        "00bc9f57"
      ]
    ],
    "bytes_sha256": "52c0509ace60376dbd24bba2a6fca66704e92731618b430e5de2c625dcd1ed37",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5d920](../00c5d/00c5d920.md)

## 呼び出し先

- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5adf0](../00c5a/00c5adf0.md)
- [00c5ae00](../00c5a/00c5ae00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1061 bytes

~~~c

void _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
                    /* catch() { ... } // from try @ 00bc9c18 with catch @ 00bc9edc */
                    /* catch() { ... } // from try @ 00bc9dc0 with catch @ 00bc9ee0 */
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
                    /* catch() { ... } // from try @ 00bc9be0 with catch @ 00bc9f20
                       catch() { ... } // from try @ 00bc9d98 with catch @ 00bc9f20 */
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
                    /* catch() { ... } // from try @ 00bc9ce8 with catch @ 00bc9f28 */
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
  if (plVar2 != (long *)0x0) {
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc9edc"></a> `00bc9edc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bc9ee0"></a> `00bc9ee0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9ee4"></a> `00bc9ee4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9ee8"></a> `00bc9ee8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc9eec"></a> `00bc9eec` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bc9ef0"></a> `00bc9ef0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bc9ef4"></a> `00bc9ef4` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bc9ef8"></a> `00bc9ef8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc9efc"></a> `00bc9efc` | `5d 43 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9f00"></a> `00bc9f00` | `74 16 00 f9` | str x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bc9f04"></a> `00bc9f04` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bc9f08"></a> `00bc9f08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc9f0c"></a> `00bc9f0c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bc9f10"></a> `00bc9f10` | `bc 43 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9f14"></a> `00bc9f14` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bc9f18"></a> `00bc9f18` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc9f1c"></a> `00bc9f1c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9f20"></a> `00bc9f20` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bc9f24"></a> `00bc9f24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc9f28"></a> `00bc9f28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc9f2c"></a> `00bc9f2c` | `b1 43 02 94` | bl 0x00c5adf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9f30"></a> `00bc9f30` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bc9f34"></a> `00bc9f34` | `a0 00 00 b4` | cbz x0,0x00bc9f48 | `CONDITIONAL_JUMP`
<a id="insn-00bc9f38"></a> `00bc9f38` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc9f3c"></a> `00bc9f3c` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bc9f40"></a> `00bc9f40` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc9f44"></a> `00bc9f44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc9f48"></a> `00bc9f48` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9f4c"></a> `00bc9f4c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9f50"></a> `00bc9f50` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bc9f54"></a> `00bc9f54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc9edc`](#insn-00bc9edc) 範囲 `[['00bc9edc', '00bc9edf']]`
  - `FALL_THROUGH` [`00bc9edc`](#insn-00bc9edc) → [`00bc9ee0`](#insn-00bc9ee0)
- ブロック [`00bc9ee0`](#insn-00bc9ee0) 範囲 `[['00bc9ee0', '00bc9f1f']]`
  - `FALL_THROUGH` [`00bc9f1c`](#insn-00bc9f1c) → [`00bc9f20`](#insn-00bc9f20)
- ブロック [`00bc9f20`](#insn-00bc9f20) 範囲 `[['00bc9f20', '00bc9f27']]`
  - `FALL_THROUGH` [`00bc9f24`](#insn-00bc9f24) → [`00bc9f28`](#insn-00bc9f28)
- ブロック [`00bc9f28`](#insn-00bc9f28) 範囲 `[['00bc9f28', '00bc9f37']]`
  - `CONDITIONAL_JUMP` [`00bc9f34`](#insn-00bc9f34) → [`00bc9f48`](#insn-00bc9f48)
  - `FALL_THROUGH` [`00bc9f34`](#insn-00bc9f34) → [`00bc9f38`](#insn-00bc9f38)
- ブロック [`00bc9f38`](#insn-00bc9f38) 範囲 `[['00bc9f38', '00bc9f47']]`
  - `FALL_THROUGH` [`00bc9f44`](#insn-00bc9f44) → [`00bc9f48`](#insn-00bc9f48)
- ブロック [`00bc9f48`](#insn-00bc9f48) 範囲 `[['00bc9f48', '00bc9f57']]`

## 命令位置別の参照

- [`00bc9edc`](#insn-00bc9edc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9ee0`](#insn-00bc9ee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9ee4`](#insn-00bc9ee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9efc`](#insn-00bc9efc) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f10`](#insn-00bc9f10) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f2c`](#insn-00bc9f2c) → [`00c5adf0`](../00c5a/00c5adf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5adf0` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f34`](#insn-00bc9f34) → [`00bc9f48`](#insn-00bc9f48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f48`](#insn-00bc9f48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f4c`](#insn-00bc9f4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc9edc`](#insn-00bc9edc)

~~~json
{
  "source": "00bc9edc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9ee0`](#insn-00bc9ee0)

~~~json
{
  "source": "00bc9ee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9ee4`](#insn-00bc9ee4)

~~~json
{
  "source": "00bc9ee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9efc`](#insn-00bc9efc)

~~~json
{
  "source": "00bc9efc",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9f10`](#insn-00bc9f10)

~~~json
{
  "source": "00bc9f10",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9f2c`](#insn-00bc9f2c)

~~~json
{
  "source": "00bc9f2c",
  "target": "00c5adf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9f34`](#insn-00bc9f34)

~~~json
{
  "source": "00bc9f34",
  "target": "00bc9f48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9f48`](#insn-00bc9f48)

~~~json
{
  "source": "00bc9f48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9f4c`](#insn-00bc9f4c)

~~~json
{
  "source": "00bc9f4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
