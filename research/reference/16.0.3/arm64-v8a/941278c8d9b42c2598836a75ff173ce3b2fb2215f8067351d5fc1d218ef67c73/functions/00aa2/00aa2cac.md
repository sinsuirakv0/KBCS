# 00aa2cac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aa1cb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa1/00aa1cb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0065.md#compare-16beaebb046ceb612f975929d3ee2935)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa2cac",
  "name": "FUN_00aa2cac",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b7b057f1e0c10301a350a6fcfc70315f8ecda252ce1ebbc4e6d4d6761282a048",
  "source_text_sha256": "b7b057f1e0c10301a350a6fcfc70315f8ecda252ce1ebbc4e6d4d6761282a048",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa2cac",
        "00aa2d4b"
      ]
    ],
    "bytes_sha256": "6253e3c308f867ef7e82bbaf8c93d6637ae92c6bce8cc93e1cad93ae70cc0875",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa2450](../00aa2/00aa2450.md)
- [00aa2e10](../00aa2/00aa2e10.md)

## 呼び出し先

- [00470ba0](../00470/00470ba0.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c590a0](../00c59/00c590a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1196 bytes

~~~c

void FUN_00aa2cac(long *param_1,long param_2,undefined4 *param_3)

{
  void *__src;
  long lVar1;
  undefined4 uVar2;
  size_t __n;
  long lVar3;
  void *__dest;
  
  lVar3 = _Znwm(0x40);
  uVar2 = *param_3;
  *param_1 = lVar3;
  param_1[1] = param_2 + 8;
  *(undefined1 *)(param_1 + 2) = 0;
  *(undefined4 *)(lVar3 + 0x20) = uVar2;
  __src = *(void **)(param_3 + 2);
  lVar1 = *(long *)(param_3 + 4);
  *(undefined8 *)(lVar3 + 0x28) = 0;
  *(undefined8 *)(lVar3 + 0x30) = 0;
  *(undefined8 *)(lVar3 + 0x38) = 0;
  __n = lVar1 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470ba0((undefined8 *)(lVar3 + 0x28));
    }
    __dest = (void *)_Znwm(__n);
                    /* try { // try from 00aa2d10 to 00ba2d13 has its CatchHandler @ 00aa3a98 */
                    /* try { // try from 00aa2d14 to 00ba2e37 has its CatchHandler @ 00aa2600 */
    *(void **)(lVar3 + 0x28) = __dest;
    *(void **)(lVar3 + 0x30) = __dest;
    *(size_t *)(lVar3 + 0x38) = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    *(size_t *)(lVar3 + 0x30) = (long)__dest + __n;
  }
  *(undefined1 *)(param_1 + 2) = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa2cac"></a> `00aa2cac` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00aa2cb0"></a> `00aa2cb0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2cb4"></a> `00aa2cb4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2cb8"></a> `00aa2cb8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa2cbc"></a> `00aa2cbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa2cc0"></a> `00aa2cc0` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00aa2cc4"></a> `00aa2cc4` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aa2cc8"></a> `00aa2cc8` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00aa2ccc"></a> `00aa2ccc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00aa2cd0"></a> `00aa2cd0` | `98 d8 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2cd4"></a> `00aa2cd4` | `e8 02 40 b9` | ldr w8,[x23] | `FALL_THROUGH`
