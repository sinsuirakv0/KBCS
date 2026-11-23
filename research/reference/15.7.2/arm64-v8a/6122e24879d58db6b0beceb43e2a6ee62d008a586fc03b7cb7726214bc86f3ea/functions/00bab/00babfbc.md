# 00babfbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bac084`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac084.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-537c7dfe5949551b0991e49dba029db7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babfbc",
  "name": "_ZNKSt6__ndk17codecvtIDsc9mbstate_tE5do_inERS1_PKcS5_RS5_PDsS7_RS7_",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8064a162dc1de59a03c611856d45e0153637913ec3249c8f0a0798841b782226",
  "source_text_sha256": "8064a162dc1de59a03c611856d45e0153637913ec3249c8f0a0798841b782226",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babfbc",
        "00bac023"
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

- [00bac024](../00bac/00bac024.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 500 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDsc9mbstate_tE5do_inERS1_PKcS5_RS5_PDsS7_RS7_
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00bac024(param_3,param_4,&uStack_28,param_6,param_7,&local_30,0x10ffff,0);
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babfbc"></a> `00babfbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00babfc0"></a> `00babfc0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00babfc4"></a> `00babfc4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babfc8"></a> `00babfc8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babfcc"></a> `00babfcc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00babfd0"></a> `00babfd0` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00babfd4"></a> `00babfd4` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00babfd8"></a> `00babfd8` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00babfdc"></a> `00babfdc` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00babfe0"></a> `00babfe0` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00babfe4"></a> `00babfe4` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00babfe8"></a> `00babfe8` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00babfec"></a> `00babfec` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00babff0"></a> `00babff0` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00babff4"></a> `00babff4` | `e4 03 06 aa` | mov x4,x6 | `FALL_THROUGH`
<a id="insn-00babff8"></a> `00babff8` | `e6 fd bf 12` | mov w6,#0x10ffff | `FALL_THROUGH`
<a id="insn-00babffc"></a> `00babffc` | `e7 03 1f 2a` | mov w7,wzr | `FALL_THROUGH`
<a id="insn-00bac000"></a> `00bac000` | `09 00 00 94` | bl 0x00bac024 | `UNCONDITIONAL_CALL`
<a id="insn-00bac004"></a> `00bac004` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00bac008"></a> `00bac008` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bac00c"></a> `00bac00c` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bac010"></a> `00bac010` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac014"></a> `00bac014` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac018"></a> `00bac018` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bac01c"></a> `00bac01c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bac020"></a> `00bac020` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babfbc`](#insn-00babfbc) 範囲 `[['00babfbc', '00bac023']]`

## 命令位置別の参照

- [`00babfc4`](#insn-00babfc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfc8`](#insn-00babfc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babff8`](#insn-00babff8) → `0010ffff`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Sym[6714]`
- [`00bac000`](#insn-00bac000) → [`00bac024`](../00bac/00bac024.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac024` · 推定シンボル `None` · 推定型 `None`
- [`00bac004`](#insn-00bac004) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac010`](#insn-00bac010) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac014`](#insn-00bac014) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babfc4`](#insn-00babfc4)

~~~json
{
  "source": "00babfc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfc8`](#insn-00babfc8)

~~~json
{
  "source": "00babfc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babff8`](#insn-00babff8)

~~~json
{
  "source": "00babff8",
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
- 参照命令 [`00bac000`](#insn-00bac000)

~~~json
{
  "source": "00bac000",
  "target": "00bac024",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac004`](#insn-00bac004)

~~~json
{
  "source": "00bac004",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac010`](#insn-00bac010)

~~~json
{
  "source": "00bac010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac014`](#insn-00bac014)

~~~json
{
  "source": "00bac014",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
