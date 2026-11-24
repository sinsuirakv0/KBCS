# 00afcfb0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afcb88`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcb88.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0036.md#compare-fa5ebc08257bc7e892a9bf02d97b4b39)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afd04c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afd/00afd04c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0036.md#compare-dce81baa449ba771588bbb58658b0e61)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcfb0",
  "name": "FUN_00afcfb0",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "184cac7be9f6bc684f81e05ebaff4e3dae97d274e8454b12ba34c7abb9d82d76",
  "source_text_sha256": "184cac7be9f6bc684f81e05ebaff4e3dae97d274e8454b12ba34c7abb9d82d76",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcfb0",
        "00afd01b"
      ]
    ],
    "bytes_sha256": "6edac9d50908793e3bb0b61695acd8fab155713c3cf2518ae3f0d379ecd3c21a",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 356 bytes

~~~c

void FUN_00afcfb0(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008514f8();
  uVar2 = FUN_005e7420(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514f8();
    *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c) = param_3;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcfb0"></a> `00afcfb0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afcfb4"></a> `00afcfb4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcfb8"></a> `00afcfb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcfbc"></a> `00afcfbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcfc0"></a> `00afcfc0` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afcfc4"></a> `00afcfc4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afcfc8"></a> `00afcfc8` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afcfcc"></a> `00afcfcc` | `4b 51 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcfd0"></a> `00afcfd0` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afcfd4"></a> `00afcfd4` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afcfd8"></a> `00afcfd8` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcfdc"></a> `00afcfdc` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afcfe0"></a> `00afcfe0` | `10 a9 eb 97` | bl 0x005e7420 | `UNCONDITIONAL_CALL`
<a id="insn-00afcfe4"></a> `00afcfe4` | `40 01 00 37` | tbnz w0,#0x0,0x00afd00c | `CONDITIONAL_JUMP`
<a id="insn-00afcfe8"></a> `00afcfe8` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afcfec"></a> `00afcfec` | `43 51 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcff0"></a> `00afcff0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcff4"></a> `00afcff4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcff8"></a> `00afcff8` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcffc"></a> `00afcffc` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afd000"></a> `00afd000` | `89 49 89 52` | mov w9,#0x4a4c | `FALL_THROUGH`
<a id="insn-00afd004"></a> `00afd004` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afd008"></a> `00afd008` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afd00c"></a> `00afd00c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afd010"></a> `00afd010` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd014"></a> `00afd014` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afd018"></a> `00afd018` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcfb0`](#insn-00afcfb0) 範囲 `[['00afcfb0', '00afcfe7']]`
  - `CONDITIONAL_JUMP` [`00afcfe4`](#insn-00afcfe4) → [`00afd00c`](#insn-00afd00c)
  - `FALL_THROUGH` [`00afcfe4`](#insn-00afcfe4) → [`00afcfe8`](#insn-00afcfe8)
- ブロック [`00afcfe8`](#insn-00afcfe8) 範囲 `[['00afcfe8', '00afd00b']]`
  - `FALL_THROUGH` [`00afd008`](#insn-00afd008) → [`00afd00c`](#insn-00afd00c)
- ブロック [`00afd00c`](#insn-00afd00c) 範囲 `[['00afd00c', '00afd01b']]`

## 命令位置別の参照

- [`00afcfb0`](#insn-00afcfb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfb4`](#insn-00afcfb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfb8`](#insn-00afcfb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfcc`](#insn-00afcfcc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afcfe0`](#insn-00afcfe0) → [`005e7420`](../005e7/005e7420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7420` · 推定シンボル `None` · 推定型 `None`
- [`00afcfe4`](#insn-00afcfe4) → [`00afd00c`](#insn-00afd00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfec`](#insn-00afcfec) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afd00c`](#insn-00afd00c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd010`](#insn-00afd010) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd014`](#insn-00afd014) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcfb0`](#insn-00afcfb0)

~~~json
{
  "source": "00afcfb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfb4`](#insn-00afcfb4)

~~~json
{
  "source": "00afcfb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfb8`](#insn-00afcfb8)

~~~json
{
  "source": "00afcfb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfcc`](#insn-00afcfcc)

~~~json
{
  "source": "00afcfcc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcfe0`](#insn-00afcfe0)

~~~json
{
  "source": "00afcfe0",
  "target": "005e7420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcfe4`](#insn-00afcfe4)

~~~json
{
  "source": "00afcfe4",
  "target": "00afd00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfec`](#insn-00afcfec)

~~~json
{
  "source": "00afcfec",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd00c`](#insn-00afd00c)

~~~json
{
  "source": "00afd00c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd010`](#insn-00afd010)

~~~json
{
  "source": "00afd010",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd014`](#insn-00afd014)

~~~json
{
  "source": "00afd014",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
