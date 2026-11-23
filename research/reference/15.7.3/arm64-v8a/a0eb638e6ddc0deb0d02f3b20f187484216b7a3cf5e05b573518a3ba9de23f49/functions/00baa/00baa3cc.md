# 00baa3cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baa304`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa304.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0077.md#compare-200e9e7226b9a28f79fcc96c81e9daec)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00baa410`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa410.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-2a11d2ee0188c78f42e130e67a98b144)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baa3cc",
  "name": "_ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dce0723b5f271ed264b2bea923eb4843345530771ae4176d6a99ae75145db73c",
  "source_text_sha256": "dce0723b5f271ed264b2bea923eb4843345530771ae4176d6a99ae75145db73c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baa3cc",
        "00baa487"
      ],
      [
        "00baa490",
        "00baa49f"
      ]
    ],
    "bytes_sha256": "f35ed668e50f15bd06892ab9843025fc479c05541c3fc783ba4775044f1d211d",
    "instruction_count": 51,
    "instruction_bytes": 204,
    "body_bytes": 204,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1800](../00be1/00be1800.md)
- [00be19a0](../00be1/00be19a0.md)

## 呼び出し先

- [00bd70ac](../00bd7/00bd70ac.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb210](../00bdb/00bdb210.md)
- [00be0f60](../00be0/00be0f60.md)
- [00be1520](../00be1/00be1520.md)
- [00be1970](../00be1/00be1970.md)

## 関連文字列（未確認候補）

~~~text
"ctype_byname<char>::ctype_byname failed to construct for "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1285 bytes

~~~c

void _ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm
               (long *param_1,byte *param_2,long param_3)

