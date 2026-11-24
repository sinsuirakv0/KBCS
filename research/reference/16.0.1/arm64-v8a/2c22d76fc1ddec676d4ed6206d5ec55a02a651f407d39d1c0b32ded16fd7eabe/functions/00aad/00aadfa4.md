# 00aadfa4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aadda8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadda8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-1cec938081c31b28cf9606191e9f66a7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aae014`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aae/00aae014.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-4bee8fc1c8e497b15aaf459369e657ef)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadfa4",
  "name": "FUN_00aadfa4",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "034249418f4bb5b367a1236c52634b97c926cad6e51e4ddc1b5caa7ca17c86e5",
  "source_text_sha256": "034249418f4bb5b367a1236c52634b97c926cad6e51e4ddc1b5caa7ca17c86e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadfa4",
        "00aae01f"
      ]
    ],
    "bytes_sha256": "648db4d29cef82d1f01b9040780a4a735824283f41f57180789a59a7b8ce0a5b",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 894 bytes

~~~c

void FUN_00aadfa4(long param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  
  pbVar2 = *(byte **)(param_1 + 8);
  if (pbVar2 == (byte *)0x0) {
    return;
  }
  pbVar1 = *(byte **)(param_1 + 0x10);
  pbVar3 = pbVar2;
  if (pbVar1 != pbVar2) {
    do {
                    /* catch() { ... } // from try @ 00aadf38 with catch @ 00aadfe4 */
      pbVar3 = pbVar1 + -0x18;
      if ((*pbVar3 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar1 + -8));
      }
      pbVar1 = pbVar3;
    } while (pbVar3 != pbVar2);
    pbVar3 = *(byte **)(param_1 + 8);
  }
  *(byte **)(param_1 + 0x10) = pbVar2;
                    /* try { // try from 00aae00c to 00bae05b has its CatchHandler @ 00aae00c
                       catch() { ... } // from try @ 00aae00c with catch @ 00aae00c
                       catch() { ... } // from try @ 00aae064 with catch @ 00aae00c */
  _ZdlPv(pbVar3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aadfa4"></a> `00aadfa4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aadfa8"></a> `00aadfa8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadfac"></a> `00aadfac` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadfb0"></a> `00aadfb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aadfb4"></a> `00aadfb4` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aadfb8"></a> `00aadfb8` | `d4 02 00 b4` | cbz x20,0x00aae010 | `CONDITIONAL_JUMP`
<a id="insn-00aadfbc"></a> `00aadfbc` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aadfc0"></a> `00aadfc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aadfc4"></a> `00aadfc4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aadfc8"></a> `00aadfc8` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00aadfcc"></a> `00aadfcc` | `80 01 00 54` | b.eq 0x00aadffc | `CONDITIONAL_JUMP`
<a id="insn-00aadfd0"></a> `00aadfd0` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00aadfd4"></a> `00aadfd4` | `04 00 00 14` | b 0x00aadfe4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadfd8"></a> `00aadfd8` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00aadfdc"></a> `00aadfdc` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00aadfe0"></a> `00aadfe0` | `c0 00 00 54` | b.eq 0x00aadff8 | `CONDITIONAL_JUMP`
<a id="insn-00aadfe4"></a> `00aadfe4` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00aadfe8"></a> `00aadfe8` | `89 ff 07 36` | tbz w9,#0x0,0x00aadfd8 | `CONDITIONAL_JUMP`
<a id="insn-00aadfec"></a> `00aadfec` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00aadff0"></a> `00aadff0` | `b0 a7 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aadff4"></a> `00aadff4` | `f9 ff ff 17` | b 0x00aadfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadff8"></a> `00aadff8` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aadffc"></a> `00aadffc` | `74 0a 00 f9` | str x20,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aae000"></a> `00aae000` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aae004"></a> `00aae004` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae008"></a> `00aae008` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aae00c"></a> `00aae00c` | `a9 a7 06 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00aae010"></a> `00aae010` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aae014"></a> `00aae014` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae018"></a> `00aae018` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aae01c"></a> `00aae01c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadfa4`](#insn-00aadfa4) 範囲 `[['00aadfa4', '00aadfbb']]`
  - `CONDITIONAL_JUMP` [`00aadfb8`](#insn-00aadfb8) → [`00aae010`](#insn-00aae010)
  - `FALL_THROUGH` [`00aadfb8`](#insn-00aadfb8) → [`00aadfbc`](#insn-00aadfbc)
- ブロック [`00aadfbc`](#insn-00aadfbc) 範囲 `[['00aadfbc', '00aadfcf']]`
  - `CONDITIONAL_JUMP` [`00aadfcc`](#insn-00aadfcc) → [`00aadffc`](#insn-00aadffc)
  - `FALL_THROUGH` [`00aadfcc`](#insn-00aadfcc) → [`00aadfd0`](#insn-00aadfd0)
- ブロック [`00aadfd0`](#insn-00aadfd0) 範囲 `[['00aadfd0', '00aadfd7']]`
  - `UNCONDITIONAL_JUMP` [`00aadfd4`](#insn-00aadfd4) → [`00aadfe4`](#insn-00aadfe4)
- ブロック [`00aadfd8`](#insn-00aadfd8) 範囲 `[['00aadfd8', '00aadfe3']]`
  - `CONDITIONAL_JUMP` [`00aadfe0`](#insn-00aadfe0) → [`00aadff8`](#insn-00aadff8)
  - `FALL_THROUGH` [`00aadfe0`](#insn-00aadfe0) → [`00aadfe4`](#insn-00aadfe4)
- ブロック [`00aadfe4`](#insn-00aadfe4) 範囲 `[['00aadfe4', '00aadfeb']]`
  - `CONDITIONAL_JUMP` [`00aadfe8`](#insn-00aadfe8) → [`00aadfd8`](#insn-00aadfd8)
  - `FALL_THROUGH` [`00aadfe8`](#insn-00aadfe8) → [`00aadfec`](#insn-00aadfec)
- ブロック [`00aadfec`](#insn-00aadfec) 範囲 `[['00aadfec', '00aadff7']]`
  - `UNCONDITIONAL_JUMP` [`00aadff4`](#insn-00aadff4) → [`00aadfd8`](#insn-00aadfd8)
- ブロック [`00aadff8`](#insn-00aadff8) 範囲 `[['00aadff8', '00aadffb']]`
  - `FALL_THROUGH` [`00aadff8`](#insn-00aadff8) → [`00aadffc`](#insn-00aadffc)
- ブロック [`00aadffc`](#insn-00aadffc) 範囲 `[['00aadffc', '00aae00b']]`
  - `FALL_THROUGH` [`00aae008`](#insn-00aae008) → [`00aae00c`](#insn-00aae00c)
- ブロック [`00aae00c`](#insn-00aae00c) 範囲 `[['00aae00c', '00aae00f']]`
- ブロック [`00aae010`](#insn-00aae010) 範囲 `[['00aae010', '00aae01f']]`

## 命令位置別の参照

- [`00aadfa4`](#insn-00aadfa4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfa8`](#insn-00aadfa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfac`](#insn-00aadfac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfb8`](#insn-00aadfb8) → [`00aae010`](#insn-00aae010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfcc`](#insn-00aadfcc) → [`00aadffc`](#insn-00aadffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfd4`](#insn-00aadfd4) → [`00aadfe4`](#insn-00aadfe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfe0`](#insn-00aadfe0) → [`00aadff8`](#insn-00aadff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfe8`](#insn-00aadfe8) → [`00aadfd8`](#insn-00aadfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadff0`](#insn-00aadff0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aadff4`](#insn-00aadff4) → [`00aadfd8`](#insn-00aadfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae000`](#insn-00aae000) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae004`](#insn-00aae004) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae008`](#insn-00aae008) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae00c`](#insn-00aae00c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aae010`](#insn-00aae010) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae014`](#insn-00aae014) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae018`](#insn-00aae018) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadfa4`](#insn-00aadfa4)

~~~json
{
  "source": "00aadfa4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfa8`](#insn-00aadfa8)

~~~json
{
  "source": "00aadfa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfac`](#insn-00aadfac)

~~~json
{
  "source": "00aadfac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfb8`](#insn-00aadfb8)

~~~json
{
  "source": "00aadfb8",
  "target": "00aae010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfcc`](#insn-00aadfcc)

~~~json
{
  "source": "00aadfcc",
  "target": "00aadffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfd4`](#insn-00aadfd4)

~~~json
{
  "source": "00aadfd4",
  "target": "00aadfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfe0`](#insn-00aadfe0)

~~~json
{
  "source": "00aadfe0",
  "target": "00aadff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfe8`](#insn-00aadfe8)

~~~json
{
  "source": "00aadfe8",
  "target": "00aadfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadff0`](#insn-00aadff0)

~~~json
{
  "source": "00aadff0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadff4`](#insn-00aadff4)

~~~json
{
  "source": "00aadff4",
  "target": "00aadfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae000`](#insn-00aae000)

~~~json
{
  "source": "00aae000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae004`](#insn-00aae004)

~~~json
{
  "source": "00aae004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae008`](#insn-00aae008)

~~~json
{
  "source": "00aae008",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae00c`](#insn-00aae00c)

~~~json
{
  "source": "00aae00c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae010`](#insn-00aae010)

~~~json
{
  "source": "00aae010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae014`](#insn-00aae014)

~~~json
{
  "source": "00aae014",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae018`](#insn-00aae018)

~~~json
{
  "source": "00aae018",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
