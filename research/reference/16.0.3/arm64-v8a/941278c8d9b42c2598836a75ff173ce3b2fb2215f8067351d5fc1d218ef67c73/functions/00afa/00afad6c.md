# 00afad6c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9d78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9d78.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0069.md#compare-536c639a271b7b51cac3c6e516b8d5ca)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afad6c",
  "name": "FUN_00afad6c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd43ba77f81938c2e0d33c1f2bf8c84d80dbf84d591333a0761fc11a44077f01",
  "source_text_sha256": "bd43ba77f81938c2e0d33c1f2bf8c84d80dbf84d591333a0761fc11a44077f01",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afad6c",
        "00afaddb"
      ]
    ],
    "bytes_sha256": "cca7c01cb61e8431f84b9780a814f637eb1ee068180074e7b775a649ec6d08fe",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 579 bytes

~~~c

bool FUN_00afad6c(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_008524fc();
                    /* try { // try from 00afadac to 00bfadaf has its CatchHandler @ 00afaeb8 */
                    /* try { // try from 00afadb0 to 00bfae3f has its CatchHandler @ 00afad10 */
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a80) != 0;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afad6c"></a> `00afad6c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afad70"></a> `00afad70` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afad74"></a> `00afad74` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afad78"></a> `00afad78` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afad7c"></a> `00afad7c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afad80"></a> `00afad80` | `df 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afad84"></a> `00afad84` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afad88"></a> `00afad88` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afad8c"></a> `00afad8c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afad90"></a> `00afad90` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afad94"></a> `00afad94` | `9f b2 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afad98"></a> `00afad98` | `60 00 00 37` | tbnz w0,#0x0,0x00afada4 | `CONDITIONAL_JUMP`
<a id="insn-00afad9c"></a> `00afad9c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afada0"></a> `00afada0` | `0c 00 00 14` | b 0x00afadd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afada4"></a> `00afada4` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afada8"></a> `00afada8` | `d5 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afadac"></a> `00afadac` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afadb0"></a> `00afadb0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afadb4"></a> `00afadb4` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afadb8"></a> `00afadb8` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afadbc"></a> `00afadbc` | `09 50 89 52` | mov w9,#0x4a80 | `FALL_THROUGH`
<a id="insn-00afadc0"></a> `00afadc0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afadc4"></a> `00afadc4` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afadc8"></a> `00afadc8` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afadcc"></a> `00afadcc` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afadd0"></a> `00afadd0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afadd4"></a> `00afadd4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afadd8"></a> `00afadd8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afad6c`](#insn-00afad6c) 範囲 `[['00afad6c', '00afad9b']]`
  - `CONDITIONAL_JUMP` [`00afad98`](#insn-00afad98) → [`00afada4`](#insn-00afada4)
  - `FALL_THROUGH` [`00afad98`](#insn-00afad98) → [`00afad9c`](#insn-00afad9c)
- ブロック [`00afad9c`](#insn-00afad9c) 範囲 `[['00afad9c', '00afada3']]`
  - `UNCONDITIONAL_JUMP` [`00afada0`](#insn-00afada0) → [`00afadd0`](#insn-00afadd0)
- ブロック [`00afada4`](#insn-00afada4) 範囲 `[['00afada4', '00afadab']]`
  - `FALL_THROUGH` [`00afada8`](#insn-00afada8) → [`00afadac`](#insn-00afadac)
- ブロック [`00afadac`](#insn-00afadac) 範囲 `[['00afadac', '00afadaf']]`
  - `FALL_THROUGH` [`00afadac`](#insn-00afadac) → [`00afadb0`](#insn-00afadb0)
- ブロック [`00afadb0`](#insn-00afadb0) 範囲 `[['00afadb0', '00afadcf']]`
  - `FALL_THROUGH` [`00afadcc`](#insn-00afadcc) → [`00afadd0`](#insn-00afadd0)
- ブロック [`00afadd0`](#insn-00afadd0) 範囲 `[['00afadd0', '00afaddb']]`

## 命令位置別の参照

- [`00afad6c`](#insn-00afad6c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad70`](#insn-00afad70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad80`](#insn-00afad80) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afad94`](#insn-00afad94) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afad98`](#insn-00afad98) → [`00afada4`](#insn-00afada4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afada0`](#insn-00afada0) → [`00afadd0`](#insn-00afadd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afada8`](#insn-00afada8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afadd0`](#insn-00afadd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadd4`](#insn-00afadd4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afad6c`](#insn-00afad6c)

~~~json
{
  "source": "00afad6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad70`](#insn-00afad70)

~~~json
{
  "source": "00afad70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad80`](#insn-00afad80)

~~~json
{
  "source": "00afad80",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad94`](#insn-00afad94)

~~~json
{
  "source": "00afad94",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad98`](#insn-00afad98)

~~~json
{
  "source": "00afad98",
  "target": "00afada4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afada0`](#insn-00afada0)

~~~json
{
  "source": "00afada0",
  "target": "00afadd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afada8`](#insn-00afada8)

~~~json
{
  "source": "00afada8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afadd0`](#insn-00afadd0)

~~~json
{
  "source": "00afadd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadd4`](#insn-00afadd4)

~~~json
{
  "source": "00afadd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
