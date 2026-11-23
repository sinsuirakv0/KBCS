# 00ba8fec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ba8f24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8f24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0077.md#compare-0793a0f198e71e520de56aef35d2a4f0)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ba9030`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9030.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-1ab39cd714bfd0fafb3659c5d56b632f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba8fec",
  "name": "_ZNSt6__ndk114collate_bynameIwEC1EPKcm",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4664daa3dd4461f5bc41334ba1eb7974b36444685403ed7cf98959fc6b971f31",
  "source_text_sha256": "4664daa3dd4461f5bc41334ba1eb7974b36444685403ed7cf98959fc6b971f31",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba8fec",
        "00ba9093"
      ],
      [
        "00ba9098",
        "00ba90ab"
      ],
      [
        "00ba90b4",
        "00ba90c3"
      ]
    ],
    "bytes_sha256": "119f4ae1b958f2288675b290dfbd2616cf60c51776a2d413479aa0def9070263",
    "instruction_count": 51,
    "instruction_bytes": 204,
    "body_bytes": 204,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0041b298](../0041b/0041b298.md)
- [00ba8a80](../00ba8/00ba8a80.md)
- [00bd70ac](../00bd7/00bd70ac.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb460](../00bdb/00bdb460.md)
- [00be0f60](../00be0/00be0f60.md)
- [00be1520](../00be1/00be1520.md)

## 関連文字列（未確認候補）

~~~text
"collate_byname<wchar_t>::collate_byname(size_t refs) failed to construct for "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1078 bytes

~~~c

void _ZNSt6__ndk114collate_bynameIwEC1EPKcm(long *param_1,char *param_2,long param_3)

