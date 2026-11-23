# 00ba8ffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba90c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba90c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0077.md#compare-33e9d6b83cecb020b7a3b9c605a3ad40)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba8ffc",
  "name": "_ZNSt6__ndk114collate_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac6cbe1e4c87c26d145a12c31cdf7f6e539b13ec2c645b71a4195ef60c5caa51",
  "source_text_sha256": "ac6cbe1e4c87c26d145a12c31cdf7f6e539b13ec2c645b71a4195ef60c5caa51",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba8ffc",
        "00ba90a7"
      ],
      [
        "00ba90b0",
        "00ba90bf"
      ]
    ],
    "bytes_sha256": "26b2634c9d381f0777ca98b3f728fa02f79ea657a9179a5ebe0138118b359700",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1740](../00be1/00be1740.md)

## 呼び出し先

- [00bd6fec](../00bd6/00bd6fec.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)
- [00be0eb0](../00be0/00be0eb0.md)
- [00be1470](../00be1/00be1470.md)

## 関連文字列（未確認候補）

~~~text
"collate_byname<wchar_t>::collate_byname(size_t refs) failed to construct for "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1236 bytes

~~~c

void _ZNSt6__ndk114collate_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm
               (long *param_1,byte *param_2,long param_3)

{
  undefined1 *puVar1;
  __locale_t p_Var2;
  undefined8 uVar3;
  byte *__locale;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk114collate_bynameIwEE_00c1be90 + 0x10);
  param_1[1] = param_3 + -1;
  __locale = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    __locale = param_2 + 1;
  }
  p_Var2 = newlocale(0x1fbf,(char *)__locale,(__locale_t)0x0);
  param_1[2] = (long)p_Var2;
  if (p_Var2 != (__locale_t)0x0) {
    return;
  }
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_38,
             "collate_byname<wchar_t>::collate_byname(size_t refs) failed to construct for ",param_2
            );
  puVar1 = local_28;
  if ((local_38 & 1) == 0) {
    puVar1 = auStack_37;
  }
  uVar3 = _ZNSt6__ndk121__throw_runtime_errorEPKc(puVar1);
  if ((local_38 & 1) != 0) {
    _ZdlPv(local_28);
  }
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
                    /* WARNING: Subroutine does not return */
  FUN_00bd6fec(uVar3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba8ffc"></a> `00ba8ffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba9000"></a> `00ba9000` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ba9004"></a> `00ba9004` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba9008"></a> `00ba9008` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba900c"></a> `00ba900c` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ba9010"></a> `00ba9010` | `88 03 00 d0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ba9014"></a> `00ba9014` | `49 04 00 d1` | sub x9,x2,#0x1 | `FALL_THROUGH`
<a id="insn-00ba9018"></a> `00ba9018` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00ba901c"></a> `00ba901c` | `08 49 47 f9` | ldr x8,[x8, #0xe90] | `FALL_THROUGH`
<a id="insn-00ba9020"></a> `00ba9020` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba9024"></a> `00ba9024` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00ba9028"></a> `00ba9028` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00ba902c"></a> `00ba902c` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00ba9030"></a> `00ba9030` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00ba9034"></a> `00ba9034` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba9038"></a> `00ba9038` | `21 15 81 9a` | csinc x1,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00ba903c"></a> `00ba903c` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00ba9040"></a> `00ba9040` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ba9044"></a> `00ba9044` | `0b e1 00 94` | bl 0x00be1470 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9048"></a> `00ba9048` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ba904c"></a> `00ba904c` | `c0 00 00 b4` | cbz x0,0x00ba9064 | `CONDITIONAL_JUMP`
<a id="insn-00ba9050"></a> `00ba9050` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba9054"></a> `00ba9054` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba9058"></a> `00ba9058` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ba905c"></a> `00ba905c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba9060"></a> `00ba9060` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba9064"></a> `00ba9064` | `20 b7 ff f0` | adrp x0,0x290000 | `FALL_THROUGH`
<a id="insn-00ba9068"></a> `00ba9068` | `00 20 1e 91` | add x0,x0,#0x788 | `FALL_THROUGH`
<a id="insn-00ba906c"></a> `00ba906c` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ba9070"></a> `00ba9070` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ba9074"></a> `00ba9074` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ba9078"></a> `00ba9078` | `3a c8 00 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00ba907c"></a> `00ba907c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba9080"></a> `00ba9080` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba9084"></a> `00ba9084` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba9088"></a> `00ba9088` | `20 15 94 9a` | csinc x0,x9,x20,ne | `FALL_THROUGH`
<a id="insn-00ba908c"></a> `00ba908c` | `89 df 00 94` | bl 0x00be0eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9090"></a> `00ba9090` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba9094"></a> `00ba9094` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ba9098"></a> `00ba9098` | `c8 00 00 36` | tbz w8,#0x0,0x00ba90b0 | `CONDITIONAL_JUMP`
<a id="insn-00ba909c"></a> `00ba909c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba90a0"></a> `00ba90a0` | `b0 c7 00 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ba90a4"></a> `00ba90a4` | `03 00 00 14` | b 0x00ba90b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba90b0"></a> `00ba90b0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba90b4"></a> `00ba90b4` | `bf c8 00 94` | bl 0x00bdb3b0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba90b8"></a> `00ba90b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ba90bc"></a> `00ba90bc` | `cc b7 00 94` | bl 0x00bd6fec | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba8ffc`](#insn-00ba8ffc) 範囲 `[['00ba8ffc', '00ba904f']]`
  - `CONDITIONAL_JUMP` [`00ba904c`](#insn-00ba904c) → [`00ba9064`](#insn-00ba9064)
  - `FALL_THROUGH` [`00ba904c`](#insn-00ba904c) → [`00ba9050`](#insn-00ba9050)
- ブロック [`00ba9050`](#insn-00ba9050) 範囲 `[['00ba9050', '00ba9063']]`
- ブロック [`00ba9064`](#insn-00ba9064) 範囲 `[['00ba9064', '00ba909b']]`
  - `CONDITIONAL_JUMP` [`00ba9098`](#insn-00ba9098) → [`00ba90b0`](#insn-00ba90b0)
  - `FALL_THROUGH` [`00ba9098`](#insn-00ba9098) → [`00ba909c`](#insn-00ba909c)
- ブロック [`00ba909c`](#insn-00ba909c) 範囲 `[['00ba909c', '00ba90a7']]`
  - `UNCONDITIONAL_JUMP` [`00ba90a4`](#insn-00ba90a4) → [`00ba90b0`](#insn-00ba90b0)
- ブロック [`00ba90b0`](#insn-00ba90b0) 範囲 `[['00ba90b0', '00ba90bf']]`

## 命令位置別の参照

- [`00ba9004`](#insn-00ba9004) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9008`](#insn-00ba9008) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba901c`](#insn-00ba901c) → `00c1be90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba9028`](#insn-00ba9028) → `00c13880`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[64]`
- [`00ba9044`](#insn-00ba9044) → [`00be1470`](../00be1/00be1470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1470` · 推定シンボル `None` · 推定型 `None`
- [`00ba904c`](#insn-00ba904c) → [`00ba9064`](#insn-00ba9064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9050`](#insn-00ba9050) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9054`](#insn-00ba9054) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9068`](#insn-00ba9068) → `00290788`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ba9078`](#insn-00ba9078) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00ba907c`](#insn-00ba907c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9080`](#insn-00ba9080) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba908c`](#insn-00ba908c) → [`00be0eb0`](../00be0/00be0eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ba9090`](#insn-00ba9090) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9098`](#insn-00ba9098) → [`00ba90b0`](#insn-00ba90b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba909c`](#insn-00ba909c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba90a0`](#insn-00ba90a0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ba90a4`](#insn-00ba90a4) → [`00ba90b0`](#insn-00ba90b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba90b4`](#insn-00ba90b4) → [`00bdb3b0`](../00bdb/00bdb3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb3b0` · 推定シンボル `None` · 推定型 `None`
- [`00ba90bc`](#insn-00ba90bc) → [`00bd6fec`](../00bd6/00bd6fec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6fec` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba9004`](#insn-00ba9004)

~~~json
{
  "source": "00ba9004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9008`](#insn-00ba9008)

~~~json
{
  "source": "00ba9008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba901c`](#insn-00ba901c)

~~~json
{
  "source": "00ba901c",
  "target": "00c1be90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1be90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba9028`](#insn-00ba9028)

~~~json
{
  "source": "00ba9028",
  "target": "00c13880",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13870",
  "offset": 16,
  "size": 64,
  "datatype": "undefined1[64]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00ba9044`](#insn-00ba9044)

~~~json
{
  "source": "00ba9044",
  "target": "00be1470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba904c`](#insn-00ba904c)

~~~json
{
  "source": "00ba904c",
  "target": "00ba9064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9050`](#insn-00ba9050)

~~~json
{
  "source": "00ba9050",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9054`](#insn-00ba9054)

~~~json
{
  "source": "00ba9054",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9068`](#insn-00ba9068)

~~~json
{
  "source": "00ba9068",
  "target": "00290788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290788",
  "offset": 0,
  "size": 78,
  "datatype": "string",
  "bytes": "636f6c6c6174655f62796e616d653c77636861725f743e3a3a636f6c6c617465",
  "capture_start": "00290788",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ba9078`](#insn-00ba9078)

~~~json
{
  "source": "00ba9078",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba907c`](#insn-00ba907c)

~~~json
{
  "source": "00ba907c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9080`](#insn-00ba9080)

~~~json
{
  "source": "00ba9080",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba908c`](#insn-00ba908c)

~~~json
{
  "source": "00ba908c",
  "target": "00be0eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba9090`](#insn-00ba9090)

~~~json
{
  "source": "00ba9090",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9098`](#insn-00ba9098)

~~~json
{
  "source": "00ba9098",
  "target": "00ba90b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba909c`](#insn-00ba909c)

~~~json
{
  "source": "00ba909c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba90a0`](#insn-00ba90a0)

~~~json
{
  "source": "00ba90a0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba90a4`](#insn-00ba90a4)

~~~json
{
  "source": "00ba90a4",
  "target": "00ba90b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba90b4`](#insn-00ba90b4)

~~~json
{
  "source": "00ba90b4",
  "target": "00bdb3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba90bc`](#insn-00ba90bc)

~~~json
{
  "source": "00ba90bc",
  "target": "00bd6fec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
