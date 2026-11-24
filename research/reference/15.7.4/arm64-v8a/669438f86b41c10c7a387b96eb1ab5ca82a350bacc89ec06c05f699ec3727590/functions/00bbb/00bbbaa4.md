# 00bbbaa4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbba60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-88c5717465e408885f0281f3d69f8d9a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c384ec`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c384ec.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-778f8ce2994dc64850c16aaa30fd01e8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbaa4",
  "name": "FUN_00bbbaa4",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56a60a2436559fdbfca3f0fc0abb78b208725c1c07588ba6df78f60c5fdd81c4",
  "source_text_sha256": "56a60a2436559fdbfca3f0fc0abb78b208725c1c07588ba6df78f60c5fdd81c4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbaa4",
        "00bbbb4f"
      ]
    ],
    "bytes_sha256": "b0b4ee161baa25af27ba352fa08b95cff3621e4ec0d5a2abfa7318242bf585e3",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb7c0](../00bdb/00bdb7c0.md)
- [00bde9d0](../00bde/00bde9d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 658 bytes

~~~c

bool FUN_00bbbaa4(long param_1,long param_2)

{
  int iVar1;
  long lVar2;
  
  if ((*(byte *)(param_1 + 0x10) & 0x18) == 0) {
    if (param_2 == 0) {
      return false;
    }
    lVar2 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                           PTR__ZTIN10__cxxabiv117__pbase_type_infoE_00c1c058,0);
    if (lVar2 == 0) {
      return false;
    }
    if ((*(byte *)(lVar2 + 0x10) & 0x18) == 0) {
      return *(long *)(param_1 + 8) == *(long *)(param_2 + 8);
    }
  }
  if (param_1 != param_2) {
    iVar1 = strcmp(*(char **)(param_1 + 8),*(char **)(param_2 + 8));
    return iVar1 == 0;
  }
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbaa4"></a> `00bbbaa4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbbaa8"></a> `00bbbaa8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbbaac"></a> `00bbbaac` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbab0"></a> `00bbbab0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbab4"></a> `00bbbab4` | `08 40 40 39` | ldrb w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbab8"></a> `00bbbab8` | `1f 05 1d 72` | tst w8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbabc"></a> `00bbbabc` | `20 01 00 54` | b.eq 0x00bbbae0 | `CONDITIONAL_JUMP`
<a id="insn-00bbbac0"></a> `00bbbac0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bbbac4"></a> `00bbbac4` | `80 03 00 54` | b.eq 0x00bbbb34 | `CONDITIONAL_JUMP`
<a id="insn-00bbbac8"></a> `00bbbac8` | `00 04 40 f9` | ldr x0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbacc"></a> `00bbbacc` | `21 04 40 f9` | ldr x1,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbad0"></a> `00bbbad0` | `c0 8b 00 94` | bl 0x00bde9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbad4"></a> `00bbbad4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bbbad8"></a> `00bbbad8` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbbadc"></a> `00bbbadc` | `19 00 00 14` | b 0x00bbbb40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbae0"></a> `00bbbae0` | `e1 02 00 b4` | cbz x1,0x00bbbb3c | `CONDITIONAL_JUMP`
<a id="insn-00bbbae4"></a> `00bbbae4` | `08 03 00 b0` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbae8"></a> `00bbbae8` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbaec"></a> `00bbbaec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbbaf0"></a> `00bbbaf0` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bbbaf4"></a> `00bbbaf4` | `42 2c 40 f9` | ldr x2,[x2, #0x58] | `FALL_THROUGH`
<a id="insn-00bbbaf8"></a> `00bbbaf8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbbafc"></a> `00bbbafc` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbbb00"></a> `00bbbb00` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbb04"></a> `00bbbb04` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bbbb08"></a> `00bbbb08` | `2e 7f 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb0c"></a> `00bbbb0c` | `a0 01 00 b4` | cbz x0,0x00bbbb40 | `CONDITIONAL_JUMP`
<a id="insn-00bbbb10"></a> `00bbbb10` | `08 40 40 39` | ldrb w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbb14"></a> `00bbbb14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbb18"></a> `00bbbb18` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbbb1c"></a> `00bbbb1c` | `1f 05 1d 72` | tst w8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbb20"></a> `00bbbb20` | `01 fd ff 54` | b.ne 0x00bbbac0 | `CONDITIONAL_JUMP`
<a id="insn-00bbbb24"></a> `00bbbb24` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbb28"></a> `00bbbb28` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbb2c"></a> `00bbbb2c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbb30"></a> `00bbbb30` | `ea ff ff 17` | b 0x00bbbad8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbb34"></a> `00bbbb34` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbb38"></a> `00bbbb38` | `02 00 00 14` | b 0x00bbbb40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbb3c"></a> `00bbbb3c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbbb40"></a> `00bbbb40` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbb44"></a> `00bbbb44` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbbb48"></a> `00bbbb48` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbb4c"></a> `00bbbb4c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbaa4`](#insn-00bbbaa4) 範囲 `[['00bbbaa4', '00bbbabf']]`
  - `CONDITIONAL_JUMP` [`00bbbabc`](#insn-00bbbabc) → [`00bbbae0`](#insn-00bbbae0)
  - `FALL_THROUGH` [`00bbbabc`](#insn-00bbbabc) → [`00bbbac0`](#insn-00bbbac0)
- ブロック [`00bbbac0`](#insn-00bbbac0) 範囲 `[['00bbbac0', '00bbbac7']]`
  - `CONDITIONAL_JUMP` [`00bbbac4`](#insn-00bbbac4) → [`00bbbb34`](#insn-00bbbb34)
  - `FALL_THROUGH` [`00bbbac4`](#insn-00bbbac4) → [`00bbbac8`](#insn-00bbbac8)
- ブロック [`00bbbac8`](#insn-00bbbac8) 範囲 `[['00bbbac8', '00bbbad7']]`
  - `FALL_THROUGH` [`00bbbad4`](#insn-00bbbad4) → [`00bbbad8`](#insn-00bbbad8)
- ブロック [`00bbbad8`](#insn-00bbbad8) 範囲 `[['00bbbad8', '00bbbadf']]`
  - `UNCONDITIONAL_JUMP` [`00bbbadc`](#insn-00bbbadc) → [`00bbbb40`](#insn-00bbbb40)
- ブロック [`00bbbae0`](#insn-00bbbae0) 範囲 `[['00bbbae0', '00bbbae3']]`
  - `CONDITIONAL_JUMP` [`00bbbae0`](#insn-00bbbae0) → [`00bbbb3c`](#insn-00bbbb3c)
  - `FALL_THROUGH` [`00bbbae0`](#insn-00bbbae0) → [`00bbbae4`](#insn-00bbbae4)
- ブロック [`00bbbae4`](#insn-00bbbae4) 範囲 `[['00bbbae4', '00bbbb0f']]`
  - `CONDITIONAL_JUMP` [`00bbbb0c`](#insn-00bbbb0c) → [`00bbbb40`](#insn-00bbbb40)
  - `FALL_THROUGH` [`00bbbb0c`](#insn-00bbbb0c) → [`00bbbb10`](#insn-00bbbb10)
- ブロック [`00bbbb10`](#insn-00bbbb10) 範囲 `[['00bbbb10', '00bbbb23']]`
  - `CONDITIONAL_JUMP` [`00bbbb20`](#insn-00bbbb20) → [`00bbbac0`](#insn-00bbbac0)
  - `FALL_THROUGH` [`00bbbb20`](#insn-00bbbb20) → [`00bbbb24`](#insn-00bbbb24)
- ブロック [`00bbbb24`](#insn-00bbbb24) 範囲 `[['00bbbb24', '00bbbb33']]`
  - `UNCONDITIONAL_JUMP` [`00bbbb30`](#insn-00bbbb30) → [`00bbbad8`](#insn-00bbbad8)
- ブロック [`00bbbb34`](#insn-00bbbb34) 範囲 `[['00bbbb34', '00bbbb3b']]`
  - `UNCONDITIONAL_JUMP` [`00bbbb38`](#insn-00bbbb38) → [`00bbbb40`](#insn-00bbbb40)
- ブロック [`00bbbb3c`](#insn-00bbbb3c) 範囲 `[['00bbbb3c', '00bbbb3f']]`
  - `FALL_THROUGH` [`00bbbb3c`](#insn-00bbbb3c) → [`00bbbb40`](#insn-00bbbb40)
- ブロック [`00bbbb40`](#insn-00bbbb40) 範囲 `[['00bbbb40', '00bbbb4f']]`

## 命令位置別の参照

- [`00bbbaa8`](#insn-00bbbaa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbaac`](#insn-00bbbaac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbabc`](#insn-00bbbabc) → [`00bbbae0`](#insn-00bbbae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbac4`](#insn-00bbbac4) → [`00bbbb34`](#insn-00bbbb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbad0`](#insn-00bbbad0) → [`00bde9d0`](../00bde/00bde9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbadc`](#insn-00bbbadc) → [`00bbbb40`](#insn-00bbbb40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbae0`](#insn-00bbbae0) → [`00bbbb3c`](#insn-00bbbb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbaf0`](#insn-00bbbaf0) → `00c1c048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbaf4`](#insn-00bbbaf4) → `00c1c058`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbaf4`](#insn-00bbbaf4) → `00c16c40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv117__pbase_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbb04`](#insn-00bbbb04) → `00c16c10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbb08`](#insn-00bbbb08) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb0c`](#insn-00bbbb0c) → [`00bbbb40`](#insn-00bbbb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb20`](#insn-00bbbb20) → [`00bbbac0`](#insn-00bbbac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb30`](#insn-00bbbb30) → [`00bbbad8`](#insn-00bbbad8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb38`](#insn-00bbbb38) → [`00bbbb40`](#insn-00bbbb40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb40`](#insn-00bbbb40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb44`](#insn-00bbbb44) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbaa8`](#insn-00bbbaa8)

~~~json
{
  "source": "00bbbaa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbaac`](#insn-00bbbaac)

~~~json
{
  "source": "00bbbaac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbabc`](#insn-00bbbabc)

~~~json
{
  "source": "00bbbabc",
  "target": "00bbbae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbac4`](#insn-00bbbac4)

~~~json
{
  "source": "00bbbac4",
  "target": "00bbbb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbad0`](#insn-00bbbad0)

~~~json
{
  "source": "00bbbad0",
  "target": "00bde9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbadc`](#insn-00bbbadc)

~~~json
{
  "source": "00bbbadc",
  "target": "00bbbb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbae0`](#insn-00bbbae0)

~~~json
{
  "source": "00bbbae0",
  "target": "00bbbb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbaf0`](#insn-00bbbaf0)

~~~json
{
  "source": "00bbbaf0",
  "target": "00c1c048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c048",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbaf4`](#insn-00bbbaf4)

~~~json
{
  "source": "00bbbaf4",
  "target": "00c1c058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c058",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbaf4`](#insn-00bbbaf4)

~~~json
{
  "source": "00bbbaf4",
  "target": "00c16c40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbb04`](#insn-00bbbb04)

~~~json
{
  "source": "00bbbb04",
  "target": "00c16c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbb08`](#insn-00bbbb08)

~~~json
{
  "source": "00bbbb08",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb0c`](#insn-00bbbb0c)

~~~json
{
  "source": "00bbbb0c",
  "target": "00bbbb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb20`](#insn-00bbbb20)

~~~json
{
  "source": "00bbbb20",
  "target": "00bbbac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb30`](#insn-00bbbb30)

~~~json
{
  "source": "00bbbb30",
  "target": "00bbbad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb38`](#insn-00bbbb38)

~~~json
{
  "source": "00bbbb38",
  "target": "00bbbb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb40`](#insn-00bbbb40)

~~~json
{
  "source": "00bbbb40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb44`](#insn-00bbbb44)

~~~json
{
  "source": "00bbbb44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
