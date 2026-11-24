# 00acba0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acaa18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acaa18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0006.md#compare-efb0cdc61da2de08e24cd771a9225e88)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acba0c",
  "name": "FUN_00acba0c",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "861e3624ba8fd93ea7915794ff31487f4c9f48b63260373eacd4c3e2d76225c0",
  "source_text_sha256": "861e3624ba8fd93ea7915794ff31487f4c9f48b63260373eacd4c3e2d76225c0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acba0c",
        "00acba9b"
      ]
    ],
    "bytes_sha256": "4bad72cb5e432128d3e0884759ffacbfbf95195dedf67731258a12306d4c91b5",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0078a214](../0078a/0078a214.md)
- [00830b70](../00830/00830b70.md)
- [00900040](../00900/00900040.md)
- [00a3f56c](../00a3f/00a3f56c.md)
- [00ac1b00](../00ac1/00ac1b00.md)

## 呼び出し先

- [00467bc0](../00467/00467bc0.md)
- [00467e8c](../00467/00467e8c.md)
- [004682b4](../00468/004682b4.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 534 bytes

~~~c

void FUN_00acba0c(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0x94) != '\0') {
    uVar4 = FUN_00467bc0();
    FUN_00467e8c(uVar4,0,0,0,*(int *)(param_1 + 0x90) * 0x14);
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
<a id="insn-00acba0c"></a> `00acba0c` | `08 50 42 39` | ldrb w8,[x0, #0x94] | `FALL_THROUGH`
<a id="insn-00acba10"></a> `00acba10` | `48 04 00 34` | cbz w8,0x00acba98 | `CONDITIONAL_JUMP`
<a id="insn-00acba14"></a> `00acba14` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acba18"></a> `00acba18` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acba1c"></a> `00acba1c` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acba20"></a> `00acba20` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acba24"></a> `00acba24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acba28"></a> `00acba28` | `66 70 e6 97` | bl 0x00467bc0 | `UNCONDITIONAL_CALL`
<a id="insn-00acba2c"></a> `00acba2c` | `68 92 40 b9` | ldr w8,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00acba30"></a> `00acba30` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acba34"></a> `00acba34` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00acba38"></a> `00acba38` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acba3c"></a> `00acba3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acba40"></a> `00acba40` | `08 09 08 0b` | add w8,w8,w8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00acba44"></a> `00acba44` | `04 75 1e 53` | lsl w4,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00acba48"></a> `00acba48` | `11 71 e6 97` | bl 0x00467e8c | `UNCONDITIONAL_CALL`
<a id="insn-00acba4c"></a> `00acba4c` | `ac 1a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acba50"></a> `00acba50` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-00acba54"></a> `00acba54` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acba58"></a> `00acba58` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acba5c"></a> `00acba5c` | `f4 03 08 4b` | neg w20,w8 | `FALL_THROUGH`
<a id="insn-00acba60"></a> `00acba60` | `a7 1a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acba64"></a> `00acba64` | `b0 84 e6 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-00acba68"></a> `00acba68` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00acba6c"></a> `00acba6c` | `a4 1a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acba70"></a> `00acba70` | `dd 84 e6 97` | bl 0x0046cde4 | `UNCONDITIONAL_CALL`
<a id="insn-00acba74"></a> `00acba74` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-00acba78"></a> `00acba78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acba7c"></a> `00acba7c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acba80"></a> `00acba80` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00acba84"></a> `00acba84` | `e3 03 15 2a` | mov w3,w21 | `FALL_THROUGH`
<a id="insn-00acba88"></a> `00acba88` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acba8c"></a> `00acba8c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acba90"></a> `00acba90` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acba94"></a> `00acba94` | `08 72 e6 17` | b 0x004682b4 | `CALL_TERMINATOR`
<a id="insn-00acba98"></a> `00acba98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acba0c`](#insn-00acba0c) 範囲 `[['00acba0c', '00acba13']]`
  - `CONDITIONAL_JUMP` [`00acba10`](#insn-00acba10) → [`00acba98`](#insn-00acba98)
  - `FALL_THROUGH` [`00acba10`](#insn-00acba10) → [`00acba14`](#insn-00acba14)
- ブロック [`00acba14`](#insn-00acba14) 範囲 `[['00acba14', '00acba97']]`
- ブロック [`00acba98`](#insn-00acba98) 範囲 `[['00acba98', '00acba9b']]`

## 命令位置別の参照

- [`00acba10`](#insn-00acba10) → [`00acba98`](#insn-00acba98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba14`](#insn-00acba14) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba18`](#insn-00acba18) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba1c`](#insn-00acba1c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba28`](#insn-00acba28) → [`00467bc0`](../00467/00467bc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467bc0` · 推定シンボル `None` · 推定型 `None`
- [`00acba48`](#insn-00acba48) → [`00467e8c`](../00467/00467e8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467e8c` · 推定シンボル `None` · 推定型 `None`
- [`00acba4c`](#insn-00acba4c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acba58`](#insn-00acba58) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acba60`](#insn-00acba60) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acba64`](#insn-00acba64) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`00acba6c`](#insn-00acba6c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acba70`](#insn-00acba70) → [`0046cde4`](../0046c/0046cde4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cde4` · 推定シンボル `None` · 推定型 `None`
- [`00acba88`](#insn-00acba88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba8c`](#insn-00acba8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba90`](#insn-00acba90) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba94`](#insn-00acba94) → [`004682b4`](../00468/004682b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004682b4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acba10`](#insn-00acba10)

~~~json
{
  "source": "00acba10",
  "target": "00acba98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba14`](#insn-00acba14)

~~~json
{
  "source": "00acba14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba18`](#insn-00acba18)

~~~json
{
  "source": "00acba18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba1c`](#insn-00acba1c)

~~~json
{
  "source": "00acba1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba28`](#insn-00acba28)

~~~json
{
  "source": "00acba28",
  "target": "00467bc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba48`](#insn-00acba48)

~~~json
{
  "source": "00acba48",
  "target": "00467e8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba4c`](#insn-00acba4c)

~~~json
{
  "source": "00acba4c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba58`](#insn-00acba58)

~~~json
{
  "source": "00acba58",
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
- 参照命令 [`00acba60`](#insn-00acba60)

~~~json
{
  "source": "00acba60",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba64`](#insn-00acba64)

~~~json
{
  "source": "00acba64",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba6c`](#insn-00acba6c)

~~~json
{
  "source": "00acba6c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba70`](#insn-00acba70)

~~~json
{
  "source": "00acba70",
  "target": "0046cde4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba88`](#insn-00acba88)

~~~json
{
  "source": "00acba88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba8c`](#insn-00acba8c)

~~~json
{
  "source": "00acba8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba90`](#insn-00acba90)

~~~json
{
  "source": "00acba90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba94`](#insn-00acba94)

~~~json
{
  "source": "00acba94",
  "target": "004682b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
