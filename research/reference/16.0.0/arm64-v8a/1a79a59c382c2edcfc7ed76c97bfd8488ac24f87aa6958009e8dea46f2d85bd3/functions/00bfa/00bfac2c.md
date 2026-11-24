# 00bfac2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e1e4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0018.md#compare-b4fd68a7208fb2fe034f47c2d06bc0c1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb054`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb054.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-eeb946eadbee1fd43aa28901bc0659b0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfac2c",
  "name": "_ZNSt6__ndk18ios_base5imbueERKNS_6localeE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d9e5bb60ea2e2c4bc05be3b4c65291d3c76f4ff04febc80bad695972007c688c",
  "source_text_sha256": "d9e5bb60ea2e2c4bc05be3b4c65291d3c76f4ff04febc80bad695972007c688c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfac2c",
        "00bfaca7"
      ]
    ],
    "bytes_sha256": "0142c824147ff758af615fc28090bf4aedf55b54e16ae2b1097a2718a6cdd3a5",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a3d0](../00c5a/00c5a3d0.md)
- [00c5dee0](../00c5d/00c5dee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 536 bytes

~~~c

void _ZNSt6__ndk18ios_base5imbueERKNS_6localeE(undefined8 param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 0x30);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 0x30,param_3);
  if (*(long *)(param_2 + 0x48) != 0) {
    lVar1 = *(long *)(param_2 + 0x48) + -1;
    do {
      (**(code **)(*(long *)(param_2 + 0x38) + lVar1 * 8))
                (1,param_2,*(undefined4 *)(*(long *)(param_2 + 0x40) + lVar1 * 4));
      lVar1 = lVar1 + -1;
    } while (lVar1 != -1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfac2c"></a> `00bfac2c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfac30"></a> `00bfac30` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfac34"></a> `00bfac34` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfac38"></a> `00bfac38` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfac3c"></a> `00bfac3c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfac40"></a> `00bfac40` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfac44"></a> `00bfac44` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfac48"></a> `00bfac48` | `01 c0 00 91` | add x1,x0,#0x30 | `FALL_THROUGH`
<a id="insn-00bfac4c"></a> `00bfac4c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bfac50"></a> `00bfac50` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bfac54"></a> `00bfac54` | `df 7d 01 94` | bl 0x00c5a3d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfac58"></a> `00bfac58` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bfac5c"></a> `00bfac5c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bfac60"></a> `00bfac60` | `a0 8c 01 94` | bl 0x00c5dee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfac64"></a> `00bfac64` | `88 26 40 f9` | ldr x8,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bfac68"></a> `00bfac68` | `68 01 00 b4` | cbz x8,0x00bfac94 | `CONDITIONAL_JUMP`
<a id="insn-00bfac6c"></a> `00bfac6c` | `15 05 00 d1` | sub x21,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfac70"></a> `00bfac70` | `88 a6 43 a9` | ldp x8,x9,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bfac74"></a> `00bfac74` | `08 79 75 f8` | ldr x8,[x8, x21, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bfac78"></a> `00bfac78` | `22 79 75 b8` | ldr w2,[x9, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00bfac7c"></a> `00bfac7c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfac80"></a> `00bfac80` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfac84"></a> `00bfac84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfac88"></a> `00bfac88` | `b5 06 00 d1` | sub x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfac8c"></a> `00bfac8c` | `bf 06 00 b1` | cmn x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfac90"></a> `00bfac90` | `01 ff ff 54` | b.ne 0x00bfac70 | `CONDITIONAL_JUMP`
<a id="insn-00bfac94"></a> `00bfac94` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfac98"></a> `00bfac98` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfac9c"></a> `00bfac9c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfaca0"></a> `00bfaca0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfaca4"></a> `00bfaca4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfac2c`](#insn-00bfac2c) 範囲 `[['00bfac2c', '00bfac6b']]`
  - `CONDITIONAL_JUMP` [`00bfac68`](#insn-00bfac68) → [`00bfac94`](#insn-00bfac94)
  - `FALL_THROUGH` [`00bfac68`](#insn-00bfac68) → [`00bfac6c`](#insn-00bfac6c)
- ブロック [`00bfac6c`](#insn-00bfac6c) 範囲 `[['00bfac6c', '00bfac6f']]`
  - `FALL_THROUGH` [`00bfac6c`](#insn-00bfac6c) → [`00bfac70`](#insn-00bfac70)
- ブロック [`00bfac70`](#insn-00bfac70) 範囲 `[['00bfac70', '00bfac93']]`
  - `CONDITIONAL_JUMP` [`00bfac90`](#insn-00bfac90) → [`00bfac70`](#insn-00bfac70)
  - `FALL_THROUGH` [`00bfac90`](#insn-00bfac90) → [`00bfac94`](#insn-00bfac94)
- ブロック [`00bfac94`](#insn-00bfac94) 範囲 `[['00bfac94', '00bfaca7']]`

## 命令位置別の参照

- [`00bfac30`](#insn-00bfac30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac34`](#insn-00bfac34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac38`](#insn-00bfac38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac54`](#insn-00bfac54) → [`00c5a3d0`](../00c5a/00c5a3d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a3d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfac60`](#insn-00bfac60) → [`00c5dee0`](../00c5d/00c5dee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dee0` · 推定シンボル `None` · 推定型 `None`
- [`00bfac68`](#insn-00bfac68) → [`00bfac94`](#insn-00bfac94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac90`](#insn-00bfac90) → [`00bfac70`](#insn-00bfac70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac94`](#insn-00bfac94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac98`](#insn-00bfac98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac9c`](#insn-00bfac9c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfac30`](#insn-00bfac30)

~~~json
{
  "source": "00bfac30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac34`](#insn-00bfac34)

~~~json
{
  "source": "00bfac34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac38`](#insn-00bfac38)

~~~json
{
  "source": "00bfac38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac54`](#insn-00bfac54)

~~~json
{
  "source": "00bfac54",
  "target": "00c5a3d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfac60`](#insn-00bfac60)

~~~json
{
  "source": "00bfac60",
  "target": "00c5dee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfac68`](#insn-00bfac68)

~~~json
{
  "source": "00bfac68",
  "target": "00bfac94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac90`](#insn-00bfac90)

~~~json
{
  "source": "00bfac90",
  "target": "00bfac70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac94`](#insn-00bfac94)

~~~json
{
  "source": "00bfac94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac98`](#insn-00bfac98)

~~~json
{
  "source": "00bfac98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac9c`](#insn-00bfac9c)

~~~json
{
  "source": "00bfac9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
