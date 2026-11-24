# 00bfa0ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfa010`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-279147a0ae6f7584e859d1a380038e44)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfb0a0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb0a0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-214612c03e5c6b060feae361339b2336)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa0ac",
  "name": "_ZNSt6__ndk113shared_futureIvEaSERKS1_",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "025e8e772dc6c446a390998dfe43922d41068911f837d42517d5acc7c4759a05",
  "source_text_sha256": "025e8e772dc6c446a390998dfe43922d41068911f837d42517d5acc7c4759a05",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa0ac",
        "00bfa123"
      ]
    ],
    "bytes_sha256": "9059070e07c053dc1695627ffdeaa259004c8ce8fb06cfa2dd38dec86a740cb1",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 397 bytes

~~~c

long * _ZNSt6__ndk113shared_futureIvEaSERKS1_(long *param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  
  if (*param_2 != 0) {
    FUN_00c53d70(1,*param_2 + 8);
  }
  plVar2 = (long *)*param_1;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
  }
  *param_1 = *param_2;
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa0ac"></a> `00bfa0ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa0b0"></a> `00bfa0b0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfa0b4"></a> `00bfa0b4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa0b8"></a> `00bfa0b8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfa0bc"></a> `00bfa0bc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa0c0"></a> `00bfa0c0` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bfa0c4"></a> `00bfa0c4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfa0c8"></a> `00bfa0c8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfa0cc"></a> `00bfa0cc` | `88 00 00 b4` | cbz x8,0x00bfa0dc | `CONDITIONAL_JUMP`
<a id="insn-00bfa0d0"></a> `00bfa0d0` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bfa0d4"></a> `00bfa0d4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfa0d8"></a> `00bfa0d8` | `26 67 01 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa0dc"></a> `00bfa0dc` | `75 02 40 f9` | ldr x21,[x19] | `FALL_THROUGH`
<a id="insn-00bfa0e0"></a> `00bfa0e0` | `35 01 00 b4` | cbz x21,0x00bfa104 | `CONDITIONAL_JUMP`
<a id="insn-00bfa0e4"></a> `00bfa0e4` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bfa0e8"></a> `00bfa0e8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00bfa0ec"></a> `00bfa0ec` | `2d 67 01 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa0f0"></a> `00bfa0f0` | `a0 00 00 b5` | cbnz x0,0x00bfa104 | `CONDITIONAL_JUMP`
<a id="insn-00bfa0f4"></a> `00bfa0f4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bfa0f8"></a> `00bfa0f8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfa0fc"></a> `00bfa0fc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa100"></a> `00bfa100` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfa104"></a> `00bfa104` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfa108"></a> `00bfa108` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfa10c"></a> `00bfa10c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfa110"></a> `00bfa110` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfa114"></a> `00bfa114` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa118"></a> `00bfa118` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfa11c"></a> `00bfa11c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa120"></a> `00bfa120` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa0ac`](#insn-00bfa0ac) 範囲 `[['00bfa0ac', '00bfa0cf']]`
  - `CONDITIONAL_JUMP` [`00bfa0cc`](#insn-00bfa0cc) → [`00bfa0dc`](#insn-00bfa0dc)
  - `FALL_THROUGH` [`00bfa0cc`](#insn-00bfa0cc) → [`00bfa0d0`](#insn-00bfa0d0)
- ブロック [`00bfa0d0`](#insn-00bfa0d0) 範囲 `[['00bfa0d0', '00bfa0db']]`
  - `FALL_THROUGH` [`00bfa0d8`](#insn-00bfa0d8) → [`00bfa0dc`](#insn-00bfa0dc)
- ブロック [`00bfa0dc`](#insn-00bfa0dc) 範囲 `[['00bfa0dc', '00bfa0e3']]`
  - `CONDITIONAL_JUMP` [`00bfa0e0`](#insn-00bfa0e0) → [`00bfa104`](#insn-00bfa104)
  - `FALL_THROUGH` [`00bfa0e0`](#insn-00bfa0e0) → [`00bfa0e4`](#insn-00bfa0e4)
- ブロック [`00bfa0e4`](#insn-00bfa0e4) 範囲 `[['00bfa0e4', '00bfa0f3']]`
  - `CONDITIONAL_JUMP` [`00bfa0f0`](#insn-00bfa0f0) → [`00bfa104`](#insn-00bfa104)
  - `FALL_THROUGH` [`00bfa0f0`](#insn-00bfa0f0) → [`00bfa0f4`](#insn-00bfa0f4)
- ブロック [`00bfa0f4`](#insn-00bfa0f4) 範囲 `[['00bfa0f4', '00bfa103']]`
  - `FALL_THROUGH` [`00bfa100`](#insn-00bfa100) → [`00bfa104`](#insn-00bfa104)
- ブロック [`00bfa104`](#insn-00bfa104) 範囲 `[['00bfa104', '00bfa123']]`

## 命令位置別の参照

- [`00bfa0b0`](#insn-00bfa0b0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0b4`](#insn-00bfa0b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0b8`](#insn-00bfa0b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0cc`](#insn-00bfa0cc) → [`00bfa0dc`](#insn-00bfa0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0d8`](#insn-00bfa0d8) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0e0`](#insn-00bfa0e0) → [`00bfa104`](#insn-00bfa104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0ec`](#insn-00bfa0ec) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa0f0`](#insn-00bfa0f0) → [`00bfa104`](#insn-00bfa104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa110`](#insn-00bfa110) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa114`](#insn-00bfa114) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa118`](#insn-00bfa118) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa0b0`](#insn-00bfa0b0)

~~~json
{
  "source": "00bfa0b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0b4`](#insn-00bfa0b4)

~~~json
{
  "source": "00bfa0b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0b8`](#insn-00bfa0b8)

~~~json
{
  "source": "00bfa0b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0cc`](#insn-00bfa0cc)

~~~json
{
  "source": "00bfa0cc",
  "target": "00bfa0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0d8`](#insn-00bfa0d8)

~~~json
{
  "source": "00bfa0d8",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa0e0`](#insn-00bfa0e0)

~~~json
{
  "source": "00bfa0e0",
  "target": "00bfa104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa0ec`](#insn-00bfa0ec)

~~~json
{
  "source": "00bfa0ec",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa0f0`](#insn-00bfa0f0)

~~~json
{
  "source": "00bfa0f0",
  "target": "00bfa104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa110`](#insn-00bfa110)

~~~json
{
  "source": "00bfa110",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa114`](#insn-00bfa114)

~~~json
{
  "source": "00bfa114",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa118`](#insn-00bfa118)

~~~json
{
  "source": "00bfa118",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