<a id="insn-00aa2cd8"></a> `00aa2cd8` | `60 56 00 a9` | stp x0,x21,[x19] | `FALL_THROUGH`
<a id="insn-00aa2cdc"></a> `00aa2cdc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aa2ce0"></a> `00aa2ce0` | `7f 42 00 39` | strb wzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2ce4"></a> `00aa2ce4` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2ce8"></a> `00aa2ce8` | `f6 a2 40 a9` | ldp x22,x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00aa2cec"></a> `00aa2cec` | `bf 8e 02 f8` | str xzr,[x21, #0x28]! | `FALL_THROUGH`
<a id="insn-00aa2cf0"></a> `00aa2cf0` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aa2cf4"></a> `00aa2cf4` | `17 01 16 eb` | subs x23,x8,x22 | `FALL_THROUGH`
<a id="insn-00aa2cf8"></a> `00aa2cf8` | `80 01 00 54` | b.eq 0x00aa2d28 | `CONDITIONAL_JUMP`
<a id="insn-00aa2cfc"></a> `00aa2cfc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aa2d00"></a> `00aa2d00` | `37 02 f8 b7` | tbnz x23,#0x3f,0x00aa2d44 | `CONDITIONAL_JUMP`
<a id="insn-00aa2d04"></a> `00aa2d04` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00aa2d08"></a> `00aa2d08` | `8a d8 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2d0c"></a> `00aa2d0c` | `15 00 17 8b` | add x21,x0,x23 | `FALL_THROUGH`
<a id="insn-00aa2d10"></a> `00aa2d10` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00aa2d14"></a> `00aa2d14` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00aa2d18"></a> `00aa2d18` | `80 82 02 a9` | stp x0,x0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aa2d1c"></a> `00aa2d1c` | `95 1e 00 f9` | str x21,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00aa2d20"></a> `00aa2d20` | `e0 d8 06 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2d24"></a> `00aa2d24` | `95 1a 00 f9` | str x21,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aa2d28"></a> `00aa2d28` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aa2d2c"></a> `00aa2d2c` | `68 42 00 39` | strb w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2d30"></a> `00aa2d30` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa2d34"></a> `00aa2d34` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2d38"></a> `00aa2d38` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2d3c"></a> `00aa2d3c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aa2d40"></a> `00aa2d40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa2d44"></a> `00aa2d44` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aa2d48"></a> `00aa2d48` | `96 37 e7 97` | bl 0x00470ba0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa2cac`](#insn-00aa2cac) 範囲 `[['00aa2cac', '00aa2cfb']]`
  - `CONDITIONAL_JUMP` [`00aa2cf8`](#insn-00aa2cf8) → [`00aa2d28`](#insn-00aa2d28)
  - `FALL_THROUGH` [`00aa2cf8`](#insn-00aa2cf8) → [`00aa2cfc`](#insn-00aa2cfc)
- ブロック [`00aa2cfc`](#insn-00aa2cfc) 範囲 `[['00aa2cfc', '00aa2d03']]`
  - `CONDITIONAL_JUMP` [`00aa2d00`](#insn-00aa2d00) → [`00aa2d44`](#insn-00aa2d44)
  - `FALL_THROUGH` [`00aa2d00`](#insn-00aa2d00) → [`00aa2d04`](#insn-00aa2d04)
- ブロック [`00aa2d04`](#insn-00aa2d04) 範囲 `[['00aa2d04', '00aa2d0f']]`
  - `FALL_THROUGH` [`00aa2d0c`](#insn-00aa2d0c) → [`00aa2d10`](#insn-00aa2d10)
- ブロック [`00aa2d10`](#insn-00aa2d10) 範囲 `[['00aa2d10', '00aa2d13']]`
  - `FALL_THROUGH` [`00aa2d10`](#insn-00aa2d10) → [`00aa2d14`](#insn-00aa2d14)
- ブロック [`00aa2d14`](#insn-00aa2d14) 範囲 `[['00aa2d14', '00aa2d27']]`
  - `FALL_THROUGH` [`00aa2d24`](#insn-00aa2d24) → [`00aa2d28`](#insn-00aa2d28)
- ブロック [`00aa2d28`](#insn-00aa2d28) 範囲 `[['00aa2d28', '00aa2d43']]`
- ブロック [`00aa2d44`](#insn-00aa2d44) 範囲 `[['00aa2d44', '00aa2d4b']]`

## 命令位置別の参照

- [`00aa2cac`](#insn-00aa2cac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cb0`](#insn-00aa2cb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cb4`](#insn-00aa2cb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cb8`](#insn-00aa2cb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cd0`](#insn-00aa2cd0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00aa2cf8`](#insn-00aa2cf8) → [`00aa2d28`](#insn-00aa2d28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2d00`](#insn-00aa2d00) → [`00aa2d44`](#insn-00aa2d44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2d08`](#insn-00aa2d08) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00aa2d20`](#insn-00aa2d20) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00aa2d30`](#insn-00aa2d30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2d34`](#insn-00aa2d34) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2d38`](#insn-00aa2d38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2d3c`](#insn-00aa2d3c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2d48`](#insn-00aa2d48) → [`00470ba0`](../00470/00470ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470ba0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa2cac`](#insn-00aa2cac)

~~~json
{
  "source": "00aa2cac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2cb0`](#insn-00aa2cb0)

~~~json
{
  "source": "00aa2cb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2cb4`](#insn-00aa2cb4)

~~~json
{
  "source": "00aa2cb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2cb8`](#insn-00aa2cb8)

~~~json
{
  "source": "00aa2cb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2cd0`](#insn-00aa2cd0)

~~~json
{
  "source": "00aa2cd0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2cf8`](#insn-00aa2cf8)

~~~json
{
  "source": "00aa2cf8",
  "target": "00aa2d28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2d00`](#insn-00aa2d00)

~~~json
{
  "source": "00aa2d00",
  "target": "00aa2d44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2d08`](#insn-00aa2d08)

~~~json
{
  "source": "00aa2d08",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2d20`](#insn-00aa2d20)

~~~json
{
  "source": "00aa2d20",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2d30`](#insn-00aa2d30)

~~~json
{
  "source": "00aa2d30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2d34`](#insn-00aa2d34)

~~~json
{
  "source": "00aa2d34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2d38`](#insn-00aa2d38)

~~~json
{
  "source": "00aa2d38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2d3c`](#insn-00aa2d3c)

~~~json
{
  "source": "00aa2d3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2d48`](#insn-00aa2d48)

~~~json
{
  "source": "00aa2d48",
  "target": "00470ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
