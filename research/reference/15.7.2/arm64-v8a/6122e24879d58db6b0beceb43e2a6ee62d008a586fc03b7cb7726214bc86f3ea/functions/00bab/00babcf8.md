# 00babcf8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00babdc0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babdc0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-21de2192ff92e4c96cdcf9232165bff0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babcf8",
  "name": "_ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "725ad31e2d52185309b09f9fdcdc5dfbcd9c3aa1b7bcf8050614642a8e25b519",
  "source_text_sha256": "725ad31e2d52185309b09f9fdcdc5dfbcd9c3aa1b7bcf8050614642a8e25b519",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babcf8",
        "00babd5f"
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

- [00babd60](../00bab/00babd60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 850 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00babd3c to 00cabf0b has its CatchHandler @ 00babd3c
                       catch() { ... } // from try @ 00babd3c with catch @ 00babd3c
                       catch() { ... } // from try @ 00babf28 with catch @ 00babd3c
                       catch() { ... } // from try @ 00bac1c4 with catch @ 00babd3c */
  FUN_00babd60(param_3,param_4,&uStack_28,param_6,param_7,&local_30,0x10ffff,0);
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babcf8"></a> `00babcf8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00babcfc"></a> `00babcfc` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00babd00"></a> `00babd00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babd04"></a> `00babd04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babd08"></a> `00babd08` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00babd0c"></a> `00babd0c` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00babd10"></a> `00babd10` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00babd14"></a> `00babd14` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00babd18"></a> `00babd18` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00babd1c"></a> `00babd1c` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00babd20"></a> `00babd20` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00babd24"></a> `00babd24` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00babd28"></a> `00babd28` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00babd2c"></a> `00babd2c` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00babd30"></a> `00babd30` | `e4 03 06 aa` | mov x4,x6 | `FALL_THROUGH`
<a id="insn-00babd34"></a> `00babd34` | `e6 fd bf 12` | mov w6,#0x10ffff | `FALL_THROUGH`
<a id="insn-00babd38"></a> `00babd38` | `e7 03 1f 2a` | mov w7,wzr | `FALL_THROUGH`
<a id="insn-00babd3c"></a> `00babd3c` | `09 00 00 94` | bl 0x00babd60 | `UNCONDITIONAL_CALL`
<a id="insn-00babd40"></a> `00babd40` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00babd44"></a> `00babd44` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00babd48"></a> `00babd48` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00babd4c"></a> `00babd4c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babd50"></a> `00babd50` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babd54"></a> `00babd54` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00babd58"></a> `00babd58` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00babd5c"></a> `00babd5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babcf8`](#insn-00babcf8) 範囲 `[['00babcf8', '00babd3b']]`
  - `FALL_THROUGH` [`00babd38`](#insn-00babd38) → [`00babd3c`](#insn-00babd3c)
- ブロック [`00babd3c`](#insn-00babd3c) 範囲 `[['00babd3c', '00babd5f']]`

## 命令位置別の参照

- [`00babd00`](#insn-00babd00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd04`](#insn-00babd04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd20`](#insn-00babd20) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd34`](#insn-00babd34) → `0010ffff`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Sym[6714]`
- [`00babd3c`](#insn-00babd3c) → [`00babd60`](00babd60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00babd60` · 推定シンボル `None` · 推定型 `None`
- [`00babd40`](#insn-00babd40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd4c`](#insn-00babd4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd50`](#insn-00babd50) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babd00`](#insn-00babd00)

~~~json
{
  "source": "00babd00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd04`](#insn-00babd04)

~~~json
{
  "source": "00babd04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd20`](#insn-00babd20)

~~~json
{
  "source": "00babd20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd34`](#insn-00babd34)

~~~json
{
  "source": "00babd34",
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
- 参照命令 [`00babd3c`](#insn-00babd3c)

~~~json
{
  "source": "00babd3c",
  "target": "00babd60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd40`](#insn-00babd40)

~~~json
{
  "source": "00babd40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd4c`](#insn-00babd4c)

~~~json
{
  "source": "00babd4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd50`](#insn-00babd50)

~~~json
{
  "source": "00babd50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
