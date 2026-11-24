# 00acba9c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acaaa8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acaaa8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0006.md#compare-47bf4286e5fc5eee79ca3df72e2faaed)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acba9c",
  "name": "FUN_00acba9c",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7e45853ff9fe2d6f98f073284f7b7e8a024412b4236a2cfafc757cad4b36091",
  "source_text_sha256": "f7e45853ff9fe2d6f98f073284f7b7e8a024412b4236a2cfafc757cad4b36091",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acba9c",
        "00acbb37"
      ]
    ],
    "bytes_sha256": "a771dfdd503d26db4b1efed4bcb1f9f7f1af4f040a57940d037c47ba2146244d",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00830b70](../00830/00830b70.md)
- [0099803c](../00998/0099803c.md)

## 呼び出し先

- [00467bc0](../00467/00467bc0.md)
- [00467e8c](../00467/00467e8c.md)
- [004682b4](../00468/004682b4.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 603 bytes

~~~c

void FUN_00acba9c(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0xa0) != '\0') {
    uVar4 = FUN_00467bc0();
    iVar1 = *(int *)(param_1 + 0xa4) * 0x14;
    if (0xfe < iVar1) {
      iVar1 = 0xff;
    }
    FUN_00467e8c(uVar4,0,0,0,iVar1);
    lVar5 = FUN_008524fc();
    iVar1 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    FUN_008524fc();
    uVar2 = FUN_0046cd24();
    FUN_008524fc();
    uVar3 = FUN_0046cde4();
    FUN_004682b4(uVar4,0,-iVar1,uVar2,uVar3);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acba9c"></a> `00acba9c` | `08 80 42 39` | ldrb w8,[x0, #0xa0] | `FALL_THROUGH`
<a id="insn-00acbaa0"></a> `00acbaa0` | `a8 04 00 34` | cbz w8,0x00acbb34 | `CONDITIONAL_JUMP`
<a id="insn-00acbaa4"></a> `00acbaa4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acbaa8"></a> `00acbaa8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbaac"></a> `00acbaac` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbab0"></a> `00acbab0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acbab4"></a> `00acbab4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbab8"></a> `00acbab8` | `42 70 e6 97` | bl 0x00467bc0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbabc"></a> `00acbabc` | `68 a6 40 b9` | ldr w8,[x19, #0xa4] | `FALL_THROUGH`
<a id="insn-00acbac0"></a> `00acbac0` | `e9 1f 80 52` | mov w9,#0xff | `FALL_THROUGH`
<a id="insn-00acbac4"></a> `00acbac4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acbac8"></a> `00acbac8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00acbacc"></a> `00acbacc` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acbad0"></a> `00acbad0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acbad4"></a> `00acbad4` | `08 09 08 0b` | add w8,w8,w8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00acbad8"></a> `00acbad8` | `08 75 1e 53` | lsl w8,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00acbadc"></a> `00acbadc` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00acbae0"></a> `00acbae0` | `04 b1 89 1a` | csel w4,w8,w9,lt | `FALL_THROUGH`
<a id="insn-00acbae4"></a> `00acbae4` | `ea 70 e6 97` | bl 0x00467e8c | `UNCONDITIONAL_CALL`
<a id="insn-00acbae8"></a> `00acbae8` | `85 1a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acbaec"></a> `00acbaec` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-00acbaf0"></a> `00acbaf0` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acbaf4"></a> `00acbaf4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acbaf8"></a> `00acbaf8` | `f3 03 08 4b` | neg w19,w8 | `FALL_THROUGH`
<a id="insn-00acbafc"></a> `00acbafc` | `80 1a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acbb00"></a> `00acbb00` | `89 84 e6 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb04"></a> `00acbb04` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00acbb08"></a> `00acbb08` | `7d 1a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acbb0c"></a> `00acbb0c` | `b6 84 e6 97` | bl 0x0046cde4 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb10"></a> `00acbb10` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-00acbb14"></a> `00acbb14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbb18"></a> `00acbb18` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acbb1c"></a> `00acbb1c` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00acbb20"></a> `00acbb20` | `e3 03 15 2a` | mov w3,w21 | `FALL_THROUGH`
<a id="insn-00acbb24"></a> `00acbb24` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbb28"></a> `00acbb28` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbb2c"></a> `00acbb2c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acbb30"></a> `00acbb30` | `e1 71 e6 17` | b 0x004682b4 | `CALL_TERMINATOR`
<a id="insn-00acbb34"></a> `00acbb34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acba9c`](#insn-00acba9c) 範囲 `[['00acba9c', '00acbaa3']]`
  - `CONDITIONAL_JUMP` [`00acbaa0`](#insn-00acbaa0) → [`00acbb34`](#insn-00acbb34)
  - `FALL_THROUGH` [`00acbaa0`](#insn-00acbaa0) → [`00acbaa4`](#insn-00acbaa4)
- ブロック [`00acbaa4`](#insn-00acbaa4) 範囲 `[['00acbaa4', '00acbb33']]`
- ブロック [`00acbb34`](#insn-00acbb34) 範囲 `[['00acbb34', '00acbb37']]`

## 命令位置別の参照

- [`00acbaa0`](#insn-00acbaa0) → [`00acbb34`](#insn-00acbb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbaa4`](#insn-00acbaa4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbaa8`](#insn-00acbaa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbaac`](#insn-00acbaac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbab8`](#insn-00acbab8) → [`00467bc0`](../00467/00467bc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467bc0` · 推定シンボル `None` · 推定型 `None`
- [`00acbae4`](#insn-00acbae4) → [`00467e8c`](../00467/00467e8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467e8c` · 推定シンボル `None` · 推定型 `None`
- [`00acbae8`](#insn-00acbae8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acbaf4`](#insn-00acbaf4) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acbafc`](#insn-00acbafc) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acbb00`](#insn-00acbb00) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`00acbb08`](#insn-00acbb08) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acbb0c`](#insn-00acbb0c) → [`0046cde4`](../0046c/0046cde4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cde4` · 推定シンボル `None` · 推定型 `None`
- [`00acbb24`](#insn-00acbb24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb28`](#insn-00acbb28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb2c`](#insn-00acbb2c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb30`](#insn-00acbb30) → [`004682b4`](../00468/004682b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004682b4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbaa0`](#insn-00acbaa0)

~~~json
{
  "source": "00acbaa0",
  "target": "00acbb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbaa4`](#insn-00acbaa4)

~~~json
{
  "source": "00acbaa4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbaa8`](#insn-00acbaa8)

~~~json
{
  "source": "00acbaa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbaac`](#insn-00acbaac)

~~~json
{
  "source": "00acbaac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbab8`](#insn-00acbab8)

~~~json
{
  "source": "00acbab8",
  "target": "00467bc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbae4`](#insn-00acbae4)

~~~json
{
  "source": "00acbae4",
  "target": "00467e8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbae8`](#insn-00acbae8)

~~~json
{
  "source": "00acbae8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbaf4`](#insn-00acbaf4)

~~~json
{
  "source": "00acbaf4",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f4c36a0094780900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acbafc`](#insn-00acbafc)

~~~json
{
  "source": "00acbafc",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb00`](#insn-00acbb00)

~~~json
{
  "source": "00acbb00",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb08`](#insn-00acbb08)

~~~json
{
  "source": "00acbb08",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb0c`](#insn-00acbb0c)

~~~json
{
  "source": "00acbb0c",
  "target": "0046cde4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb24`](#insn-00acbb24)

~~~json
{
  "source": "00acbb24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb28`](#insn-00acbb28)

~~~json
{
  "source": "00acbb28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb2c`](#insn-00acbb2c)

~~~json
{
  "source": "00acbb2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb30`](#insn-00acbb30)

~~~json
{
  "source": "00acbb30",
  "target": "004682b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