{
  undefined1 *puVar1;
  __locale_t p_Var2;
  undefined8 uVar3;
  byte local_50 [16];
  void *local_40;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk114collate_bynameIwEE_00c1bf40 + 0x10);
  param_1[1] = param_3 + -1;
  p_Var2 = newlocale(0x1fbf,param_2,(__locale_t)0x0);
  param_1[2] = (long)p_Var2;
  if (p_Var2 != (__locale_t)0x0) {
    return;
  }
  FUN_0041b298(local_50,param_2);
  FUN_00ba8a80(&local_38,
               "collate_byname<wchar_t>::collate_byname(size_t refs) failed to construct for ",
               local_50);
  puVar1 = local_28;
  if ((local_38 & 1) == 0) {
    puVar1 = auStack_37;
  }
  uVar3 = _ZNSt6__ndk121__throw_runtime_errorEPKc(puVar1);
  if ((local_38 & 1) != 0) {
    _ZdlPv(local_28);
  }
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
                    /* WARNING: Subroutine does not return */
  FUN_00bd70ac(uVar3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba8fec"></a> `00ba8fec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba8ff0"></a> `00ba8ff0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba8ff4"></a> `00ba8ff4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba8ff8"></a> `00ba8ff8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba8ffc"></a> `00ba8ffc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ba9000"></a> `00ba9000` | `88 03 00 d0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ba9004"></a> `00ba9004` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00ba9008"></a> `00ba9008` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba900c"></a> `00ba900c` | `08 a1 47 f9` | ldr x8,[x8, #0xf40] | `FALL_THROUGH`
<a id="insn-00ba9010"></a> `00ba9010` | `49 04 00 d1` | sub x9,x2,#0x1 | `FALL_THROUGH`
<a id="insn-00ba9014"></a> `00ba9014` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00ba9018"></a> `00ba9018` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00ba901c"></a> `00ba901c` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00ba9020"></a> `00ba9020` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ba9024"></a> `00ba9024` | `3f e1 00 94` | bl 0x00be1520 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9028"></a> `00ba9028` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ba902c"></a> `00ba902c` | `c0 00 00 b4` | cbz x0,0x00ba9044 | `CONDITIONAL_JUMP`
<a id="insn-00ba9030"></a> `00ba9030` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba9034"></a> `00ba9034` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba9038"></a> `00ba9038` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba903c"></a> `00ba903c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba9040"></a> `00ba9040` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba9044"></a> `00ba9044` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ba9048"></a> `00ba9048` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ba904c"></a> `00ba904c` | `93 c8 e1 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9050"></a> `00ba9050` | `20 b7 ff f0` | adrp x0,0x290000 | `FALL_THROUGH`
<a id="insn-00ba9054"></a> `00ba9054` | `00 20 1e 91` | add x0,x0,#0x788 | `FALL_THROUGH`
<a id="insn-00ba9058"></a> `00ba9058` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ba905c"></a> `00ba905c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00ba9060"></a> `00ba9060` | `f4 63 00 91` | add x20,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ba9064"></a> `00ba9064` | `87 fe ff 97` | bl 0x00ba8a80 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9068"></a> `00ba9068` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba906c"></a> `00ba906c` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba9070"></a> `00ba9070` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba9074"></a> `00ba9074` | `20 15 94 9a` | csinc x0,x9,x20,ne | `FALL_THROUGH`
<a id="insn-00ba9078"></a> `00ba9078` | `ba df 00 94` | bl 0x00be0f60 | `UNCONDITIONAL_CALL`
<a id="insn-00ba907c"></a> `00ba907c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba9080"></a> `00ba9080` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ba9084"></a> `00ba9084` | `a8 00 00 36` | tbz w8,#0x0,0x00ba9098 | `CONDITIONAL_JUMP`
<a id="insn-00ba9088"></a> `00ba9088` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba908c"></a> `00ba908c` | `e1 c7 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9090"></a> `00ba9090` | `02 00 00 14` | b 0x00ba9098 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba9098"></a> `00ba9098` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ba909c"></a> `00ba909c` | `c8 00 00 36` | tbz w8,#0x0,0x00ba90b4 | `CONDITIONAL_JUMP`
<a id="insn-00ba90a0"></a> `00ba90a0` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba90a4"></a> `00ba90a4` | `db c7 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00ba90a8"></a> `00ba90a8` | `03 00 00 14` | b 0x00ba90b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba90b4"></a> `00ba90b4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba90b8"></a> `00ba90b8` | `ea c8 00 94` | bl 0x00bdb460 | `UNCONDITIONAL_CALL`
<a id="insn-00ba90bc"></a> `00ba90bc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ba90c0"></a> `00ba90c0` | `fb b7 00 94` | bl 0x00bd70ac | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba8fec`](#insn-00ba8fec) 範囲 `[['00ba8fec', '00ba902f']]`
  - `CONDITIONAL_JUMP` [`00ba902c`](#insn-00ba902c) → [`00ba9044`](#insn-00ba9044)
  - `FALL_THROUGH` [`00ba902c`](#insn-00ba902c) → [`00ba9030`](#insn-00ba9030)
- ブロック [`00ba9030`](#insn-00ba9030) 範囲 `[['00ba9030', '00ba9043']]`
- ブロック [`00ba9044`](#insn-00ba9044) 範囲 `[['00ba9044', '00ba9087']]`
  - `CONDITIONAL_JUMP` [`00ba9084`](#insn-00ba9084) → [`00ba9098`](#insn-00ba9098)
  - `FALL_THROUGH` [`00ba9084`](#insn-00ba9084) → [`00ba9088`](#insn-00ba9088)
- ブロック [`00ba9088`](#insn-00ba9088) 範囲 `[['00ba9088', '00ba9093']]`
  - `UNCONDITIONAL_JUMP` [`00ba9090`](#insn-00ba9090) → [`00ba9098`](#insn-00ba9098)
- ブロック [`00ba9098`](#insn-00ba9098) 範囲 `[['00ba9098', '00ba909f']]`
  - `CONDITIONAL_JUMP` [`00ba909c`](#insn-00ba909c) → [`00ba90b4`](#insn-00ba90b4)
  - `FALL_THROUGH` [`00ba909c`](#insn-00ba909c) → [`00ba90a0`](#insn-00ba90a0)
- ブロック [`00ba90a0`](#insn-00ba90a0) 範囲 `[['00ba90a0', '00ba90ab']]`
  - `UNCONDITIONAL_JUMP` [`00ba90a8`](#insn-00ba90a8) → [`00ba90b4`](#insn-00ba90b4)
- ブロック [`00ba90b4`](#insn-00ba90b4) 範囲 `[['00ba90b4', '00ba90c3']]`

## 命令位置別の参照

- [`00ba8ff4`](#insn-00ba8ff4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8ff8`](#insn-00ba8ff8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba900c`](#insn-00ba900c) → `00c1bf40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba9018`](#insn-00ba9018) → `00c13930`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[64]`
- [`00ba9024`](#insn-00ba9024) → [`00be1520`](../00be1/00be1520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1520` · 推定シンボル `None` · 推定型 `None`
- [`00ba902c`](#insn-00ba902c) → [`00ba9044`](#insn-00ba9044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9030`](#insn-00ba9030) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9034`](#insn-00ba9034) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba904c`](#insn-00ba904c) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00ba9054`](#insn-00ba9054) → `00290788`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ba9064`](#insn-00ba9064) → [`00ba8a80`](00ba8a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba8a80` · 推定シンボル `None` · 推定型 `None`
- [`00ba9068`](#insn-00ba9068) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba906c`](#insn-00ba906c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9078`](#insn-00ba9078) → [`00be0f60`](../00be0/00be0f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0f60` · 推定シンボル `None` · 推定型 `None`
- [`00ba907c`](#insn-00ba907c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9084`](#insn-00ba9084) → [`00ba9098`](#insn-00ba9098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9088`](#insn-00ba9088) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba908c`](#insn-00ba908c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ba9090`](#insn-00ba9090) → [`00ba9098`](#insn-00ba9098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9098`](#insn-00ba9098) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba909c`](#insn-00ba909c) → [`00ba90b4`](#insn-00ba90b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba90a0`](#insn-00ba90a0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba90a4`](#insn-00ba90a4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ba90a8`](#insn-00ba90a8) → [`00ba90b4`](#insn-00ba90b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba90b8`](#insn-00ba90b8) → [`00bdb460`](../00bdb/00bdb460.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb460` · 推定シンボル `None` · 推定型 `None`
- [`00ba90c0`](#insn-00ba90c0) → [`00bd70ac`](../00bd7/00bd70ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd70ac` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba8ff4`](#insn-00ba8ff4)

~~~json
{
  "source": "00ba8ff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8ff8`](#insn-00ba8ff8)

~~~json
{
  "source": "00ba8ff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba900c`](#insn-00ba900c)

~~~json
{
  "source": "00ba900c",
  "target": "00c1bf40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba9018`](#insn-00ba9018)

~~~json
{
  "source": "00ba9018",
  "target": "00c13930",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13920",
  "offset": 16,
  "size": 64,
  "datatype": "undefined1[64]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00ba9024`](#insn-00ba9024)

~~~json
{
  "source": "00ba9024",
  "target": "00be1520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba902c`](#insn-00ba902c)

~~~json
{
  "source": "00ba902c",
  "target": "00ba9044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9030`](#insn-00ba9030)

~~~json
{
  "source": "00ba9030",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9034`](#insn-00ba9034)

~~~json
{
  "source": "00ba9034",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba904c`](#insn-00ba904c)

~~~json
{
  "source": "00ba904c",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba9054`](#insn-00ba9054)

~~~json
{
  "source": "00ba9054",
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
- 参照命令 [`00ba9064`](#insn-00ba9064)

~~~json
{
  "source": "00ba9064",
  "target": "00ba8a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba9068`](#insn-00ba9068)

~~~json
{
  "source": "00ba9068",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba906c`](#insn-00ba906c)

~~~json
{
  "source": "00ba906c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9078`](#insn-00ba9078)

~~~json
{
  "source": "00ba9078",
  "target": "00be0f60",
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
- 参照命令 [`00ba9084`](#insn-00ba9084)

~~~json
{
  "source": "00ba9084",
  "target": "00ba9098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9088`](#insn-00ba9088)

~~~json
{
  "source": "00ba9088",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba908c`](#insn-00ba908c)

~~~json
{
  "source": "00ba908c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba9090`](#insn-00ba9090)

~~~json
{
  "source": "00ba9090",
  "target": "00ba9098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9098`](#insn-00ba9098)

~~~json
{
  "source": "00ba9098",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba909c`](#insn-00ba909c)

~~~json
{
  "source": "00ba909c",
  "target": "00ba90b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba90a0`](#insn-00ba90a0)

~~~json
{
  "source": "00ba90a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba90a4`](#insn-00ba90a4)

~~~json
{
  "source": "00ba90a4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba90a8`](#insn-00ba90a8)

~~~json
{
  "source": "00ba90a8",
  "target": "00ba90b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba90b8`](#insn-00ba90b8)

~~~json
{
  "source": "00ba90b8",
  "target": "00bdb460",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba90c0`](#insn-00ba90c0)

~~~json
{
  "source": "00ba90c0",
  "target": "00bd70ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
