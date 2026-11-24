# 00afcd7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-405ed2babd584c2a6756f2eada783104)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afd1a4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afd1a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0036.md#compare-3a247526e2222c522385d4dd6c99b601)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcd7c",
  "name": "FUN_00afcd7c",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fda00cbea4222361d8c1e2a7c15d554f90df6e1460382b0c7eb4d9806ddb24f",
  "source_text_sha256": "9fda00cbea4222361d8c1e2a7c15d554f90df6e1460382b0c7eb4d9806ddb24f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcd7c",
        "00afce2f"
      ]
    ],
    "bytes_sha256": "810ed1c5430023f84bbcca7a877bffd29116d8578250674a09727a81a6b80305",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00716d50](../00716/00716d50.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 627 bytes

~~~c

void FUN_00afcd7c(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  int iVar3;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    iVar3 = *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a64);
  }
  else {
    iVar3 = 0;
  }
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a64) = iVar3 + param_3;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcd7c"></a> `00afcd7c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afcd80"></a> `00afcd80` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcd84"></a> `00afcd84` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcd88"></a> `00afcd88` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcd8c"></a> `00afcd8c` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afcd90"></a> `00afcd90` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afcd94"></a> `00afcd94` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afcd98"></a> `00afcd98` | `c8 51 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcd9c"></a> `00afcd9c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afcda0"></a> `00afcda0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afcda4"></a> `00afcda4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcda8"></a> `00afcda8` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afcdac"></a> `00afcdac` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afcdb0"></a> `00afcdb0` | `8c a9 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afcdb4"></a> `00afcdb4` | `40 01 00 37` | tbnz w0,#0x0,0x00afcddc | `CONDITIONAL_JUMP`
<a id="insn-00afcdb8"></a> `00afcdb8` | `c0 51 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcdbc"></a> `00afcdbc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcdc0"></a> `00afcdc0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcdc4"></a> `00afcdc4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcdc8"></a> `00afcdc8` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcdcc"></a> `00afcdcc` | `89 4c 89 52` | mov w9,#0x4a64 | `FALL_THROUGH`
<a id="insn-00afcdd0"></a> `00afcdd0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcdd4"></a> `00afcdd4` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcdd8"></a> `00afcdd8` | `02 00 00 14` | b 0x00afcde0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afcddc"></a> `00afcddc` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00afcde0"></a> `00afcde0` | `b6 51 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcde4"></a> `00afcde4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afcde8"></a> `00afcde8` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afcdec"></a> `00afcdec` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcdf0"></a> `00afcdf0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afcdf4"></a> `00afcdf4` | `7b a9 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afcdf8"></a> `00afcdf8` | `40 01 00 37` | tbnz w0,#0x0,0x00afce20 | `CONDITIONAL_JUMP`
<a id="insn-00afcdfc"></a> `00afcdfc` | `d4 02 14 0b` | add w20,w22,w20 | `FALL_THROUGH`
<a id="insn-00afce00"></a> `00afce00` | `ae 51 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afce04"></a> `00afce04` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afce08"></a> `00afce08` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afce0c"></a> `00afce0c` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afce10"></a> `00afce10` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afce14"></a> `00afce14` | `89 4c 89 52` | mov w9,#0x4a64 | `FALL_THROUGH`
<a id="insn-00afce18"></a> `00afce18` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afce1c"></a> `00afce1c` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afce20"></a> `00afce20` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afce24"></a> `00afce24` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afce28"></a> `00afce28` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afce2c"></a> `00afce2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcd7c`](#insn-00afcd7c) 範囲 `[['00afcd7c', '00afcdb7']]`
  - `CONDITIONAL_JUMP` [`00afcdb4`](#insn-00afcdb4) → [`00afcddc`](#insn-00afcddc)
  - `FALL_THROUGH` [`00afcdb4`](#insn-00afcdb4) → [`00afcdb8`](#insn-00afcdb8)
- ブロック [`00afcdb8`](#insn-00afcdb8) 範囲 `[['00afcdb8', '00afcddb']]`
  - `UNCONDITIONAL_JUMP` [`00afcdd8`](#insn-00afcdd8) → [`00afcde0`](#insn-00afcde0)
- ブロック [`00afcddc`](#insn-00afcddc) 範囲 `[['00afcddc', '00afcddf']]`
  - `FALL_THROUGH` [`00afcddc`](#insn-00afcddc) → [`00afcde0`](#insn-00afcde0)
- ブロック [`00afcde0`](#insn-00afcde0) 範囲 `[['00afcde0', '00afcdfb']]`
  - `CONDITIONAL_JUMP` [`00afcdf8`](#insn-00afcdf8) → [`00afce20`](#insn-00afce20)
  - `FALL_THROUGH` [`00afcdf8`](#insn-00afcdf8) → [`00afcdfc`](#insn-00afcdfc)
- ブロック [`00afcdfc`](#insn-00afcdfc) 範囲 `[['00afcdfc', '00afce1f']]`
  - `FALL_THROUGH` [`00afce1c`](#insn-00afce1c) → [`00afce20`](#insn-00afce20)
- ブロック [`00afce20`](#insn-00afce20) 範囲 `[['00afce20', '00afce2f']]`

## 命令位置別の参照

- [`00afcd7c`](#insn-00afcd7c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd80`](#insn-00afcd80) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd84`](#insn-00afcd84) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd98`](#insn-00afcd98) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcdb0`](#insn-00afcdb0) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afcdb4`](#insn-00afcdb4) → [`00afcddc`](#insn-00afcddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcdb8`](#insn-00afcdb8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcdd8`](#insn-00afcdd8) → [`00afcde0`](#insn-00afcde0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcde0`](#insn-00afcde0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcdf4`](#insn-00afcdf4) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afcdf8`](#insn-00afcdf8) → [`00afce20`](#insn-00afce20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce00`](#insn-00afce00) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afce20`](#insn-00afce20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce24`](#insn-00afce24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce28`](#insn-00afce28) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcd7c`](#insn-00afcd7c)

~~~json
{
  "source": "00afcd7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd80`](#insn-00afcd80)

~~~json
{
  "source": "00afcd80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd84`](#insn-00afcd84)

~~~json
{
  "source": "00afcd84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd98`](#insn-00afcd98)

~~~json
{
  "source": "00afcd98",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcdb0`](#insn-00afcdb0)

~~~json
{
  "source": "00afcdb0",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcdb4`](#insn-00afcdb4)

~~~json
{
  "source": "00afcdb4",
  "target": "00afcddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcdb8`](#insn-00afcdb8)

~~~json
{
  "source": "00afcdb8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcdd8`](#insn-00afcdd8)

~~~json
{
  "source": "00afcdd8",
  "target": "00afcde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcde0`](#insn-00afcde0)

~~~json
{
  "source": "00afcde0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcdf4`](#insn-00afcdf4)

~~~json
{
  "source": "00afcdf4",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcdf8`](#insn-00afcdf8)

~~~json
{
  "source": "00afcdf8",
  "target": "00afce20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce00`](#insn-00afce00)

~~~json
{
  "source": "00afce00",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afce20`](#insn-00afce20)

~~~json
{
  "source": "00afce20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce24`](#insn-00afce24)

~~~json
{
  "source": "00afce24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce28`](#insn-00afce28)

~~~json
{
  "source": "00afce28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
