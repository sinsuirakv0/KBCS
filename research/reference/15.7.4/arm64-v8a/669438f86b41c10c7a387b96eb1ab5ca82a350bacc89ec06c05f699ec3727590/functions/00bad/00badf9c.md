# 00badf9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00badf58`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00badf58.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-bf2fd6b6aa00be537feff3acaa3e980c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2a9e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a9e4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-c329d013efe83cf139f1e3e63cc0c848)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badf9c",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE9do_lengthER9mbstate_tPKcS5_m",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aecec18433ac70b423049afa4ffad1f023d33637c2d34453d7897c45d2b6c528",
  "source_text_sha256": "aecec18433ac70b423049afa4ffad1f023d33637c2d34453d7897c45d2b6c528",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badf9c",
        "00bae02f"
      ]
    ],
    "bytes_sha256": "f18482f6fdb556a7d8638deeea8680e07603898ffd93a9001a0381d398bbb50e",
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

## 疑似コード / UTF-8 842 bytes

~~~c

int _ZNKSt6__ndk115__codecvt_utf16IDsLb0EE9do_lengthER9mbstate_tPKcS5_m
              (long param_1,undefined8 param_2,byte *param_3,long param_4,ulong param_5)

{
  bool bVar1;
  bool bVar2;
  int iVar3;
  ulong uVar4;
  
  iVar3 = (int)param_3;
  if (((1 < param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == 0xfe)) {
    param_3 = param_3 + (ulong)(param_3[1] == 0xff) * 2;
  }
  if ((param_5 != 0) && (param_3 < (byte *)(param_4 + -1))) {
    uVar4 = 1;
    do {
      if ((*param_3 & 0xf8) == 0xd8) break;
      bVar1 = (ulong)CONCAT11(*param_3,param_3[1]) <= *(ulong *)(param_1 + 0x10);
      param_3 = param_3 + (ulong)bVar1 * 2;
      bVar2 = uVar4 < param_5;
      uVar4 = uVar4 + 1;
    } while ((bVar1 && param_3 < (byte *)(param_4 + -1)) && bVar2);
  }
  return (int)param_3 - iVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badf9c"></a> `00badf9c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badfa0"></a> `00badfa0` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00badfa4"></a> `00badfa4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badfa8"></a> `00badfa8` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00badfac"></a> `00badfac` | `8b 01 00 54` | b.lt 0x00badfdc | `CONDITIONAL_JUMP`
<a id="insn-00badfb0"></a> `00badfb0` | `09 18 40 b9` | ldr w9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badfb4"></a> `00badfb4` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00badfb8"></a> `00badfb8` | `29 01 10 36` | tbz w9,#0x2,0x00badfdc | `CONDITIONAL_JUMP`
<a id="insn-00badfbc"></a> `00badfbc` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00badfc0"></a> `00badfc0` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00badfc4"></a> `00badfc4` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00badfc8"></a> `00badfc8` | `a1 00 00 54` | b.ne 0x00badfdc | `CONDITIONAL_JUMP`
<a id="insn-00badfcc"></a> `00badfcc` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badfd0"></a> `00badfd0` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00badfd4"></a> `00badfd4` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00badfd8"></a> `00badfd8` | `48 44 28 8b` | add x8,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00badfdc"></a> `00badfdc` | `64 02 00 b4` | cbz x4,0x00bae028 | `CONDITIONAL_JUMP`
<a id="insn-00badfe0"></a> `00badfe0` | `69 04 00 d1` | sub x9,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00badfe4"></a> `00badfe4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00badfe8"></a> `00badfe8` | `02 02 00 54` | b.cs 0x00bae028 | `CONDITIONAL_JUMP`
<a id="insn-00badfec"></a> `00badfec` | `0a 08 40 f9` | ldr x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00badff0"></a> `00badff0` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-00badff4"></a> `00badff4` | `0c 01 40 39` | ldrb w12,[x8] | `FALL_THROUGH`
<a id="insn-00badff8"></a> `00badff8` | `8d 11 1d 12` | and w13,w12,#0xf8 | `FALL_THROUGH`
<a id="insn-00badffc"></a> `00badffc` | `bf 61 03 71` | cmp w13,#0xd8 | `FALL_THROUGH`
<a id="insn-00bae000"></a> `00bae000` | `40 01 00 54` | b.eq 0x00bae028 | `CONDITIONAL_JUMP`
<a id="insn-00bae004"></a> `00bae004` | `0d 05 40 39` | ldrb w13,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bae008"></a> `00bae008` | `ac 21 0c 2a` | orr w12,w13,w12, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00bae00c"></a> `00bae00c` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00bae010"></a> `00bae010` | `ec 37 9f 1a` | cset w12,cs | `FALL_THROUGH`
<a id="insn-00bae014"></a> `00bae014` | `08 45 2c 8b` | add x8,x8,w12, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00bae018"></a> `00bae018` | `02 21 49 fa` | ccmp x8,x9,#0x2,cs | `FALL_THROUGH`
<a id="insn-00bae01c"></a> `00bae01c` | `62 31 44 fa` | ccmp x11,x4,#0x2,cc | `FALL_THROUGH`
<a id="insn-00bae020"></a> `00bae020` | `6b 05 00 91` | add x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bae024"></a> `00bae024` | `83 fe ff 54` | b.cc 0x00badff4 | `CONDITIONAL_JUMP`
<a id="insn-00bae028"></a> `00bae028` | `00 01 02 4b` | sub w0,w8,w2 | `FALL_THROUGH`
<a id="insn-00bae02c"></a> `00bae02c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00badf9c`](#insn-00badf9c) 範囲 `[['00badf9c', '00badfaf']]`
  - `CONDITIONAL_JUMP` [`00badfac`](#insn-00badfac) → [`00badfdc`](#insn-00badfdc)
  - `FALL_THROUGH` [`00badfac`](#insn-00badfac) → [`00badfb0`](#insn-00badfb0)
- ブロック [`00badfb0`](#insn-00badfb0) 範囲 `[['00badfb0', '00badfbb']]`
  - `CONDITIONAL_JUMP` [`00badfb8`](#insn-00badfb8) → [`00badfdc`](#insn-00badfdc)
  - `FALL_THROUGH` [`00badfb8`](#insn-00badfb8) → [`00badfbc`](#insn-00badfbc)
- ブロック [`00badfbc`](#insn-00badfbc) 範囲 `[['00badfbc', '00badfcb']]`
  - `CONDITIONAL_JUMP` [`00badfc8`](#insn-00badfc8) → [`00badfdc`](#insn-00badfdc)
  - `FALL_THROUGH` [`00badfc8`](#insn-00badfc8) → [`00badfcc`](#insn-00badfcc)
- ブロック [`00badfcc`](#insn-00badfcc) 範囲 `[['00badfcc', '00badfdb']]`
  - `FALL_THROUGH` [`00badfd8`](#insn-00badfd8) → [`00badfdc`](#insn-00badfdc)
- ブロック [`00badfdc`](#insn-00badfdc) 範囲 `[['00badfdc', '00badfdf']]`
  - `CONDITIONAL_JUMP` [`00badfdc`](#insn-00badfdc) → [`00bae028`](#insn-00bae028)
  - `FALL_THROUGH` [`00badfdc`](#insn-00badfdc) → [`00badfe0`](#insn-00badfe0)
- ブロック [`00badfe0`](#insn-00badfe0) 範囲 `[['00badfe0', '00badfeb']]`
  - `CONDITIONAL_JUMP` [`00badfe8`](#insn-00badfe8) → [`00bae028`](#insn-00bae028)
  - `FALL_THROUGH` [`00badfe8`](#insn-00badfe8) → [`00badfec`](#insn-00badfec)
- ブロック [`00badfec`](#insn-00badfec) 範囲 `[['00badfec', '00badff3']]`
  - `FALL_THROUGH` [`00badff0`](#insn-00badff0) → [`00badff4`](#insn-00badff4)
- ブロック [`00badff4`](#insn-00badff4) 範囲 `[['00badff4', '00bae003']]`
  - `CONDITIONAL_JUMP` [`00bae000`](#insn-00bae000) → [`00bae028`](#insn-00bae028)
  - `FALL_THROUGH` [`00bae000`](#insn-00bae000) → [`00bae004`](#insn-00bae004)
- ブロック [`00bae004`](#insn-00bae004) 範囲 `[['00bae004', '00bae027']]`
  - `CONDITIONAL_JUMP` [`00bae024`](#insn-00bae024) → [`00badff4`](#insn-00badff4)
  - `FALL_THROUGH` [`00bae024`](#insn-00bae024) → [`00bae028`](#insn-00bae028)
- ブロック [`00bae028`](#insn-00bae028) 範囲 `[['00bae028', '00bae02f']]`

## 命令位置別の参照

- [`00badfac`](#insn-00badfac) → [`00badfdc`](#insn-00badfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badfb8`](#insn-00badfb8) → [`00badfdc`](#insn-00badfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badfc8`](#insn-00badfc8) → [`00badfdc`](#insn-00badfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badfdc`](#insn-00badfdc) → [`00bae028`](#insn-00bae028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badfe8`](#insn-00badfe8) → [`00bae028`](#insn-00bae028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae000`](#insn-00bae000) → [`00bae028`](#insn-00bae028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae024`](#insn-00bae024) → [`00badff4`](#insn-00badff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badfac`](#insn-00badfac)

~~~json
{
  "source": "00badfac",
  "target": "00badfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badfb8`](#insn-00badfb8)

~~~json
{
  "source": "00badfb8",
  "target": "00badfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badfc8`](#insn-00badfc8)

~~~json
{
  "source": "00badfc8",
  "target": "00badfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badfdc`](#insn-00badfdc)

~~~json
{
  "source": "00badfdc",
  "target": "00bae028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badfe8`](#insn-00badfe8)

~~~json
{
  "source": "00badfe8",
  "target": "00bae028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae000`](#insn-00bae000)

~~~json
{
  "source": "00bae000",
  "target": "00bae028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae024`](#insn-00bae024)

~~~json
{
  "source": "00bae024",
  "target": "00badff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
