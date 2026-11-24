# 00ae0dec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0162.md#review-c63c19c746a62e0140f816168e98adb5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ae1214`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae1214.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-173fc949e2508bd10b98f44b83dbe15e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae0dec",
  "name": "FUN_00ae0dec",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b5e46ff9d5aae287c454a1b048d54c82af0b68df633822709c6c49effd7b486",
  "source_text_sha256": "8b5e46ff9d5aae287c454a1b048d54c82af0b68df633822709c6c49effd7b486",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae0dec",
        "00ae0e63"
      ]
    ],
    "bytes_sha256": "13d26e1aa76a32da8860046541760bf85d4e09b2619a68dc3181d438a30a3460",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad6d50](../00ad6/00ad6d50.md)

## 呼び出し先

- [009df498](../009df/009df498.md)
- [009e0e24](../009e0/009e0e24.md)
- [009e2df8](../009e2/009e2df8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 557 bytes

~~~c

void FUN_00ae0dec(long param_1,int param_2,undefined4 param_3)

{
  ulong uVar1;
  long lVar2;
  undefined4 *puVar3;
  
  uVar1 = FUN_009e0e24(param_1 + 0x50,0xffffffff,0xffffffff);
  if ((uVar1 & 1) == 0) {
    puVar3 = (undefined4 *)(param_1 + (long)param_2 * 4 + 0x49934);
  }
  else {
    lVar2 = FUN_009e2df8(param_1 + 0x50,0xffffffff,0xffffffff);
    if (lVar2 == 0) {
      return;
    }
    lVar2 = FUN_009df498(lVar2,param_2);
    if (lVar2 == 0) {
      return;
    }
    puVar3 = (undefined4 *)(lVar2 + 4);
  }
  *puVar3 = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae0dec"></a> `00ae0dec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ae0df0"></a> `00ae0df0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0df4"></a> `00ae0df4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae0df8"></a> `00ae0df8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ae0dfc"></a> `00ae0dfc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00ae0e00"></a> `00ae0e00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00ae0e04"></a> `00ae0e04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ae0e08"></a> `00ae0e08` | `00 40 01 91` | add x0,x0,#0x50 | `FALL_THROUGH`
<a id="insn-00ae0e0c"></a> `00ae0e0c` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ae0e10"></a> `00ae0e10` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ae0e14"></a> `00ae0e14` | `04 00 fc 97` | bl 0x009e0e24 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0e18"></a> `00ae0e18` | `60 01 00 36` | tbz w0,#0x0,0x00ae0e44 | `CONDITIONAL_JUMP`
<a id="insn-00ae0e1c"></a> `00ae0e1c` | `a0 42 01 91` | add x0,x21,#0x50 | `FALL_THROUGH`
<a id="insn-00ae0e20"></a> `00ae0e20` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ae0e24"></a> `00ae0e24` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ae0e28"></a> `00ae0e28` | `f4 07 fc 97` | bl 0x009e2df8 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0e2c"></a> `00ae0e2c` | `40 01 00 b4` | cbz x0,0x00ae0e54 | `CONDITIONAL_JUMP`
<a id="insn-00ae0e30"></a> `00ae0e30` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ae0e34"></a> `00ae0e34` | `99 f9 fb 97` | bl 0x009df498 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0e38"></a> `00ae0e38` | `e0 00 00 b4` | cbz x0,0x00ae0e54 | `CONDITIONAL_JUMP`
<a id="insn-00ae0e3c"></a> `00ae0e3c` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00ae0e40"></a> `00ae0e40` | `04 00 00 14` | b 0x00ae0e50 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae0e44"></a> `00ae0e44` | `a8 ca 34 8b` | add x8,x21,w20, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00ae0e48"></a> `00ae0e48` | `08 25 41 91` | add x8,x8,#0x49, LSL #12 | `FALL_THROUGH`
<a id="insn-00ae0e4c"></a> `00ae0e4c` | `08 d1 24 91` | add x8,x8,#0x934 | `FALL_THROUGH`
<a id="insn-00ae0e50"></a> `00ae0e50` | `13 01 00 b9` | str w19,[x8] | `FALL_THROUGH`
<a id="insn-00ae0e54"></a> `00ae0e54` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae0e58"></a> `00ae0e58` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0e5c"></a> `00ae0e5c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ae0e60"></a> `00ae0e60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae0dec`](#insn-00ae0dec) 範囲 `[['00ae0dec', '00ae0e1b']]`
  - `CONDITIONAL_JUMP` [`00ae0e18`](#insn-00ae0e18) → [`00ae0e44`](#insn-00ae0e44)
  - `FALL_THROUGH` [`00ae0e18`](#insn-00ae0e18) → [`00ae0e1c`](#insn-00ae0e1c)
- ブロック [`00ae0e1c`](#insn-00ae0e1c) 範囲 `[['00ae0e1c', '00ae0e2f']]`
  - `CONDITIONAL_JUMP` [`00ae0e2c`](#insn-00ae0e2c) → [`00ae0e54`](#insn-00ae0e54)
  - `FALL_THROUGH` [`00ae0e2c`](#insn-00ae0e2c) → [`00ae0e30`](#insn-00ae0e30)
- ブロック [`00ae0e30`](#insn-00ae0e30) 範囲 `[['00ae0e30', '00ae0e3b']]`
  - `CONDITIONAL_JUMP` [`00ae0e38`](#insn-00ae0e38) → [`00ae0e54`](#insn-00ae0e54)
  - `FALL_THROUGH` [`00ae0e38`](#insn-00ae0e38) → [`00ae0e3c`](#insn-00ae0e3c)
- ブロック [`00ae0e3c`](#insn-00ae0e3c) 範囲 `[['00ae0e3c', '00ae0e43']]`
  - `UNCONDITIONAL_JUMP` [`00ae0e40`](#insn-00ae0e40) → [`00ae0e50`](#insn-00ae0e50)
- ブロック [`00ae0e44`](#insn-00ae0e44) 範囲 `[['00ae0e44', '00ae0e4f']]`
  - `FALL_THROUGH` [`00ae0e4c`](#insn-00ae0e4c) → [`00ae0e50`](#insn-00ae0e50)
- ブロック [`00ae0e50`](#insn-00ae0e50) 範囲 `[['00ae0e50', '00ae0e53']]`
  - `FALL_THROUGH` [`00ae0e50`](#insn-00ae0e50) → [`00ae0e54`](#insn-00ae0e54)
- ブロック [`00ae0e54`](#insn-00ae0e54) 範囲 `[['00ae0e54', '00ae0e63']]`

## 命令位置別の参照

- [`00ae0dec`](#insn-00ae0dec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0df0`](#insn-00ae0df0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0df4`](#insn-00ae0df4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e14`](#insn-00ae0e14) → [`009e0e24`](../009e0/009e0e24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e0e24` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e18`](#insn-00ae0e18) → [`00ae0e44`](#insn-00ae0e44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e28`](#insn-00ae0e28) → [`009e2df8`](../009e2/009e2df8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e2df8` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e2c`](#insn-00ae0e2c) → [`00ae0e54`](#insn-00ae0e54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e34`](#insn-00ae0e34) → [`009df498`](../009df/009df498.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009df498` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e38`](#insn-00ae0e38) → [`00ae0e54`](#insn-00ae0e54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e40`](#insn-00ae0e40) → [`00ae0e50`](#insn-00ae0e50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e54`](#insn-00ae0e54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e58`](#insn-00ae0e58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e5c`](#insn-00ae0e5c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae0dec`](#insn-00ae0dec)

~~~json
{
  "source": "00ae0dec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0df0`](#insn-00ae0df0)

~~~json
{
  "source": "00ae0df0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0df4`](#insn-00ae0df4)

~~~json
{
  "source": "00ae0df4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e14`](#insn-00ae0e14)

~~~json
{
  "source": "00ae0e14",
  "target": "009e0e24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0e18`](#insn-00ae0e18)

~~~json
{
  "source": "00ae0e18",
  "target": "00ae0e44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e28`](#insn-00ae0e28)

~~~json
{
  "source": "00ae0e28",
  "target": "009e2df8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0e2c`](#insn-00ae0e2c)

~~~json
{
  "source": "00ae0e2c",
  "target": "00ae0e54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e34`](#insn-00ae0e34)

~~~json
{
  "source": "00ae0e34",
  "target": "009df498",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0e38`](#insn-00ae0e38)

~~~json
{
  "source": "00ae0e38",
  "target": "00ae0e54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e40`](#insn-00ae0e40)

~~~json
{
  "source": "00ae0e40",
  "target": "00ae0e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e54`](#insn-00ae0e54)

~~~json
{
  "source": "00ae0e54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e58`](#insn-00ae0e58)

~~~json
{
  "source": "00ae0e58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e5c`](#insn-00ae0e5c)

~~~json
{
  "source": "00ae0e5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