{
  undefined1 *puVar1;
  undefined *puVar2;
  __locale_t p_Var3;
  undefined8 uVar4;
  byte *__locale;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  param_1[2] = (long)&DAT_002fb120;
  puVar2 = PTR__ZTVNSt6__ndk112ctype_bynameIcEE_00c1bf50;
  *(undefined1 *)(param_1 + 3) = 0;
  *param_1 = (long)(puVar2 + 0x10);
  param_1[1] = param_3 + -1;
  __locale = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    __locale = param_2 + 1;
  }
  p_Var3 = newlocale(0x1fbf,(char *)__locale,(__locale_t)0x0);
  param_1[4] = (long)p_Var3;
  if (p_Var3 != (__locale_t)0x0) {
    return;
  }
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_38,"ctype_byname<char>::ctype_byname failed to construct for ",param_2);
  puVar1 = local_28;
  if ((local_38 & 1) == 0) {
    puVar1 = auStack_37;
  }
  uVar4 = _ZNSt6__ndk121__throw_runtime_errorEPKc(puVar1);
  if ((local_38 & 1) != 0) {
    _ZdlPv(local_28);
  }
  _ZNSt6__ndk15ctypeIcED2Ev(param_1);
                    /* WARNING: Subroutine does not return */
  FUN_00bd70ac(uVar4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baa3cc"></a> `00baa3cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baa3d0"></a> `00baa3d0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baa3d4"></a> `00baa3d4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baa3d8"></a> `00baa3d8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baa3dc"></a> `00baa3dc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00baa3e0"></a> `00baa3e0` | `88 ba ff b0` | adrp x8,0x2fb000 | `FALL_THROUGH`
<a id="insn-00baa3e4"></a> `00baa3e4` | `08 81 04 91` | add x8,x8,#0x120 | `FALL_THROUGH`
<a id="insn-00baa3e8"></a> `00baa3e8` | `49 04 00 d1` | sub x9,x2,#0x1 | `FALL_THROUGH`
<a id="insn-00baa3ec"></a> `00baa3ec` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baa3f0"></a> `00baa3f0` | `88 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00baa3f4"></a> `00baa3f4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00baa3f8"></a> `00baa3f8` | `08 a9 47 f9` | ldr x8,[x8, #0xf50] | `FALL_THROUGH`
<a id="insn-00baa3fc"></a> `00baa3fc` | `1f 60 00 39` | strb wzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baa400"></a> `00baa400` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baa404"></a> `00baa404` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00baa408"></a> `00baa408` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00baa40c"></a> `00baa40c` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00baa410"></a> `00baa410` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00baa414"></a> `00baa414` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baa418"></a> `00baa418` | `21 15 81 9a` | csinc x1,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00baa41c"></a> `00baa41c` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00baa420"></a> `00baa420` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00baa424"></a> `00baa424` | `3f dc 00 94` | bl 0x00be1520 | `UNCONDITIONAL_CALL`
<a id="insn-00baa428"></a> `00baa428` | `60 12 00 f9` | str x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00baa42c"></a> `00baa42c` | `c0 00 00 b4` | cbz x0,0x00baa444 | `CONDITIONAL_JUMP`
<a id="insn-00baa430"></a> `00baa430` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baa434"></a> `00baa434` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baa438"></a> `00baa438` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baa43c"></a> `00baa43c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baa440"></a> `00baa440` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baa444"></a> `00baa444` | `c0 b7 ff d0` | adrp x0,0x2a4000 | `FALL_THROUGH`
<a id="insn-00baa448"></a> `00baa448` | `00 a0 03 91` | add x0,x0,#0xe8 | `FALL_THROUGH`
<a id="insn-00baa44c"></a> `00baa44c` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baa450"></a> `00baa450` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00baa454"></a> `00baa454` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baa458"></a> `00baa458` | `6e c3 00 94` | bl 0x00bdb210 | `UNCONDITIONAL_CALL`
<a id="insn-00baa45c"></a> `00baa45c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00baa460"></a> `00baa460` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00baa464"></a> `00baa464` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baa468"></a> `00baa468` | `20 15 94 9a` | csinc x0,x9,x20,ne | `FALL_THROUGH`
<a id="insn-00baa46c"></a> `00baa46c` | `bd da 00 94` | bl 0x00be0f60 | `UNCONDITIONAL_CALL`
<a id="insn-00baa470"></a> `00baa470` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00baa474"></a> `00baa474` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baa478"></a> `00baa478` | `c8 00 00 36` | tbz w8,#0x0,0x00baa490 | `CONDITIONAL_JUMP`
<a id="insn-00baa47c"></a> `00baa47c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00baa480"></a> `00baa480` | `e4 c2 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00baa484"></a> `00baa484` | `03 00 00 14` | b 0x00baa490 | `UNCONDITIONAL_JUMP`
<a id="insn-00baa490"></a> `00baa490` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baa494"></a> `00baa494` | `37 dd 00 94` | bl 0x00be1970 | `UNCONDITIONAL_CALL`
<a id="insn-00baa498"></a> `00baa498` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baa49c"></a> `00baa49c` | `04 b3 00 94` | bl 0x00bd70ac | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baa3cc`](#insn-00baa3cc) 範囲 `[['00baa3cc', '00baa42f']]`
  - `CONDITIONAL_JUMP` [`00baa42c`](#insn-00baa42c) → [`00baa444`](#insn-00baa444)
  - `FALL_THROUGH` [`00baa42c`](#insn-00baa42c) → [`00baa430`](#insn-00baa430)
- ブロック [`00baa430`](#insn-00baa430) 範囲 `[['00baa430', '00baa443']]`
- ブロック [`00baa444`](#insn-00baa444) 範囲 `[['00baa444', '00baa47b']]`
  - `CONDITIONAL_JUMP` [`00baa478`](#insn-00baa478) → [`00baa490`](#insn-00baa490)
  - `FALL_THROUGH` [`00baa478`](#insn-00baa478) → [`00baa47c`](#insn-00baa47c)
- ブロック [`00baa47c`](#insn-00baa47c) 範囲 `[['00baa47c', '00baa487']]`
  - `UNCONDITIONAL_JUMP` [`00baa484`](#insn-00baa484) → [`00baa490`](#insn-00baa490)
- ブロック [`00baa490`](#insn-00baa490) 範囲 `[['00baa490', '00baa49f']]`

## 命令位置別の参照

- [`00baa3d4`](#insn-00baa3d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa3d8`](#insn-00baa3d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa3ec`](#insn-00baa3ec) → `002fb120`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa3f8`](#insn-00baa3f8) → `00c1bf50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baa408`](#insn-00baa408) → `00c139d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[104]`
- [`00baa424`](#insn-00baa424) → [`00be1520`](../00be1/00be1520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1520` · 推定シンボル `None` · 推定型 `None`
- [`00baa42c`](#insn-00baa42c) → [`00baa444`](#insn-00baa444) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa430`](#insn-00baa430) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa434`](#insn-00baa434) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa448`](#insn-00baa448) → `002a40e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00baa458`](#insn-00baa458) → [`00bdb210`](../00bdb/00bdb210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb210` · 推定シンボル `None` · 推定型 `None`
- [`00baa45c`](#insn-00baa45c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa460`](#insn-00baa460) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa46c`](#insn-00baa46c) → [`00be0f60`](../00be0/00be0f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0f60` · 推定シンボル `None` · 推定型 `None`
- [`00baa470`](#insn-00baa470) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa478`](#insn-00baa478) → [`00baa490`](#insn-00baa490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa47c`](#insn-00baa47c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa480`](#insn-00baa480) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00baa484`](#insn-00baa484) → [`00baa490`](#insn-00baa490) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa494`](#insn-00baa494) → [`00be1970`](../00be1/00be1970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1970` · 推定シンボル `None` · 推定型 `None`
- [`00baa49c`](#insn-00baa49c) → [`00bd70ac`](../00bd7/00bd70ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd70ac` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baa3d4`](#insn-00baa3d4)

~~~json
{
  "source": "00baa3d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa3d8`](#insn-00baa3d8)

~~~json
{
  "source": "00baa3d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa3ec`](#insn-00baa3ec)

~~~json
{
  "source": "00baa3ec",
  "target": "002fb120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa3f8`](#insn-00baa3f8)

~~~json
{
  "source": "00baa3f8",
  "target": "00c1bf50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf50",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baa408`](#insn-00baa408)

~~~json
{
  "source": "00baa408",
  "target": "00c139d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c139c8",
  "offset": 16,
  "size": 104,
  "datatype": "undefined1[104]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00baa424`](#insn-00baa424)

~~~json
{
  "source": "00baa424",
  "target": "00be1520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa42c`](#insn-00baa42c)

~~~json
{
  "source": "00baa42c",
  "target": "00baa444",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa430`](#insn-00baa430)

~~~json
{
  "source": "00baa430",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa434`](#insn-00baa434)

~~~json
{
  "source": "00baa434",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa448`](#insn-00baa448)

~~~json
{
  "source": "00baa448",
  "target": "002a40e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a40e8",
  "offset": 0,
  "size": 58,
  "datatype": "string",
  "bytes": "63747970655f62796e616d653c636861723e3a3a63747970655f62796e616d65",
  "capture_start": "002a40e8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00baa458`](#insn-00baa458)

~~~json
{
  "source": "00baa458",
  "target": "00bdb210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa45c`](#insn-00baa45c)

~~~json
{
  "source": "00baa45c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa460`](#insn-00baa460)

~~~json
{
  "source": "00baa460",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa46c`](#insn-00baa46c)

~~~json
{
  "source": "00baa46c",
  "target": "00be0f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa470`](#insn-00baa470)

~~~json
{
  "source": "00baa470",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa478`](#insn-00baa478)

~~~json
{
  "source": "00baa478",
  "target": "00baa490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa47c`](#insn-00baa47c)

~~~json
{
  "source": "00baa47c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa480`](#insn-00baa480)

~~~json
{
  "source": "00baa480",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa484`](#insn-00baa484)

~~~json
{
  "source": "00baa484",
  "target": "00baa490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa494`](#insn-00baa494)

~~~json
{
  "source": "00baa494",
  "target": "00be1970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa49c`](#insn-00baa49c)

~~~json
{
  "source": "00baa49c",
  "target": "00bd70ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
