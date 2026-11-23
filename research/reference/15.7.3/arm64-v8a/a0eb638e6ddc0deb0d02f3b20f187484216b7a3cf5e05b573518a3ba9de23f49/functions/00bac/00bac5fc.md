# 00bac5fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bac534`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac534.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-6fddb17f64b3a3755741cf82c61dc7c1)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bac640`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac640.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-d4d50d335b59a7fcafc5cc8cfddc4359)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bac5fc",
  "name": "_ZNKSt6__ndk17codecvtIDsDu9mbstate_tE6do_outERS1_PKDsS5_RS5_PDuS7_RS7_",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5aa65ed1bdcf4d0d62603aafa4dd2ff1b8cc33a29266d4c9a65071c6fa4184f5",
  "source_text_sha256": "5aa65ed1bdcf4d0d62603aafa4dd2ff1b8cc33a29266d4c9a65071c6fa4184f5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bac5fc",
        "00bac663"
      ]
    ],
    "bytes_sha256": "4633f596554af3e3e0cd914df0d66c3bef53528e4ea3f809be069ca5e8b5f591",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00babe28](../00bab/00babe28.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 503 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE6do_outERS1_PKDsS5_RS5_PDuS7_RS7_
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00babe28(param_3,param_4,&uStack_28,param_6,param_7,&local_30,0x10ffff,0);
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bac5fc"></a> `00bac5fc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bac600"></a> `00bac600` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bac604"></a> `00bac604` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac608"></a> `00bac608` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac60c"></a> `00bac60c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bac610"></a> `00bac610` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00bac614"></a> `00bac614` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00bac618"></a> `00bac618` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bac61c"></a> `00bac61c` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00bac620"></a> `00bac620` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00bac624"></a> `00bac624` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00bac628"></a> `00bac628` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bac62c"></a> `00bac62c` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00bac630"></a> `00bac630` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00bac634"></a> `00bac634` | `e4 03 06 aa` | mov x4,x6 | `FALL_THROUGH`
<a id="insn-00bac638"></a> `00bac638` | `e6 fd bf 12` | mov w6,#0x10ffff | `FALL_THROUGH`
<a id="insn-00bac63c"></a> `00bac63c` | `e7 03 1f 2a` | mov w7,wzr | `FALL_THROUGH`
<a id="insn-00bac640"></a> `00bac640` | `fa fd ff 97` | bl 0x00babe28 | `UNCONDITIONAL_CALL`
<a id="insn-00bac644"></a> `00bac644` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00bac648"></a> `00bac648` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bac64c"></a> `00bac64c` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bac650"></a> `00bac650` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac654"></a> `00bac654` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac658"></a> `00bac658` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bac65c"></a> `00bac65c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bac660"></a> `00bac660` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bac5fc`](#insn-00bac5fc) 範囲 `[['00bac5fc', '00bac663']]`

## 命令位置別の参照

- [`00bac604`](#insn-00bac604) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac608`](#insn-00bac608) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac624`](#insn-00bac624) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac638`](#insn-00bac638) → `0010ffff`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Sym[6714]`
- [`00bac640`](#insn-00bac640) → [`00babe28`](../00bab/00babe28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00babe28` · 推定シンボル `None` · 推定型 `None`
- [`00bac644`](#insn-00bac644) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac650`](#insn-00bac650) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac654`](#insn-00bac654) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bac604`](#insn-00bac604)

~~~json
{
  "source": "00bac604",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac608`](#insn-00bac608)

~~~json
{
  "source": "00bac608",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac624`](#insn-00bac624)

~~~json
{
  "source": "00bac624",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac638`](#insn-00bac638)

~~~json
{
  "source": "00bac638",
  "target": "0010ffff",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "001002f8",
  "offset": 64775,
  "size": 161136,
  "datatype": "Elf64_Sym[6714]",
  "bytes": "0000000000000000000000000000000000000000000000000100000012000000",
  "capture_start": "001002f8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bac640`](#insn-00bac640)

~~~json
{
  "source": "00bac640",
  "target": "00babe28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac644`](#insn-00bac644)

~~~json
{
  "source": "00bac644",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac650`](#insn-00bac650)

~~~json
{
  "source": "00bac650",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac654`](#insn-00bac654)

~~~json
{
  "source": "00bac654",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
