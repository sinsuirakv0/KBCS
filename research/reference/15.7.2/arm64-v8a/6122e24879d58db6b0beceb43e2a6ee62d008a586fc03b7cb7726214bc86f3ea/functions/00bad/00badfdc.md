# 00badfdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bae0a4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae0a4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-e60e5718acd0ec2f11111ca45981bc15)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badfdc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c204010534c030bf8bc1c310ae6da38e01859de6d9549f120772f5f71d735ff",
  "source_text_sha256": "1c204010534c030bf8bc1c310ae6da38e01859de6d9549f120772f5f71d735ff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badfdc",
        "00bae06f"
      ]
    ],
    "bytes_sha256": "71bb2248382085753830fd6e97b1f5bb3ee55ee50a3055829abfe322418c833f",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1238 bytes

~~~c

undefined1
_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_
          (long param_1,undefined8 param_2,char *param_3,char *param_4,ulong *param_5,
          ushort *param_6,ushort *param_7,undefined8 *param_8)

{
  ushort uVar1;
  undefined1 uVar2;
  ushort *puVar3;
  ulong uVar4;
  
  if (((1 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == -1)) {
    param_3 = param_3 + (ulong)(param_3[1] == -2) * 2;
  }
  if (param_3 < param_4 + -1) {
    uVar4 = *(ulong *)(param_1 + 0x10);
    uVar2 = 2;
    puVar3 = param_6;
    while (param_6 = puVar3, puVar3 < param_7) {
                    /* try { // try from 00bae02c to 00cae04f has its CatchHandler @ 00bae59c */
      if (((param_3[1] & 0xf8U) == 0xd8) || (uVar1 = CONCAT11(param_3[1],*param_3), uVar4 < uVar1))
      goto LAB_00bae064;
      param_3 = param_3 + 2;
      param_6 = puVar3 + 1;
      *puVar3 = uVar1;
      puVar3 = param_6;
      if (param_4 + -1 <= param_3) break;
    }
  }
  uVar2 = param_3 < param_4;
LAB_00bae064:
  *param_5 = (ulong)param_3;
                    /* try { // try from 00bae068 to 00cae06f has its CatchHandler @ 00bae568 */
  *param_8 = param_6;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badfdc"></a> `00badfdc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badfe0"></a> `00badfe0` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00badfe4"></a> `00badfe4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badfe8"></a> `00badfe8` | `4b 01 00 54` | b.lt 0x00bae010 | `CONDITIONAL_JUMP`
<a id="insn-00badfec"></a> `00badfec` | `08 18 40 b9` | ldr w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badff0"></a> `00badff0` | `08 01 10 36` | tbz w8,#0x2,0x00bae010 | `CONDITIONAL_JUMP`
<a id="insn-00badff4"></a> `00badff4` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00badff8"></a> `00badff8` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00badffc"></a> `00badffc` | `a1 00 00 54` | b.ne 0x00bae010 | `CONDITIONAL_JUMP`
<a id="insn-00bae000"></a> `00bae000` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00bae004"></a> `00bae004` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00bae008"></a> `00bae008` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00bae00c"></a> `00bae00c` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00bae010"></a> `00bae010` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00bae014"></a> `00bae014` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00bae018"></a> `00bae018` | `22 02 00 54` | b.cs 0x00bae05c | `CONDITIONAL_JUMP`
<a id="insn-00bae01c"></a> `00bae01c` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bae020"></a> `00bae020` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bae024"></a> `00bae024` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00bae028"></a> `00bae028` | `a2 01 00 54` | b.cs 0x00bae05c | `CONDITIONAL_JUMP`
<a id="insn-00bae02c"></a> `00bae02c` | `4a 04 40 39` | ldrb w10,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00bae030"></a> `00bae030` | `4b 11 1d 12` | and w11,w10,#0xf8 | `FALL_THROUGH`
<a id="insn-00bae034"></a> `00bae034` | `7f 61 03 71` | cmp w11,#0xd8 | `FALL_THROUGH`
<a id="insn-00bae038"></a> `00bae038` | `60 01 00 54` | b.eq 0x00bae064 | `CONDITIONAL_JUMP`
<a id="insn-00bae03c"></a> `00bae03c` | `4b 00 40 39` | ldrb w11,[x2] | `FALL_THROUGH`
<a id="insn-00bae040"></a> `00bae040` | `6a 21 0a 2a` | orr w10,w11,w10, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00bae044"></a> `00bae044` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bae048"></a> `00bae048` | `e3 00 00 54` | b.cc 0x00bae064 | `CONDITIONAL_JUMP`
<a id="insn-00bae04c"></a> `00bae04c` | `42 08 00 91` | add x2,x2,#0x2 | `FALL_THROUGH`
<a id="insn-00bae050"></a> `00bae050` | `aa 24 00 78` | strh w10,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00bae054"></a> `00bae054` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00bae058"></a> `00bae058` | `63 fe ff 54` | b.cc 0x00bae024 | `CONDITIONAL_JUMP`
<a id="insn-00bae05c"></a> `00bae05c` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bae060"></a> `00bae060` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00bae064"></a> `00bae064` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00bae068"></a> `00bae068` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00bae06c"></a> `00bae06c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00badfdc`](#insn-00badfdc) 範囲 `[['00badfdc', '00badfeb']]`
  - `CONDITIONAL_JUMP` [`00badfe8`](#insn-00badfe8) → [`00bae010`](#insn-00bae010)
  - `FALL_THROUGH` [`00badfe8`](#insn-00badfe8) → [`00badfec`](#insn-00badfec)
- ブロック [`00badfec`](#insn-00badfec) 範囲 `[['00badfec', '00badff3']]`
  - `CONDITIONAL_JUMP` [`00badff0`](#insn-00badff0) → [`00bae010`](#insn-00bae010)
  - `FALL_THROUGH` [`00badff0`](#insn-00badff0) → [`00badff4`](#insn-00badff4)
- ブロック [`00badff4`](#insn-00badff4) 範囲 `[['00badff4', '00badfff']]`
  - `CONDITIONAL_JUMP` [`00badffc`](#insn-00badffc) → [`00bae010`](#insn-00bae010)
  - `FALL_THROUGH` [`00badffc`](#insn-00badffc) → [`00bae000`](#insn-00bae000)
- ブロック [`00bae000`](#insn-00bae000) 範囲 `[['00bae000', '00bae00f']]`
  - `FALL_THROUGH` [`00bae00c`](#insn-00bae00c) → [`00bae010`](#insn-00bae010)
- ブロック [`00bae010`](#insn-00bae010) 範囲 `[['00bae010', '00bae01b']]`
  - `CONDITIONAL_JUMP` [`00bae018`](#insn-00bae018) → [`00bae05c`](#insn-00bae05c)
  - `FALL_THROUGH` [`00bae018`](#insn-00bae018) → [`00bae01c`](#insn-00bae01c)
- ブロック [`00bae01c`](#insn-00bae01c) 範囲 `[['00bae01c', '00bae023']]`
  - `FALL_THROUGH` [`00bae020`](#insn-00bae020) → [`00bae024`](#insn-00bae024)
- ブロック [`00bae024`](#insn-00bae024) 範囲 `[['00bae024', '00bae02b']]`
  - `CONDITIONAL_JUMP` [`00bae028`](#insn-00bae028) → [`00bae05c`](#insn-00bae05c)
  - `FALL_THROUGH` [`00bae028`](#insn-00bae028) → [`00bae02c`](#insn-00bae02c)
- ブロック [`00bae02c`](#insn-00bae02c) 範囲 `[['00bae02c', '00bae03b']]`
  - `CONDITIONAL_JUMP` [`00bae038`](#insn-00bae038) → [`00bae064`](#insn-00bae064)
  - `FALL_THROUGH` [`00bae038`](#insn-00bae038) → [`00bae03c`](#insn-00bae03c)
- ブロック [`00bae03c`](#insn-00bae03c) 範囲 `[['00bae03c', '00bae04b']]`
  - `CONDITIONAL_JUMP` [`00bae048`](#insn-00bae048) → [`00bae064`](#insn-00bae064)
  - `FALL_THROUGH` [`00bae048`](#insn-00bae048) → [`00bae04c`](#insn-00bae04c)
- ブロック [`00bae04c`](#insn-00bae04c) 範囲 `[['00bae04c', '00bae05b']]`
  - `CONDITIONAL_JUMP` [`00bae058`](#insn-00bae058) → [`00bae024`](#insn-00bae024)
  - `FALL_THROUGH` [`00bae058`](#insn-00bae058) → [`00bae05c`](#insn-00bae05c)
- ブロック [`00bae05c`](#insn-00bae05c) 範囲 `[['00bae05c', '00bae063']]`
  - `FALL_THROUGH` [`00bae060`](#insn-00bae060) → [`00bae064`](#insn-00bae064)
- ブロック [`00bae064`](#insn-00bae064) 範囲 `[['00bae064', '00bae067']]`
  - `FALL_THROUGH` [`00bae064`](#insn-00bae064) → [`00bae068`](#insn-00bae068)
- ブロック [`00bae068`](#insn-00bae068) 範囲 `[['00bae068', '00bae06f']]`

## 命令位置別の参照

- [`00badfe8`](#insn-00badfe8) → [`00bae010`](#insn-00bae010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badff0`](#insn-00badff0) → [`00bae010`](#insn-00bae010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badffc`](#insn-00badffc) → [`00bae010`](#insn-00bae010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae018`](#insn-00bae018) → [`00bae05c`](#insn-00bae05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae028`](#insn-00bae028) → [`00bae05c`](#insn-00bae05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae038`](#insn-00bae038) → [`00bae064`](#insn-00bae064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae048`](#insn-00bae048) → [`00bae064`](#insn-00bae064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae058`](#insn-00bae058) → [`00bae024`](#insn-00bae024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badfe8`](#insn-00badfe8)

~~~json
{
  "source": "00badfe8",
  "target": "00bae010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badff0`](#insn-00badff0)

~~~json
{
  "source": "00badff0",
  "target": "00bae010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badffc`](#insn-00badffc)

~~~json
{
  "source": "00badffc",
  "target": "00bae010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae018`](#insn-00bae018)

~~~json
{
  "source": "00bae018",
  "target": "00bae05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae028`](#insn-00bae028)

~~~json
{
  "source": "00bae028",
  "target": "00bae05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae038`](#insn-00bae038)

~~~json
{
  "source": "00bae038",
  "target": "00bae064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae048`](#insn-00bae048)

~~~json
{
  "source": "00bae048",
  "target": "00bae064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae058`](#insn-00bae058)

~~~json
{
  "source": "00bae058",
  "target": "00bae024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
