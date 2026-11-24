# 00b5bfbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5bf78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bf78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0012.md#compare-712e04fa053288fa04e26bb02fbbf6de)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcb4bc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb4bc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0004.md#compare-73069c28549269589fbbd3088e62816d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5bfbc",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56875e91d0a12a8f0dd69edad475536de591bc1cce3fe39959c0bd6ae1b6128a",
  "source_text_sha256": "56875e91d0a12a8f0dd69edad475536de591bc1cce3fe39959c0bd6ae1b6128a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5bfbc",
        "00b5c043"
      ]
    ],
    "bytes_sha256": "61ad224562aa63c1c4753590d01a6ee460ea442eb46af81bbbf73175fbf04d0d",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be0ae0](../00be0/00be0ae0.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bddeb0](../00bdd/00bddeb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 921 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_
               (undefined8 *param_1,long *param_2)

{
  void *__dest;
  size_t __n;
  ulong uVar1;
  
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  if (param_2[1] - *param_2 != 0) {
    uVar1 = param_2[1] - *param_2 >> 3;
    if (uVar1 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
    }
    __dest = (void *)_Znwm();
    *param_1 = __dest;
    param_1[1] = __dest;
    param_1[2] = (void *)((long)__dest + uVar1 * 8);
                    /* try { // try from 00b5c004 to 00c5c02b has its CatchHandler @ 00b5c32c */
    __n = param_2[1] - *param_2;
    if (0 < (long)__n) {
      memcpy(__dest,(void *)*param_2,__n);
      __dest = (void *)((long)__dest + __n);
    }
    param_1[1] = __dest;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5bfbc"></a> `00b5bfbc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b5bfc0"></a> `00b5bfc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bfc4"></a> `00b5bfc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bfc8"></a> `00b5bfc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b5bfcc"></a> `00b5bfcc` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b5bfd0"></a> `00b5bfd0` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bfd4"></a> `00b5bfd4` | `28 24 40 a9` | ldp x8,x9,[x1] | `FALL_THROUGH`
<a id="insn-00b5bfd8"></a> `00b5bfd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5bfdc"></a> `00b5bfdc` | `20 01 08 eb` | subs x0,x9,x8 | `FALL_THROUGH`
<a id="insn-00b5bfe0"></a> `00b5bfe0` | `60 02 00 54` | b.eq 0x00b5c02c | `CONDITIONAL_JUMP`
<a id="insn-00b5bfe4"></a> `00b5bfe4` | `16 fc 43 93` | asr x22,x0,#0x3 | `FALL_THROUGH`
<a id="insn-00b5bfe8"></a> `00b5bfe8` | `c8 fe 7d d3` | lsr x8,x22,#0x3d | `FALL_THROUGH`
<a id="insn-00b5bfec"></a> `00b5bfec` | `88 02 00 b5` | cbnz x8,0x00b5c03c | `CONDITIONAL_JUMP`
<a id="insn-00b5bff0"></a> `00b5bff0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b5bff4"></a> `00b5bff4` | `13 fc 01 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bff8"></a> `00b5bff8` | `08 0c 16 8b` | add x8,x0,x22, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00b5bffc"></a> `00b5bffc` | `60 02 00 a9` | stp x0,x0,[x19] | `FALL_THROUGH`
<a id="insn-00b5c000"></a> `00b5c000` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b5c004"></a> `00b5c004` | `81 22 40 a9` | ldp x1,x8,[x20] | `FALL_THROUGH`
<a id="insn-00b5c008"></a> `00b5c008` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b5c00c"></a> `00b5c00c` | `14 01 01 cb` | sub x20,x8,x1 | `FALL_THROUGH`
<a id="insn-00b5c010"></a> `00b5c010` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00b5c014"></a> `00b5c014` | `ab 00 00 54` | b.lt 0x00b5c028 | `CONDITIONAL_JUMP`
<a id="insn-00b5c018"></a> `00b5c018` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5c01c"></a> `00b5c01c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00b5c020"></a> `00b5c020` | `64 fc 01 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5c024"></a> `00b5c024` | `b5 02 14 8b` | add x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00b5c028"></a> `00b5c028` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b5c02c"></a> `00b5c02c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5c030"></a> `00b5c030` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5c034"></a> `00b5c034` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b5c038"></a> `00b5c038` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5c03c"></a> `00b5c03c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5c040"></a> `00b5c040` | `9c 07 02 94` | bl 0x00bddeb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5bfbc`](#insn-00b5bfbc) 範囲 `[['00b5bfbc', '00b5bfe3']]`
  - `CONDITIONAL_JUMP` [`00b5bfe0`](#insn-00b5bfe0) → [`00b5c02c`](#insn-00b5c02c)
  - `FALL_THROUGH` [`00b5bfe0`](#insn-00b5bfe0) → [`00b5bfe4`](#insn-00b5bfe4)
- ブロック [`00b5bfe4`](#insn-00b5bfe4) 範囲 `[['00b5bfe4', '00b5bfef']]`
  - `CONDITIONAL_JUMP` [`00b5bfec`](#insn-00b5bfec) → [`00b5c03c`](#insn-00b5c03c)
  - `FALL_THROUGH` [`00b5bfec`](#insn-00b5bfec) → [`00b5bff0`](#insn-00b5bff0)
- ブロック [`00b5bff0`](#insn-00b5bff0) 範囲 `[['00b5bff0', '00b5c003']]`
  - `FALL_THROUGH` [`00b5c000`](#insn-00b5c000) → [`00b5c004`](#insn-00b5c004)
- ブロック [`00b5c004`](#insn-00b5c004) 範囲 `[['00b5c004', '00b5c017']]`
  - `CONDITIONAL_JUMP` [`00b5c014`](#insn-00b5c014) → [`00b5c028`](#insn-00b5c028)
  - `FALL_THROUGH` [`00b5c014`](#insn-00b5c014) → [`00b5c018`](#insn-00b5c018)
- ブロック [`00b5c018`](#insn-00b5c018) 範囲 `[['00b5c018', '00b5c027']]`
  - `FALL_THROUGH` [`00b5c024`](#insn-00b5c024) → [`00b5c028`](#insn-00b5c028)
- ブロック [`00b5c028`](#insn-00b5c028) 範囲 `[['00b5c028', '00b5c02b']]`
  - `FALL_THROUGH` [`00b5c028`](#insn-00b5c028) → [`00b5c02c`](#insn-00b5c02c)
- ブロック [`00b5c02c`](#insn-00b5c02c) 範囲 `[['00b5c02c', '00b5c03b']]`
- ブロック [`00b5c03c`](#insn-00b5c03c) 範囲 `[['00b5c03c', '00b5c043']]`

## 命令位置別の参照

- [`00b5bfbc`](#insn-00b5bfbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bfc0`](#insn-00b5bfc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bfc4`](#insn-00b5bfc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bfe0`](#insn-00b5bfe0) → [`00b5c02c`](#insn-00b5c02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bfec`](#insn-00b5bfec) → [`00b5c03c`](#insn-00b5c03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bff4`](#insn-00b5bff4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b5c014`](#insn-00b5c014) → [`00b5c028`](#insn-00b5c028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5c020`](#insn-00b5c020) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b5c02c`](#insn-00b5c02c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5c030`](#insn-00b5c030) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5c040`](#insn-00b5c040) → [`00bddeb0`](../00bdd/00bddeb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddeb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5bfbc`](#insn-00b5bfbc)

~~~json
{
  "source": "00b5bfbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bfc0`](#insn-00b5bfc0)

~~~json
{
  "source": "00b5bfc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bfc4`](#insn-00b5bfc4)

~~~json
{
  "source": "00b5bfc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bfe0`](#insn-00b5bfe0)

~~~json
{
  "source": "00b5bfe0",
  "target": "00b5c02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bfec`](#insn-00b5bfec)

~~~json
{
  "source": "00b5bfec",
  "target": "00b5c03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bff4`](#insn-00b5bff4)

~~~json
{
  "source": "00b5bff4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5c014`](#insn-00b5c014)

~~~json
{
  "source": "00b5c014",
  "target": "00b5c028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5c020`](#insn-00b5c020)

~~~json
{
  "source": "00b5c020",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5c02c`](#insn-00b5c02c)

~~~json
{
  "source": "00b5c02c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5c030`](#insn-00b5c030)

~~~json
{
  "source": "00b5c030",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5c040`](#insn-00b5c040)

~~~json
{
  "source": "00b5c040",
  "target": "00bddeb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
