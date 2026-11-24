# 00bced7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5f87c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f87c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0004.md#compare-005477b6d1a593740109b6a58a4e45c4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcf1a4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf1a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-611e80d7873d8a31284460540e9f9319)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bced7c",
  "name": "_ZN8firebase4auth4Auth12current_userEv",
  "size": 220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d363c7793845079a474c3a3aa265281b804cdf3c2c5436ad2c5d16709e57f8c7",
  "source_text_sha256": "d363c7793845079a474c3a3aa265281b804cdf3c2c5436ad2c5d16709e57f8c7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bced7c",
        "00bcee57"
      ]
    ],
    "bytes_sha256": "c56245d5c5588d100f4c92b81d48f76d2c661aa6a61ff2eb53acab596b3d2f92",
    "instruction_count": 55,
    "instruction_bytes": 220,
    "body_bytes": 220,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5a630](../00c5a/00c5a630.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5a640](../00c5a/00c5a640.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1436 bytes

~~~c

void _ZN8firebase4auth4Auth12current_userEv(long *param_1,long *param_2)

{
  long lVar1;
  undefined *puVar2;
  
  puVar2 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
  if (*param_2 == 0) {
    param_1[0x12] = 0;
    param_1[0x11] = 0;
    param_1[0x10] = 0;
    param_1[0xf] = 0;
    param_1[0xe] = 0;
    param_1[0xd] = 0;
    param_1[0xc] = 0;
    param_1[0xb] = 0;
    param_1[10] = 0;
    param_1[9] = 0;
    param_1[8] = 0;
    param_1[7] = 0;
    param_1[6] = 0;
    param_1[5] = 0;
    param_1[4] = 0;
    param_1[3] = 0;
    param_1[2] = 0;
    param_1[1] = 0;
    *param_1 = (long)(puVar2 + 0x10);
    param_1[0x13] = 0;
  }
  else {
    lVar1 = *param_2 + 0x18;
    _ZN8firebase5Mutex7AcquireEv(lVar1);
    puVar2 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
    if (*(long *)(*param_2 + 0x200) == 0) {
      param_1[0x12] = 0;
      param_1[0x11] = 0;
      param_1[0x10] = 0;
      param_1[0xf] = 0;
      param_1[0xe] = 0;
      param_1[0xd] = 0;
      param_1[0xc] = 0;
      param_1[0xb] = 0;
      param_1[10] = 0;
      param_1[9] = 0;
      param_1[8] = 0;
      param_1[7] = 0;
      param_1[6] = 0;
      param_1[5] = 0;
      param_1[4] = 0;
      param_1[3] = 0;
      param_1[2] = 0;
      param_1[1] = 0;
      *param_1 = (long)(puVar2 + 0x10);
      param_1[0x13] = 0;
    }
    else {
      _ZN8firebase4auth4UserC1ERKS1_(param_1,*param_2 + 0x158);
    }
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bced7c"></a> `00bced7c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bced80"></a> `00bced80` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bced84"></a> `00bced84` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bced88"></a> `00bced88` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bced8c"></a> `00bced8c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bced90"></a> `00bced90` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bced94"></a> `00bced94` | `89 01 00 b4` | cbz x9,0x00bcedc4 | `CONDITIONAL_JUMP`
<a id="insn-00bced98"></a> `00bced98` | `34 61 00 91` | add x20,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00bced9c"></a> `00bced9c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bceda0"></a> `00bceda0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bceda4"></a> `00bceda4` | `17 2e 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bceda8"></a> `00bceda8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcedac"></a> `00bcedac` | `09 01 41 f9` | ldr x9,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bcedb0"></a> `00bcedb0` | `a9 02 00 b4` | cbz x9,0x00bcee04 | `CONDITIONAL_JUMP`
<a id="insn-00bcedb4"></a> `00bcedb4` | `01 61 05 91` | add x1,x8,#0x158 | `FALL_THROUGH`
<a id="insn-00bcedb8"></a> `00bcedb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcedbc"></a> `00bcedbc` | `21 2e 02 94` | bl 0x00c5a640 | `UNCONDITIONAL_CALL`
<a id="insn-00bcedc0"></a> `00bcedc0` | `20 00 00 14` | b 0x00bcee40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcedc4"></a> `00bcedc4` | `68 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcedc8"></a> `00bcedc8` | `08 e1 42 f9` | ldr x8,[x8, #0x5c0] | `FALL_THROUGH`
<a id="insn-00bcedcc"></a> `00bcedcc` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bcedd0"></a> `00bcedd0` | `60 82 88 3c` | stur q0,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bcedd4"></a> `00bcedd4` | `60 82 87 3c` | stur q0,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bcedd8"></a> `00bcedd8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bceddc"></a> `00bceddc` | `60 82 86 3c` | stur q0,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bcede0"></a> `00bcede0` | `60 82 85 3c` | stur q0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bcede4"></a> `00bcede4` | `60 82 84 3c` | stur q0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bcede8"></a> `00bcede8` | `60 82 83 3c` | stur q0,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bcedec"></a> `00bcedec` | `60 82 82 3c` | stur q0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcedf0"></a> `00bcedf0` | `60 82 81 3c` | stur q0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bcedf4"></a> `00bcedf4` | `60 82 80 3c` | stur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcedf8"></a> `00bcedf8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcedfc"></a> `00bcedfc` | `7f 4e 00 f9` | str xzr,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00bcee00"></a> `00bcee00` | `12 00 00 14` | b 0x00bcee48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcee04"></a> `00bcee04` | `68 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcee08"></a> `00bcee08` | `08 e1 42 f9` | ldr x8,[x8, #0x5c0] | `FALL_THROUGH`
<a id="insn-00bcee0c"></a> `00bcee0c` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bcee10"></a> `00bcee10` | `60 82 88 3c` | stur q0,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bcee14"></a> `00bcee14` | `60 82 87 3c` | stur q0,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bcee18"></a> `00bcee18` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcee1c"></a> `00bcee1c` | `60 82 86 3c` | stur q0,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bcee20"></a> `00bcee20` | `60 82 85 3c` | stur q0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bcee24"></a> `00bcee24` | `60 82 84 3c` | stur q0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bcee28"></a> `00bcee28` | `60 82 83 3c` | stur q0,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bcee2c"></a> `00bcee2c` | `60 82 82 3c` | stur q0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcee30"></a> `00bcee30` | `60 82 81 3c` | stur q0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bcee34"></a> `00bcee34` | `60 82 80 3c` | stur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcee38"></a> `00bcee38` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcee3c"></a> `00bcee3c` | `7f 4e 00 f9` | str xzr,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00bcee40"></a> `00bcee40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcee44"></a> `00bcee44` | `f3 2d 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bcee48"></a> `00bcee48` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcee4c"></a> `00bcee4c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcee50"></a> `00bcee50` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcee54"></a> `00bcee54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bced7c`](#insn-00bced7c) 範囲 `[['00bced7c', '00bced97']]`
  - `CONDITIONAL_JUMP` [`00bced94`](#insn-00bced94) → [`00bcedc4`](#insn-00bcedc4)
  - `FALL_THROUGH` [`00bced94`](#insn-00bced94) → [`00bced98`](#insn-00bced98)
- ブロック [`00bced98`](#insn-00bced98) 範囲 `[['00bced98', '00bcedb3']]`
  - `CONDITIONAL_JUMP` [`00bcedb0`](#insn-00bcedb0) → [`00bcee04`](#insn-00bcee04)
  - `FALL_THROUGH` [`00bcedb0`](#insn-00bcedb0) → [`00bcedb4`](#insn-00bcedb4)
- ブロック [`00bcedb4`](#insn-00bcedb4) 範囲 `[['00bcedb4', '00bcedc3']]`
  - `UNCONDITIONAL_JUMP` [`00bcedc0`](#insn-00bcedc0) → [`00bcee40`](#insn-00bcee40)
- ブロック [`00bcedc4`](#insn-00bcedc4) 範囲 `[['00bcedc4', '00bcee03']]`
  - `UNCONDITIONAL_JUMP` [`00bcee00`](#insn-00bcee00) → [`00bcee48`](#insn-00bcee48)
- ブロック [`00bcee04`](#insn-00bcee04) 範囲 `[['00bcee04', '00bcee3f']]`
  - `FALL_THROUGH` [`00bcee3c`](#insn-00bcee3c) → [`00bcee40`](#insn-00bcee40)
- ブロック [`00bcee40`](#insn-00bcee40) 範囲 `[['00bcee40', '00bcee47']]`
  - `FALL_THROUGH` [`00bcee44`](#insn-00bcee44) → [`00bcee48`](#insn-00bcee48)
- ブロック [`00bcee48`](#insn-00bcee48) 範囲 `[['00bcee48', '00bcee57']]`

## 命令位置別の参照

- [`00bced7c`](#insn-00bced7c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced80`](#insn-00bced80) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced84`](#insn-00bced84) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced94`](#insn-00bced94) → [`00bcedc4`](#insn-00bcedc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceda4`](#insn-00bceda4) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcedb0`](#insn-00bcedb0) → [`00bcee04`](#insn-00bcee04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedbc`](#insn-00bcedbc) → [`00c5a640`](../00c5a/00c5a640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a640` · 推定シンボル `None` · 推定型 `None`
- [`00bcedc0`](#insn-00bcedc0) → [`00bcee40`](#insn-00bcee40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcedc8`](#insn-00bcedc8) → `00c9b5c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcedf8`](#insn-00bcedf8) → `00c924a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bcee00`](#insn-00bcee00) → [`00bcee48`](#insn-00bcee48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee08`](#insn-00bcee08) → `00c9b5c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcee38`](#insn-00bcee38) → `00c924a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bcee44`](#insn-00bcee44) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcee48`](#insn-00bcee48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcee4c`](#insn-00bcee4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bced7c`](#insn-00bced7c)

~~~json
{
  "source": "00bced7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced80`](#insn-00bced80)

~~~json
{
  "source": "00bced80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced84`](#insn-00bced84)

~~~json
{
  "source": "00bced84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced94`](#insn-00bced94)

~~~json
{
  "source": "00bced94",
  "target": "00bcedc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceda4`](#insn-00bceda4)

~~~json
{
  "source": "00bceda4",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedb0`](#insn-00bcedb0)

~~~json
{
  "source": "00bcedb0",
  "target": "00bcee04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedbc`](#insn-00bcedbc)

~~~json
{
  "source": "00bcedbc",
  "target": "00c5a640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcedc0`](#insn-00bcedc0)

~~~json
{
  "source": "00bcedc0",
  "target": "00bcee40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcedc8`](#insn-00bcedc8)

~~~json
{
  "source": "00bcedc8",
  "target": "00c9b5c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcedf8`](#insn-00bcedf8)

~~~json
{
  "source": "00bcedf8",
  "target": "00c924a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92498",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bcee00`](#insn-00bcee00)

~~~json
{
  "source": "00bcee00",
  "target": "00bcee48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee08`](#insn-00bcee08)

~~~json
{
  "source": "00bcee08",
  "target": "00c9b5c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcee38`](#insn-00bcee38)

~~~json
{
  "source": "00bcee38",
  "target": "00c924a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92498",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bcee44`](#insn-00bcee44)

~~~json
{
  "source": "00bcee44",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcee48`](#insn-00bcee48)

~~~json
{
  "source": "00bcee48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcee4c`](#insn-00bcee4c)

~~~json
{
  "source": "00bcee4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
