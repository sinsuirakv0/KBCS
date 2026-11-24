# 00baca3c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bac9f8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac9f8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-4b880827b1d44e48eaf343efb8046057)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c29484`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29484.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0005.md#compare-6af5c5ea0a64e3c3495e6c786664349d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baca3c",
  "name": "_ZNKSt6__ndk17codecvtIDic9mbstate_tE5do_inERS1_PKcS5_RS5_PDiS7_RS7_",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "06ecc74554b1a2580203135a8a87305b6ba18975c798aa353f50694679a9ce62",
  "source_text_sha256": "06ecc74554b1a2580203135a8a87305b6ba18975c798aa353f50694679a9ce62",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baca3c",
        "00bacaa3"
      ]
    ],
    "bytes_sha256": "8aaa5dcbe6deefeb9fcfec12e1ba187e7a4d04562662ee505165509266551468",
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

- [00bacaa4](../00bac/00bacaa4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 500 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDic9mbstate_tE5do_inERS1_PKcS5_RS5_PDiS7_RS7_
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00bacaa4(param_3,param_4,&uStack_28,param_6,param_7,&local_30,0x10ffff,0);
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baca3c"></a> `00baca3c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baca40"></a> `00baca40` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baca44"></a> `00baca44` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baca48"></a> `00baca48` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baca4c"></a> `00baca4c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baca50"></a> `00baca50` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00baca54"></a> `00baca54` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00baca58"></a> `00baca58` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00baca5c"></a> `00baca5c` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00baca60"></a> `00baca60` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baca64"></a> `00baca64` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00baca68"></a> `00baca68` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baca6c"></a> `00baca6c` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00baca70"></a> `00baca70` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00baca74"></a> `00baca74` | `e4 03 06 aa` | mov x4,x6 | `FALL_THROUGH`
<a id="insn-00baca78"></a> `00baca78` | `e6 fd bf 12` | mov w6,#0x10ffff | `FALL_THROUGH`
<a id="insn-00baca7c"></a> `00baca7c` | `e7 03 1f 2a` | mov w7,wzr | `FALL_THROUGH`
<a id="insn-00baca80"></a> `00baca80` | `09 00 00 94` | bl 0x00bacaa4 | `UNCONDITIONAL_CALL`
<a id="insn-00baca84"></a> `00baca84` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00baca88"></a> `00baca88` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baca8c"></a> `00baca8c` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baca90"></a> `00baca90` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baca94"></a> `00baca94` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baca98"></a> `00baca98` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baca9c"></a> `00baca9c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bacaa0"></a> `00bacaa0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baca3c`](#insn-00baca3c) 範囲 `[['00baca3c', '00bacaa3']]`

## 命令位置別の参照

- [`00baca44`](#insn-00baca44) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca48`](#insn-00baca48) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca64`](#insn-00baca64) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca78`](#insn-00baca78) → `0010ffff`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Sym[6714]`
- [`00baca80`](#insn-00baca80) → [`00bacaa4`](00bacaa4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bacaa4` · 推定シンボル `None` · 推定型 `None`
- [`00baca84`](#insn-00baca84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca90`](#insn-00baca90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca94`](#insn-00baca94) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baca44`](#insn-00baca44)

~~~json
{
  "source": "00baca44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca48`](#insn-00baca48)

~~~json
{
  "source": "00baca48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca64`](#insn-00baca64)

~~~json
{
  "source": "00baca64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca78`](#insn-00baca78)

~~~json
{
  "source": "00baca78",
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
- 参照命令 [`00baca80`](#insn-00baca80)

~~~json
{
  "source": "00baca80",
  "target": "00bacaa4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baca84`](#insn-00baca84)

~~~json
{
  "source": "00baca84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca90`](#insn-00baca90)

~~~json
{
  "source": "00baca90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca94`](#insn-00baca94)

~~~json
{
  "source": "00baca94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
